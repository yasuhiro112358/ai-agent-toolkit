[ドキュメント](../README.md) > [ハウツー](README.md) > 図を更新する

> **Diataxis: How-to** — コード変更後にマスタを最新状態に保つ。

# ハウツー: 図を更新する（Upsert）

コードを追加・変更したとき、マスタ 2 枚（クラス図・コールグラフ）を最新状態に更新する手順。

## 通常の更新（小〜中規模の変更）

```bash
# 1. 変更があったディレクトリをバンドル
python bundle.py --root ./src/auth --out bundle.txt

# 2. AI に以下を 1 メッセージで貼り付ける
#    - diagrams-upsert.md の全文
#    - 既存の class-diagram.md の全文
#    - 既存の call-graph.md の全文
#    - bundle.txt の内容

# 3. 応答から class-diagram.md / call-graph.md を diagrams/ に上書き保存
```

> バンドルに含まれないファイルのエントリは変更されない。パッケージ単位でバンドルを投入しても、他パッケージのエントリはマスタに保持される。

## 大規模コードを分割して投入する（チャンク Upsert）

コードが大きく 1 回の貼り付けに収まらない場合、`--max-chars` でチャンク分割してから繰り返し投入する。

```bash
# チャンク分割してバンドル（例: 50,000 字ずつ）
python bundle.py --root ./src --out bundle.txt --max-chars 50000
# → bundle-001.txt, bundle-002.txt, ... が生成される
```

投入手順:

```
1. bundle-001.txt を Upsert → class-diagram.md, call-graph.md を保存
2. 前ステップの出力をマスタとして bundle-002.txt を Upsert → 上書き保存
3. 全チャンクが終わるまで繰り返す
4. VS Code でプレビュー確認 → Git コミット
```

> チャンクごとに「既存マスタ = 前ステップの出力」を使うこと。初回投入のマスタを使い回すとエントリが失われる。

## 特定ディレクトリだけ更新する（--include / --exclude）

変更があったサブディレクトリだけをターゲットにする場合:

```bash
# auth パッケージだけバンドル
python bundle.py --root ./src \
  --include 'auth/*' \
  --out bundle-auth.txt
```

## 関連

- [エントリを削除する](delete-entries.md)
- [bundle.py CLI リファレンス](../reference/bundle-py.md)（チャンクサイズの決め方はこちら）

---

[← ハウツー一覧](README.md) | [ドキュメント一覧](../README.md)
