🤔 Question: How do nodes work in PocketFlow?

  🔍 Agent decides to read 'nodes'
  📄 Reading document: nodes
  ✅ Added 'nodes' to context
  💡 Agent decides it has enough context to answer
  ✍️ Generating answer...

🎯 Final Answer:
In PocketFlow, nodes have three lifecycle methods:

- **`prep`** — reads data from the shared store (preparation)
- **`exec`** — performs the actual work (LLM calls, computations); this is the only method that retries on failure
- **`post`** — writes results back to the shared store

**`BatchNode`** is a specialized variant that handles list/batch inputs.
