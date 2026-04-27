[ドキュメント](../README.md) > [チュートリアル](README.md) > マスタ図を活用する

> **Diataxis: Tutorial** — 既存のマスタ図を手元に、実際に読んで・動かして・派生させる体験をする。マスタ図の作り方は扱わない。

# チュートリアル: マスタ図を活用する

このチュートリアルは「マスタ図（`diagrams/class-diagram.md` と `diagrams/call-graph.md`）が手元にある状態」から始まる。コードを読まなくても、マスタ図と AI だけでアーキテクチャの調査や影響範囲の把握ができる。

## 前提

- VS Code + Mermaid Chart 拡張（`MermaidChart.vscode-mermaid-chart`）がインストール済み
- `diagrams/class-diagram.md` と `diagrams/call-graph.md` が手元にある
- Claude.ai / ChatGPT 等の対話型 AI にアクセスできる

---

## Step 1: VS Code でマスタ図を開いてプレビューする

1. VS Code で `diagrams/class-diagram.md` を開く
2. コマンドパレット（`Cmd+Shift+P` / `Ctrl+Shift+P`）を開き「Mermaid: Preview Current File」を実行する
3. クラス図が横に表示されることを確認する
4. `diagrams/call-graph.md` も同様にプレビューする

> プレビューが表示されない場合は Mermaid Chart 拡張がインストールされているか確認する。

---

## Step 2: クラス図を読む（静的構造の把握）

クラス図（`classDiagram`）は「このコードベースに何があるか」を一覧できる図。

**読み方の基本:**

| 記号 | 意味 |
|------|------|
| `<<interface>>` | インターフェース |
| `+` / `-` / `#` | public / private / protected |
| `<\|--` | 継承（矢印の先が親クラス） |
| `<\|..` | インターフェース実装 |
| `*--` | 合成（ライフサイクルが一体） |
| `o--` | 集約（独立して存在できる） |
| `..>` | 依存（一方的に使う） |

**確認してみること:**
- 「このクラスは何を継承しているか」→ `<|--` の矢印をたどる
- 「このインターフェースを実装しているクラスはどれか」→ `<|..` の矢印をたどる
- 「このクラスが持つメソッド一覧」→ クラスブロック内を確認する

---

## Step 3: コールグラフを読む（呼び出し関係の把握）

コールグラフ（`flowchart LR`）は「このメソッドを変えたら何に波及するか」を調べる図。

**読み方の基本:**

- ノード = メソッド（`ClassName.methodName` 形式）
- 矢印 = 「左が右を呼ぶ」という関係（時系列ではない）

**確認してみること:**
- 「`AuthManager.authenticate` を変えたら何が影響を受けるか」→ そのノードに入ってくる矢印をたどる
- 「`Main.run` から何が呼ばれるか」→ そのノードから出ていく矢印をたどる

---

## Step 4: シーケンス図を派生させる

コールグラフの呼び出し関係を「時系列」に展開したのがシーケンス図。特定のシナリオについて AI に生成させる。

### 4-1. AI にプロンプトとマスタを貼り付ける

対話型 AI の入力欄に以下を **1 メッセージで** 貼り付けて送信する:

```
1. diagrams-convert-to-sequence.md の全文
2. diagrams/class-diagram.md の全文
3. diagrams/call-graph.md の全文
4. シナリオ指示（自然言語）
```

**シナリオ指示の例:**

```
AuthManager.authenticate から始まる処理の時系列を描いて
```

```
auth パッケージ内部の相互作用だけ、正常系で
```

### 4-2. 応答を確認する

AI が `sequenceDiagram` を含む Mermaid ブロックを返す。返ってきた内容を新しいファイルに貼り付けて VS Code でプレビューすると図として表示される。

```
diagrams/sequences/auth-login.md  ← ここに保存すると Git 管理できる
```

使い捨てでよければ保存しなくていい。

---

## 完了

マスタ図を読み、シーケンス図を派生させるところまで体験できた。

次にやること:
- シナリオを変えてシーケンス図をいくつか試す → [シーケンス図を派生する](../how-to/derive-sequence.md)
- 図の読み方の詳細 → [プロンプトファイル仕様](../reference/prompts.md)
- マスタ図を自分で作りたい場合 → [コードから初めてマスタ図を作る](first-diagram.md)（管理者向け）

---

[← チュートリアル一覧](README.md) | [ドキュメント一覧](../README.md)
