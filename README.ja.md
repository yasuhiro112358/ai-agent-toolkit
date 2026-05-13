# ai-agent-toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AIエージェント・生成AIサービスで使える、再利用可能なプロンプト・スキル・エージェントのコレクションです。

[English version](README.md)

---

## このリポジトリについて

Claude Code、Claude.ai、ChatGPT など、あらゆるAIエージェント・チャットAIサービスで活用できるプロンプトとスキルを公開しています。

- **Claude Code ユーザー向け**: スキルフォルダを `~/.claude/skills/` にコピーして `/スキル名` で呼び出す
- **その他のチャットAI ユーザー向け**: プロンプト本文をそのまま会話に貼り付けて使う

---

## プロンプト

Claude Code 不要で使える単体プロンプト。ファイル内容をそのままチャット AI に貼り付けて使います。

| 名前 | 概要 | 依存 |
| --- | --- | --- |
| [diagram-keeper](prompts/diagram-keeper/README.ja.md) | 生成 AI でコードのクラス図・コールグラフ（Mermaid）を生成・維持管理し、コードの変化と同期し続ける | Python 3.8+、VS Code + Mermaid Chart 拡張 |
| [prompt-create-from-conversation](prompts/prompt-create-from-conversation/README.md) | 完了した AI 作業から再利用可能なプロンプトを生成 | なし |
| [task-management](prompts/task-management/README.md) | チャット AI（Claude.ai・ChatGPT 等）に貼り付けるだけで動くプロンプト駆動タスク管理システム。API キー・サーバー不要 | なし |

---

## スキル一覧

| 名前 | カテゴリ | 概要 | 依存 |
| --- | --- | --- | --- |
| *(準備中)* | - | - | - |

---

## エージェント一覧

| 名前 | 概要 | 必要なツール |
| --- | --- | --- |
| *(準備中)* | - | - |

---

## ライセンス

MIT License — 詳細は [LICENSE](LICENSE) を参照してください。
