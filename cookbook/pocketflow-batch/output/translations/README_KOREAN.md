<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100줄 미니멀리스트 LLM 프레임워크" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | 한국어

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow는 [100줄](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)짜리 미니멀리스트 LLM 프레임워크입니다

- **경량**: 단 100줄. 불필요한 코드 없음, 의존성 없음, 벤더 종속 없음.
  
- **표현력**: 원하는 모든 것—([멀티-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[에이전트](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [워크플로우](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) 등을 지원합니다.

- **[에이전틱 코딩](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: AI 에이전트(예: Cursor AI)가 에이전트를 만들도록 하세요—생산성 10배 향상!

Pocket Flow 시작하기:
- 설치하려면, ```pip install pocketflow``` 또는 [소스 코드](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)를 직접 복사하세요 (100줄뿐입니다).
- 더 알아보려면 [동영상 튜토리얼](https://youtu.be/0Zr3NwcvpA0)과 [문서](https://the-pocket.github.io/PocketFlow/)를 확인하세요
- 🎉 Pocket Flow로 개발하는 다른 개발자들과 소통하려면 [Discord](https://discord.gg/hUHHE9Sa6T)에 참여하세요!
- 🎉 Pocket Flow는 이제 [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP), [Go](https://github.com/The-Pocket/PocketFlow-Go), [Rust](https://github.com/The-Pocket/PocketFlow-Rust), [PHP](https://github.com/The-Pocket/PocketFlow-PHP) 버전도 있습니다!

## 왜 Pocket Flow인가요?

현재 LLM 프레임워크는 너무 비대합니다... LLM 프레임워크에는 100줄이면 충분합니다!

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **추상화**          | **앱별 래퍼**                                      | **벤더별 래퍼**                                    | **줄 수**       | **크기**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | 에이전트, 체인               | 다수 <br><sup><sub>(예: QA, 요약)</sub></sup>              | 다수 <br><sup><sub>(예: OpenAI, Pinecone 등)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | 에이전트, 체인            | 다수 <br><sup><sub>(예: FileReadTool, SerperDevTool)</sub></sup>         | 다수 <br><sup><sub>(예: OpenAI, Anthropic, Pinecone 등)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | 에이전트                      | 일부 <br><sup><sub>(예: CodeAgent, VisitWebTool)</sub></sup>         | 일부 <br><sup><sub>(예: DuckDuckGo, Hugging Face 등)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | 에이전트, 그래프           | 일부 <br><sup><sub>(예: 시맨틱 검색)</sub></sup>                     | 일부 <br><sup><sub>(예: PostgresStore, SqliteSaver 등) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | 에이전트                | 일부 <br><sup><sub>(예: Tool Agent, Chat Agent)</sub></sup>              | 다수 <sup><sub>[선택적]<br> (예: OpenAI, Pinecone 등)</sub></sup>        | 7K <br><sup><sub>(코어만)</sub></sup>    | +26MB <br><sup><sub>(코어만)</sub></sup>          |
| **PocketFlow** | **그래프**                    | **없음**                                                 | **없음**                                                  | **100**       | **+56KB**                  |

</div>

## Pocket Flow는 어떻게 작동하나요?

[100줄](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)로 LLM 프레임워크의 핵심 추상화인 그래프를 구현합니다!
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

그로부터 ([멀티-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[에이전트](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [워크플로우](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) 등 인기 있는 디자인 패턴을 쉽게 구현할 수 있습니다.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ 아래는 기본 튜토리얼입니다:

<div align="center">
  
|  이름  | 난이도    |  설명  |  
| :-------------:  | :-------------: | :--------------------- |  
| [채팅](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*입문*</sup>  | 대화 기록이 있는 기본 챗봇 |
| [구조화된 출력](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*입문*</sup> | 프롬프팅을 통해 이력서에서 구조화된 데이터 추출 |
| [워크플로우](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*입문*</sup> | 개요 작성, 내용 작성, 스타일 적용을 하는 글쓰기 워크플로우 |
| [에이전트](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*입문*</sup>  | 웹 검색 및 질문 답변이 가능한 리서치 에이전트 |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*입문*</sup> | 간단한 검색 증강 생성 프로세스 |
| [배치](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*입문*</sup> | 마크다운을 여러 언어로 번역하는 배치 프로세서 |
| [스트리밍](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*입문*</sup> | 사용자 인터럽트 기능이 있는 실시간 LLM 스트리밍 데모 |
| [채팅 가드레일](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*입문*</sup> | 여행 관련 쿼리만 처리하는 여행 어드바이저 챗봇 |
| [다수결 투표](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*입문*</sup> | 여러 풀이 시도를 집계하여 추론 정확도 향상 |
| [맵-리듀스](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*입문*</sup>  | 맵-리듀스 패턴을 이용한 이력서 일괄 자격 평가 |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*입문*</sup>  | 인간 피드백 루프가 있는 커맨드라인 농담 생성기 |
| [멀티-에이전트](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*초급*</sup> | 2개의 에이전트 간 비동기 통신을 위한 금지어 게임 |
| [수퍼바이저](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*초급*</sup> | 리서치 에이전트가 불안정해지고 있습니다... 감독 프로세스를 구축해봅시다 |
| [병렬](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*초급*</sup> | 3배 속도 향상을 보여주는 병렬 실행 데모 |
| [병렬 플로우](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*초급*</sup> | 8배 속도 향상을 보여주는 병렬 이미지 처리 |
| [사고](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*초급*</sup> | 생각의 사슬을 통해 복잡한 추론 문제 해결 |
| [메모리](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*초급*</sup> | 단기 및 장기 메모리가 있는 챗봇 |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*초급*</sup>  | 자동 디버그 루프로 자연어를 SQL 쿼리로 변환 |
| [코드 생성기](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*초급*</sup> | 테스트 케이스 생성, 솔루션 구현, 코드 반복 개선 |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*초급*</sup> |  수치 연산을 위해 모델 컨텍스트 프로토콜을 사용하는 에이전트 |
| [에이전트 스킬](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*초급*</sup> | 재사용 가능한 마크다운 스킬로 요청을 라우팅하고 에이전트 플로우에서 적용 |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*초급*</sup> | 에이전트 간 통신을 위한 A2A 프로토콜로 래핑된 에이전트 |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*초급*</sup> | HITL 이미지 생성을 위한 유한 상태 머신이 있는 Streamlit 앱 |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*초급*</sup> | WebSocket을 통한 스트리밍 LLM 응답이 있는 실시간 채팅 인터페이스 |
| [FastAPI 백그라운드](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*초급*</sup> | 백그라운드 작업과 SSE를 통한 실시간 진행 상황이 있는 FastAPI 앱 |
| [음성 채팅](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*초급*</sup> | VAD, STT, LLM, TTS가 있는 대화형 음성 채팅 애플리케이션 |
| [판정자](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*초급*</sup> | 반복적인 콘텐츠 개선을 위한 LLM-as-Judge 평가자-최적화기 루프 |
| [토론](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*초급*</sup> | 두 명의 지지자와 공정한 심판이 있는 대립적 추론 |
| [에이전틱 RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*초급*</sup> | 어떤 문서를 읽을지 결정하는 에이전트 기반 RAG |
| [자가 치유 머메이드](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*초급*</sup> | 자동 오류 복구로 머메이드 다이어그램 생성 |
| [하트비트](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*초급*</sup> | 중첩 플로우가 있는 ClawBot과 같은 상시 주기적 모니터링 |
| [리드 생성](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*중급*</sup> | 영업 파이프라인: 스크래핑, 강화, 점수 매기기, 이메일 개인화 |
| [뉴스레터](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*중급*</sup> | AI 뉴스레터 큐레이션: 검색, 필터링, 요약, 포맷 |
| [인보이스 처리](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*중급*</sup> | 비전을 사용하여 PDF에서 인보이스 데이터 추출 및 검증 |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*중급*</sup> | 두 명의 AI 호스트가 진행하는 팟캐스트로 문서 변환 |
| [딥 리서치](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*중급*</sup> | 반복적 개선이 있는 재귀적 맵-리듀스 리서치 |
| [코딩 에이전트](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*고급*</sup> | 6개의 도구, 메모리, 서브플로우로서의 패치가 있는 프로덕션 코딩 에이전트 |

</div>

👀 입문자를 위한 다른 튜토리얼을 보고 싶으신가요? [이슈를 생성하세요!](https://github.com/The-Pocket/PocketFlow/issues/new)

## Pocket Flow를 어떻게 사용하나요?

🚀 **에이전틱 코딩**을 통해—가장 빠른 LLM 앱 개발 패러다임—*인간이 설계*하고 *에이전트가 코딩*합니다!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ 아래는 더 복잡한 LLM 앱의 예시입니다:

<div align="center">
  
|  앱 이름     |  난이도    | 주제  | 인간 설계 | 에이전트 코드 |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [웹사이트 챗봇](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>웹사이트를 24/7 고객 지원 전문가로 변환</sup></sub> | ★★☆ <br> *중급* | [에이전트](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [설계 문서](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [단간론파 시뮬레이터](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>튜링 테스트는 잊어버리세요. 단간론파, 궁극의 AI 실험!</sup></sub> | ★★★ <br> *고급*   | [워크플로우](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [에이전트](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [설계 문서](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [코드베이스 지식 빌더](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>다른 사람의 코드를 혼란스럽게 바라보기엔 인생이 너무 짧습니다</sup></sub> |  ★★☆ <br> *중급* | [워크플로우](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [설계 문서](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Cursor로 Cursor 만들기](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>우리는 곧 특이점에 도달할 것입니다...</sup></sub> | ★★★ <br> *고급*   | [에이전트](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [설계 문서](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [AI Paul Graham에게 물어보기](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>합격하지 못한 경우를 대비해 AI Paul Graham에게 물어보세요</sup></sub> | ★★☆ <br> *중급*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [맵 리듀스](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [설계 문서](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [유튜브 요약기](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub>유튜브 동영상을 5살 어린이도 이해할 수 있게 설명 </sup></sub> | ★☆☆ <br> *초급*   | [맵 리듀스](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [설계 문서](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [콜드 오프너 생성기](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub>차가운 리드를 뜨겁게 바꾸는 즉각적인 아이스브레이커 </sup></sub> | ★☆☆ <br> *초급*   | [맵 리듀스](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [웹 검색](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [설계 문서](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [플로우 코드](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- **에이전틱 코딩**을 배우고 싶으신가요?

  - 위의 일부 앱이 어떻게 만들어졌는지 동영상 튜토리얼을 보려면 [제 유튜브](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1)를 확인하세요!

  - 자신만의 LLM 앱을 만들고 싶으신가요? 이 [포스트](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)를 읽어보세요! [이 템플릿](https://github.com/The-Pocket/PocketFlow-Template-Python)으로 시작하세요!