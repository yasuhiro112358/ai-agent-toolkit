[diagram-keeper/](../index.md) > explanation

# Explanation: pack.py / pack.cfg の設計判断

`pack.py` とその設定ファイル `pack.cfg` の設計において行った判断の一覧。

---

| 判断 | 詳細 |
| --- | --- |
| なぜスクリプト名を `pack` にしたか | [pack-naming.md](pack-naming.md) |
| なぜ設定ファイル方式（pack.cfg）を採用したか | [pack-cfg-design.md](pack-cfg-design.md) |
| なぜ変数名を `src` / `dest` にしたか | [pack-src-dest.md](pack-src-dest.md) |
| `chunk_size` の命名とデフォルト値 | [pack-chunk-size.md](pack-chunk-size.md) |
| なぜ出力ヘッダを `=== INDEX ===` にしたか | [pack-index-header.md](pack-index-header.md) |
| なぜ `ext` は追加ではなく置き換えか | [pack-ext-override.md](pack-ext-override.md) |
| `include` / `exclude` の評価順 | [pack-filter-order.md](pack-filter-order.md) |

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
- ツール全体の設計背景 → [architecture-overview.md](architecture-overview.md)
