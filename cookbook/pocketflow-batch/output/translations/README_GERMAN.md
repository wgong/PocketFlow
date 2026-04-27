<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100-Zeilen minimalistisches LLM-Framework" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | Deutsch | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![Lizenz: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Dokumentation](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow ist ein [100-Zeilen](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) minimalistisches LLM-Framework

- **Leichtgewichtig**: Nur 100 Zeilen. Kein Ballast, keine Abhängigkeiten, keine Anbieterbindung.
  
- **Ausdrucksstark**: Alles, was du liebst – ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agenten](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) und mehr.

- **[Agentisches Programmieren](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: Lass KI-Agenten (z. B. Cursor AI) Agenten bauen – 10-facher Produktivitätsschub!

Einstieg mit Pocket Flow:
- Zur Installation: ```pip install pocketflow``` oder einfach den [Quellcode](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) kopieren (nur 100 Zeilen).
- Mehr erfahren: Schau dir das [Video-Tutorial](https://youtu.be/0Zr3NwcvpA0) und die [Dokumentation](https://the-pocket.github.io/PocketFlow/) an.
- 🎉 Tritt unserem [Discord](https://discord.gg/hUHHE9Sa6T) bei und vernetze dich mit anderen Entwicklern, die mit Pocket Flow bauen!
- 🎉 Pocket Flow gibt es jetzt auch in [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP), [Go](https://github.com/The-Pocket/PocketFlow-Go), [Rust](https://github.com/The-Pocket/PocketFlow-Rust) und [PHP](https://github.com/The-Pocket/PocketFlow-PHP)!

## Warum Pocket Flow?

Aktuelle LLM-Frameworks sind aufgebläht... Du brauchst nur 100 Zeilen für ein LLM-Framework!

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **Abstraktion**          | **App-spezifische Wrapper**                                      | **Anbieter-spezifische Wrapper**                                    | **Zeilen**       | **Größe**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agent, Chain               | Viele <br><sup><sub>(z. B. QA, Zusammenfassung)</sub></sup>              | Viele <br><sup><sub>(z. B. OpenAI, Pinecone, etc.)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agent, Chain            | Viele <br><sup><sub>(z. B. FileReadTool, SerperDevTool)</sub></sup>         | Viele <br><sup><sub>(z. B. OpenAI, Anthropic, Pinecone, etc.)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agent                      | Einige <br><sup><sub>(z. B. CodeAgent, VisitWebTool)</sub></sup>         | Einige <br><sup><sub>(z. B. DuckDuckGo, Hugging Face, etc.)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agent, Graph           | Einige <br><sup><sub>(z. B. Semantische Suche)</sub></sup>                     | Einige <br><sup><sub>(z. B. PostgresStore, SqliteSaver, etc.) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agent                | Einige <br><sup><sub>(z. B. Tool Agent, Chat Agent)</sub></sup>              | Viele <sup><sub>[Optional]<br> (z. B. OpenAI, Pinecone, etc.)</sub></sup>        | 7K <br><sup><sub>(nur Kern)</sub></sup>    | +26MB <br><sup><sub>(nur Kern)</sub></sup>          |
| **PocketFlow** | **Graph**                    | **Keine**                                                 | **Keine**                                                  | **100**       | **+56KB**                  |

</div>

## Wie funktioniert Pocket Flow?

Die [100 Zeilen](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) erfassen die Kernabstraktion von LLM-Frameworks: Graph!
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

Darauf aufbauend lassen sich beliebte Entwurfsmuster wie ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agenten](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) usw. einfach umsetzen.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ Nachfolgend grundlegende Tutorials:

<div align="center">
  
|  Name  | Schwierigkeit    |  Beschreibung  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*Einsteiger*</sup>  | Ein einfacher Chatbot mit Gesprächsverlauf |
| [Strukturierte Ausgabe](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*Einsteiger*</sup> | Strukturierte Daten aus Lebensläufen per Prompt extrahieren |
| [Workflow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*Einsteiger*</sup> | Ein Schreib-Workflow mit Gliederung, Inhaltserstellung und Formatierung |
| [Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*Einsteiger*</sup>  | Ein Recherche-Agent, der das Web durchsuchen und Fragen beantworten kann |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*Einsteiger*</sup> | Ein einfacher Retrieval-augmented Generation Prozess |
| [Batch](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*Einsteiger*</sup> | Ein Batch-Prozessor, der Markdown in mehrere Sprachen übersetzt |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*Einsteiger*</sup> | Eine Echtzeit-LLM-Streaming-Demo mit Benutzerunterbrechungsfunktion |
| [Chat Guardrail](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*Einsteiger*</sup> | Ein Reiseberater-Chatbot, der nur reisebezogene Anfragen verarbeitet |
| [Mehrheitsvoting](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*Einsteiger*</sup> | Schlussfolgerungsgenauigkeit durch Aggregation mehrerer Lösungsversuche verbessern |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*Einsteiger*</sup>  | Batch-Lebenslaufqualifizierung mit Map-Reduce-Muster |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*Einsteiger*</sup>  | Ein Kommandozeilen-Jokegenerator mit menschlicher Rückkopplungsschleife |
| [Multi-Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*Anfänger*</sup> | Ein Taboo-Wortspiel für asynchrone Kommunikation zwischen 2 Agenten |
| [Supervisor](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*Anfänger*</sup> | Der Recherche-Agent wird unzuverlässig... Lass uns einen Überwachungsprozess aufbauen |
| [Parallel](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*Anfänger*</sup> | Eine Demo zur parallelen Ausführung mit 3-fachem Geschwindigkeitszuwachs |
| [Paralleler Flow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*Anfänger*</sup> | Parallele Bildverarbeitung mit 8-fachem Geschwindigkeitszuwachs |
| [Denken](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*Anfänger*</sup> | Komplexe Denkaufgaben durch Schritt-für-Schritt-Schlussfolgerung lösen |
| [Gedächtnis](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*Anfänger*</sup> | Ein Chatbot mit Kurz- und Langzeitgedächtnis |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*Anfänger*</sup>  | Natürliche Sprache in SQL-Abfragen umwandeln mit automatischer Debug-Schleife |
| [Code-Generator](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*Anfänger*</sup> | Testfälle generieren, Lösungen implementieren und Code iterativ verbessern |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*Anfänger*</sup> |  Agent mit Model Context Protocol für numerische Operationen |
| [Agent-Fähigkeiten](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*Anfänger*</sup> | Anfragen an wiederverwendbare Markdown-Fähigkeiten weiterleiten und in einem Agenten-Flow anwenden |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*Anfänger*</sup> | Agent mit A2A-Protokoll für die Kommunikation zwischen Agenten |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*Anfänger*</sup> | Streamlit-App mit endlichem Zustandsautomaten für HITL-Bildgenerierung |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*Anfänger*</sup> | Echtzeit-Chat-Oberfläche mit gestreamten LLM-Antworten über WebSocket |
| [FastAPI Hintergrund](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*Anfänger*</sup> | FastAPI-App mit Hintergrundjobs und Echtzeit-Fortschritt über SSE |
| [Sprach-Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*Anfänger*</sup> | Eine interaktive Sprach-Chat-Anwendung mit VAD, STT, LLM und TTS. |
| [Bewerter](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*Anfänger*</sup> | LLM-als-Richter Bewerter-Optimierer-Schleife zur iterativen Inhaltsverbesserung |
| [Debatte](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*Anfänger*</sup> | Kontradiktorisches Denken mit zwei Anwälten und einem unparteiischen Richter |
| [Agentisches RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*Anfänger*</sup> | Agenten-gesteuertes RAG, das entscheidet, welche Dokumente gelesen werden |
| [Selbstheilendes Mermaid](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*Anfänger*</sup> | Mermaid-Diagramme mit automatischer Fehlerbehebung generieren |
| [Herzschlag](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*Anfänger*</sup> | ClawBot-ähnliche dauerhaft aktive periodische Überwachung mit verschachtelten Flows |
| [Lead-Generierung](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*Fortgeschritten*</sup> | Vertriebspipeline: scrapen, anreichern, bewerten und E-Mails personalisieren |
| [Newsletter](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*Fortgeschritten*</sup> | KI-Newsletter-Kuration: suchen, filtern, zusammenfassen und formatieren |
| [Rechnungsverarbeitung](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*Fortgeschritten*</sup> | Rechnungsdaten aus PDFs per Vision extrahieren und validieren |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*Fortgeschritten*</sup> | Dokumente in einen Podcast mit zwei KI-Moderatoren verwandeln |
| [Tiefenrecherche](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*Fortgeschritten*</sup> | Rekursive Map-Reduce-Recherche mit iterativer Verfeinerung |
| [Programmier-Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*Experte*</sup> | Produktionsreifer Programmier-Agent mit 6 Werkzeugen, Gedächtnis und Patch-als-Subflow |

</div>

👀 Möchtest du weitere Tutorials für Einsteiger sehen? [Erstelle ein Issue!](https://github.com/The-Pocket/PocketFlow/issues/new)

## Wie verwendet man Pocket Flow?

🚀 Durch **Agentisches Programmieren** – das schnellste LLM-App-Entwicklungsparadigma – bei dem *Menschen entwerfen* und *Agenten programmieren*!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="BILD ALTERNATIVTEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ Nachfolgend Beispiele komplexerer LLM-Apps:

<div align="center">
  
|  App-Name     |  Schwierigkeit    | Themen  | Menschliches Design | Agenten-Code |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Website-Chatbot](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>Verwandle deine Website in einen 24/7-Kundensupport-Experten</sup></sub> | ★★☆ <br> *Mittel* | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [Design-Dokument](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [Danganronpa-Simulator](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>Vergiss den Turing-Test. Danganronpa – das ultimative KI-Experiment!</sup></sub> | ★★★ <br> *Experte*   | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Design-Dokument](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [Codebase-Wissensaufbau](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>Das Leben ist zu kurz, um verwirrt auf den Code anderer zu starren</sup></sub> |  ★★☆ <br> *Mittel* | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Design-Dokument](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Cursor mit Cursor bauen](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>Die Singularität rückt näher ...</sup></sub> | ★★★ <br> *Experte*   | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Design-Dokument](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [KI Paul Graham befragen](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Frag KI Paul Graham, falls du nicht aufgenommen wirst</sup></sub> | ★★☆ <br> *Mittel*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Design-Dokument](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Youtube-Zusammenfasser](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> YouTube-Videos so erklärt, als wärst du 5 </sup></sub> | ★☆☆ <br> *Anfänger*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Design-Dokument](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Kalt-Einstieg-Generator](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> Sofortige Gesprächseinstiege, die kalte Leads heiß machen </sup></sub> | ★☆☆ <br> *Anfänger*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Websuche](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Design-Dokument](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Flow-Code](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- Möchtest du **Agentisches Programmieren** erlernen?

  - Schau dir [meinen YouTube-Kanal](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) für Video-Tutorials an, wie einige der oben genannten Apps erstellt wurden!

  - Möchtest du deine eigene LLM-App bauen? Lies diesen [Beitrag](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! Starte mit [dieser Vorlage](https://github.com/The-Pocket/PocketFlow-Template-Python)!