🤔 Question: How do nodes work in PocketFlow?

  🔍 Agent decides to read 'nodes'
  📄 Reading document: nodes
  ✅ Added 'nodes' to context
  💡 Agent decides it has enough context to answer
  ✍️ Generating answer...

🎯 Final Answer:
Nodes in PocketFlow have three lifecycle methods:

- **`prep`** — reads data from the shared store to prepare inputs
- **`exec`** — performs the actual work (e.g., LLM calls); this is the only method that retries on failure
- **`post`** — writes results back to the shared store

`BatchNode` is a variant that handles list inputs, running the node logic over multiple items.
