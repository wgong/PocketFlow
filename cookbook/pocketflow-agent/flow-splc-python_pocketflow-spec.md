## 0. High-level Description

This workflow implements a **ReAct-style agentic research loop** using a WHILE-like cycle that iterates until the agent is confident enough to answer. The WORKFLOW begins by initializing a shared context store with the user's question, then enters a GENERATE step backed by the `DecideAction` function — a structured YAML-output prompt that reasons step-by-step and selects between two actions: `search` or `answer`. The EVALUATE branch on that output either routes to a `SearchWeb` side-effect node (a CALL to DuckDuckGo that appends retrieved snippets into the accumulated `@context` variable) and loops back, or exits the WHILE loop by routing to an `AnswerQuestion` GENERATE step that synthesizes all gathered research into a final prose response. The RETURN delivers `@answer` with implicit `status=done`. Exception handling for malformed YAML is managed inline within `DecideAction` via a two-pass parse-and-repair strategy. No multi-model design is present — a single configurable LLM adapter (OpenAI-compatible, switchable via SPL shim to Ollama or Claude CLI) services all GENERATE calls.

---

## 1. Purpose

Answers an arbitrary research question by autonomously deciding how many web searches to perform before synthesizing a comprehensive final answer.

---

## 2. SPL ↔ Python — PocketFlow Construct Mapping

| SPL Construct | Python — PocketFlow Equivalent | Notes |
|---|---|---|
| `WORKFLOW <name>` | `create_agent_flow()` + `Flow(start=decide)` | The `Flow` object is the workflow; `start=` names the entry node |
| `CREATE FUNCTION <name>` | `Node` subclass with `prep` / `exec` / `post` | Each node is a reusable prompt template; `exec` holds the prompt string |
| `GENERATE <fn>(...) INTO @<var>` | `call_llm(prompt)` inside `exec`, result stored via `shared[key] =` in `post` | `@context`, `@search_query`, `@answer` are the shared-store variables |
| `CALL <tool>(...) INTO @<var>` | `search_web_duckduckgo(query)` in `SearchWeb.exec`, appended into `shared["context"]` | Side-effect call with no LLM involved; maps cleanly to SPL CALL |
| `WHILE <cond> DO ... END` | `search - "decide" >> decide` edge (cycle back) | Loop continues as long as `DecideAction` returns `"search"`; no explicit counter |
| `EVALUATE @<var> WHEN ... THEN ... ELSE ...` | `post()` returning `"search"` or `"answer"` string; PocketFlow routes on that return value | `decide - "search" >> search` and `decide - "answer" >> answer` encode the branch |
| `RETURN @<var> WITH status=` | `AnswerQuestion.post` returning `"done"`; `shared["answer"]` read in `main.py` | `"done"` is the terminal action; no successor node registered for it |
| `EXCEPTION WHEN <Type> THEN` | `parse_yaml_safely` two-pass repair + `raise ValueError(...)` in `DecideAction.exec` | Catches `yaml.YAMLError`; repairs block-scalar formatting before re-raising |
| SPL `@vars` (shared state) | `shared` dict passed through every `prep` / `post` | Keys: `question`, `context`, `search_query`, `answer` |

---

## 3. Logical Functions / Prompts

### `DecideAction` — ReAct Decision Prompt
- **Role:** The cognitive core of the loop. Given the original question and all accumulated research, it reasons and selects the next action.
- **Key conventions:**
  - Output format: fenced ` ```yaml ``` ` block with keys `thinking`, `action`, `reason`, `answer`, `search_query`.
  - `thinking` and `reason` use YAML block scalar (`|`) to tolerate colons in prose.
  - Sentinel values: `action: search` or `action: answer` drive the EVALUATE branch.
  - Two-pass YAML repair: first tries `yaml.safe_load`; on `YAMLError`, rewrites plain-string fields as block scalars and retries.
  - `search_query` is a single-line string (no `|`) consumed directly by the next CALL.

### `AnswerQuestion` — Synthesis Prompt
- **Role:** Terminal GENERATE step. Consumes the full accumulated `@context` (all search results concatenated) and produces a final human-readable answer.
- **Key conventions:**
  - Unstructured prose output — no YAML, no sentinel tokens.
  - Prompt explicitly labels sections (`### CONTEXT`, `## YOUR ANSWER:`) for clarity.
  - Result is stored verbatim into `shared["answer"]`.

---

## 4. Control Flow

```
START
  └─► GENERATE DecideAction(@question, @context)
        │
        EVALUATE @action
        ├─ WHEN "search"
        │     └─► CALL SearchWeb(@search_query) INTO @context   ← appends to history
        │           └─► loop back to GENERATE DecideAction       ← WHILE continues
        │
        └─ WHEN "answer"
              └─► GENERATE AnswerQuestion(@question, @context) INTO @answer
                    └─► RETURN @answer WITH status="done"        ← WHILE exits
```

- The WHILE condition is implicit: the loop runs as long as `DecideAction.post` returns `"search"`. No maximum-iteration guard exists in the current implementation.
- `@context` is an append-only log: each iteration prepends `\n\nSEARCH: <query>\nRESULTS: <snippets>`.
- The `"done"` terminal action has no registered successor in the `Flow`, so PocketFlow naturally halts.

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