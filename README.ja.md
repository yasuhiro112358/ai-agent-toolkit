# claude-code-skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yasuhiro112358/claude-code-skills/pulls)

再利用可能な Claude Code スキル・プロンプトのコレクションです。

[English version](README.md)

---

## このリポジトリについて

[Claude Code](https://claude.ai/code) のスキル（`SKILL.md` 形式）と単体プロンプトを公開しています。

- **Claude Code ユーザー向け**: スキルフォルダを `~/.claude/skills/` にコピーして `/スキル名` で呼び出す
- **Claude.ai / API ユーザー向け**: `SKILL.md` のプロンプト本文をそのまま会話に貼り付けて使う

---

## クイックスタート

```bash
# リポジトリをクローン
git clone https://github.com/yasuhiro112358/claude-code-skills.git

# スキルを Claude Code のスキルディレクトリにコピー
cp -r claude-code-skills/skills/smart-commit ~/.claude/skills/

# Claude Code で呼び出す
# /smart-commit
```

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

## プロンプト

Claude Code 不要で使える単体プロンプト。ファイル内容をそのままチャット AI に貼り付けて使います。

| 名前 | 概要 | 依存 |
| --- | --- | --- |
| [generate-prompt-from-conversation](prompts/generate-prompt-from-conversation.md) | 完了した AI 作業から再利用可能なプロンプトを生成 | なし |
| [diagram-keeper](prompts/diagram-keeper/) | 生成 AI でコードのクラス図・コールグラフ（Mermaid）を生成・維持管理し、コードの変化と同期し続ける | Python 3.8+、VS Code + Mermaid Chart 拡張 |
| [task-management](prompts/task-management/) | チャット AI（Claude.ai・ChatGPT 等）に貼り付けるだけで動くプロンプト駆動タスク管理システム。API キー・サーバー不要 | なし |

---

## ライセンス

MIT License — 詳細は [LICENSE](LICENSE) を参照してください。
