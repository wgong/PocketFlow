# PocketFlow - Minimalist LLM Framework

PocketFlow is a minimalist, 100-line LLM framework designed for **Agentic Coding**, where humans design the architecture and AI agents implement the logic. It provides a lightweight yet expressive core abstraction based on **Graphs** (Nodes and Flows).

## Project Overview

- **Core Philosophy**: Zero bloat, zero dependencies, and zero vendor lock-in.
- **Main Technologies**: Python (Sync and Async support).
- **Primary Abstraction**: 
  - **Node**: The atomic unit of work, encapsulating preparation, execution, and post-processing.
  - **Flow**: A graph orchestrator that manages the execution sequence and transitions between nodes.
- **Key Features**: 
  - Retries and fallbacks.
  - Batch processing (Sequential and Parallel).
  - First-class Asynchronous support (`AsyncNode`, `AsyncFlow`, etc.).
  - Conditional branching based on node outputs.

## Architecture

The framework is contained entirely within `pocketflow/__init__.py`.

### Core Classes
- **`BaseNode`**: Foundation for all nodes. Handles transitions and shared state interaction.
- **`Node`**: Extends `BaseNode` with `max_retries` and `wait` (retry delay) logic.
- **`Flow`**: Orchestrates nodes. Nodes are connected using the `>>` operator (default transition) or conditional transitions.
- **`BatchNode` / `BatchFlow`**: Handle sequential processing of item lists.
- **`Async` variants**: `AsyncNode`, `AsyncFlow`, `AsyncBatchNode`, `AsyncParallelBatchNode`, `AsyncParallelBatchFlow`, etc., for high-performance concurrent operations.

## Building and Running

### Installation
```bash
pip install pocketflow
```
Alternatively, since the core is only 100 lines, you can directly copy `pocketflow/__init__.py` into your project.

### Running Examples (Cookbook)
The `cookbook/` directory contains numerous examples (Chat, RAG, Multi-Agent, etc.).
To run an example:
1. Navigate to the example directory: `cd cookbook/pocketflow-hello-world`
2. Install specific requirements: `pip install -r requirements.txt` (if present)
3. Run the main script: `python main.py`

## Testing

The project uses `unittest` for its test suite.
To run all tests:
```bash
python -m unittest discover tests
```
Or specifically:
```bash
python -m unittest tests/test_flow_basic.py
```

## Development Conventions

### 1. Node Implementation
Subclass `Node` or `AsyncNode` and implement these methods:
- `prep(self, shared)`: Extract data from the `shared` dictionary.
- `exec(self, prep_res)`: Perform the core logic (e.g., LLM call).
- `post(self, shared, prep_res, exec_res)`: Store results back in `shared`. Return a string for conditional branching.

### 2. Flow Construction
- **Linear**: `flow.start(node1) >> node2 >> node3`
- **Conditional**: `node1 - "success" >> node2` and `node1 - "failure" >> node3`
- **Execution**: `flow.run(shared_dict)`

### 3. Shared State
Data is passed between nodes via a `shared` dictionary. Nodes should be decoupled, relying only on this shared storage for context and results.

### 4. Async Usage
When using `AsyncFlow`, ensure all nodes in the flow are either `AsyncNode` or handled appropriately within the async loop. Use `await flow.run_async(shared)` to execute.

## Documentation
Comprehensive guides and design patterns are available in the `docs/` directory and at [the-pocket.github.io/PocketFlow/](https://the-pocket.github.io/PocketFlow/).
