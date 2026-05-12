[diagram-keeper/](../index.md) > reference

# Reference: 制約条件・対象範囲

このツールが動作する制約条件、対応言語、対象外事項、環境要件、成功条件。

---

## 制約条件

| 項目 | 内容 |
| --- | --- |
| 利用可能な AI | 対話形式の生成 AI（UI のみ、API キー利用不可） |
| GitHub | 利用不可 |
| 外部アカウント | 利用不可 |
| 実行環境 | ローカル完結（VS Code + Python） |

> これらの制約がこのツールの設計の出発点。詳細は [../explanation/architecture-overview.md](../explanation/architecture-overview.md) 参照。

---

## 対応言語

| 言語 | 依存関係の記述形式 |
| --- | --- |
| C / C++ | `#include`（ヘッダ）、継承、前方宣言 |
| Java | `import`、`extends` / `implements`、パッケージ宣言 |
| C# | `using`、`namespace`、継承・インターフェース実装 |
| Visual Basic | `Imports`、`Inherits`、`Implements`、`Namespace` |
| Python | `import` / `from … import`、継承（クラス定義の括弧内） |
| TypeScript | `import`、`extends`、`implements` |
| JavaScript | `import` / `require`、`extends` |
| PHP | `use`（名前空間）、`extends`、`implements`、`namespace` |
| Rust | `use`、`impl`、`trait` 実装（`impl Trait for Type`） |

対象拡張子の詳細は [bundle-py.md](bundle-py.md) 参照。

---

## 対象外

| 項目 | 理由 |
| --- | --- |
| 依存関係の自動修正 | スコープ外 |
| API を使った完全自動化 | UI のみ利用のため |
| クラウド同期・共有 | MermaidChart アカウント必須のため |
| PlantUML | Java ローカルインストールが必要 |
| Graphviz / DOT 形式 | VS Code 公式エクステンションのサポートが弱い |
| 状態機械図・コンポーネント図・ER 図・ユースケース図等 | マスタに含めない。必要になったら個別対応を検討 |

---

## 環境要件

| 対象 | 要件 |
| --- | --- |
| 管理者 | Python 3.8 以上（標準ライブラリのみ） |
| 全員 | VS Code + Mermaid Chart 拡張（`MermaidChart.vscode-mermaid-chart`） |
| 全員 | 対話型 AI（Claude.ai / ChatGPT 等）へのアクセス |
| ネットワーク | 外部ネットワーク接続不要でローカル完結 |
| 追加インストール | VS Code エクステンションのみ |

---

## 成功条件

- 対話 UI のみで完結する（CLI / API キー不要）
- マスタ2枚が Mermaid Chart 拡張 / 標準的な Markdown レンダラでそのまま表示できる
- マスタ更新が CRUD プロンプト（Upsert / Delete）の貼り付けだけで完結する
- 大規模コードは複数チャンクに分けて Upsert を繰り返せば 1 コンテキストに収まり続ける
- シーケンス図がマスタ2枚のみからオンデマンドで派生できる（コード再読込不要）
- 各プロンプトファイルはその全文を貼り付けるだけで動作する

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- なぜこれらの制約のもとでこの設計になったか → [../explanation/architecture-overview.md](../explanation/architecture-overview.md)
- bundle.py の対象拡張子オプション → [bundle-py.md](bundle-py.md)
