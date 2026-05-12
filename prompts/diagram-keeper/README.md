# diagram-keeper

コードベースのクラス図・コールグラフを Mermaid 形式で生成し、コードが変わるたびに最新状態を保ち続けるツール。
生成 AI（Claude.ai・ChatGPT 等）に貼り付けるだけで動く。API キー・外部サービス不要。

## 2 つのロール

## 利用者（図を読む・活用する）

既存のクラス図・コールグラフを VS Code でプレビューし、任意のシナリオのシーケンス図をオンデマンドで派生させる。`bundle.py` 不要。

## 管理者（図を作る・維持する）

コード変更のたびに `bundle.py` でソースをバンドルし、AI にプロンプトと合わせて貼り付けてマスタ図を更新する。9 言語対応（C/C++・Java・C#・Python・TypeScript・JavaScript・PHP・Rust・Visual Basic）。

## 前提環境

### 利用者

- VS Code + [Mermaid Chart 拡張](https://marketplace.visualstudio.com/items?itemName=MermaidChart.vscode-mermaid-chart)
- 生成 AI（Claude.ai・ChatGPT 等）

### 管理者（上記に加えて）

- Python 3.8 以上（標準ライブラリのみ）

## ドキュメント

→ [docs/index.md](docs/index.md)

## ファイル構成

| パス | 役割 |
| --- | --- |
| `scripts/bundle.py` | ソースツリーを MANIFEST 形式に変換 |
| `prompts/diagrams-upsert.md` | マスタ2枚の Upsert（Create + Update） |
| `prompts/diagrams-delete.md` | マスタ2枚の Delete |
| `prompts/diagrams-convert-to-sequence.md` | マスタ2枚からシーケンス図を派生 |
| `docs/` | Diataxis 形式のドキュメント |
