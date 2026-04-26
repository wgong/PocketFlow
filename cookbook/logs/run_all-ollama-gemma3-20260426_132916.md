
============================================================
PocketFlow Cookbook — 23 recipe(s)  [20260426_132917]
Adapter: ollama  Model: gemma3
============================================================

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
[34] SUCCESS  (0.3s)  log: 34_pocketflow-nested-batch_20260426_132917.md

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
     |   💡 Selected 4 stories
     |   ✍️ Summarized 4 stories
     |   ✅ Newsletter formatted
     | 
     | 📰 Newsletter:
     | 
     | # AI Weekly Digest
     | 
     | ## 1. MIT Develops AI Tool for Faster, Higher-Quality Image Generation
     | Forget endless waiting! MIT's new AI model generates stunning images *fast* and with top-tier quality – this means faster design, marketing, and creative workflows for everyone.
     | 
     | ## 2. MIT Researchers Teach AI Models to Admit 'I Don't Know'
     | AI can't be right about everything, and these MIT researchers are fixing it!  Their 'Calibration Rewards' technique helps AI honestly admit when it's stumped, leading to more reliable and trustworthy results.
     | 
     | ## 3. Improving AI Models’ Ability to Explain Their Predictions
     | Ever wonder *why* an AI made a decision? MIT’s breakthrough transforms image recognition, finally offering transparent explanations and boosting trust in AI systems.
     | 
     | ## 4. AI Assist - Stack Overflow
     | Stack Overflow just got a serious upgrade! AI Assist uses AI to supercharge your coding searches, leading to faster problem-solving and a more efficient developer experience – because debugging shouldn’t feel like a maze.
     | 
     | ✅ Saved to: output/newsletter.md
[35] SUCCESS  (9.7s)  log: 35_pocketflow-newsletter_20260426_132917.md

[36] 36-pocketflow-node
     | 
     | Input:   PocketFlow is a minimalist LLM framework that models workflows as a Nested Direc...
     | 
     | Summary: **PocketFlow: Simple, nested LLM workflow automation with task decomposition.**
[36] SUCCESS  (1.8s)  log: 36_pocketflow-node_20260426_132917.md

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
     |   🔍 Extracted nuggets from 4 documents
     |   ✍️  Generated script with 10 lines
     |     Alex: Okay, Jamie, let's dive into this PocketFlow thing. They’re saying 'Zero Depende...
     |     Jamie: I know, right?! It sounds almost *too* good to be true. Like, most LLM framework...
     |     Alex: Wait, what? A *nested directed graph*? That’s… impressive. It's like they’re int...
     |     Jamie: Absolutely! It’s a brilliant contradiction. Let's shift gears. What about Node P...
     |     Alex: Seriously! It’s like they’re obsessive about performance. And the claim about 'C...
     |     Alex: Yeah, the '>>' thing is bizarre! Like they invented a new language just for this...
     |     Jamie: I know! 'Reflection' as a design pattern! It’s not a common term to begin with, ...
     |     Alex: And the ‘Agent for Autonomous Loops’ – an agent *within* a flow? That’s a huge l...
     |     Jamie: Exactly! It’s a step up in sophistication. I’m really fascinated by this. It see...
     |     Alex: Definitely. It’s a fascinating blend of minimalism and depth. I think we need to...
     |     🎙️  Generating audio for Alex (line 1/10)...
     |     🎙️  Generating audio for Jamie (line 2/10)...
     |     🎙️  Generating audio for Alex (line 3/10)...
     |     🎙️  Generating audio for Jamie (line 4/10)...
     |     🎙️  Generating audio for Alex (line 5/10)...
     |     🎙️  Generating audio for Alex (line 6/10)...
     |     🎙️  Generating audio for Jamie (line 7/10)...
     |     🎙️  Generating audio for Alex (line 8/10)...
     |     🎙️  Generating audio for Jamie (line 9/10)...
     |     🎙️  Generating audio for Alex (line 10/10)...
     |   ✅ Audio saved to output/podcast.mp3
     | ==================================================
     | Podcast saved to: output/podcast.mp3
     | ==================================================
[37] SUCCESS  (65.8s)  log: 37_pocketflow-notebook-lm_20260426_132917.md

[38] 38-pocketflow-parallel-batch
