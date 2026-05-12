# code-dependency-analysis/

コードベースの依存関係を、AI との会話だけでクラス図・コールグラフとして可視化・維持管理するツールのドキュメント。
[Diátaxis](https://diataxis.fr/) フレームワーク（tutorials / how-to / reference / explanation）で構造化。

---

## 用途別ナビゲーション

| やりたいこと | 参照先 |
| --- | --- |
| 初めてマスタ図を作りたい | [tutorials/first-diagram.md](tutorials/first-diagram.md) |
| 既存のマスタ図を読んで活用したい | [tutorials/use-existing-diagrams.md](tutorials/use-existing-diagrams.md) |
| コード変更後にマスタを更新したい | [how-to/update-diagrams.md](how-to/update-diagrams.md) |
| コードを削除したのでマスタからも消したい | [how-to/delete-entries.md](how-to/delete-entries.md) |
| シーケンス図をオンデマンドで生成したい | [how-to/derive-sequence.md](how-to/derive-sequence.md) |
| マスタが肥大化したので分割したい | [how-to/split-diagrams.md](how-to/split-diagrams.md) |
| bundle.py のオプションを確認したい | [reference/bundle-py.md](reference/bundle-py.md) |
| プロンプトファイルの仕様を確認したい | [reference/prompts.md](reference/prompts.md) |
| マスタ2枚の仕様を確認したい | [reference/diagram-spec.md](reference/diagram-spec.md) |
| 対応言語・制約条件を確認したい | [reference/constraints.md](reference/constraints.md) |
| なぜこの設計になっているかを理解したい | [explanation/architecture-overview.md](explanation/architecture-overview.md) |

---

## 全ファイル索引

### tutorials/ — まず動かす

| ファイル | 内容 |
| --- | --- |
| [first-diagram.md](tutorials/first-diagram.md) | bundle.py でコードをバンドルし、AI でマスタ図を初めて作る（管理者向け） |
| [use-existing-diagrams.md](tutorials/use-existing-diagrams.md) | 既存マスタ図を VS Code でプレビューし、シーケンス図を派生させる（利用者向け） |

### how-to/ — 特定の作業をこなす

| ファイル | 内容 |
| --- | --- |
| [update-diagrams.md](how-to/update-diagrams.md) | コード変更後にマスタを Upsert する |
| [delete-entries.md](how-to/delete-entries.md) | 削除されたコードをマスタから除去する |
| [derive-sequence.md](how-to/derive-sequence.md) | マスタ2枚からシーケンス図をオンデマンド生成する |
| [split-diagrams.md](how-to/split-diagrams.md) | 肥大化したマスタをパッケージ単位に分割・統合する |

### reference/ — 正確な仕様を調べる

| ファイル | 内容 |
| --- | --- |
| [bundle-py.md](reference/bundle-py.md) | bundle.py のCLIオプション・出力フォーマット・チャンクサイズの決め方 |
| [prompts.md](reference/prompts.md) | 3プロンプトファイルの入出力・挙動・共通フォーマット |
| [diagram-spec.md](reference/diagram-spec.md) | クラス図・コールグラフの仕様・ファイルレイアウト・スケーリング方針 |
| [constraints.md](reference/constraints.md) | 対応言語・制約条件・対象外・環境要件・成功条件 |

### explanation/ — なぜこうなっているかを理解する

| ファイル | 内容 |
| --- | --- |
| [architecture-overview.md](explanation/architecture-overview.md) | 背景・目的・全体アーキテクチャ（ツール全体の設計思想の起点） |
| [direct-generation.md](explanation/direct-generation.md) | なぜ JSON 中間層を挟まず直接 Mermaid を生成するか |
| [two-diagram-design.md](explanation/two-diagram-design.md) | なぜクラス図＋コールグラフの2枚構成か |
| [sequence-as-derived.md](explanation/sequence-as-derived.md) | なぜシーケンス図をマスタに含めず派生物として扱うか |
| [batch-input.md](explanation/batch-input.md) | なぜ対話型でなく一括投入型のプロンプト設計か |
| [mermaid-choice.md](explanation/mermaid-choice.md) | なぜ Mermaid を採用し PlantUML / Graphviz を不採用にしたか |

---

← [README に戻る](../README.md)
