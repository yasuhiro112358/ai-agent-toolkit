# Tutorial: マスタ図の活用

[diagram-keeper/](../index.md) > tutorials


`diagrams/class-diagram.md` と `diagrams/call-graph.md` が手元にある状態から始める。マスタ図を読んで、シーケンス図を派生させるまでを体験する。

前提: VS Code + Mermaid Chart 拡張（`MermaidChart.vscode-mermaid-chart`）・生成 AI（Claude.ai 等）・マスタ2枚が手元にあること

---

## Step 1: VS Code でプレビューする

1. VS Code で `diagrams/class-diagram.md` を開く
2. コマンドパレット（`Cmd+Shift+P` / `Ctrl+Shift+P`）から「Mermaid: Preview Current File」を実行する
3. クラス図が横に表示されることを確認する
4. `diagrams/call-graph.md` も同様にプレビューする

> プレビューが表示されない場合は Mermaid Chart 拡張がインストールされているか確認する。

## Step 2: クラス図を読む

クラス図（`classDiagram`）は「このコードベースに何があるか」を一覧できる図。

| 記号 | 意味 |
| --- | --- |
| `<<interface>>` | インターフェース |
| `+` / `-` / `#` | public / private / protected |
| `<\|--` | 継承（矢印の先が親クラス） |
| `<\|..` | インターフェース実装 |
| `*--` | 合成（ライフサイクルが一体） |
| `o--` | 集約（独立して存在できる） |
| `..>` | 依存（一方的に使う） |

確認してみること:

- 「このクラスは何を継承しているか」→ `<|--` の矢印をたどる
- 「このインターフェースを実装しているクラスはどれか」→ `<|..` の矢印をたどる
- 「このクラスが持つメソッド一覧」→ クラスブロック内を確認する

## Step 3: コールグラフを読む

コールグラフ（`flowchart LR`）は「この変更はどこに波及するか」を調べる図。

- ノード = メソッド（`ClassName.methodName` 形式）
- 矢印 = 「左が右を呼ぶ」という静的な関係（時系列ではない）

確認してみること:

- 「`AuthManager.authenticate` を変えたら何が影響を受けるか」→ そのノードに入ってくる矢印をたどる
- 「`Main.run` から何が呼ばれるか」→ そのノードから出ていく矢印をたどる

## Step 4: シーケンス図を派生させる

生成 AI の入力欄に以下を **1 メッセージで** 貼り付けて送信する。

1. `prompts/diagrams-convert-to-sequence.md` の全文
2. `diagrams/class-diagram.md` の全文
3. `diagrams/call-graph.md` の全文
4. シナリオ指示（例: `AuthManager.authenticate から始まる処理の時系列を描いて`）

AI が `sequenceDiagram` ブロックを含む Mermaid を返す。新しいファイルに貼り付けて VS Code でプレビューすると図として表示される。

保存する場合: `diagrams/sequences/auth-login.md` のように保存すると Git 管理できる。

## 完了

マスタ図を読み、シーケンス図を派生させるところまで体験できた。

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- シーケンス指示のバリエーション → [../how-to/derive-sequence.md](../how-to/derive-sequence.md)
- マスタ2枚の仕様（記号の完全版） → [../reference/diagram-spec.md](../reference/diagram-spec.md)
- マスタを自分で作りたい → [first-diagram.md](first-diagram.md)
