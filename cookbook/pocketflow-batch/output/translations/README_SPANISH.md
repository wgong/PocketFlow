<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – Marco LLM minimalista de 100 líneas" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | Español | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow es un marco LLM minimalista de [100 líneas](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)

- **Ligero**: Solo 100 líneas. Sin bloat, sin dependencias, sin bloqueo de proveedor.
  
- **Expresivo**: Todo lo que necesitas—([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agentes](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Flujo de trabajo](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), y más.

- **[Codificación Agéntica](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: ¡Deja que los Agentes de IA (p. ej., Cursor AI) construyan Agentes—un aumento de productividad de 10x!

Empieza con Pocket Flow:
- Para instalar, ```pip install pocketflow``` o simplemente copia el [código fuente](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) (solo 100 líneas).
- Para aprender más, consulta el [tutorial en video](https://youtu.be/0Zr3NwcvpA0) y la [documentación](https://the-pocket.github.io/PocketFlow/)
- 🎉 ¡Únete a nuestro [Discord](https://discord.gg/hUHHE9Sa6T) para conectarte con otros desarrolladores que construyen con Pocket Flow!
- 🎉 ¡Pocket Flow ahora tiene versiones en [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP), [Go](https://github.com/The-Pocket/PocketFlow-Go), [Rust](https://github.com/The-Pocket/PocketFlow-Rust) y [PHP](https://github.com/The-Pocket/PocketFlow-PHP)!

## ¿Por qué Pocket Flow?

Los marcos LLM actuales son demasiado pesados... ¡Solo necesitas 100 líneas para un Marco LLM!

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **Abstracción**          | **Wrappers específicos de app**                                      | **Wrappers específicos de proveedor**                                    | **Líneas**       | **Tamaño**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agente, Cadena               | Muchos <br><sup><sub>(p. ej., QA, Resumen)</sub></sup>              | Muchos <br><sup><sub>(p. ej., OpenAI, Pinecone, etc.)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agente, Cadena            | Muchos <br><sup><sub>(p. ej., FileReadTool, SerperDevTool)</sub></sup>         | Muchos <br><sup><sub>(p. ej., OpenAI, Anthropic, Pinecone, etc.)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agente                      | Algunos <br><sup><sub>(p. ej., CodeAgent, VisitWebTool)</sub></sup>         | Algunos <br><sup><sub>(p. ej., DuckDuckGo, Hugging Face, etc.)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agente, Grafo           | Algunos <br><sup><sub>(p. ej., Búsqueda Semántica)</sub></sup>                     | Algunos <br><sup><sub>(p. ej., PostgresStore, SqliteSaver, etc.) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agente                | Algunos <br><sup><sub>(p. ej., Tool Agent, Chat Agent)</sub></sup>              | Muchos <sup><sub>[Opcional]<br> (p. ej., OpenAI, Pinecone, etc.)</sub></sup>        | 7K <br><sup><sub>(solo núcleo)</sub></sup>    | +26MB <br><sup><sub>(solo núcleo)</sub></sup>          |
| **PocketFlow** | **Grafo**                    | **Ninguno**                                                 | **Ninguno**                                                  | **100**       | **+56KB**                  |

</div>

## ¿Cómo funciona Pocket Flow?

Las [100 líneas](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) capturan la abstracción central de los marcos LLM: ¡el Grafo!
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

A partir de ahí, es fácil implementar patrones de diseño populares como ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agentes](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Flujo de trabajo](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), etc.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ A continuación se muestran tutoriales básicos:

<div align="center">
  
|  Nombre  | Dificultad    |  Descripción  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*Básico*</sup>  | Un chatbot básico con historial de conversación |
| [Salida Estructurada](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*Básico*</sup> | Extracción de datos estructurados de currículums mediante prompts |
| [Flujo de trabajo](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*Básico*</sup> | Un flujo de escritura que crea esquemas, redacta contenido y aplica estilos |
| [Agente](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*Básico*</sup>  | Un agente de investigación que puede buscar en la web y responder preguntas |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*Básico*</sup> | Un proceso simple de Generación Aumentada por Recuperación |
| [Lote](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*Básico*</sup> | Un procesador por lotes que traduce markdown a múltiples idiomas |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*Básico*</sup> | Una demo de streaming LLM en tiempo real con capacidad de interrupción del usuario |
| [Guardarraíl de Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*Básico*</sup> | Un chatbot asesor de viajes que solo procesa consultas relacionadas con viajes |
| [Voto por Mayoría](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*Básico*</sup> | Mejora la precisión del razonamiento agregando múltiples intentos de solución |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*Básico*</sup>  | Calificación de currículums por lotes usando el patrón map-reduce |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*Básico*</sup>  | Un generador de chistes por línea de comandos con retroalimentación humana en el bucle |
| [Multi-Agente](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*Principiante*</sup> | Un juego de palabras tabú para comunicación asíncrona entre 2 agentes |
| [Supervisor](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*Principiante*</sup> | El agente de investigación se está volviendo poco fiable... ¡Construyamos un proceso de supervisión! |
| [Paralelo](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*Principiante*</sup> | Una demo de ejecución paralela que muestra una aceleración de 3x |
| [Flujo Paralelo](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*Principiante*</sup> | Procesamiento de imágenes en paralelo que muestra una aceleración de 8x |
| [Pensamiento](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*Principiante*</sup> | Resuelve problemas de razonamiento complejos mediante Cadena de Pensamiento |
| [Memoria](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*Principiante*</sup> | Un chatbot con memoria a corto y largo plazo |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*Principiante*</sup>  | Convierte lenguaje natural a consultas SQL con un bucle de auto-depuración |
| [Generador de Código](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*Principiante*</sup> | Genera casos de prueba, implementa soluciones y mejora el código iterativamente |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*Principiante*</sup> |  Agente usando el Protocolo de Contexto de Modelo para operaciones numéricas |
| [Habilidades del Agente](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*Principiante*</sup> | Enruta solicitudes a habilidades markdown reutilizables y las aplica en un flujo de agente |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*Principiante*</sup> | Agente envuelto con el protocolo A2A para comunicación entre agentes |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*Principiante*</sup> | Aplicación Streamlit con máquina de estados finitos para generación de imágenes HITL |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*Principiante*</sup> | Interfaz de chat en tiempo real con respuestas LLM en streaming vía WebSocket |
| [FastAPI en Segundo Plano](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*Principiante*</sup> | Aplicación FastAPI con tareas en segundo plano y progreso en tiempo real vía SSE |
| [Chat de Voz](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*Principiante*</sup> | Una aplicación de chat de voz interactiva con VAD, STT, LLM y TTS. |
| [Juez](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*Principiante*</sup> | Bucle evaluador-optimizador LLM-como-Juez para refinamiento iterativo de contenido |
| [Debate](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*Principiante*</sup> | Razonamiento adversarial con dos defensores y un juez imparcial |
| [RAG Agéntico](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*Principiante*</sup> | RAG impulsado por agentes que decide qué documentos leer |
| [Mermaid Auto-reparable](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*Principiante*</sup> | Genera diagramas Mermaid con recuperación automática de errores |
| [Heartbeat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*Principiante*</sup> | Monitoreo periódico siempre activo similar a ClawBot con flujos anidados |
| [Generación de Leads](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*Intermedio*</sup> | Pipeline de ventas: extrae, enriquece, puntúa y personaliza correos |
| [Boletín](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*Intermedio*</sup> | Curación de boletines con IA: busca, filtra, resume y formatea |
| [Procesamiento de Facturas](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*Intermedio*</sup> | Extrae y valida datos de facturas desde PDFs usando visión |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*Intermedio*</sup> | Convierte documentos en un podcast con dos presentadores de IA |
| [Investigación Profunda](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*Intermedio*</sup> | Investigación map-reduce recursiva con refinamiento iterativo |
| [Agente de Codificación](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*Avanzado*</sup> | Agente de codificación de producción con 6 herramientas, memoria y parche como subflujo |

</div>

👀 ¿Quieres ver otros tutoriales para principiantes? [¡Crea un issue!](https://github.com/The-Pocket/PocketFlow/issues/new)

## ¿Cómo usar Pocket Flow?

🚀 ¡A través de la **Codificación Agéntica**—el paradigma de desarrollo de apps LLM más rápido—donde *los humanos diseñan* y *los agentes codifican*!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ A continuación se muestran ejemplos de apps LLM más complejas:

<div align="center">
  
|  Nombre de la App     |  Dificultad    | Temas  | Diseño Humano | Código del Agente |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Chatbot de Sitio Web](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>Convierte tu sitio web en un genio de atención al cliente 24/7</sup></sub> | ★★☆ <br> *Medio* | [Agente](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [Doc de Diseño](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [Simulador Danganronpa](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>Olvídate del test de Turing. ¡Danganronpa, el experimento de IA definitivo!</sup></sub> | ★★★ <br> *Avanzado*   | [Flujo de trabajo](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [Agente](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Doc de Diseño](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [Constructor de Conocimiento de Código](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>La vida es demasiado corta para quedarse mirando el código ajeno con confusión</sup></sub> |  ★★☆ <br> *Medio* | [Flujo de trabajo](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Doc de Diseño](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Construye Cursor con Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>Pronto alcanzaremos la singularidad...</sup></sub> | ★★★ <br> *Avanzado*   | [Agente](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Doc de Diseño](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [Pregúntale a la IA Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Pregúntale a la IA Paul Graham, por si no entras</sup></sub> | ★★☆ <br> *Medio*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Doc de Diseño](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Resumidor de YouTube](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> Explica videos de YouTube como si tuvieras 5 años </sup></sub> | ★☆☆ <br> *Principiante*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Doc de Diseño](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Generador de Apertura en Frío](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> Rompehielos instantáneos que convierten leads fríos en calientes </sup></sub> | ★☆☆ <br> *Principiante*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Búsqueda Web](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Doc de Diseño](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Código del Flujo](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- ¿Quieres aprender **Codificación Agéntica**?

  - ¡Visita [mi canal de YouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) para ver tutoriales en video sobre cómo se hicieron algunas de las apps anteriores!

  - ¿Quieres construir tu propia app LLM? ¡Lee este [artículo](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! ¡Empieza con [esta plantilla](https://github.com/The-Pocket/PocketFlow-Template-Python)!