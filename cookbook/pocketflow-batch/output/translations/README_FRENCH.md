<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – framework LLM minimaliste en 100 lignes" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | Français | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow est un framework LLM minimaliste en [100 lignes](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)

- **Léger** : Seulement 100 lignes. Zéro superflu, zéro dépendance, zéro verrouillage fournisseur.
  
- **Expressif** : Tout ce que vous aimez—([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agents](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), et bien plus.

- **[Codage Agentique](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)** : Laissez les agents IA (ex. : Cursor AI) construire des agents—gain de productivité multiplié par 10 !

Démarrez avec Pocket Flow :
- Pour installer : ```pip install pocketflow``` ou copiez simplement le [code source](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) (seulement 100 lignes).
- Pour en savoir plus, consultez le [tutoriel vidéo](https://youtu.be/0Zr3NwcvpA0) et la [documentation](https://the-pocket.github.io/PocketFlow/)
- 🎉 Rejoignez notre [Discord](https://discord.gg/hUHHE9Sa6T) pour échanger avec d'autres développeurs qui construisent avec Pocket Flow !
- 🎉 Pocket Flow est maintenant disponible en versions [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP), [Go](https://github.com/The-Pocket/PocketFlow-Go), [Rust](https://github.com/The-Pocket/PocketFlow-Rust) et [PHP](https://github.com/The-Pocket/PocketFlow-PHP) !

## Pourquoi Pocket Flow ?

Les frameworks LLM actuels sont trop lourds... Vous n'avez besoin que de 100 lignes pour un framework LLM !

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **Abstraction**          | **Wrappers spécifiques aux apps**                                      | **Wrappers spécifiques aux fournisseurs**                                    | **Lignes**       | **Taille**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agent, Chain               | Nombreux <br><sup><sub>(ex. : QA, Résumé)</sub></sup>              | Nombreux <br><sup><sub>(ex. : OpenAI, Pinecone, etc.)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agent, Chain            | Nombreux <br><sup><sub>(ex. : FileReadTool, SerperDevTool)</sub></sup>         | Nombreux <br><sup><sub>(ex. : OpenAI, Anthropic, Pinecone, etc.)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agent                      | Quelques-uns <br><sup><sub>(ex. : CodeAgent, VisitWebTool)</sub></sup>         | Quelques-uns <br><sup><sub>(ex. : DuckDuckGo, Hugging Face, etc.)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agent, Graph           | Quelques-uns <br><sup><sub>(ex. : Recherche Sémantique)</sub></sup>                     | Quelques-uns <br><sup><sub>(ex. : PostgresStore, SqliteSaver, etc.) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agent                | Quelques-uns <br><sup><sub>(ex. : Tool Agent, Chat Agent)</sub></sup>              | Nombreux <sup><sub>[Optionnel]<br> (ex. : OpenAI, Pinecone, etc.)</sub></sup>        | 7K <br><sup><sub>(noyau seul)</sub></sup>    | +26MB <br><sup><sub>(noyau seul)</sub></sup>          |
| **PocketFlow** | **Graph**                    | **Aucun**                                                 | **Aucun**                                                  | **100**       | **+56KB**                  |

</div>

## Comment fonctionne Pocket Flow ?

Les [100 lignes](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) capturent l'abstraction centrale des frameworks LLM : le Graphe !
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

À partir de là, il est facile d'implémenter des modèles de conception populaires comme ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agents](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), etc.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ Voici des tutoriels de base :

<div align="center">
  
|  Nom  | Difficulté    |  Description  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*Débutant*</sup>  | Un chatbot basique avec historique de conversation |
| [Sortie Structurée](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*Débutant*</sup> | Extraction de données structurées à partir de CV par prompting |
| [Workflow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*Débutant*</sup> | Un workflow d'écriture qui structure, rédige et met en forme le contenu |
| [Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*Débutant*</sup>  | Un agent de recherche capable de naviguer sur le web et de répondre à des questions |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*Débutant*</sup> | Un processus simple de génération augmentée par récupération |
| [Batch](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*Débutant*</sup> | Un processeur par lots qui traduit du markdown en plusieurs langues |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*Débutant*</sup> | Une démo de streaming LLM en temps réel avec interruption utilisateur |
| [Garde-fou Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*Débutant*</sup> | Un chatbot conseiller voyage qui ne traite que les questions liées aux voyages |
| [Vote Majoritaire](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*Débutant*</sup> | Améliorer la précision du raisonnement en agrégeant plusieurs tentatives de résolution |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*Débutant*</sup>  | Qualification de CV en lot avec le modèle map-reduce |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*Débutant*</sup>  | Un générateur de blagues en ligne de commande avec retour humain dans la boucle |
| [Multi-Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*Élémentaire*</sup> | Un jeu du mot Tabou pour la communication asynchrone entre 2 agents |
| [Superviseur](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*Élémentaire*</sup> | L'agent de recherche devient peu fiable... Construisons un processus de supervision |
| [Parallèle](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*Élémentaire*</sup> | Une démo d'exécution parallèle montrant une accélération de 3x |
| [Flux Parallèle](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*Élémentaire*</sup> | Un traitement d'images en parallèle montrant une accélération de 8x |
| [Réflexion](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*Élémentaire*</sup> | Résoudre des problèmes de raisonnement complexes via la Chaîne de Pensée |
| [Mémoire](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*Élémentaire*</sup> | Un chatbot avec mémoire à court et long terme |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*Élémentaire*</sup>  | Convertir le langage naturel en requêtes SQL avec une boucle de débogage automatique |
| [Générateur de Code](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*Élémentaire*</sup> | Générer des cas de test, implémenter des solutions et améliorer le code de façon itérative |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*Élémentaire*</sup> |  Agent utilisant le Protocole de Contexte de Modèle pour les opérations numériques |
| [Compétences Agent](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*Élémentaire*</sup> | Acheminer les requêtes vers des compétences markdown réutilisables et les appliquer dans un flux agent |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*Élémentaire*</sup> | Agent encapsulé avec le protocole A2A pour la communication inter-agents |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*Élémentaire*</sup> | Application Streamlit avec machine à états finis pour la génération d'images HITL |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*Élémentaire*</sup> | Interface de chat en temps réel avec réponses LLM en streaming via WebSocket |
| [FastAPI Arrière-plan](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*Élémentaire*</sup> | Application FastAPI avec tâches en arrière-plan et progression en temps réel via SSE |
| [Chat Vocal](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*Élémentaire*</sup> | Une application de chat vocal interactif avec VAD, STT, LLM et TTS. |
| [Juge](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*Élémentaire*</sup> | Boucle évaluateur-optimiseur LLM-as-Judge pour le raffinement itératif du contenu |
| [Débat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*Élémentaire*</sup> | Raisonnement contradictoire avec deux avocats et un juge impartial |
| [RAG Agentique](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*Élémentaire*</sup> | RAG piloté par agent qui décide quels documents lire |
| [Mermaid Auto-Réparant](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*Élémentaire*</sup> | Générer des diagrammes Mermaid avec récupération automatique des erreurs |
| [Heartbeat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*Élémentaire*</sup> | Surveillance périodique permanente de type ClawBot avec flux imbriqués |
| [Génération de Leads](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*Intermédiaire*</sup> | Pipeline de vente : scraping, enrichissement, scoring et personnalisation d'emails |
| [Newsletter](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*Intermédiaire*</sup> | Curation de newsletter IA : recherche, filtrage, résumé et mise en forme |
| [Traitement de Factures](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*Intermédiaire*</sup> | Extraire et valider des données de factures depuis des PDF avec la vision |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*Intermédiaire*</sup> | Transformer des documents en podcast avec deux hôtes IA |
| [Recherche Approfondie](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*Intermédiaire*</sup> | Recherche map-reduce récursive avec raffinement itératif |
| [Agent de Codage](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*Avancé*</sup> | Agent de codage en production avec 6 outils, mémoire et patch en sous-flux |

</div>

👀 Vous souhaitez voir d'autres tutoriels pour débutants ? [Créez une issue !](https://github.com/The-Pocket/PocketFlow/issues/new)

## Comment utiliser Pocket Flow ?

🚀 Via le **Codage Agentique**—le paradigme de développement d'applications LLM le plus rapide—où *les humains conçoivent* et *les agents codent* !

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ Voici des exemples d'applications LLM plus complexes :

<div align="center">
  
|  Nom de l'App     |  Difficulté    | Sujets  | Conception Humaine | Code Agent |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Chatbot de Site Web](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>Transformez votre site web en génie du support client 24h/24 et 7j/7</sup></sub> | ★★☆ <br> *Moyen* | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [Doc de Conception](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [Simulateur Danganronpa](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>Oubliez le test de Turing. Danganronpa, l'expérience IA ultime !</sup></sub> | ★★★ <br> *Avancé*   | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Doc de Conception](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [Constructeur de Connaissance de Base de Code](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>La vie est trop courte pour fixer le code des autres avec perplexité</sup></sub> |  ★★☆ <br> *Moyen* | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Doc de Conception](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Construire Cursor avec Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>Nous atteindrons bientôt la singularité...</sup></sub> | ★★★ <br> *Avancé*   | [Agent](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Doc de Conception](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [Demandez à l'IA Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Demandez à l'IA Paul Graham, au cas où vous ne seriez pas accepté</sup></sub> | ★★☆ <br> *Moyen*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Doc de Conception](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Résumeur YouTube](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> Explique les vidéos YouTube comme si vous aviez 5 ans </sup></sub> | ★☆☆ <br> *Débutant*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Doc de Conception](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Générateur d'Accroche](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> Des brise-glaces instantanés qui transforment les prospects froids en chauds </sup></sub> | ★☆☆ <br> *Débutant*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Recherche Web](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Doc de Conception](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Code du Flux](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- Vous souhaitez apprendre le **Codage Agentique** ?

  - Consultez [ma chaîne YouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) pour des tutoriels vidéo sur la création de certaines des applications ci-dessus !

  - Vous souhaitez créer votre propre application LLM ? Lisez ce [post](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to) ! Commencez avec [ce modèle](https://github.com/The-Pocket/PocketFlow-Template-Python) !