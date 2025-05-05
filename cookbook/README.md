# Pocket Flow Cookbook

## Docs

- [PocketFlow](https://the-pocket.github.io/PocketFlow/)
- [Zach's Blogs](https://zacharyhuang.substack.com/)

## Basic Concept

see [pocketflow_demo.ipynb](https://github.com/wgong/PocketFlow/blob/main/cookbook/pocketflow_demo.ipynb)

## Demo Catalog

see more use-cases in [cookbook](https://github.com/wgong/PocketFlow/tree/main/cookbook) folder, if not listed below

<div align="center">
  
|  Name  | Difficulty    |  Description  |  Blog  |
| :-------------:  | :-------------: | :--------------------- |  ------ |
| [Hello World](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-hello-world) | ☆☆☆ <br> *Dummy*   | A basic flow | |
| [Flow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-flow) | ☆☆☆ <br> *Dummy*   | interactive loop with branching paths | |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <br> *Dummy*   | real-time LLM streaming | |
| [Async](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-async-basic) | ☆☆☆ <br> *Dummy*   | A basic Async flow | |
| [Batch](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <br> *Dummy*   | A basic Batch flow | |
| [Communication](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-communication) | ☆☆☆ <br> *Dummy*   | Explain shared store pattern | |
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <br> *Dummy*   | A basic chat bot with conversation history | |
| [Structured Output](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <br> *Dummy* | Extracting structured data from resumes by prompting | [Promp Tips](https://zacharyhuang.substack.com/p/structured-output-for-beginners-3) |
| [Workflow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <br> *Dummy*   | A writing workflow that outlines, writes content, and applies styling | |
| [Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <br> *Dummy*   | A research agent that can search the web and answer questions | [Agent as Graph](https://zacharyhuang.substack.com/p/llm-agent-internal-as-a-graph-tutorial) |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <br> *Dummy*   | A simple Retrieval-augmented Generation process | [RAG](https://zacharyhuang.substack.com/p/retrieval-augmented-generation-rag) |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) | ☆☆☆ <br> *Dummy*   | A simple Text-to-SQL process | [text2SQL](https://zacharyhuang.substack.com/p/text-to-sql-from-scratch-tutorial) |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <br> *Dummy* | A resume qualification processor using map-reduce pattern for batch evaluation | |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <br> *Dummy*   | A real-time LLM streaming demo with user interrupt capability | |
| [Human-in-the-Loop](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-web-hitl) | ★☆☆ <br> *Beginner* |  web application for human-in-the-loop (HITL) workflows using PocketFlow, FastAPI, and Server-Sent Events (SSE) |  |
| [Chat Guardrail](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <br> *Dummy*  | A travel advisor chatbot that only processes travel-related queries | |
| [Multi-Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <br> *Beginner* | A Taboo word game for asynchronous communication between two agents | |
| [Supervisor](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <br> *Beginner* | Research agent is getting unreliable... Let's build a supervision process| |
| [Parallel](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) | ★☆☆ <br> *Beginner*   | A parallel execution demo that shows 3x speedup | |
| [Parallel Flow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <br> *Beginner*   | A parallel image processing demo showing 8x speedup with multiple filters | |
| [Thinking](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) | ★☆☆ <br> *Beginner*   | Solve complex reasoning problems through Chain-of-Thought | [Chain-of-Thought](https://zacharyhuang.substack.com/p/build-chain-of-thought-from-scratch) |
| [Majority Vote Reasoning](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ★☆☆ <br> *Beginner*   | consensus-based reasoning | |
| [Memory](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) | ★☆☆ <br> *Beginner* | A chat bot with short-term and long-term memory | [Memory](https://zacharyhuang.substack.com/p/build-ai-agent-memory-from-scratch) |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) | ★☆☆ <br> *Medium* |  Agent using Model Context Protocol for numerical operations | [MCP or Function Call](https://zacharyhuang.substack.com/p/mcp-simply-explained-function-calling) |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) | ★☆☆ <br> *Medium* |  demo Agent-to-Agent (A2A) communication protocol | [How A2A works](https://zacharyhuang.substack.com/p/a2a-protocol-simply-explained-here) |
| [Codebase Knowledge Builder](https://github.com/The-Pocket/PocketFlow-Tutorial-Codebase-Knowledge) | ★☆☆ <br> *Advanced* |  Project: Codebase to Tutorial | [AI Codebase Knowledge Builder](https://zacharyhuang.substack.com/p/ai-codebase-knowledge-builder-full) |
| [Cursor](https://github.com/The-Pocket/PocketFlow-Tutorial-Cursor) | ★☆☆ <br> *Advanced* |  Project: Build Cursor with Cursor | [Build Cursor with Cursor](https://zacharyhuang.substack.com/p/building-cursor-with-cursor-a-step) |

</div>

## Request

👀 Want to see other tutorials? [Create an issue!](https://github.com/The-Pocket/PocketFlow/issues/new)
