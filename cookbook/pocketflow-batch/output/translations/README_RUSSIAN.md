<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100-line minimalist LLM framework" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | Русский | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow — это минималистичный LLM-фреймворк из [100 строк](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)

- **Лёгкий**: Всего 100 строк. Никакого раздутия, никаких зависимостей, никакой привязки к поставщику.

- **Выразительный**: Всё, что вы любите — ([Мульти-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Агенты](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Рабочий процесс](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) и многое другое.

- **[Агентное программирование](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: Позвольте ИИ-агентам (например, Cursor AI) создавать агентов — 10-кратный рост производительности!

Начните работу с Pocket Flow:
- Для установки: ```pip install pocketflow``` или просто скопируйте [исходный код](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) (всего 100 строк).
- Чтобы узнать больше, ознакомьтесь с [видеоуроком](https://youtu.be/0Zr3NwcvpA0) и [документацией](https://the-pocket.github.io/PocketFlow/)
- 🎉 Присоединяйтесь к нашему [Discord](https://discord.gg/hUHHE9Sa6T), чтобы общаться с другими разработчиками, создающими приложения с Pocket Flow!
- 🎉 Pocket Flow теперь доступен на [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP), [Go](https://github.com/The-Pocket/PocketFlow-Go), [Rust](https://github.com/The-Pocket/PocketFlow-Rust) и [PHP](https://github.com/The-Pocket/PocketFlow-PHP)!

## Почему Pocket Flow?

Современные LLM-фреймворки раздуты... Для LLM-фреймворка нужно всего 100 строк!

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **Абстракция**          | **Обёртки для приложений**                                      | **Обёртки для поставщиков**                                    | **Строки**       | **Размер**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Агент, Цепочка               | Много <br><sup><sub>(например, QA, Суммаризация)</sub></sup>              | Много <br><sup><sub>(например, OpenAI, Pinecone и др.)</sub></sup>                   | 405K          | +166МБ                     |
| CrewAI     | Агент, Цепочка            | Много <br><sup><sub>(например, FileReadTool, SerperDevTool)</sub></sup>         | Много <br><sup><sub>(например, OpenAI, Anthropic, Pinecone и др.)</sub></sup>        | 18K           | +173МБ                     |
| SmolAgent   | Агент                      | Некоторые <br><sup><sub>(например, CodeAgent, VisitWebTool)</sub></sup>         | Некоторые <br><sup><sub>(например, DuckDuckGo, Hugging Face и др.)</sub></sup>           | 8K            | +198МБ                     |
| LangGraph   | Агент, Граф           | Некоторые <br><sup><sub>(например, Семантический поиск)</sub></sup>                     | Некоторые <br><sup><sub>(например, PostgresStore, SqliteSaver и др.) </sub></sup>        | 37K           | +51МБ                      |
| AutoGen    | Агент                | Некоторые <br><sup><sub>(например, Tool Agent, Chat Agent)</sub></sup>              | Много <sup><sub>[Опционально]<br> (например, OpenAI, Pinecone и др.)</sub></sup>        | 7K <br><sup><sub>(только ядро)</sub></sup>    | +26МБ <br><sup><sub>(только ядро)</sub></sup>          |
| **PocketFlow** | **Граф**                    | **Нет**                                                 | **Нет**                                                  | **100**       | **+56КБ**                  |

</div>

## Как работает Pocket Flow?

[100 строк](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) отражают ключевую абстракцию LLM-фреймворков: Граф!
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

На этой основе легко реализовать популярные паттерны проектирования, такие как ([Мульти-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Агенты](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Рабочий процесс](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) и другие.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ Ниже представлены базовые руководства:

<div align="center">
  
|  Название  | Сложность    |  Описание  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Чат](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*Для новичков*</sup>  | Базовый чат-бот с историей разговора |
| [Структурированный вывод](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*Для новичков*</sup> | Извлечение структурированных данных из резюме с помощью промптов |
| [Рабочий процесс](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*Для новичков*</sup> | Рабочий процесс написания: составление плана, написание содержания и стилизация |
| [Агент](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*Для новичков*</sup>  | Исследовательский агент, способный искать в интернете и отвечать на вопросы |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*Для новичков*</sup> | Простой процесс генерации с извлечением информации |
| [Пакетная обработка](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*Для новичков*</sup> | Пакетный обработчик для перевода markdown на несколько языков |
| [Потоковая передача](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*Для новичков*</sup> | Демонстрация потоковой передачи LLM в реальном времени с возможностью прерывания |
| [Ограничения чата](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*Для новичков*</sup> | Чат-бот туристического советника, обрабатывающий только связанные с путешествиями запросы |
| [Голосование большинством](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*Для новичков*</sup> | Повышение точности рассуждений путём агрегации нескольких попыток решения |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*Для новичков*</sup>  | Пакетная квалификация резюме с использованием паттерна map-reduce |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*Для новичков*</sup>  | Генератор шуток в командной строке с обратной связью от человека |
| [Мульти-агент](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*Начинающий*</sup> | Игра в «Табу» для асинхронного взаимодействия между 2 агентами |
| [Супервизор](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*Начинающий*</sup> | Исследовательский агент становится ненадёжным... Давайте создадим процесс надзора |
| [Параллельность](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*Начинающий*</sup> | Демонстрация параллельного выполнения с 3-кратным ускорением |
| [Параллельный поток](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*Начинающий*</sup> | Параллельная обработка изображений с 8-кратным ускорением |
| [Мышление](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*Начинающий*</sup> | Решение сложных задач рассуждения с помощью Цепочки мыслей |
| [Память](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*Начинающий*</sup> | Чат-бот с краткосрочной и долгосрочной памятью |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*Начинающий*</sup>  | Преобразование естественного языка в SQL-запросы с циклом автоматической отладки |
| [Генератор кода](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*Начинающий*</sup> | Генерация тестовых случаев, реализация решений и итеративное улучшение кода |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*Начинающий*</sup> |  Агент, использующий протокол контекста модели для числовых операций |
| [Навыки агента](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*Начинающий*</sup> | Маршрутизация запросов к многоразовым markdown-навыкам и их применение в потоке агента |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*Начинающий*</sup> | Агент, обёрнутый в протокол A2A для межагентного взаимодействия |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*Начинающий*</sup> | Приложение Streamlit с конечным автоматом для генерации изображений с участием человека |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*Начинающий*</sup> | Интерфейс чата в реальном времени с потоковыми ответами LLM через WebSocket |
| [FastAPI Background](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*Начинающий*</sup> | Приложение FastAPI с фоновыми задачами и обновлениями прогресса в реальном времени через SSE |
| [Голосовой чат](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*Начинающий*</sup> | Интерактивное приложение для голосового чата с VAD, STT, LLM и TTS |
| [Судья](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*Начинающий*</sup> | Цикл оценщик-оптимизатор LLM-as-Judge для итеративного улучшения контента |
| [Дебаты](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*Начинающий*</sup> | Состязательное рассуждение с двумя защитниками и беспристрастным судьёй |
| [Агентный RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*Начинающий*</sup> | Управляемый агентом RAG, решающий, какие документы читать |
| [Самовосстанавливающийся Mermaid](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*Начинающий*</sup> | Генерация диаграмм Mermaid с автоматическим восстановлением после ошибок |
| [Мониторинг](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*Начинающий*</sup> | Постоянный периодический мониторинг с вложенными потоками, как в ClawBot |
| [Генерация лидов](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*Средний*</sup> | Воронка продаж: сбор, обогащение, оценка и персонализация писем |
| [Рассылка](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*Средний*</sup> | ИИ-курирование новостной рассылки: поиск, фильтрация, суммаризация и форматирование |
| [Обработка счетов](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*Средний*</sup> | Извлечение и проверка данных счётов из PDF с использованием зрения |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*Средний*</sup> | Преобразование документов в подкаст с двумя ИИ-ведущими |
| [Глубокое исследование](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*Средний*</sup> | Рекурсивное исследование map-reduce с итеративным уточнением |
| [Агент программирования](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*Продвинутый*</sup> | Производственный агент программирования с 6 инструментами, памятью и патчем как субпотоком |

</div>

👀 Хотите увидеть другие руководства для новичков? [Создайте задачу!](https://github.com/The-Pocket/PocketFlow/issues/new)

## Как использовать Pocket Flow?

🚀 Через **Агентное программирование** — самую быструю парадигму разработки LLM-приложений, где *люди проектируют*, а *агенты программируют*!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ Ниже приведены примеры более сложных LLM-приложений:

<div align="center">
  
|  Название приложения     |  Сложность    | Темы  | Дизайн человека | Код агента |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Чат-бот для сайта](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>Превратите ваш сайт в круглосуточного гения поддержки клиентов</sup></sub> | ★★☆ <br> *Средний* | [Агент](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [Документ дизайна](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [Код потока](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [Симулятор Danganronpa](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>Забудьте о тесте Тьюринга. Danganronpa — главный ИИ-эксперимент!</sup></sub> | ★★★ <br> *Продвинутый*   | [Рабочий процесс](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [Агент](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Документ дизайна](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [Код потока](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [Построитель знаний о кодовой базе](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>Жизнь слишком коротка, чтобы растерянно смотреть на чужой код</sup></sub> |  ★★☆ <br> *Средний* | [Рабочий процесс](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Документ дизайна](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Код потока](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Создайте Cursor с помощью Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>Мы скоро достигнем сингулярности...</sup></sub> | ★★★ <br> *Продвинутый*   | [Агент](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Документ дизайна](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Код потока](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [Спросите ИИ Пола Грэма](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Спросите ИИ Пола Грэма, если вас не возьмут</sup></sub> | ★★☆ <br> *Средний*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Документ дизайна](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Код потока](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Суммаризатор YouTube](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub>Объясняет видео на YouTube, как будто вам 5 лет</sup></sub> | ★☆☆ <br> *Начинающий*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Документ дизайна](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Код потока](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Генератор вступлений для холодных писем](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub>Мгновенные ледоколы, превращающие холодных лидов в горячих</sup></sub> | ★☆☆ <br> *Начинающий*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Веб-поиск](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Документ дизайна](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Код потока](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- Хотите научиться **Агентному программированию**?

  - Посетите [мой YouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) для видеоуроков о том, как создавались некоторые из приведённых приложений!

  - Хотите создать собственное LLM-приложение? Прочитайте этот [пост](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! Начните с [этого шаблона](https://github.com/The-Pocket/PocketFlow-Template-Python)!