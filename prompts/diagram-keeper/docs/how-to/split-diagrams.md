[diagram-keeper/](../index.md) > how-to

# How-to: マスタを分割・統合する

マスタ図が肥大化してレンダリングが困難になった場合、パッケージ単位に分割する。

---

## いつ分割するか

分割は必要になってから行う。既定は常に1枚。

| 図 | 分割トリガー |
| --- | --- |
| クラス図 | 50 クラス超 / 200 関係超、またはレンダリング不可 |
| コールグラフ | 300 ノード超、または AI が出力途中で打ち切られる |

---

## 分割する手順

Upsert 時に AI への貼り付けに分割指示を加える。

AI に以下を **1 メッセージで** 貼り付けて送信する。

1. `prompts/diagrams-upsert.md` の全文
2. 既存マスタ2枚の全文
3. `bundle.txt` の内容
4. 分割指示（例: 「パッケージ単位に分割して `class-<packageName>.md` と `call-graph-<packageName>.md` で返して。あわせてパッケージ間の依存を示す `package-diagram.md` も作って」）

応答から各ファイルを取り出して保存し、VS Code でプレビュー確認 → Git コミット。

分割後のファイルレイアウト:

```text
diagrams/
├── package-diagram.md             # パッケージ間の全体俯瞰
├── class-auth.md                  # auth パッケージのクラス図
├── class-core.md                  # core パッケージのクラス図
├── call-graph-auth.md             # auth パッケージのコールグラフ
├── call-graph-core.md             # core パッケージのコールグラフ
└── sequences/
    └── <name>.md
```

---

## 統合する手順

Upsert 時の指示に「全パッケージを1枚に統合して」を加えるだけでよい。マスタはテキストファイルなので、Upsert 時の粒度指示を切り替えれば再生成で可逆に統合・分割できる。

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- マスタを更新する基本手順 → [update-diagrams.md](update-diagrams.md)
- クラス図・コールグラフの仕様 → [../reference/diagram-spec.md](../reference/diagram-spec.md)
