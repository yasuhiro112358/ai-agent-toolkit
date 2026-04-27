# 対話型生成AIによるコード依存関係分析ツール

C++ / Java / C# コードベースの依存関係を、対話型 AI（UI のみ）＋ VS Code ローカルプレビューで可視化するツール。API キー・GitHub・外部アカウント不要。

## 前提環境

- Python 3.8 以上（標準ライブラリのみ）
- VS Code + [Mermaid Chart 拡張](https://marketplace.visualstudio.com/items?itemName=MermaidChart.vscode-mermaid-chart)（アカウント登録不要）
- 対話型 AI（Claude.ai / ChatGPT 等の UI）

## クイックスタート

```bash
# 1. ソースをバンドル
python bundle.py --root /path/to/src

# 2. AI に貼り付け（diagrams-upsert.md の全文 + bundle.txt の内容）

# 3. 応答の class-diagram.md と call-graph.md を diagrams/ に保存
```

初回の詳細手順は [チュートリアル](docs/tutorials/first-diagram.md) を参照。

## ドキュメント

| カテゴリ | ドキュメント |
|---------|------------|
| チュートリアル | [はじめての依存関係図](docs/tutorials/first-diagram.md) |
| ハウツー | [図を更新する](docs/how-to/update-diagrams.md) / [エントリを削除する](docs/how-to/delete-entries.md) / [シーケンス図を派生する](docs/how-to/derive-sequence.md) |
| リファレンス | [bundle.py CLI](docs/reference/bundle-py.md) / [プロンプトファイル仕様](docs/reference/prompts.md) |
| 解説 | [設計の判断](docs/explanation/design-decisions.md) |

## ファイル構成

| ファイル | 役割 |
|---------|------|
| `requirements.md` | 要件確認書（SRS-lite） |
| `bundle.py` | ソースツリーを MANIFEST 形式に変換 |
| `diagrams-upsert.md` | マスタ 2 枚の Upsert（Create + Update） |
| `diagrams-delete.md` | マスタ 2 枚の Delete |
| `diagrams-convert-to-sequence.md` | マスタ 2 枚からシーケンス図を派生 |
| `docs/` | Diataxis 形式の利用者向けドキュメント |
