
============================================================
PocketFlow Cookbook — 38 recipe(s)  [20260426_163316]
Adapter: claude_cli  Model: claude-sonnet-4-6
============================================================

[01] 01-pocketflow-a2a
     | 🤔 Processing question: Who won the Nobel Prize in Physics 2024?
     | 🤔 Agent deciding what to do next...
     | 💡 Agent decided to answer the question
     | ✍️ Crafting final answer...
     | ✅ Answer generated successfully
     | 
     | 🎯 Final Answer:
     | The 2024 Nobel Prize in Physics was awarded to **John J. Hopfield** and **Geoffrey E. Hinton** for their foundational contributions to machine learning with artificial neural networks.
     | 
     | - **John J. Hopfield** invented the *Hopfield network*, an associative memory model that can store and reconstruct patterns.
     | - **Geoffrey E. Hinton** developed the *Boltzmann machine*, which laid critical groundwork for modern deep learning.
     | 
     | Their work established the theoretical and practical foundations of the artificial neural network revolution that underpins today's AI systems.
[01] SUCCESS  (14.7s)  log: 01_pocketflow-a2a_20260426_163316.md

[02] 02-pocketflow-agent
     | 🤔 Processing question: chinese characters a new exploration from simplification to deeper understanding
     | 🤔 Agent deciding what to do next...
     | 💡 Agent decided to answer the question
     | ✍️ Crafting final answer...
     | ✅ Answer generated successfully
     | 
     | 🎯 Final Answer:
     | # Chinese Characters: From Simplification to Deeper Understanding
     | 
     | ## The Two Writing Systems
     | 
     | Chinese characters exist in two modern forms:
     | 
     | - **Traditional (繁體字)** — used in Taiwan, Hong Kong, Macau, and diaspora communities; preserves historical forms evolved over millennia
     | - **Simplified (简体字)** — standardized by the PRC in the 1950s–60s to boost literacy; reduced stroke counts but sometimes obscured original meaning
     | 
     | The key insight of this exploration: **simplified characters are a starting point, not an endpoint.**
     | 
     | ---
     | 
     | ## The Six Classical Categories (六書 Liùshū)
     | 
     | Ancient scholars classified characters into six types:
     | 
     | | Category | Chinese | Example |
     | |----------|---------|---------|
     | | Pictographs | 象形 | 日 (sun), 月 (moon), 山 (mountain) |
     | | Simple Ideographs | 指事 | 上 (above), 下 (below) |
     | | Compound Ideographs | 会意 | 明 (bright) = 日 + 月 |
     | | Phono-semantic compounds | 形声 | 请 (qǐng) = 讠(speech) + 青 (qīng) |
     | | Mutually explanatory | 转注 | — |
     | | Borrowings | 假借 | — |
     | 
     | > **Over 80% of modern characters are phono-semantic compounds** — one part signals meaning, the other signals pronunciation.
     | 
     | ---
     | 
     | ## Where Simplification Stripped Meaning
     | 
     | Some simplified characters lost their semantic depth:
     | 
     | | Simplified | Traditional | What Was Lost |
     | |------------|-------------|---------------|
     | | 爱 (ài, love) | 愛 | Removed 心 (heart) — love without a heart |
     | | 亲 (qīn, close/parent) | 親 | Removed 見 (see) — closeness without seeing |
     | | 讠(speech radical) | 言 | Condensed the full "word/speech" character |
     | 
     | Studying both forms together **restores the conceptual richness** the original designers embedded.
     | 
     | ---
     | 
     | ## The Radical System (部首)
     | 
     | Characters are organized by semantic radicals. Simplification sometimes merged or altered radicals, breaking visual connections. For example:
     | 
     | - 讠→ 言 (speech): The simplified radical is a mere abbreviation of the full character meaning "words/language"
     | - Recognizing the traditional radical reconnects the learner to the semantic family
     | 
     | ---
     | 
     | ## A Practical Learning Path
     | 
     | 1. **Learn** the simplified form and pronunciation
     | 2. **Compare** with the traditional counterpart
     | 3. **Trace back** to oracle bone script (甲骨文) or seal script forms
     | 4. **Identify** the radical (semantic) + phonetic components
     | 5. **Connect** the meaning to the original root imagery
     | 
     | ---
     | 
     | ## Classical Resources
     | 
     | - **说文解字 (Shuowen Jiezi, ~100 CE)** by Xu Shen — the foundational etymological dictionary analyzing ~9,000 characters; still the primary reference
     | - **甲骨文 (Oracle bone script)** — the earliest attested Chinese writing (~1200 BCE), reveals pictographic origins most clearly
     | - **Rick Harbaugh** — *Chinese Characters: A Genealogy and Dictionary* — maps character family trees
     | - **Outlier Linguistics** — systematically traces components to historical origins for modern learners
     | 
     | ---
     | 
     | ## Why This Approach Matters
     | 
     | - **Retention**: Visual mnemonics rooted in etymology are far more memorable than rote stroke memorization
     | - **Cultural access**: Characters encode philosophical and cultural worldviews — 安 (peace/safety) = woman 女 under a roof 宀
     | - **Cross-community literacy**: Bridges Mainland and Taiwan/Hong Kong reading communities
     | - **Classical Chinese**: Opens access to pre-modern literature, philosophy (Confucius, Laozi), and historical documents
     | 
     | The deeper truth this exploration reveals: **Chinese characters are not arbitrary symbols but a coherent visual language with logic, history, and philosophy embedded in every stroke.**
[02] SUCCESS  (68.8s)  log: 02_pocketflow-agent_20260426_163316.md

[03] 03-pocketflow-agent-skills
     | 🧩 Task   : Summarize this text for a VP audience
     | 
     | === Skill Used ===
     | executive_brief
     | 
     | === Output ===
     | Please provide the text you'd like me to summarize for the VP audience.
[03] SUCCESS  (12.8s)  log: 03_pocketflow-agent-skills_20260426_163316.md

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
     | In PocketFlow, nodes have three lifecycle methods:
     | 
     | - **`prep`** — reads data from the shared store (preparation)
     | - **`exec`** — performs the actual work (LLM calls, computations); this is the only method that retries on failure
     | - **`post`** — writes results back to the shared store
     | 
     | **`BatchNode`** is a specialized variant that handles list/batch inputs.
[04] SUCCESS  (14.7s)  log: 04_pocketflow-agentic-rag_20260426_163316.md

[06] 06-pocketflow-batch
     | Starting sequential translation into 8 languages...
     |   Translated: Chinese
     |   Translated: Spanish
     |   Translated: Japanese
     |   Translated: German
     |   Translated: Russian
     |   Translated: Portuguese
     |   Translated: French
     |   Translated: Korean
     |   Saved: output/translations/README_CHINESE.md
     |   Saved: output/translations/README_SPANISH.md
     |   Saved: output/translations/README_JAPANESE.md
     |   Saved: output/translations/README_GERMAN.md
     |   Saved: output/translations/README_RUSSIAN.md
     |   Saved: output/translations/README_PORTUGUESE.md
     |   Saved: output/translations/README_FRENCH.md
     |   Saved: output/translations/README_KOREAN.md
     | 
     | Total time: 850.25s
     | Translations saved to: output/translations
[06] SUCCESS  (851.3s)  log: 06_pocketflow-batch_20260426_163316.md

[07] 07-pocketflow-batch-flow
     | Processing images with filters...
     | Saved filtered image to: output/cat_grayscale.jpg
     | Saved filtered image to: output/cat_blur.jpg
     | Saved filtered image to: output/cat_sepia.jpg
     | Saved filtered image to: output/dog_grayscale.jpg
     | Saved filtered image to: output/dog_blur.jpg
     | Saved filtered image to: output/dog_sepia.jpg
     | Saved filtered image to: output/bird_grayscale.jpg
     | Saved filtered image to: output/bird_blur.jpg
     | Saved filtered image to: output/bird_sepia.jpg
     | 
     | All images processed successfully!
     | Check the 'output' directory for results.
[07] SUCCESS  (0.5s)  log: 07_pocketflow-batch-flow_20260426_163316.md

[08] 08-pocketflow-batch-node
     | Processing data/sales.csv in chunks...
     | 
     | Final Statistics:
     | - Total Sales: $999,359.04
     | - Average Sale: $99.94
     | - Total Transactions: 10,000
     | 
[08] SUCCESS  (0.9s)  log: 08_pocketflow-batch-node_20260426_163316.md

[13] 13-pocketflow-code-generator
     | Starting PocketFlow Code Generator...
     | /home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py:44: UserWarning: Flow ends: 'success' not found in ['failure']
     |   if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
     | 
     | === Generated 7 Test Cases ===
     | 1. Basic case - answer at start
     |    input: {'nums': [2, 7, 11, 15], 'target': 9}
     |    expected: [0, 1]
     | 2. Basic case - answer in middle
     |    input: {'nums': [3, 2, 4], 'target': 6}
     |    expected: [1, 2]
     | 3. Duplicate values
     |    input: {'nums': [3, 3], 'target': 6}
     |    expected: [0, 1]
     | 4. Negative numbers
     |    input: {'nums': [-3, 4, 3, 90], 'target': 0}
     |    expected: [0, 2]
     | 5. Mixed negative and positive target
     |    input: {'nums': [1, -2, 5, 8], 'target': 3}
     |    expected: [1, 2]
     | 6. Answer pair far apart in large array
     |    input: {'nums': [1, 3, 5, 7, 9, 11, 4], 'target': 5}
     |    expected: [0, 6]
     | 7. Minimum array size
     |    input: {'nums': [6, 4], 'target': 10}
     |    expected: [0, 1]
     | 
     | === Implemented Function ===
     | def run_code(nums, target):
     |     seen = {}
     |     for i, num in enumerate(nums):
     |         complement = target - num
     |         if complement in seen:
     |             return [seen[complement], i]
     |         seen[num] = i
     | 
     | === Test Results: 7/7 Passed ===
     | 
     | === Final Results ===
     | Problem:    Two Sum
     | 
     | Given an array of integers nums and an integer targ...
     | Iterations: 1
     | Tests:      7/7 passed
     | Function:
     | def run_code(nums, target):
     |     seen = {}
     |     for i, num in enumerate(nums):
     |         complement = target - num
     |         if complement in seen:
     |             return [seen[complement], i]
     |         seen[num] = i
     | 
     | ✅ Saved to: output/solution.py
[13] SUCCESS  (16.7s)  log: 13_pocketflow-code-generator_20260426_163316.md

[14] 14-pocketflow-coding-agent
     | ✅ Test project created in /home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-coding-agent/test_project
     |    Files: employees.csv, departments.csv, projects.csv, database.py, db.py, test_tokenizer.py, test_parser.py, test_executor.py
     | 🤖 Coding Agent starting...
     | 📋 Task: Implement the skeleton functions to make all tests pass. Run: python -m pytest test_tokenizer.py test_parser.py test_executor.py -v
     | 📁 Working in: /home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-coding-agent/test_project
     | 
     |   🔧 [1] run_command — Run the tests to see what's failing
     |   ✅ ============================= test session starts ==============================
     | platform linux -- Python 3.11.15, pytest-9.0.3, pluggy-1.6.0 -- /home/gong2/anaconda3/envs/pocket/bin/python
     | cachedir:
     |   🔧 [2] list_files — Need to see what files exist in the current directory
     |   ✅ departments.csv
     | test_parser.py
     | projects.csv
     | database.py
     | db.py
     | employees.csv
     | test_tokenizer.py
     | test_executor.py
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-coding-agent/main.py", line 25, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-coding-agent/main.py", line 20, in main
     |     create_coding_agent_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-coding-agent/nodes.py", line 76, in exec
     |     resp = call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[14] FAILED  (381.3s)  log: 14_pocketflow-coding-agent_20260426_163316.md

[16] 16-pocketflow-debate
     | 🤔 Debating claim: "Remote work is more productive than office work"
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-debate/main.py", line 30, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-debate/main.py", line 12, in main
     |     create_debate_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-debate/nodes.py", line 25, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[16] FAILED  (29.1s)  log: 16_pocketflow-debate_20260426_163316.md

[17] 17-pocketflow-deep-research
     | 🤔 Researching: The current state of quantum computing in 2025
     | 
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-deep-research/main.py", line 26, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-deep-research/main.py", line 14, in main
     |     create_deep_research_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-deep-research/nodes.py", line 32, in exec
     |     resp = call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[17] FAILED  (3.0s)  log: 17_pocketflow-deep-research_20260426_163316.md

[22] 22-pocketflow-google-calendar
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-google-calendar/main.py", line 4, in <module>
     |     from nodes import CreateCalendarEventNode, ListCalendarEventsNode, ListCalendarsNode
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-google-calendar/nodes.py", line 2, in <module>
     |     from utils.google_calendar import create_event, list_events, list_calendar_lists
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-google-calendar/utils/google_calendar.py", line 1, in <module>
     |     from google.oauth2.credentials import Credentials
     | ModuleNotFoundError: No module named 'google.oauth2'
[22] FAILED  (0.1s)  log: 22_pocketflow-google-calendar_20260426_163316.md

[24] 24-pocketflow-heartbeat
     | 🚀 Starting Heartbeat Email Monitor
     |    Polling every 2 seconds for 4 cycles...
     | 
     | /home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py:44: UserWarning: Flow ends: 'None' not found in ['new_email']
     |   if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
     | 
     | --- 💓 Heartbeat 1 ---
     |   📭 No new emails.
     | 
     | --- 💓 Heartbeat 2 ---
     |   📬 1 new email(s)!
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-heartbeat/main.py", line 18, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-heartbeat/main.py", line 12, in main
     |     create_heartbeat_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-heartbeat/nodes.py", line 49, in exec
     |     summary = call_llm(
     |               ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[24] FAILED  (6.9s)  log: 24_pocketflow-heartbeat_20260426_163316.md

[25] 25-pocketflow-hello-world
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-hello-world/main.py", line 22, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-hello-world/main.py", line 11, in main
     |     qa_flow.run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-hello-world/flow.py", line 12, in exec
     |     return call_llm(question)
     |            ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[25] FAILED  (3.9s)  log: 25_pocketflow-hello-world_20260426_163316.md

[26] 26-pocketflow-invoice
     | 🧾 PocketFlow Invoice Processor
     | 
     | Error: 'data/invoice.pdf' not found.
     | Run 'python create_invoice.py' first to generate a sample invoice.
[26] FAILED  (0.3s)  log: 26_pocketflow-invoice_20260426_163316.md

[27] 27-pocketflow-judge
     | 🤔 Generating product description for: A noise-cancelling wireless headphone with 30-hour battery life
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-judge/main.py", line 28, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-judge/main.py", line 12, in main
     |     create_judge_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-judge/nodes.py", line 23, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[27] FAILED  (28.7s)  log: 27_pocketflow-judge_20260426_163316.md

[28] 28-pocketflow-lead-generation
     | 🚀 Starting Lead-Generation Pipeline
     | ==================================================
     | 
     | 📋 Step 1 — Scraping leads
     | 🔍 Step 2 — Enriching leads
     | 🤔 Step 3 — Scoring leads with LLM
     | ✍️  Step 4 — Personalizing emails
     | 
     |   📋 Loaded 3 leads
     |   🔍 Enriched 3 leads with company intel
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-lead-generation/main.py", line 37, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-lead-generation/main.py", line 18, in main
     |     create_lead_generation_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-lead-generation/nodes.py", line 58, in exec
     |     resp = call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[28] FAILED  (3.2s)  log: 28_pocketflow-lead-generation_20260426_163316.md

[30] 30-pocketflow-majority-vote
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-majority-vote/main.py", line 62, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-majority-vote/main.py", line 55, in main
     |     Flow(start=MajorityVoteNode()).run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                                         ^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-majority-vote/main.py", line 39, in post
     |     best, freq = collections.Counter(valid).most_common(1)[0]
     |                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
     | IndexError: list index out of range
[30] FAILED  (16.9s)  log: 30_pocketflow-majority-vote_20260426_163316.md

[31] 31-pocketflow-map-reduce
     | Starting resume qualification processing...
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-map-reduce/main.py", line 21, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-map-reduce/main.py", line 10, in main
     |     create_resume_processing_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 37, in _exec
     |     def _exec(self,items): return [super(BatchNode,self)._exec(i) for i in (items or [])]
     |                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 37, in <listcomp>
     |     def _exec(self,items): return [super(BatchNode,self)._exec(i) for i in (items or [])]
     |                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-map-reduce/nodes.py", line 55, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[31] FAILED  (3.9s)  log: 31_pocketflow-map-reduce_20260426_163316.md

[32] 32-pocketflow-mcp
     | Processing question: What is 982713504867129384651 plus 73916582047365810293746529?
     | Getting available tools...
     | 
     | 
     | ╭──────────────────────────────────────────────────────────────────────────────╮
     | │                                                                              │
     | │                                                                              │
     | │                         ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                        │
     | │                         █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                        │
     | │                                                                              │
     | │                                                                              │
     | │                                                                              │
     | │                                FastMCP 3.2.4                                 │
     | │                            https://gofastmcp.com                             │
     | │                                                                              │
     | │                🖥  Server:      Math Operations Server, 3.2.4                 │
     | │                🚀 Deploy free: https://horizon.prefect.io                    │
     | │                                                                              │
     | ╰──────────────────────────────────────────────────────────────────────────────╯
     | 
     | 
     | [04/26/26 16:57:37] INFO     Starting MCP server 'Math          transport.py:209
     |                              Operations Server' with transport
     |                              'stdio'
     | Analyzing question and deciding which tool to use...
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-mcp/main.py", line 132, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-mcp/main.py", line 122, in main
     |     create_mcp_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-mcp/main.py", line 70, in exec
     |     return call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[32] FAILED  (6.1s)  log: 32_pocketflow-mcp_20260426_163316.md

[33] 33-pocketflow-multi-agent
     | =========== Taboo Game Starting! ===========
     | Target word: nostalgic
     | Forbidden words: ['memory', 'past', 'remember', 'feeling', 'longing']
     | ============================================
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 108, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 104, in main
     |     asyncio.run(run_game(word, forbidden_list, max_turns=max_turns))
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/runners.py", line 190, in run
     |     return runner.run(main)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/runners.py", line 118, in run
     |     return self._loop.run_until_complete(task)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
     |     return future.result()
     |            ^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 86, in run_game
     |     await asyncio.gather(
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 72, in run_async
     |     return await self._run_async(shared)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 87, in _run_async
     |     async def _run_async(self,shared): p=await self.prep_async(shared); o=await self._orch_async(shared); return await self.post_async(shared,p,o)
     |                                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 85, in _orch_async
     |     while curr: curr.set_params(p); last_action=await curr._run_async(shared) if isinstance(curr,AsyncNode) else curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 73, in _run_async
     |     async def _run_async(self,shared): p=await self.prep_async(shared); e=await self._exec(p); return await self.post_async(shared,p,e)
     |                                                                           ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 68, in _exec
     |     if self.cur_retry==self.max_retries-1: return await self.exec_fallback_async(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 62, in exec_fallback_async
     |     async def exec_fallback_async(self,prep_res,exc): raise exc
     |                                                       ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 66, in _exec
     |     try: return await self.exec_async(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 22, in exec_async
     |     hint = call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[33] FAILED  (4.0s)  log: 33_pocketflow-multi-agent_20260426_163316.md

[34] 34-pocketflow-nested-batch
     | Processing school grades...
     | 
     | - student2.txt: Average = 8.3
     | - student1.txt: Average = 8.2
     | Class A Average: 8.25
     | 
     | - student3.txt: Average = 7.3
     | - student4.txt: Average = 8.8
     | Class B Average: 8.08
     | 
     | School Average: 8.17
[34] SUCCESS  (0.1s)  log: 34_pocketflow-nested-batch_20260426_163316.md

[35] 35-pocketflow-newsletter
     | 🤔 Curating newsletter from 3 topics...
     | 
     | /home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-newsletter/utils.py:33: RuntimeWarning: This package (`duckduckgo_search`) has been renamed to `ddgs`! Use `pip install ddgs` instead.
     |   results = DDGS().text(query, max_results=max_results)
     | /home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-newsletter/utils.py:33: RuntimeWarning: This package (`duckduckgo_search`) has been renamed to `ddgs`! Use `pip install ddgs` instead.
     |   results = DDGS().text(query, max_results=max_results)
     | /home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-newsletter/utils.py:33: RuntimeWarning: This package (`duckduckgo_search`) has been renamed to `ddgs`! Use `pip install ddgs` instead.
     |   results = DDGS().text(query, max_results=max_results)
     |   🔍 Searching: AI agents framework news this week
     |   🔍 Searching: LLM benchmark results 2025 2026
     |   🔍 Searching: AI startup funding rounds this month
     |   📚 Curated 3 topic searches
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-newsletter/main.py", line 31, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-newsletter/main.py", line 19, in main
     |     create_newsletter_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-newsletter/nodes.py", line 56, in exec
     |     resp = call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[35] FAILED  (3.6s)  log: 35_pocketflow-newsletter_20260426_163316.md

[36] 36-pocketflow-node
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-node/flow.py", line 14, in exec
     |     summary = call_llm(prompt)  # might fail
     |               ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
     | 
     | During handling of the above exception, another exception occurred:
     | 
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-node/main.py", line 36, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-node/main.py", line 24, in main
     |     flow.run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     | TypeError: Summarize.exec_fallback() missing 1 required positional argument: 'exc'
[36] FAILED  (9.4s)  log: 36_pocketflow-node_20260426_163316.md

[37] 37-pocketflow-notebook-lm
     | Starting Podcast Generation Pipeline
     | ==================================================
     |   4 source documents
     |   Output: output/podcast.mp3
     | 
     | Step 1 — Analyzing documents for interesting nuggets
     | Step 2 — Writing conversational podcast script
     | Step 3 — Converting script to audio with TTS
     | 
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-notebook-lm/main.py", line 38, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-notebook-lm/main.py", line 29, in main
     |     create_podcast_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-notebook-lm/nodes.py", line 26, in exec
     |     return call_llm(prompt)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[37] FAILED  (3.1s)  log: 37_pocketflow-notebook-lm_20260426_163316.md

[38] 38-pocketflow-parallel-batch
     | Starting parallel translation into 8 languages...
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-parallel-batch/main.py", line 87, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-parallel-batch/main.py", line 79, in main
     |     asyncio.run(create_parallel_translation_flow().run_async(shared))
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/runners.py", line 190, in run
     |     return runner.run(main)
     |            ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/runners.py", line 118, in run
     |     return self._loop.run_until_complete(task)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
     |     return future.result()
     |            ^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 72, in run_async
     |     return await self._run_async(shared)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 87, in _run_async
     |     async def _run_async(self,shared): p=await self.prep_async(shared); o=await self._orch_async(shared); return await self.post_async(shared,p,o)
     |                                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 85, in _orch_async
     |     while curr: curr.set_params(p); last_action=await curr._run_async(shared) if isinstance(curr,AsyncNode) else curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 73, in _run_async
     |     async def _run_async(self,shared): p=await self.prep_async(shared); e=await self._exec(p); return await self.post_async(shared,p,e)
     |                                                                           ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 80, in _exec
     |     async def _exec(self,items): return await asyncio.gather(*(super(AsyncParallelBatchNode,self)._exec(i) for i in items))
     |                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 68, in _exec
     |     if self.cur_retry==self.max_retries-1: return await self.exec_fallback_async(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 62, in exec_fallback_async
     |     async def exec_fallback_async(self,prep_res,exc): raise exc
     |                                                       ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 66, in _exec
     |     try: return await self.exec_async(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-parallel-batch/main.py", line 30, in exec_async
     |     result = await call_llm(prompt)
     |              ^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 125, in call_llm_async
     |     return await loop.run_in_executor(None, call_llm, prompt_or_messages)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/concurrent/futures/thread.py", line 58, in run
     |     result = self.fn(*self.args, **self.kwargs)
     |              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[38] FAILED  (18.2s)  log: 38_pocketflow-parallel-batch_20260426_163316.md

[39] 39-pocketflow-parallel-batch-flow
     | Found 3 images:
     |   - images/dog.jpg
     |   - images/bird.jpg
     |   - images/cat.jpg
     | 
     | Running sequential batch flow...
     | Processing 3 images with 3 filters...
     | Total combinations: 9
     | Loading image: images/dog.jpg
     | Applying grayscale filter...
     | Saved: output/dog_grayscale.jpg
     | Loading image: images/dog.jpg
     | Applying blur filter...
     | Saved: output/dog_blur.jpg
     | Loading image: images/dog.jpg
     | Applying sepia filter...
     | Saved: output/dog_sepia.jpg
     | Loading image: images/bird.jpg
     | Applying grayscale filter...
     | Saved: output/bird_grayscale.jpg
     | Loading image: images/bird.jpg
     | Applying blur filter...
     | Saved: output/bird_blur.jpg
     | Loading image: images/bird.jpg
     | Applying sepia filter...
     | Saved: output/bird_sepia.jpg
     | Loading image: images/cat.jpg
     | Applying grayscale filter...
     | Saved: output/cat_grayscale.jpg
     | Loading image: images/cat.jpg
     | Applying blur filter...
     | Saved: output/cat_blur.jpg
     | Loading image: images/cat.jpg
     | Applying sepia filter...
     | Saved: output/cat_sepia.jpg
     | 
     | Running parallel batch flow...
     | Processing 3 images with 3 filters...
     | Total combinations: 9
     | Loading image: images/dog.jpg
     | Loading image: images/dog.jpg
     | Loading image: images/dog.jpg
     | Loading image: images/bird.jpg
     | Loading image: images/bird.jpg
     | Loading image: images/bird.jpg
     | Loading image: images/cat.jpg
     | Loading image: images/cat.jpg
     | Loading image: images/cat.jpg
     | Applying grayscale filter...
     | Applying blur filter...
     | Applying sepia filter...
     | Applying grayscale filter...
     | Applying blur filter...
     | Applying sepia filter...
     | Applying grayscale filter...
     | Applying blur filter...
     | Applying sepia filter...
     | Saved: output/dog_grayscale.jpg
     | Saved: output/dog_blur.jpg
     | Saved: output/dog_sepia.jpg
     | Saved: output/bird_grayscale.jpg
     | Saved: output/bird_blur.jpg
     | Saved: output/bird_sepia.jpg
     | Saved: output/cat_grayscale.jpg
     | Saved: output/cat_blur.jpg
     | Saved: output/cat_sepia.jpg
     | 
     | Timing Results:
     |   Sequential: 14.24s
     |   Parallel:   2.00s
     |   Speedup:    7.12x
     | 
     | Processing complete! Check the output/ directory for results.
[39] SUCCESS  (16.5s)  log: 39_pocketflow-parallel-batch-flow_20260426_163316.md

[40] 40-pocketflow-rag
     | ==================================================
     | PocketFlow RAG Document Retrieval
     | Documents: 5  |  Query: How to install PocketFlow?
     | ==================================================
     | ✅ Created 5 chunks from 5 documents
     | ✅ Created 5 document embeddings
     | 🔍 Creating search index...
     | ✅ Index created with 5 vectors
     | 🔍 Embedding query: How to install PocketFlow?
     | 🔎 Searching for relevant documents...
     | 📄 Retrieved document (index: 0, distance: 0.2701)
     | 📄 Most relevant text: "Pocket Flow is a 100-line minimalist LLM framework. Lightweight, zero bloat, zero dependencies, zero vendor lock-in. Install: pip install pocketflow"
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-rag/main.py", line 61, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-rag/main.py", line 50, in main
     |     online_flow.run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-rag/nodes.py", line 135, in exec
     |     answer = call_llm(prompt)
     |              ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[40] FAILED  (8.9s)  log: 40_pocketflow-rag_20260426_163316.md

[41] 41-pocketflow-self-healing-mermaid
     | 🎨 PocketFlow Self-Healing Mermaid Generator
     | 
     | 🤔 Task: A flowchart showing a CI/CD pipeline: code push triggers build, then parallel test and lint, then deploy to staging, manual approval, deploy to production
     | 
     | ✍️  Generating Mermaid diagram...
     | ✍️  Generating Mermaid diagram...
     | ✍️  Generating Mermaid diagram...
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-self-healing-mermaid/main.py", line 44, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-self-healing-mermaid/main.py", line 21, in main
     |     create_mermaid_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-self-healing-mermaid/nodes.py", line 35, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[41] FAILED  (18.6s)  log: 41_pocketflow-self-healing-mermaid_20260426_163316.md

[43] 43-pocketflow-structured-output
     | === Resume Parser — Structured Output ===
     | 
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-structured-output/main.py", line 103, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-structured-output/main.py", line 77, in main
     |     Flow(start=ResumeParserNode(max_retries=3, wait=10)).run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-structured-output/main.py", line 48, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[43] FAILED  (30.3s)  log: 43_pocketflow-structured-output_20260426_163316.md

[44] 44-pocketflow-supervisor
     | 🤔 Processing question: Who won the Nobel Prize in Physics 2024?
     | 🤔 Agent deciding what to do next...
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-supervisor/main.py", line 24, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-supervisor/main.py", line 12, in main
     |     create_agent_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-supervisor/nodes.py", line 54, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[44] FAILED  (3.9s)  log: 44_pocketflow-supervisor_20260426_163316.md

[45] 45-pocketflow-tao
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-tao/main.py", line 31, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-tao/main.py", line 16, in main
     |     create_tao_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-tao/nodes.py", line 56, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[45] FAILED  (3.8s)  log: 45_pocketflow-tao_20260426_163316.md

[46] 46-pocketflow-text2sql
     | 
     | === Text-to-SQL ===
     | Query:    total products per category
     | Database: ecommerce.db
     | ====================================
     | 
     | ===== DB SCHEMA =====
     | 
     | Table: customers
     |   - customer_id (INTEGER)
     |   - first_name (TEXT)
     |   - last_name (TEXT)
     |   - email (TEXT)
     |   - registration_date (DATE)
     |   - city (TEXT)
     |   - country (TEXT)
     | 
     | Table: sqlite_sequence
     |   - name ()
     |   - seq ()
     | 
     | Table: products
     |   - product_id (INTEGER)
     |   - name (TEXT)
     |   - description (TEXT)
     |   - category (TEXT)
     |   - price (REAL)
     |   - stock_quantity (INTEGER)
     | 
     | Table: orders
     |   - order_id (INTEGER)
     |   - customer_id (INTEGER)
     |   - order_date (TIMESTAMP)
     |   - status (TEXT)
     |   - total_amount (REAL)
     |   - shipping_address (TEXT)
     | 
     | Table: order_items
     |   - order_item_id (INTEGER)
     |   - order_id (INTEGER)
     |   - product_id (INTEGER)
     |   - quantity (INTEGER)
     |   - price_per_unit (REAL)
     | 
     | =====================
     | 
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-text2sql/main.py", line 41, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-text2sql/main.py", line 31, in main
     |     create_text_to_sql_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-text2sql/nodes.py", line 52, in exec
     |     llm_response = call_llm(prompt)
     |                    ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[46] FAILED  (3.9s)  log: 46_pocketflow-text2sql_20260426_163316.md

[47] 47-pocketflow-thinking
     | 🤔 Processing question: You keep rolling a fair die until you roll three, four, five in that order consecutively on three rolls. What is the probability that you roll the die an odd number of times?
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-thinking/main.py", line 33, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-thinking/main.py", line 24, in main
     |     create_chain_of_thought_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-thinking/nodes.py", line 196, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[47] FAILED  (30.1s)  log: 47_pocketflow-thinking_20260426_163316.md

[49] 49-pocketflow-tool-database
     | Database Status: Database initialized
     | Task Status:     Task created successfully
     | 
     | All Tasks:
     |   [1] Example Task | pending | 2025-03-02 05:10:57
     |        This is an example task created using PocketFlow
     |   [2] Example Task | pending | 2026-04-26 17:45:48
     |        This is an example task created using PocketFlow
     |   [3] Example Task | pending | 2026-04-26 21:00:14
     |        This is an example task created using PocketFlow
[49] SUCCESS  (0.1s)  log: 49_pocketflow-tool-database_20260426_163316.md

[50] 50-pocketflow-tool-embeddings
     | Text:                What's the meaning of life?
     | Embedding dimension: 1536
     | First 5 values:      [0.003033011918887496, -0.028630640357732773, -0.0036315510515123606, 0.0031942762434482574, -0.017577823251485825]
[50] SUCCESS  (1.9s)  log: 50_pocketflow-tool-embeddings_20260426_163316.md

[51] 51-pocketflow-tool-pdf-vision
     | Found 1 PDF files
     | 
     | Processing: pocket-flow.pdf
     | --------------------------------------------------
     | 
     | File: pocket-flow.pdf
     | --------------------------------------------------
     | === Page 1 ===
     | ```plaintext
     | 3/2/25, 2:44 AM                                                       Home | Pocket Flow
     | 
     | Pocket Flow
     | 
     | Pocket Flow
     | 
     | A 100-line minimalist LLM framework for Agents, Task Decomposition, RAG, etc.
     | 
     | We model the LLM workflow as a Nested Directed Graph:
     | 
     | •  Nodes handle simple (LLM) tasks.
     | •  Nodes connect through Actions (labeled edges) for Agents.
     | •  Flows orchestrate a directed graph of Nodes for Task Decomposition.
     | •  A Flow can be used as a Node (for Nesting).
     | •  Batch Nodes/Flows for data-intensive tasks.
     | •  Async Nodes/Flows allow waits or Parallel execution
     | 
     | POCKET FLOW                                                             POCKET FLOW
     | 
     |               34%                                                                        34%
     | 
     |                                       LANGCHAIN, CREW, VLLM,
     |                                       RAYSERVE, SEMANTIC
     |                                       KERNEL, AUTO GPT...
     | 
     |    0.1%            2%
     | 
     | 0                   55                      70                            85                         100                       115 145             >115
     | 
     | 0.1%       14%                           14%                                                                                2%         0.1%
     | 
     | NOTE
     | 
     | https://the-pocket.github.io/PocketFlow/                                                                                                                                              1/3
     | ```
     | 
     | === Page 2 ===
     | ```plaintext
     | 3/2/25, 2:44 AM                                           Home | Pocket Flow
     | 
     | Pocket Flow                                         Have questions? Chat with AI Assistant
     | 
     | Core Abstraction
     | • Node
     | • Flow
     | • Communication
     | • Batch
     | • (Advanced) Async
     | • (Advanced) Parallel
     | 
     | Utility Function
     | • LLM Wrapper
     | • Tool
     | • Viz and Debug
     | • Chunking
     | 
     | WARNING
     | We do not provide built-in utility functions. Example implementations are provided as reference.
     | 
     | Design Pattern
     | • Structured Output
     | • Workflow
     | 
     | https://the-pocket.github.io/PocketFlow/                                                                         2/3
     | ```
     | 
     | === Page 3 ===
     | Sure, here is the extracted text preserving the formatting and layout:
     | 
     | ```
     | 3/2/25, 2:44 AM                                            Home | Pocket Flow
     | 
     | Pocket Flow
     | 
     |     •  Map Reduce
     |     •  RAG
     |     •  Chat Memory
     |     •  Agent
     |     •  (Advanced) Multi-Agents
     |     •  Evaluation
     | 
     | LLM Application Development Playbook
     | 
     | https://the-pocket.github.io/PocketFlow/                       3/3
     | ```
     | 
     | 
     | ✅ Saved to: output/extracted_text.md
[51] SUCCESS  (12.3s)  log: 51_pocketflow-tool-pdf-vision_20260426_163316.md

[56] 56-pocketflow-workflow
     | 
     | === Article Workflow: AI Safety ===
     | 
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-workflow/main.py", line 29, in <module>
     |     main()
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
     |     return self.main(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
     |     rv = self.invoke(ctx)
     |          ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
     |     return ctx.invoke(self.callback, **ctx.params)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
     |     return callback(*args, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-workflow/main.py", line 14, in main
     |     create_article_flow().run(shared)
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
     |     return self._run(shared)
     |            ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
     |     def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
     |                                                   ^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
     |     while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
     |                                                 ^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
     |     def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
     |                                                   ^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 33, in _exec
     |     if self.cur_retry==self.max_retries-1: return self.exec_fallback(prep_res,e)
     |                                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 28, in exec_fallback
     |     def exec_fallback(self,prep_res,exc): raise exc
     |                                           ^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 31, in _exec
     |     try: return self.exec(prep_res)
     |                 ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-workflow/nodes.py", line 26, in exec
     |     response = call_llm(prompt)
     |                ^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
     |     raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
     | RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
[56] FAILED  (3.7s)  log: 56_pocketflow-workflow_20260426_163316.md


============================================================
Summary: 13/38 passed  (1636.3s total)
Adapter: claude_cli  Model: claude-sonnet-4-6

Failed:
  [14] 14-pocketflow-coding-agent
  [16] 16-pocketflow-debate
  [17] 17-pocketflow-deep-research
  [22] 22-pocketflow-google-calendar
  [24] 24-pocketflow-heartbeat
  [25] 25-pocketflow-hello-world
  [26] 26-pocketflow-invoice
  [27] 27-pocketflow-judge
  [28] 28-pocketflow-lead-generation
  [30] 30-pocketflow-majority-vote
  [31] 31-pocketflow-map-reduce
  [32] 32-pocketflow-mcp
  [33] 33-pocketflow-multi-agent
  [35] 35-pocketflow-newsletter
  [36] 36-pocketflow-node
  [37] 37-pocketflow-notebook-lm
  [38] 38-pocketflow-parallel-batch
  [40] 40-pocketflow-rag
  [41] 41-pocketflow-self-healing-mermaid
  [43] 43-pocketflow-structured-output
  [44] 44-pocketflow-supervisor
  [45] 45-pocketflow-tao
  [46] 46-pocketflow-text2sql
  [47] 47-pocketflow-thinking
  [56] 56-pocketflow-workflow
============================================================

