## 0. High-level Description

This workflow implements a **ReAct-style (Reason + Act) web research agent** that iteratively decides whether to search the web or produce a final answer. The WORKFLOW begins with a user question placed in shared state (`@question`, `@context`). A `decide_action` CREATE FUNCTION issues a GENERATE call whose prompt presents the current question and accumulated research context, instructing the LLM to emit a YAML block containing either `action: search` (with a `search_query` field) or `action: answer` (with an `answer` field); the response is parsed and routed accordingly. Control flow is expressed as a WHILE loop that continues as long as the LLM selects the `search` action: each iteration issues a CALL to the `search_web` tool (a side-effecting DuckDuckGo lookup), appends the results to `@context`, then re-enters the GENERATE/EVALUATE cycle. When the LLM selects `action: answer`, the loop exits and a second CREATE FUNCTION, `answer_question`, issues a final GENERATE call that synthesises `@context` into a comprehensive answer stored in `@answer`. The workflow RETURNs `@answer` with `status=completed`. The entire execution is wrapped in an EXCEPTION WHEN handler that catches any runtime failure, marks the task `status=failed`, and surfaces an error artifact. An A2A server/client harness wraps the synchronous PocketFlow execution, translating incoming JSON-RPC requests into shared-state initialisation and outgoing A2A `Task` responses, but this transport layer is external to the core WORKFLOW logic.

---

## 1. Purpose

Answers arbitrary natural-language questions by autonomously deciding when to perform web searches and when sufficient context exists to synthesise a final answer, then returning that answer to the caller.

---

## 2. SPL ↔ Python — PocketFlow Construct Mapping

| SPL Construct | Python — PocketFlow Equivalent | Notes |
|---|---|---|
| `WORKFLOW research_agent` | `create_agent_flow()` in `flow.py`; `Flow(start=decide)` | The `Flow` object is the named workflow entry point |
| `CREATE FUNCTION decide_action` | `DecideAction.exec()` prompt string in `nodes.py` | Builds the YAML-structured decision prompt |
| `CREATE FUNCTION answer_question` | `AnswerQuestion.exec()` prompt string in `nodes.py` | Builds the synthesis prompt |
| `GENERATE decide_action(...) INTO @decision` | `call_llm(prompt)` inside `DecideAction.exec()` + `yaml.safe_load(...)` | Returns parsed dict; `action`, `search_query`, `answer` fields |
| `GENERATE answer_question(...) INTO @answer` | `call_llm(prompt)` inside `AnswerQuestion.exec()` | Raw text answer stored in `shared["answer"]` |
| `CALL search_web(@query) INTO @results` | `search_web(search_query)` in `SearchWeb.exec()` | Side-effecting DuckDuckGo call via `DDGS().text()` |
| `@var` (shared state variables) | `shared` dict passed through all `Node.prep/exec/post` calls | `shared["question"]`, `shared["context"]`, `shared["search_query"]`, `shared["answer"]` |
| `WHILE @decision.action == "search" DO ... END` | `search - "decide" >> decide` edge in `flow.py`; loop continues until `DecideAction.post` returns `"answer"` | PocketFlow action-string routing encodes the loop back-edge |
| `EVALUATE @decision WHEN contains("search") THEN ... ELSE ... END` | `DecideAction.post()` branching on `exec_res["action"]` | Returns `"search"` or `"answer"` string to select the next node |
| `RETURN @answer WITH status=completed` | `AnswerQuestion.post()` returning `"done"` (terminal); `shared["answer"]` read by caller | No outgoing edge from `AnswerQuestion` terminates the flow |
| `EXCEPTION WHEN RuntimeError THEN status=failed` | `try/except Exception` in `PocketFlowTaskManager.on_send_task()` | Sets `TaskState.FAILED`, returns `InternalError` JSON-RPC response |
| A2A transport (no direct SPL equivalent) | `A2AServer` + `PocketFlowTaskManager` + `A2AClient` | Wraps synchronous WORKFLOW execution in async JSON-RPC task lifecycle |

---

## 3. Logical Functions / Prompts

### `decide_action`
- **Role:** The agent's reasoning core; runs at every loop iteration to decide the next action.
- **Prompt conventions:**
  - Sections delimited by `### CONTEXT` and `### ACTION SPACE` and `## NEXT ACTION` headers.
  - Two enumerated actions (`[1] search`, `[2] answer`) with explicit parameter schemas prevent hallucinated actions.
  - Output **must** be a fenced ` ```yaml ``` ` block; parsed with `yaml.safe_load` after splitting on the fence tokens — these are the sentinel tokens.
  - Key output fields: `thinking` (multi-line `|` block for chain-of-thought), `action`, `reason`, `answer` (populated only when `action: answer`), `search_query` (populated only when `action: search`).
  - Prompt explicitly instructs 4-space indentation and `|` for multi-line fields to ensure reliable YAML parsing.

### `answer_question`
- **Role:** Terminal synthesis step; converts accumulated research context into a final user-facing answer.
- **Prompt conventions:**
  - Sections: `### CONTEXT` (question + full `@context` dump) and `## YOUR ANSWER:`.
  - No sentinel tokens or structured output format required — raw prose is acceptable.
  - Receives the full `@context` string, which is a concatenated log of all prior `SEARCH: <query>\nRESULTS: <snippets>` entries.

---

## 4. Control Flow

```
START
  │
  ▼
[DecideAction] ── GENERATE decide_action(@question, @context) INTO @decision
  │
  EVALUATE @decision.action
  ├── "search" ──► [SearchWeb] ── CALL search_web(@search_query) INTO @results
  │                               append to @context
  │                               └──► back to [DecideAction]   ← WHILE loop
  │
  └── "answer" ──► [AnswerQuestion] ── GENERATE answer_question(@question, @context) INTO @answer
                                        RETURN @answer WITH status=completed

EXCEPTION WHEN any error THEN
  RETURN WITH status=failed, error=<exception message>
```

- **Loop condition (WHILE):** Implicit — the `"decide"` back-edge from `SearchWeb` to `DecideAction` in `flow.py` continues until `DecideAction` emits `"answer"`.
- **Termination:** `AnswerQuestion.post()` returns `"done"`, which has no registered outgoing edge, causing `Flow.run()` to exit.
- **No explicit max-iterations guard** exists in this implementation; the LLM is expected to converge to `action: answer` within a reasonable number of searches.

---

## 5. How to Regenerate as SPL

```bash
# Step 1 — generate SPL from this spec (Section 0 above as text2spl input)
spl3 text2spl --description "<paste Section 0 here>" --mode workflow

# Step 2 — compile to any target
spl3 splc compile <output.spl> --lang python/pocketflow
spl3 splc compile <output.spl> --lang python/langgraph
spl3 splc compile <output.spl> --lang go
```