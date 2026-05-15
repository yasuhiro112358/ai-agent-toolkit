# ディレクトリ構造の設計意図

## 構成

```text
task-streamliner/
├── templates/   ← ユーザーが直接触るファイル
├── prompts/     ← 保険用の単体プロンプト
├── examples/    ← 動作確認・チュートリアル用サンプル
└── docs/        ← ドキュメント
```

## templates/ と prompts/ を分けた理由

役割の明確化のため。

- **`templates/`** はユーザーが毎回コピペして使うテンプレート置き場。「このディレクトリを見れば使い始められる」という自明性を持たせる
- **`prompts/`** はAIへの指示文書置き場。`templates/tasks.md` の AI Instructions が壊れた際の復旧用として存在し、通常は触れない

diagram-keeper が `prompts/` にプロンプトファイルを置く構成と対応しており、リポジトリ全体での命名規則とも整合している。

---

← [ドキュメント一覧](../index.md)
