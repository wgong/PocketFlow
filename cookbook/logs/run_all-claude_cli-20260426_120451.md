
============================================================
PocketFlow Cookbook — 35 recipe(s)  [20260426_120451]
Adapter: claude_cli  Model: claude-sonnet-4-6
============================================================

[22] 22-pocketflow-google-calendar
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-google-calendar/main.py", line 4, in <module>
     |     from nodes import CreateCalendarEventNode, ListCalendarEventsNode, ListCalendarsNode
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-google-calendar/nodes.py", line 2, in <module>
     |     from utils.google_calendar import create_event, list_events, list_calendar_lists
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-google-calendar/utils/google_calendar.py", line 1, in <module>
     |     from google.oauth2.credentials import Credentials
     | ModuleNotFoundError: No module named 'google.oauth2'
[22] FAILED  (0.1s)  log: 22_pocketflow-google-calendar_20260426_120451.md

[23] 23-pocketflow-gradio-hitl
     | /home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-gradio-hitl/main.py:88: UserWarning: The parameters have been moved from the Blocks constructor to the launch() method in Gradio 6.0: theme. Please pass these parameters to launch() instead.
     |   with gr.Blocks(fill_height=True, theme="ocean") as demo:
     | Traceback (most recent call last):
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-gradio-hitl/main.py", line 92, in <module>
     |     chatbot = gr.Chatbot(type="messages", scale=1)
     |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/gradio/component_meta.py", line 194, in wrapper
     |     return fn(self, **kwargs)
     |            ^^^^^^^^^^^^^^^^^^
     | TypeError: Chatbot.__init__() got an unexpected keyword argument 'type'
[23] FAILED  (6.6s)  log: 23_pocketflow-gradio-hitl_20260426_120451.md

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
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 103, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 75, in _claude_cli
     |     raise RuntimeError(f"claude CLI error: {result.stderr.strip()}")
     | RuntimeError: claude CLI error:
[24] FAILED  (7.5s)  log: 24_pocketflow-heartbeat_20260426_120451.md

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
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 103, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 75, in _claude_cli
     |     raise RuntimeError(f"claude CLI error: {result.stderr.strip()}")
     | RuntimeError: claude CLI error:
[25] FAILED  (4.1s)  log: 25_pocketflow-hello-world_20260426_120451.md

[26] 26-pocketflow-invoice
     | 🧾 PocketFlow Invoice Processor
     | 
     | Error: 'data/invoice.pdf' not found.
     | Run 'python create_invoice.py' first to generate a sample invoice.
[26] FAILED  (0.5s)  log: 26_pocketflow-invoice_20260426_120451.md

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
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 103, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 75, in _claude_cli
     |     raise RuntimeError(f"claude CLI error: {result.stderr.strip()}")
     | RuntimeError: claude CLI error:
[27] FAILED  (33.8s)  log: 27_pocketflow-judge_20260426_120451.md

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
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 103, in call_llm
     |     return _claude_cli(prompt)
     |            ^^^^^^^^^^^^^^^^^^^
     |   File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 75, in _claude_cli
     |     raise RuntimeError(f"claude CLI error: {result.stderr.strip()}")
     | RuntimeError: claude CLI error:
[28] FAILED  (3.2s)  log: 28_pocketflow-lead-generation_20260426_120451.md

[29] 29-pocketflow-llm-streaming
