[diagram-keeper/](../index.md) > explanation

# Explanation: なぜスクリプト名を pack にしたか

「コードを1つのテキストにまとめる」操作を表す動詞として `pack` を採用した。

候補として `bundle` も検討したが、JavaScript エコシステムの「バンドラー（webpack 等）」と混同しやすいため回避した。`pack` はビルドツール文脈でも自然に読め、「詰め込む」という操作の意味が直接伝わる。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
