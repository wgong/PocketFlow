<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100行极简LLM框架" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | 中文 | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow 是一个 [100行](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) 的极简LLM框架

- **轻量级**：仅100行代码。零冗余、零依赖、零供应商锁定。
  
- **表达力强**：您所喜爱的一切——([多](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)、[工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)、[RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) 等，一应俱全。

- **[智能体编程](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**：让AI智能体（如Cursor AI）来构建智能体——生产力提升10倍！

开始使用 Pocket Flow：
- 安装方式：```pip install pocketflow```，或直接复制 [源代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)（仅100行）。
- 了解更多，请查看 [视频教程](https://youtu.be/0Zr3NwcvpA0) 和 [文档](https://the-pocket.github.io/PocketFlow/)
- 🎉 加入我们的 [Discord](https://discord.gg/hUHHE9Sa6T)，与其他使用 Pocket Flow 的开发者交流！
- 🎉 Pocket Flow 现已推出 [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript)、[Java](https://github.com/The-Pocket/PocketFlow-Java)、[C++](https://github.com/The-Pocket/PocketFlow-CPP)、[Go](https://github.com/The-Pocket/PocketFlow-Go)、[Rust](https://github.com/The-Pocket/PocketFlow-Rust) 和 [PHP](https://github.com/The-Pocket/PocketFlow-PHP) 版本！

## 为什么选择 Pocket Flow？

现有的LLM框架过于臃肿……构建LLM框架只需100行代码！

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **抽象层**          | **应用专属封装**                                      | **供应商专属封装**                                    | **代码行数**       | **体积**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | 智能体、链               | 众多 <br><sup><sub>（如：问答、摘要生成）</sub></sup>              | 众多 <br><sup><sub>（如：OpenAI、Pinecone 等）</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | 智能体、链            | 众多 <br><sup><sub>（如：FileReadTool、SerperDevTool）</sub></sup>         | 众多 <br><sup><sub>（如：OpenAI、Anthropic、Pinecone 等）</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | 智能体                      | 部分 <br><sup><sub>（如：CodeAgent、VisitWebTool）</sub></sup>         | 部分 <br><sup><sub>（如：DuckDuckGo、Hugging Face 等）</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | 智能体、图           | 部分 <br><sup><sub>（如：语义搜索）</sub></sup>                     | 部分 <br><sup><sub>（如：PostgresStore、SqliteSaver 等） </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | 智能体                | 部分 <br><sup><sub>（如：工具智能体、聊天智能体）</sub></sup>              | 众多 <sup><sub>[可选]<br> （如：OpenAI、Pinecone 等）</sub></sup>        | 7K <br><sup><sub>（仅核心）</sub></sup>    | +26MB <br><sup><sub>（仅核心）</sub></sup>          |
| **PocketFlow** | **图**                    | **无**                                                 | **无**                                                  | **100**       | **+56KB**                  |

</div>

## Pocket Flow 是如何工作的？

这 [100行代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) 捕捉了LLM框架的核心抽象：图！
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

在此基础上，可以轻松实现流行的设计模式，如（[多](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html)）[智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)、[工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)、[RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) 等。
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ 以下是基础教程：

<div align="center">
  
|  名称  | 难度    |  描述  |  
| :-------------:  | :-------------: | :--------------------- |  
| [聊天机器人](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*入门*</sup>  | 带有对话历史的基础聊天机器人 |
| [结构化输出](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*入门*</sup> | 通过提示词从简历中提取结构化数据 |
| [工作流](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*入门*</sup> | 包含大纲生成、内容撰写和样式应用的写作工作流 |
| [智能体](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*入门*</sup>  | 可搜索网页并回答问题的研究型智能体 |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*入门*</sup> | 简单的检索增强生成流程 |
| [批处理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*入门*</sup> | 将Markdown翻译成多种语言的批处理器 |
| [流式输出](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*入门*</sup> | 带有用户中断功能的实时LLM流式输出演示 |
| [聊天护栏](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*入门*</sup> | 仅处理旅行相关问题的旅行顾问聊天机器人 |
| [多数投票](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*入门*</sup> | 通过汇总多次求解结果提升推理准确性 |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*入门*</sup>  | 使用Map-Reduce模式批量处理简历资质筛选 |
| [命令行人机协作](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*入门*</sup>  | 带有人工反馈的命令行笑话生成器 |
| [多智能体](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*初级*</sup> | 两个智能体之间异步通信的禁忌词游戏 |
| [监督者](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*初级*</sup> | 研究智能体变得不可靠了……让我们构建一个监督流程 |
| [并行](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*初级*</sup> | 展示3倍速度提升的并行执行演示 |
| [并行流](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*初级*</sup> | 展示8倍速度提升的并行图像处理 |
| [思维链](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*初级*</sup> | 通过思维链解决复杂推理问题 |
| [记忆](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*初级*</sup> | 具有短期和长期记忆的聊天机器人 |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*初级*</sup>  | 通过自动调试循环将自然语言转换为SQL查询 |
| [代码生成器](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*初级*</sup> | 生成测试用例、实现解决方案并迭代优化代码 |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*初级*</sup> |  使用模型上下文协议进行数值运算的智能体 |
| [智能体技能](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*初级*</sup> | 将请求路由到可复用的Markdown技能并在智能体流中应用 |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*初级*</sup> | 封装A2A协议实现智能体间通信的智能体 |
| [Streamlit 有限状态机](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*初级*</sup> | 带有有限状态机的Streamlit应用，用于人机协作图像生成 |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*初级*</sup> | 通过WebSocket实现流式LLM响应的实时聊天界面 |
| [FastAPI 后台任务](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*初级*</sup> | 带有后台任务和SSE实时进度的FastAPI应用 |
| [语音聊天](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*初级*</sup> | 集成VAD、STT、LLM和TTS的交互式语音聊天应用 |
| [评判者](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*初级*</sup> | 用于迭代内容优化的LLM评判-优化循环 |
| [辩论](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*初级*</sup> | 两位辩手与一位公正裁判的对抗性推理 |
| [智能体RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*初级*</sup> | 由智能体驱动、自主决定阅读哪些文档的RAG |
| [自愈Mermaid](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*初级*</sup> | 具有自动错误恢复功能的Mermaid图表生成 |
| [心跳监控](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*初级*</sup> | 类似ClawBot的嵌套流周期性常驻监控 |
| [线索生成](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*中级*</sup> | 销售管道：抓取、丰富、评分并个性化邮件 |
| [新闻简报](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*中级*</sup> | AI新闻简报策划：搜索、过滤、摘要和格式化 |
| [发票处理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*中级*</sup> | 使用视觉能力从PDF中提取并验证发票数据 |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*中级*</sup> | 将文档转化为两位AI主持人的播客 |
| [深度研究](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*中级*</sup> | 带有迭代优化的递归Map-Reduce研究 |
| [编程智能体](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*高级*</sup> | 具备6种工具、记忆和补丁子流的生产级编程智能体 |

</div>

👀 想看更多入门教程？[提交Issue！](https://github.com/The-Pocket/PocketFlow/issues/new)

## 如何使用 Pocket Flow？

🚀 通过**智能体编程**——最快的LLM应用开发范式——*人类负责设计*，*智能体负责编码*！

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ 以下是更复杂LLM应用的示例：

<div align="center">
  
|  应用名称     |  难度    | 主题  | 人类设计 | 智能体编码 |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [网站聊天机器人](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>将您的网站打造成全天候客户支持专家</sup></sub> | ★★☆ <br> *中级* | [智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [设计文档](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [流程代码](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [弹丸论破模拟器](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>忘掉图灵测试吧，弹丸论破才是终极AI实验！</sup></sub> | ★★★ <br> *高级*   | [工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [设计文档](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [流程代码](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [代码库知识构建器](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>人生苦短，无需对着别人的代码发呆</sup></sub> |  ★★☆ <br> *中级* | [工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [设计文档](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [流程代码](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [用Cursor构建Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>奇点即将到来……</sup></sub> | ★★★ <br> *高级*   | [智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [设计文档](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [流程代码](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [问AI Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>万一没被录取，就来问问AI Paul Graham吧</sup></sub> | ★★☆ <br> *中级*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [设计文档](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [流程代码](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [YouTube摘要生成器](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub>用五岁小孩能懂的方式解释YouTube视频</sup></sub> | ★☆☆ <br> *初级*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [设计文档](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [流程代码](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [冷启动开场白生成器](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub>即时破冰，将冷门线索转化为热门商机</sup></sub> | ★☆☆ <br> *初级*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [网络搜索](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [设计文档](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [流程代码](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- 想学习**智能体编程**？

  - 查看 [我的YouTube频道](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1)，观看上述部分应用的视频教程！

  - 想构建自己的LLM应用？阅读这篇 [文章](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)！从 [这个模板](https://github.com/The-Pocket/PocketFlow-Template-Python) 开始！