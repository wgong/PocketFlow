
============================================================
PocketFlow Cookbook — 52 recipe(s)  [20260426_031022]
Adapter: ollama  Model: gemma3
============================================================

[01] 01-pocketflow-a2a
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-a2a/main.py", line 2, in <module>
     |     from flow import create_agent_flow
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-a2a/flow.py", line 2, in <module>
     |     from nodes import DecideAction, SearchWeb, AnswerQuestion
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-a2a/nodes.py", line 2, in <module>
     |     from utils import call_llm, search_web
     | ImportError: cannot import name 'search_web' from 'utils' (/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-a2a/utils.py)
[01] FAILED  (1.0s)  log: 01_pocketflow-a2a_20260426_031022.md

[02] 02-pocketflow-agent
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-agent/main.py", line 2, in <module>
     |     from flow import create_agent_flow
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-agent/flow.py", line 2, in <module>
     |     from nodes import DecideAction, SearchWeb, AnswerQuestion
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-agent/nodes.py", line 2, in <module>
     |     from utils import call_llm, search_web_duckduckgo
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-agent/utils.py", line 3, in <module>
     |     from ddgs import DDGS
     | ModuleNotFoundError: No module named 'ddgs'
[02] FAILED  (0.9s)  log: 02_pocketflow-agent_20260426_031022.md

[03] 03-pocketflow-agent-skills
     | 🧩 Task: Summarize this launch plan for a VP audience
     | 
     | === Skill Used ===
     | executive_brief
     | 
     | === Output ===
     | Okay, please provide the launch plan you want me to summarize for the VP audience. I’m ready when you are.
[03] SUCCESS  (2.0s)  log: 03_pocketflow-agent-skills_20260426_031022.md

[04] 04-pocketflow-agentic-rag
     | 🤔 Question: How do nodes work in PocketFlow?
     | 
     |   🔍 Agent decides to read 'nodes'
     |   📄 Reading document: nodes
     |   ✅ Added 'nodes' to context
     |   💡 Agent decides it has enough context to answer
     |   ✍️ Generating answer...
     | 
     | 🎯 Final Answer:
     | Nodes in PocketFlow consist of three phases: prep (reads shared store), exec (performs LLM calls), and post (writes back). Only the exec node retries on failure, and BatchNode handles lists.
[04] SUCCESS  (3.1s)  log: 04_pocketflow-agentic-rag_20260426_031022.md

[05] 05-pocketflow-async-basic
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-async-basic/main.py", line 2, in <module>
     |     from flow import create_flow
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-async-basic/flow.py", line 4, in <module>
     |     from nodes import FetchRecipes, SuggestRecipe, GetApproval
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-async-basic/nodes.py", line 2, in <module>
     |     from utils import fetch_recipes, call_llm_async, get_user_input
     | ImportError: cannot import name 'get_user_input' from 'utils' (/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-async-basic/utils.py)
[05] FAILED  (1.1s)  log: 05_pocketflow-async-basic_20260426_031022.md

[06] 06-pocketflow-batch
