<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – framework LLM minimalista de 100 linhas" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | Português | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow é um framework LLM minimalista de [100 linhas](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)

- **Leve**: Apenas 100 linhas. Zero inchaço, zero dependências, zero aprisionamento de fornecedor.
  
- **Expressivo**: Tudo que você ama—([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agentes](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), e muito mais.

- **[Codificação Agêntica](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: Deixe Agentes de IA (ex.: Cursor AI) construírem Agentes—aumento de produtividade de 10x!

Comece a usar o Pocket Flow:
- Para instalar, ```pip install pocketflow``` ou simplesmente copie o [código-fonte](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) (apenas 100 linhas).
- Para saber mais, confira o [tutorial em vídeo](https://youtu.be/0Zr3NwcvpA0) e a [documentação](https://the-pocket.github.io/PocketFlow/)
- 🎉 Entre no nosso [Discord](https://discord.gg/hUHHE9Sa6T) para se conectar com outros desenvolvedores criando com Pocket Flow!
- 🎉 O Pocket Flow agora tem versões em [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript), [Java](https://github.com/The-Pocket/PocketFlow-Java), [C++](https://github.com/The-Pocket/PocketFlow-CPP), [Go](https://github.com/The-Pocket/PocketFlow-Go), [Rust](https://github.com/The-Pocket/PocketFlow-Rust) e [PHP](https://github.com/The-Pocket/PocketFlow-PHP)!

## Por que Pocket Flow?

Os frameworks LLM atuais são inflados... Você só precisa de 100 linhas para um Framework LLM!

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **Abstração**          | **Wrappers Específicos de App**                                      | **Wrappers Específicos de Fornecedor**                                    | **Linhas**       | **Tamanho**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agente, Cadeia               | Muitos <br><sup><sub>(ex.: QA, Sumarização)</sub></sup>              | Muitos <br><sup><sub>(ex.: OpenAI, Pinecone, etc.)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agente, Cadeia            | Muitos <br><sup><sub>(ex.: FileReadTool, SerperDevTool)</sub></sup>         | Muitos <br><sup><sub>(ex.: OpenAI, Anthropic, Pinecone, etc.)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agente                      | Alguns <br><sup><sub>(ex.: CodeAgent, VisitWebTool)</sub></sup>         | Alguns <br><sup><sub>(ex.: DuckDuckGo, Hugging Face, etc.)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agente, Grafo           | Alguns <br><sup><sub>(ex.: Busca Semântica)</sub></sup>                     | Alguns <br><sup><sub>(ex.: PostgresStore, SqliteSaver, etc.) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agente                | Alguns <br><sup><sub>(ex.: Agente de Ferramenta, Agente de Chat)</sub></sup>              | Muitos <sup><sub>[Opcional]<br> (ex.: OpenAI, Pinecone, etc.)</sub></sup>        | 7K <br><sup><sub>(somente núcleo)</sub></sup>    | +26MB <br><sup><sub>(somente núcleo)</sub></sup>          |
| **PocketFlow** | **Grafo**                    | **Nenhum**                                                 | **Nenhum**                                                  | **100**       | **+56KB**                  |

</div>

## Como o Pocket Flow funciona?

As [100 linhas](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) capturam a abstração central dos frameworks LLM: Grafo!
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

A partir daí, é fácil implementar padrões de design populares como ([Multi-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[Agentes](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html), [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html), [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html), etc.
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ Abaixo estão tutoriais básicos:

<div align="center">
  
|  Nome  | Dificuldade    |  Descrição  |  
| :-------------:  | :-------------: | :--------------------- |  
| [Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*Iniciante*</sup>  | Um chatbot básico com histórico de conversa |
| [Saída Estruturada](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*Iniciante*</sup> | Extração de dados estruturados de currículos via prompts |
| [Workflow](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*Iniciante*</sup> | Um fluxo de escrita que cria esboços, escreve conteúdo e aplica estilização |
| [Agente](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*Iniciante*</sup>  | Um agente de pesquisa que pode buscar na web e responder perguntas |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*Iniciante*</sup> | Um processo simples de Geração Aumentada por Recuperação |
| [Lote](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*Iniciante*</sup> | Um processador em lote que traduz markdown para múltiplos idiomas |
| [Streaming](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*Iniciante*</sup> | Uma demo de streaming LLM em tempo real com capacidade de interrupção pelo usuário |
| [Guardrail de Chat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*Iniciante*</sup> | Um chatbot de assessor de viagens que processa apenas consultas relacionadas a viagens |
| [Votação por Maioria](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*Iniciante*</sup> | Melhora a precisão do raciocínio agregando múltiplas tentativas de solução |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*Iniciante*</sup>  | Qualificação de currículos em lote usando o padrão map-reduce |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*Iniciante*</sup>  | Um gerador de piadas na linha de comando com feedback humano no loop |
| [Multi-Agente](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*Básico*</sup> | Um jogo de palavras tabu para comunicação assíncrona entre 2 agentes |
| [Supervisor](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*Básico*</sup> | O agente de pesquisa está ficando não confiável... Vamos construir um processo de supervisão|
| [Paralelo](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*Básico*</sup> | Uma demo de execução paralela que mostra aceleração de 3x |
| [Fluxo Paralelo](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*Básico*</sup> | Um processamento de imagem paralelo mostrando aceleração de 8x |
| [Raciocínio](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*Básico*</sup> | Resolve problemas complexos de raciocínio através de Cadeia de Pensamento |
| [Memória](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*Básico*</sup> | Um chatbot com memória de curto e longo prazo |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*Básico*</sup>  | Converte linguagem natural em consultas SQL com um loop de auto-depuração |
| [Gerador de Código](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*Básico*</sup> | Gera casos de teste, implementa soluções e melhora código iterativamente |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*Básico*</sup> |  Agente usando o Protocolo de Contexto de Modelo para operações numéricas |
| [Habilidades de Agente](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*Básico*</sup> | Encaminha requisições para habilidades markdown reutilizáveis e as aplica em um fluxo de agente |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*Básico*</sup> | Agente encapsulado com protocolo A2A para comunicação inter-agentes |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*Básico*</sup> | App Streamlit com máquina de estados finitos para geração de imagem com humano no loop |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*Básico*</sup> | Interface de chat em tempo real com respostas LLM em streaming via WebSocket |
| [FastAPI Background](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*Básico*</sup> | App FastAPI com jobs em segundo plano e progresso em tempo real via SSE |
| [Chat por Voz](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*Básico*</sup> | Uma aplicação interativa de chat por voz com VAD, STT, LLM e TTS. |
| [Juiz](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*Básico*</sup> | Loop avaliador-otimizador LLM-como-Juiz para refinamento iterativo de conteúdo |
| [Debate](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*Básico*</sup> | Raciocínio adversarial com dois defensores e um juiz imparcial |
| [RAG Agêntico](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*Básico*</sup> | RAG conduzido por agente que decide quais documentos ler |
| [Mermaid Auto-Reparável](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*Básico*</sup> | Gera diagramas Mermaid com recuperação automática de erros |
| [Heartbeat](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*Básico*</sup> | Monitoramento periódico sempre ativo semelhante ao ClawBot com fluxos aninhados |
| [Geração de Leads](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*Intermediário*</sup> | Pipeline de vendas: raspar, enriquecer, pontuar e personalizar e-mails |
| [Newsletter](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*Intermediário*</sup> | Curadoria de newsletter com IA: buscar, filtrar, sumarizar e formatar |
| [Processamento de Faturas](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*Intermediário*</sup> | Extrair e validar dados de faturas em PDFs usando visão |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*Intermediário*</sup> | Transforme documentos em um podcast com dois apresentadores de IA |
| [Pesquisa Profunda](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*Intermediário*</sup> | Pesquisa map-reduce recursiva com refinamento iterativo |
| [Agente de Codificação](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*Avançado*</sup> | Agente de codificação de produção com 6 ferramentas, memória e patch como subfluxo |

</div>

👀 Quer ver outros tutoriais para iniciantes? [Crie uma issue!](https://github.com/The-Pocket/PocketFlow/issues/new)

## Como usar o Pocket Flow?

🚀 Através da **Codificação Agêntica**—o paradigma de desenvolvimento de aplicações LLM mais rápido—onde *humanos projetam* e *agentes codificam*!

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ Abaixo estão exemplos de aplicações LLM mais complexas:

<div align="center">
  
|  Nome do App     |  Dificuldade    | Tópicos  | Design Humano | Código do Agente |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [Chatbot de Website](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>Transforme seu site em um gênio de suporte ao cliente 24/7</sup></sub> | ★★☆ <br> *Médio* | [Agente](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [Doc de Design](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [Simulador Danganronpa](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>Esqueça o teste de Turing. Danganronpa, o experimento de IA definitivo!</sup></sub> | ★★★ <br> *Avançado*   | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [Agente](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Doc de Design](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [Construtor de Conhecimento de Base de Código](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>A vida é curta demais para ficar encarando o código alheio com confusão</sup></sub> |  ★★☆ <br> *Médio* | [Workflow](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [Doc de Design](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [Construa o Cursor com o Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>Chegaremos à singularidade em breve ...</sup></sub> | ★★★ <br> *Avançado*   | [Agente](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [Doc de Design](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [Pergunte ao AI Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>Pergunte ao AI Paul Graham, caso você não seja aceito</sup></sub> | ★★☆ <br> *Médio*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [Doc de Design](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Resumidor do Youtube](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> Explica vídeos do YouTube para você como se tivesse 5 anos </sup></sub> | ★☆☆ <br> *Iniciante*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [Doc de Design](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [Gerador de Abertura Fria](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> Quebra-gelos instantâneos que transformam leads frios em quentes </sup></sub> | ★☆☆ <br> *Iniciante*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Busca na Web](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [Doc de Design](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Código do Fluxo](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- Quer aprender **Codificação Agêntica**?

  - Confira [meu YouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) para tutoriais em vídeo sobre como alguns dos apps acima foram criados!

  - Quer construir seu próprio App LLM? Leia este [post](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)! Comece com [este template](https://github.com/The-Pocket/PocketFlow-Template-Python)!