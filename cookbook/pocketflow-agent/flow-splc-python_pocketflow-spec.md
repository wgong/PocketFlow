## 0. High-level Description
The research agent workflow implements an iterative search-and-synthesize pattern using a `WHILE` loop to refine its knowledge base until a definitive answer can be produced. It begins with a `CREATE FUNCTION` for the decision-making prompt, which uses `GENERATE` to produce a YAML-formatted plan containing a thinking process and a chosen action. The control flow uses `EVALUATE` to branch based on the LLM's decision: if the action is "search", the workflow executes a `CALL` to a web search tool to update the `@context` variable before looping back to the decision step. Once the LLM determines it has sufficient information, it selects the "answer" action, triggering a final `GENERATE` call to a synthesis function that crafts the response. Finally, the workflow uses `RETURN` to provide the `@answer` to the user, terminating the process once the research goal is met.

## 1. Purpose
This implementation creates an autonomous research agent that iteratively searches the web to gather context until it has enough information to provide a comprehensive answer to a user's question.

## 2. SPL ↔ Python — PocketFlow Construct Mapping

| SPL Construct | Python — PocketFlow Equivalent | Notes |
| :--- | :--- | :--- |
| `WORKFLOW` | `create_agent_flow()` / `Flow` | Defines the overall structure and entry point of the graph. |
| `CREATE FUNCTION` | Prompt strings in `DecideAction` and `AnswerQuestion` | Templates for LLM interactions with `{question}` and `{context}` slots. |
| `GENERATE` | `call_llm(prompt)` in `exec` methods | The actual invocation of the LLM to process a prompt. |
| `CALL` | `search_web_duckduckgo(query)` | Invocation of an external tool/side-effect (web search). |
| `EVALUATE` | `decide - "action" >> next_node` | Conditional routing logic based on the output of a node. |
| `WHILE` | `search - "decide" >> decide` | The cyclic connection in the graph that creates the loop. |
| `@vars` | `shared` dictionary | The shared state object passed between nodes. |
| `RETURN` | `shared["answer"]` + Flow termination | The final state of the shared dictionary upon completing the `AnswerQuestion` node. |
| `EXCEPTION` | (Implicit in `parse_yaml_safely`) | Error handling during YAML parsing of LLM output. |

## 3. Logical Functions / Prompts

### `DecideAction`
- **Role:** The controller/router of the agent. It analyzes the current research context and decides whether more information is needed or if a final answer can be written.
- **Key Prompt Conventions:** 
    - Employs a **YAML Output Format** with specific keys: `thinking`, `action`, `reason`, `answer`, and `search_query`.
    - Uses **Block Scalars (`\|`)** to ensure multi-line LLM responses do not break YAML parsing.
    - Defines a clear **Action Space** (`search` or `answer`) for the LLM to choose from.

### `AnswerQuestion`
- **Role:** The final synthesis step.
- **Key Prompt Conventions:**
    - Provides a `CONTEXT` section containing the original question and the accumulated `Research` results.
    - Instructs the LLM to provide a "comprehensive answer" based specifically on the gathered information.

## 4. Control Flow
1. **Initial Step:** The workflow starts at the `DecideAction` node.
2. **Loop Condition (`WHILE`):** The agent enters a loop where it generates a decision based on the current `@context` (initially empty).
3. **Branch Logic (`EVALUATE`):**
    - **`WHEN action == 'search'`**: The workflow executes the `SearchWeb` node, which `CALL`s the DuckDuckGo tool, appends results to `@context`, and returns to `DecideAction`.
    - **`WHEN action == 'answer'`**: The workflow proceeds to the `AnswerQuestion` node.
4. **Termination:** The `AnswerQuestion` node generates the final `@answer`, stores it in the shared state, and returns a `done` status to terminate the `WORKFLOW`.

## 5. How to Regenerate as SPL
```bash
# Step 1 — generate SPL from this spec (Section 0 above as text2spl input)
spl3 text2spl --description "The research agent workflow implements an iterative search-and-synthesize pattern using a WHILE loop to refine its knowledge base until a definitive answer can be produced. It begins with a CREATE FUNCTION for the decision-making prompt, which uses GENERATE to produce a YAML-formatted plan containing a thinking process and a chosen action. The control flow uses EVALUATE to branch based on the LLM's decision: if the action is 'search', the workflow executes a CALL to a web search tool to update the @context variable before looping back to the decision step. Once the LLM determines it has sufficient information, it selects the 'answer' action, triggering a final GENERATE call to a synthesis function that crafts the response. Finally, the workflow uses RETURN to provide the @answer to the user, terminating the process once the research goal is met." --mode workflow

# Step 2 — compile to any target
spl3 splc compile research_agent.spl --lang python/pocketflow
spl3 splc compile research_agent.spl --lang python/langgraph
spl3 splc compile research_agent.spl --lang go
```