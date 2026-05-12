[diagram-keeper/](../index.md) > explanation

# Explanation: chunk_size の命名とデフォルト値

## 設定キー名: chunk_size

`max_chars` から `chunk_size` に変更した。

`max_chars` は「文字数の上限」という実装詳細が前面に出ており、ユーザーにとっての操作単位が見えにくい。`chunk_size` は「AI に1回で投入する塊のサイズ」という用途を直接表し、`chunk_size = 50000` のように書いたときに意味が伝わりやすい。

## デフォルト値: 50000

実運用の経験から、50000 文字（概ね 10〜30 ファイル相当）が AI のコンテキスト処理・応答品質・往復回数のバランスとして妥当な値だった。

小さすぎると往復回数が増えて Upsert の集約ミスが起きやすくなり、大きすぎると AI がクラスやエッジを取りこぼしやすくなる。調整の目安は [../how-to/update-with-chunks.md](../how-to/update-with-chunks.md) を参照。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
- チャンク分割して更新する手順 → [../how-to/update-with-chunks.md](../how-to/update-with-chunks.md)
