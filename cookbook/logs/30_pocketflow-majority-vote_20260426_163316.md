Traceback (most recent call last):
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-majority-vote/main.py", line 62, in <module>
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
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-majority-vote/main.py", line 55, in main
    Flow(start=MajorityVoteNode()).run(shared)
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 16, in run
    return self._run(shared)
           ^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 50, in _run
    def _run(self,shared): p=self.prep(shared); o=self._orch(shared); return self.post(shared,p,o)
                                                  ^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 48, in _orch
    while curr: curr.set_params(p); last_action=curr._run(shared); curr=copy.copy(self.get_next_node(curr,last_action))
                                                ^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py", line 13, in _run
    def _run(self,shared): p=self.prep(shared); e=self._exec(p); return self.post(shared,p,e)
                                                                        ^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-majority-vote/main.py", line 39, in post
    best, freq = collections.Counter(valid).most_common(1)[0]
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
IndexError: list index out of range
