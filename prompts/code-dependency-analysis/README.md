# 対話型生成AIによるコード依存関係分析ツール

コードベースの依存関係を、AI との会話だけでクラス図・コールグラフとして可視化・維持管理するツール。
成果物は Mermaid 形式の `.md` ファイルとしてリポジトリに保存される。API キー・外部サービス不要。

## 2 つの使い方

**利用者**（図を読む・活用する）  
既存のクラス図・コールグラフを VS Code でプレビューし、任意のシナリオに対応するシーケンス図をオンデマンドで生成する。`bundle.py` もプロンプト操作も不要。

**管理者**（図を作る・維持する）  
コード変更のたびに `bundle.py` でソースをバンドルし、AI に貼り付けてマスタ図を更新する。9 言語対応（C/C++・Java・C#・Python・TypeScript・JavaScript・PHP・Rust・Visual Basic）。

## 前提環境

**利用者**
- VS Code + [Mermaid Chart 拡張](https://marketplace.visualstudio.com/items?itemName=MermaidChart.vscode-mermaid-chart)
- 対話型 AI（Claude.ai / ChatGPT 等の UI）

**管理者**（上記に加えて）
- Python 3.8 以上（標準ライブラリのみ）

## ドキュメント

| カテゴリ | 内容 |
|---------|------|
| [チュートリアル](docs/tutorials/README.md) | 図を読む（利用者向け）・図を作る（管理者向け） |
| [ハウツー](docs/how-to/README.md) | 図の更新・削除・シーケンス派生 |
| [リファレンス](docs/reference/README.md) | bundle.py CLI・プロンプトファイル仕様 |
| [解説](docs/explanation/design-decisions.md) | 設計の判断根拠 |

## ファイル構成

| ファイル | 役割 |
|---------|------|
| `requirements.md` | 要件確認書（SRS-lite） |
| `bundle.py` | ソースツリーを MANIFEST 形式に変換 |
| `diagrams-upsert.md` | マスタ 2 枚の Upsert（Create + Update） |
| `diagrams-delete.md` | マスタ 2 枚の Delete |
| `diagrams-convert-to-sequence.md` | マスタ 2 枚からシーケンス図を派生 |
| `docs/` | Diataxis 形式のドキュメント |
