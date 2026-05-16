# Explanation: include / exclude の評価順

[diagram-keeper/](../index.md) > explanation


`include` を先に評価し、その結果に対して `exclude` を適用する。

これにより「`src/auth/` 配下を対象にしつつ、その中のテストファイルは除く」という自然な絞り込みが1つの `pack.cfg` で表現できる。`include` で範囲を定め、`exclude` でさらに除外するという直感的な順序に従った。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
