
============================================================
PocketFlow Cookbook — 35 recipe(s)  [20260426_130705]
Adapter: ollama  Model: gemma3
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
[22] FAILED  (0.1s)  log: 22_pocketflow-google-calendar_20260426_130705.md

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
[23] FAILED  (5.8s)  log: 23_pocketflow-gradio-hitl_20260426_130705.md

[24] 24-pocketflow-heartbeat
     | 🚀 Starting Heartbeat Email Monitor
     |    Polling every 2 seconds for 4 cycles...
     | 
     | /home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py:44: UserWarning: Flow ends: 'None' not found in ['new_email']
     |   if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
     | /home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py:44: UserWarning: Flow ends: 'done' not found in ['default']
     |   if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
     | 
     | --- 💓 Heartbeat 1 ---
     |   📭 No new emails.
     | 
     | --- 💓 Heartbeat 2 ---
     |   📬 1 new email(s)!
     |   💡 Here's a one-sentence summary and suggested reply action:
     | 
     | **Summary:** Your boss needs the finalized Q3 report numbers submitted by Friday.
     | 
     | **Reply Action:** Respond immediately confirming receipt and stating you will deliver the report by the deadline.  (Example: "Received - Will deliver the Q3 report by Friday.")
     | 
     | --- 💓 Heartbeat 3 ---
     |   📭 No new emails.
     | 
     | --- 💓 Heartbeat 4 ---
     | 🛑 Max cycles reached. Stopping.
     | 
     | ✅ Monitor stopped.
     | 📊 Total emails processed: 1
[24] SUCCESS  (14.8s)  log: 24_pocketflow-heartbeat_20260426_130705.md

[25] 25-pocketflow-hello-world
     | Question: In one sentence, what's the end of universe?
     | Answer:   The ultimate end of the universe – often referred to as the "heat death" – is a state of maximum entropy where all energy is evenly distributed, and no further processes, including life, can occur.
[25] SUCCESS  (2.3s)  log: 25_pocketflow-hello-world_20260426_130705.md

[26] 26-pocketflow-invoice
     | 🧾 PocketFlow Invoice Processor
     | 
     | Error: 'data/invoice.pdf' not found.
     | Run 'python create_invoice.py' first to generate a sample invoice.
[26] FAILED  (0.3s)  log: 26_pocketflow-invoice_20260426_130705.md

[27] 27-pocketflow-judge
     | 🤔 Generating product description for: A noise-cancelling wireless headphone with 30-hour battery life
     | /home/gong2/projects/wgong/PocketFlow/pocketflow/__init__.py:44: UserWarning: Flow ends: 'pass' not found in ['fail']
     |   if not nxt and curr.successors: warnings.warn(f"Flow ends: '{action}' not found in {list(curr.successors)}")
     | 
     | ✍️  --- Draft (Attempt 1) ---
     | Escape the noise and immerse yourself in pure audio bliss with the AuraFlow Noise-Cancelling Headphones. Featuring powerful active noise cancellation and an incredible 30-hour battery life, you can enjoy your favorite music, podcasts, or audiobooks uninterrupted, wherever your day takes you.  Experience sound like never before – order your AuraFlow headphones today!
     | 
     | 🔍 Judge Score: 8/10
     | 💡 Reasoning: The description is generally clear and persuasive. It highlights key features (noise cancellation, battery life) and uses appealing language ("pure audio bliss," "experience sound like never before"). The call to action ("order your AuraFlow headphones today!") is effective. However, it could be slightly more specific about *who* would benefit from these headphones (e.g., commuters, students, frequent travelers) and perhaps a tiny detail about the sound quality beyond just "incredible" would strengthen it.
     | ✅ PASS - Description accepted!
     | 
     | === Final Result ===
     | 📝 Description: Escape the noise and immerse yourself in pure audio bliss with the AuraFlow Noise-Cancelling Headphones. Featuring powerful active noise cancellation and an incredible 30-hour battery life, you can enjoy your favorite music, podcasts, or audiobooks uninterrupted, wherever your day takes you.  Experience sound like never before – order your AuraFlow headphones today!
     | ⭐ Score:       8/10
     | ====================
[27] SUCCESS  (5.5s)  log: 27_pocketflow-judge_20260426_130705.md

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
     |   🟢 Sarah Chen (CTO): 9/10 — CTO at a Series A AI analytics company with a clear need for LLM tooling and an existing ML engineering team.
     |   🟢 Marcus Johnson (VP Engineering): 7/10 — VP Engineering at a growing cloud tools company with a recent AI code assistant launch - suggests potential LLM integration interest.
     |   🟢 Priya Patel (Head of AI): 6/10 — Head of AI at a seed-stage company pivoting to LLMs - likely exploring options but with limited existing infrastructure and resources.
     |   ✍️  Generating personalized emails for 3 qualified leads...
     |   ✅ Generated 3 personalized emails
     | 
     | ==================================================
     | 📧 Generated Emails
     | ==================================================
     | 
     | --- Sarah Chen (CTO @ DataStack AI) | Score: 9/10 ---
     | Subject: Streamlining LLM Development at DataStack AI
     | 
     | I noticed DataStack AI’s recent Series A funding and exciting work in LLM-powered analytics – particularly your focus on Python and AWS. Building AI apps with complex dependencies can significantly slow down development, and PocketFlow’s 100-line framework eliminates that hurdle entirely.  Would you be open to a 15-minute call to discuss how PocketFlow could accelerate your team’s innovation?
     | 
     | --- Marcus Johnson (VP Engineering @ CloudNine Labs) | Score: 7/10 ---
     | Subject: Streamlining AI Development at CloudNine Labs
     | 
     | I noticed CloudNine Labs’ recent AI code assistant launch – exciting work leveraging TypeScript and GCP! Many teams struggle with the complexity of managing LLM frameworks, leading to slower development cycles and increased dependencies. Would you be open to a 15-minute call to discuss how PocketFlow, our 100-line LLM framework, could accelerate your team’s AI app development?
     | 
     | --- Priya Patel (Head of AI @ FinBot) | Score: 6/10 ---
     | Subject: Streamlining FinBot's LLM Development
     | 
     | We noticed FinBot's recent pivot to an LLM-based chatbot – building complex AI applications with existing frameworks can be time-consuming and require significant dependency management. PocketFlow offers a 100-line LLM framework using Python and the OpenAI API, enabling rapid development without those complications. Would you be open to a 15-minute call to discuss how PocketFlow could accelerate FinBot’s innovation?
     | 
     | ✅ Saved to: output/emails.md
[28] SUCCESS  (10.1s)  log: 28_pocketflow-lead-generation_20260426_130705.md

[29] 29-pocketflow-llm-streaming
