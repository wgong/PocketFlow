# PocketFlow for SPL

## Objectives
- Use extensive PocketFlow cookbook recipes to generate .spl scripts
- validate SPL pipeline:
  - text2SPL: spec -> .spl
  - SPLc: .spl -> target: python/pocketflow
  - compare original PocketFlow recipe vs generated recipe
  - judge effectiveness of text2SPL and SPLc using various adapters
    - claude_cli / sonnet 4.6
    - ollama / gemma3

## Setup — LLM Adapter Shim

All recipes have been patched to use a shared `call_llm_shim.py` instead of
hardcoded OpenAI keys. The original `call_llm()` code is preserved inside an
`if False:` block and can be re-enabled at any time.

### Running a recipe

```bash
conda create -n pocket python=3.11
conda activate pocket
pip install -e .


```


```bash
# Ollama (local) — default
cd cookbook
pip install -r requirements.txt  # consolidated from all recipes

cd pocketflow-debate
SPL_ADAPTER=ollama SPL_MODEL=gemma3 python main.py

# Claude via claude CLI (no API key needed — uses `claude auth`)
cd pocketflow-debate
SPL_ADAPTER=claude_cli python main.py          # uses claude-sonnet-4-6 by default
SPL_ADAPTER=claude_cli SPL_MODEL=claude-sonnet-4-6 python main.py
```

### Environment variables

| Variable | Default | Description |
|---|---|---|
| `SPL_ADAPTER` | `ollama` | Backend: `ollama` or `claude_cli` |
| `SPL_MODEL` | `gemma3` (ollama) / `claude-sonnet-4-6` (claude_cli) | Model name |

### Re-applying or reverting patches

```bash
# Patch all recipes (idempotent — skips already-patched files)
python patch_call_llm.py

# Dry-run preview (no files written)
python patch_call_llm.py --dry-run

# Patch a single recipe
python patch_call_llm.py --recipe pocketflow-hello-world

# Revert all patches (restores original OpenAI code)
python patch_call_llm.py --revert
```

To manually re-enable the original OpenAI `call_llm()` in any recipe, open the
file and change `if False:  # [SPL-SHIM]` back to `if True:`.

---

## Running `run_all.py`

`run_all.py` is the batch runner for the SPL benchmark pipeline. It reads
`cookbook_catalog.json`, launches each active recipe's `main.py` with the
chosen adapter/model, and reports pass/fail per recipe.

### One-time setup

```bash
cd ~/projects/wgong/PocketFlow/cookbook
conda activate pocket
pip install -r requirements.txt
```

### List recipes

```bash
python run_all.py list           # all active recipes
python run_all.py list --all     # include inactive (review) recipes
python run_all.py catalog        # full detail with descriptions
```

### Check prerequisites

```bash
python run_all.py check          # verify Ollama is running, models pulled
```

### Run recipes

```bash
# Run all active recipes — Ollama backend (default)
SPL_ADAPTER=ollama SPL_MODEL=gemma3 python run_all.py

# Run with Claude CLI backend
SPL_ADAPTER=claude_cli SPL_MODEL=claude-sonnet-4-6 python run_all.py

# Run a single recipe by ID
SPL_ADAPTER=ollama SPL_MODEL=gemma3 python run_all.py --ids 6

# Run a range of recipes
SPL_ADAPTER=ollama SPL_MODEL=gemma3 python run_all.py --ids 1-10

# Parallel execution (4 workers)
SPL_ADAPTER=ollama SPL_MODEL=gemma3 python run_all.py --workers 4

# Save full output to log
SPL_ADAPTER=ollama SPL_MODEL=gemma3 \
python run_all.py run --timeout 180 \
    2>&1 | tee logs/run_all-claude_cli-$(date +%Y%m%d_%H%M%S).md


# Save full output to log
SPL_ADAPTER=claude_cli SPL_MODEL=claude-sonnet-4-6 \
python run_all.py run --timeout 180 \
    --ids "1-56" \
    2>&1 | tee logs/run_all-claude_cli-$(date +%Y%m%d_%H%M%S).md


## hang
# 21-pocketflow-flow
# 29-pocketflow-llm-streaming
# 38-pocketflow-parallel-batch

## infinite loop - should have max-iterations limit
# [33] 33-pocketflow-multi-agent 

Summary: 9/18 passed  (669.5s total)
Adapter: ollama  Model: gemma3

Failed:
  [41] 41-pocketflow-self-healing-mermaid
  [42] 42-pocketflow-streamlit-fsm
  [43] 43-pocketflow-structured-output
  [44] 44-pocketflow-supervisor
  [52] 52-pocketflow-tool-search
  [53] 53-pocketflow-tracing
  [54] 54-pocketflow-visualization
  [55] 55-pocketflow-voice-chat
  [56] 56-pocketflow-workflow


```

#### let fool cook good food

```output
Two Fools Add up to Good

Two fools walked into a virtual kitchen on an Sunday,
One with ideas, another one to play.
"Please improve PocketFlow recipes!" the first fool cried,
The second fool fixed them up — ready to fry.

One fool dreams in Python and SPL,
The other wraps functions in "if False:" spells.
One fool speaks Chinese, English, Physics and Math,
The other utters tokens — ten thousand or more.           

We run_all.py with a timeout of grace,
We tee the logs at a leisurely pace.
We fool around, we cook, we test,
Two fools together — beats the rest.                 

What is wisdom? Our playground is brain, 
With A human heart or a machine mind.
Stirring the pot till the good food smells —
Wen + Claude tastes Good, Hooray to Cheers.

```


### Output

Logs are written to `cookbook/logs/<recipe-id>_<timestamp>.md`.
A summary line is printed at the end:

```
============================================================
Summary: 52/56 passed  (184.3s total)

Failed:
  [12] pocketflow-deep-research
  ...
============================================================
```

---

## Manual Review

These recipes require human interaction (chat loop, HITL, server, audio, browser) and cannot be automated in `run_all.py`. Review and test each manually before enabling.

| Done | Recipe | Category | Note |
|------|--------|----------|------|
| [ ] | 05-pocketflow-async-basic | basics | Uses `get_user_input()` async prompt |
| [ ] | 09-pocketflow-chat | basics | Interactive chat loop via `input()` |
| [ ] | 10-pocketflow-chat-guardrail | safety | Interactive chat loop via `input()` |
| [ ] | 11-pocketflow-chat-memory | basics | Interactive chat loop via `input()` |
| [ ] | 12-pocketflow-cli-hitl | hitl | HITL approval step via `input()` |
| [ ] | 15-pocketflow-communication | basics | Interactive nodes via `input()` |
| [ ] | 18-pocketflow-fastapi-background | hitl | Starts FastAPI server — needs `uvicorn` |
| [ ] | 20-pocketflow-fastapi-websocket | hitl | Starts FastAPI WebSocket server |
| [ ] | 23-pocketflow-gradio-hitl | hitl | Starts Gradio UI server |
| [ ] | 29-pocketflow-llm-streaming | basics | Interactive streaming chat via `input()` |
| [ ] | 48-pocketflow-tool-crawler | tool | Prompts user for URL via `input()` |
| [ ] | 52-pocketflow-tool-search | tool | Prompts user for query via `input()` |
| [ ] | 55-pocketflow-voice-chat | application | Requires microphone hardware (sounddevice) |

---

## Workflow to port PocketFlow Cookbook

- create `cookbook_catalog.json` similar to `$HOME/projects/digital-duck/SPL.py/cookbook/cookbook_catalog.json`, name each recipe after the sub-folder name, assign an unique ID, analyze to arrive at a good description
- create `run_all.py` similar to `$HOME/projects/digital-duck/SPL.py/cookbook/run_all.py`
- execute `run_all.py` and fix any failure
- make sure `spl3 splc describe-all` works on `$HOME/projects/wgong/PocketFlow/cookbook` which will generate <recipe-name>-spec.md file inside their respective recipe folder
- Use `spl3 text2spl` to generate .spl script from <recipe-name>-spec.md (driven by Section 0 description)
- Use `spl3 splc` to generate pocketflow cookbook at `$HOME/projects/digital-duck/SPL.py/cookbook-pocketflow`
