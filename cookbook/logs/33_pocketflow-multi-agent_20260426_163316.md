=========== Taboo Game Starting! ===========
Target word: nostalgic
Forbidden words: ['memory', 'past', 'remember', 'feeling', 'longing']
============================================
Traceback (most recent call last):
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 108, in <module>
    main()
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1514, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1435, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/click/core.py", line 853, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 104, in main
    asyncio.run(run_game(word, forbidden_list, max_turns=max_turns))
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 86, in run_game
    await asyncio.gather(
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 72, in run_async
    return await self._run_async(shared)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 87, in _run_async
    async def _run_async(self,shared): p=await self.prep_async(shared); o=await self._orch_async(shared); return await self.post_async(shared,p,o)
                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 85, in _orch_async
    while curr: curr.set_params(p); last_action=await curr._run_async(shared) if isinstance(curr,AsyncNode) else curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 73, in _run_async
    async def _run_async(self,shared): p=await self.prep_async(shared); e=await self._exec(p); return await self.post_async(shared,p,e)
                                                                          ^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 68, in _exec
    if self.cur_retry==self.max_retries-1: return await self.exec_fallback_async(prep_res,e)
                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 62, in exec_fallback_async
    async def exec_fallback_async(self,prep_res,exc): raise exc
                                                      ^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 66, in _exec
    try: return await self.exec_async(prep_res)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-multi-agent/main.py", line 22, in exec_async
    hint = call_llm(prompt)
           ^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 118, in call_llm
    return _claude_cli(prompt)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/call_llm_shim.py", line 84, in _claude_cli
    raise RuntimeError(f"Claude CLI Rate Limit: {out if out else err}")
RuntimeError: Claude CLI Rate Limit: You've hit your limit · resets 8:50pm (America/New_York)
