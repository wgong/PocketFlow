<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100行のミニマリストLLMフレームワーク" width="600"/>
</div>

<!-- For translation, replace English with [English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md), and remove the link for the target language. -->

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | [中文](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_CHINESE.md) | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | 日本語 | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://the-pocket.github.io/PocketFlow/)
 <a href="https://discord.gg/hUHHE9Sa6T">
    <img src="https://img.shields.io/discord/1346833819172601907?logo=discord&style=flat">
</a>

Pocket Flow は [100行](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) のミニマリストLLMフレームワークです

- **軽量**: わずか100行。余分な肥大化ゼロ、依存関係ゼロ、ベンダーロックインゼロ。
  
- **表現力豊か**: あなたが好きなすべて——([マルチ-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[エージェント](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)、[ワークフロー](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)、[RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html)、その他多数。

- **[エージェントコーディング](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**: AIエージェント（例：Cursor AI）にエージェントを構築させる——生産性が10倍に！

Pocket Flowを始めましょう：
- インストールするには、```pip install pocketflow``` または [ソースコード](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)（わずか100行）をコピーするだけ。
- 詳しく学ぶには、[動画チュートリアル](https://youtu.be/0Zr3NwcvpA0) と [ドキュメント](https://the-pocket.github.io/PocketFlow/) をご覧ください。
- 🎉 Pocket Flowを使って開発する他の開発者と交流するために [Discord](https://discord.gg/hUHHE9Sa6T) に参加しましょう！
- 🎉 Pocket Flowは [Typescript](https://github.com/The-Pocket/PocketFlow-Typescript)、[Java](https://github.com/The-Pocket/PocketFlow-Java)、[C++](https://github.com/The-Pocket/PocketFlow-CPP)、[Go](https://github.com/The-Pocket/PocketFlow-Go)、[Rust](https://github.com/The-Pocket/PocketFlow-Rust)、[PHP](https://github.com/The-Pocket/PocketFlow-PHP) 版も登場！

## なぜPocket Flowなのか？

現在のLLMフレームワークは肥大化しています……LLMフレームワークに必要なのは100行だけ！

<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/meme.jpg" width="400"/>


  |                | **抽象化**          | **アプリ固有のラッパー**                                      | **ベンダー固有のラッパー**                                    | **行数**       | **サイズ**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | エージェント、チェーン               | 多数 <br><sup><sub>（例：QA、要約）</sub></sup>              | 多数 <br><sup><sub>（例：OpenAI、Pineconeなど）</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | エージェント、チェーン            | 多数 <br><sup><sub>（例：FileReadTool、SerperDevTool）</sub></sup>         | 多数 <br><sup><sub>（例：OpenAI、Anthropic、Pineconeなど）</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | エージェント                      | 一部 <br><sup><sub>（例：CodeAgent、VisitWebTool）</sub></sup>         | 一部 <br><sup><sub>（例：DuckDuckGo、Hugging Faceなど）</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | エージェント、グラフ           | 一部 <br><sup><sub>（例：セマンティック検索）</sub></sup>                     | 一部 <br><sup><sub>（例：PostgresStore、SqliteSaverなど）</sub></sup>        | 37K           | +51MB                      |
| AutoGen    | エージェント                | 一部 <br><sup><sub>（例：ツールエージェント、チャットエージェント）</sub></sup>              | 多数 <sup><sub>[オプション]<br>（例：OpenAI、Pineconeなど）</sub></sup>        | 7K <br><sup><sub>（コアのみ）</sub></sup>    | +26MB <br><sup><sub>（コアのみ）</sub></sup>          |
| **PocketFlow** | **グラフ**                    | **なし**                                                 | **なし**                                                  | **100**       | **+56KB**                  |

</div>

## Pocket Flowはどのように機能するのか？

[100行](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py) はLLMフレームワークのコア抽象化、すなわちグラフを捉えています！
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

そこから、([マルチ-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[エージェント](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)、[ワークフロー](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)、[RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) などの人気のデザインパターンを簡単に実装できます。
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ 以下は基本チュートリアルです：

<div align="center">
  
|  名前  | 難易度    |  説明  |  
| :-------------:  | :-------------: | :--------------------- |  
| [チャット](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <sup>*超簡単*</sup>  | 会話履歴を持つ基本的なチャットボット |
| [構造化出力](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <sup>*超簡単*</sup> | プロンプティングで履歴書から構造化データを抽出 |
| [ワークフロー](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <sup>*超簡単*</sup> | アウトライン作成、コンテンツ執筆、スタイル適用を行うライティングワークフロー |
| [エージェント](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <sup>*超簡単*</sup>  | ウェブ検索して質問に答えるリサーチエージェント |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <sup>*超簡単*</sup> | シンプルな検索拡張生成プロセス |
| [バッチ](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <sup>*超簡単*</sup> | マークダウンを複数言語に翻訳するバッチプロセッサー |
| [ストリーミング](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <sup>*超簡単*</sup> | ユーザー割り込み機能付きリアルタイムLLMストリーミングデモ |
| [チャットガードレール](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <sup>*超簡単*</sup> | 旅行関連のクエリのみ処理する旅行アドバイザーチャットボット |
| [多数決](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ☆☆☆ <sup>*超簡単*</sup> | 複数の解答を集約して推論精度を向上 |
| [マップリデュース](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ☆☆☆ <sup>*超簡単*</sup>  | マップリデュースパターンを使った履歴書の一括審査 |
| [CLI HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-cli-hitl) | ☆☆☆ <sup>*超簡単*</sup>  | 人間参加型フィードバック付きコマンドラインジョークジェネレーター |
| [マルチエージェント](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <sup>*初級*</sup> | 2つのエージェント間の非同期通信によるタブーワードゲーム |
| [スーパーバイザー](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <sup>*初級*</sup> | リサーチエージェントが不安定に……監督プロセスを構築しよう|
| [並列](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) |  ★☆☆ <sup>*初級*</sup> | 3倍の高速化を示す並列実行デモ |
| [並列フロー](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <sup>*初級*</sup> | 8倍の高速化を示す並列画像処理 |
| [思考](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) |  ★☆☆ <sup>*初級*</sup> | チェーンオブソートで複雑な推論問題を解決 |
| [メモリ](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) |  ★☆☆ <sup>*初級*</sup> | 短期・長期メモリを持つチャットボット |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) |  ★☆☆ <sup>*初級*</sup>  | 自動デバッグループで自然言語をSQLクエリに変換 |
| [コードジェネレーター](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-code-generator) | ★☆☆ <sup>*初級*</sup> | テストケースを生成し、解決策を実装し、コードを繰り返し改善 |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) |  ★☆☆ <sup>*初級*</sup> |  数値演算にモデルコンテキストプロトコルを使用するエージェント |
| [エージェントスキル](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent-skills) |  ★☆☆ <sup>*初級*</sup> | 再利用可能なマークダウンスキルにリクエストをルーティングしエージェントフローで適用 |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) |  ★☆☆ <sup>*初級*</sup> | エージェント間通信のためにA2Aプロトコルでラップされたエージェント |
| [Streamlit FSM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-streamlit-fsm) | ★☆☆ <sup>*初級*</sup> | HITL画像生成のための有限状態機械を持つStreamlitアプリ |
| [FastAPI WebSocket](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-websocket) | ★☆☆ <sup>*初級*</sup> | WebSocket経由でストリーミングLLMレスポンスを提供するリアルタイムチャットインターフェース |
| [FastAPI バックグラウンド](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-fastapi-background) | ★☆☆ <sup>*初級*</sup> | バックグラウンドジョブとSSEによるリアルタイム進捗表示を持つFastAPIアプリ |
| [ボイスチャット](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-voice-chat) | ★☆☆ <sup>*初級*</sup> | VAD、STT、LLM、TTSを備えたインタラクティブな音声チャットアプリケーション |
| [ジャッジ](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-judge) | ★☆☆ <sup>*初級*</sup> | 反復的なコンテンツ改善のためのLLM-as-Judge評価-最適化ループ |
| [ディベート](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-debate) | ★☆☆ <sup>*初級*</sup> | 2人の主張者と公平な審判による対立的推論 |
| [エージェントRAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agentic-rag) | ★☆☆ <sup>*初級*</sup> | どのドキュメントを読むかを判断するエージェント駆動型RAG |
| [自己修復Mermaid](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-self-healing-mermaid) | ★☆☆ <sup>*初級*</sup> | 自動エラー回復でMermaidダイアグラムを生成 |
| [ハートビート](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-heartbeat) | ★☆☆ <sup>*初級*</sup> | ネストされたフローを持つClawBot風の常時稼働型定期モニタリング |
| [リード生成](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-lead-generation) | ★★☆ <sup>*中級*</sup> | 営業パイプライン：スクレイピング、エンリッチメント、スコアリング、メールパーソナライズ |
| [ニュースレター](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-newsletter) | ★★☆ <sup>*中級*</sup> | AIニュースレターキュレーション：検索、フィルタリング、要約、フォーマット |
| [請求書処理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-invoice) | ★★☆ <sup>*中級*</sup> | ビジョンを使ってPDFから請求書データを抽出・検証 |
| [NotebookLM](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-notebook-lm) | ★★☆ <sup>*中級*</sup> | ドキュメントを2人のAIホストによるポッドキャストに変換 |
| [ディープリサーチ](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-deep-research) | ★★☆ <sup>*中級*</sup> | 反復的改善による再帰的マップリデュースリサーチ |
| [コーディングエージェント](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-coding-agent) | ★★★ <sup>*上級*</sup> | 6つのツール、メモリ、サブフローとしてのパッチを持つプロダクションコーディングエージェント |

</div>

👀 初心者向けの他のチュートリアルを見たいですか？ [イシューを作成してください！](https://github.com/The-Pocket/PocketFlow/issues/new)

## Pocket Flowの使い方は？

🚀 **エージェントコーディング**を通じて——最速のLLMアプリ開発パラダイム——*人間が設計*し、*エージェントがコーディング*します！

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ 以下はより複雑なLLMアプリの例です：

<div align="center">
  
|  アプリ名     |  難易度    | トピック  | 人間による設計 | エージェントによるコード |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [ウェブサイトチャットボット](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot) <br> <sup><sub>あなたのウェブサイトを24時間365日のカスタマーサポートの天才に変える</sup></sub> | ★★☆ <br> *中級* | [エージェント](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) <br> [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) | [設計ドキュメント](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/docs/design.md) | [フローコード](https://github.com/The-Pocket/PocketFlow-Tutorial-Website-Chatbot/blob/main/flow.py)
| [ダンガンロンパシミュレーター](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator) <br> <sup><sub>チューリングテストは忘れて。ダンガンロンパこそ究極のAI実験！</sup></sub> | ★★★ <br> *上級*   | [ワークフロー](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) <br> [エージェント](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [設計ドキュメント](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/docs/design.md) | [フローコード](https://github.com/The-Pocket/PocketFlow-Tutorial-Danganronpa-Simulator/blob/main/flow.py)
| [コードベース知識ビルダー](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>他人のコードを混乱しながら眺める人生は短すぎる</sup></sub> |  ★★☆ <br> *中級* | [ワークフロー](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [設計ドキュメント](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [フローコード](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [CursorでCursorを作る](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>もうすぐシンギュラリティに到達する……</sup></sub> | ★★★ <br> *上級*   | [エージェント](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [設計ドキュメント](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [フローコード](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [AI Paul Grahamに聞く](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>採用されなかった時のために、AI Paul Grahamに聞こう</sup></sub> | ★★☆ <br> *中級*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [マップリデュース](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [設計ドキュメント](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [フローコード](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [YouTube要約](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub>YouTubeの動画を5歳の子供にもわかるように説明する</sup></sub> | ★☆☆ <br> *初級*   | [マップリデュース](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [設計ドキュメント](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [フローコード](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [コールドオープナージェネレーター](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub>冷たいリードを熱くする即席のアイスブレーカー</sup></sub> | ★☆☆ <br> *初級*   | [マップリデュース](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [ウェブ検索](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [設計ドキュメント](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [フローコード](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)


</div>

- **エージェントコーディング**を学びたいですか？

  - 上記のアプリがどのように作られているかを紹介した動画チュートリアルは [私のYouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1) をご覧ください！

  - 独自のLLMアプリを構築したいですか？こちらの [投稿](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to) をお読みください！[このテンプレート](https://github.com/The-Pocket/PocketFlow-Template-Python) から始めましょう！