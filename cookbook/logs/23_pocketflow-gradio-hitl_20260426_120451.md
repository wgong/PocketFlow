/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-gradio-hitl/main.py:88: UserWarning: The parameters have been moved from the Blocks constructor to the launch() method in Gradio 6.0: theme. Please pass these parameters to launch() instead.
  with gr.Blocks(fill_height=True, theme="ocean") as demo:
Traceback (most recent call last):
  File "/home/gong2/projects/wgong/PocketFlow/cookbook/pocketflow-gradio-hitl/main.py", line 92, in <module>
    chatbot = gr.Chatbot(type="messages", scale=1)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gong2/anaconda3/envs/pocket/lib/python3.11/site-packages/gradio/component_meta.py", line 194, in wrapper
    return fn(self, **kwargs)
           ^^^^^^^^^^^^^^^^^^
TypeError: Chatbot.__init__() got an unexpected keyword argument 'type'
