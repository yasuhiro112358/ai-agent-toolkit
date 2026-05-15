# WBS テーブル フィールド定義

`## WBS` セクションのテーブル仕様。

```markdown
| id | wbs | title | status | due | depends_on | tags | estimate |
|----|-----|-------|--------|-----|------------|------|----------|
```

---

## `id`

| 項目 | 値 |
| --- | --- |
| 型 | integer |
| 制約 | 採番後に変わらない。アーカイブ・削除後も再利用しない |
| 例 | `1`, `2`, `3` |

`depends_on` の参照先。WBS を再採番しても `id` は変わらないため、依存関係が壊れない。詳細は [explanation/archive-dataflow.md](../explanation/archive-dataflow.md) を参照。

## `wbs`

| 項目 | 値 |
| --- | --- |
| 型 | string |
| 形式 | ドット区切りの整数（`1`, `1.1`, `1.1.2`） |
| 制約 | 同一階層内で連番。削除後も再利用しない |
| 例 | `1`（サマリー）、`1.1`（リーフ）、`1.2.1`（深いリーフ） |

WBS の詳細は [explanation/wbs.md](../explanation/wbs.md) を参照。

## `title`

| 項目 | 値 |
| --- | --- |
| 型 | string |
| 制約 | 自由記述。パイプ文字（`\|`）は使用不可 |

## `status`

| 項目 | 値 |
| --- | --- |
| 型 | enum |
| 有効値 | `Todo` / `In-Progress` / `Waiting` / `Done` / `Cancelled` |
| リーフタスク | 直接管理する |
| サマリータスク | 子タスクの status から自動導出する |

遷移の詳細は [reference/status-transitions.md](status-transitions.md) を参照。

## `due`

| 項目 | 値 |
| --- | --- |
| 型 | string |
| 制約 | ISO 8601 date（`YYYY-MM-DD`）。期日なしは `—` |

## `depends_on`

| 項目 | 値 |
| --- | --- |
| 型 | string |
| 制約 | 先行タスクの `id` をカンマ区切りで列挙。なければ `—` |
| 例 | `2`, `2, 3`, `—` |
| 備考 | サマリータスクを参照した場合、配下のリーフタスクがすべて完了するまで待ち |

CPM 計算の入力として使用する。詳細は [explanation/cpm-prioritization.md](../explanation/cpm-prioritization.md) を参照。

## `tags`

| 項目 | 値 |
| --- | --- |
| 型 | string |
| 制約 | カンマ区切り。なければ `—` |
| 例 | `work, report`, `—` |

## `estimate`

| 項目 | 値 |
| --- | --- |
| 型 | string |
| 形式 | `{数値}{単位}`。単位は `m`（分）・`h`（時間）・`d`（日） |
| リーフタスク | 入力必須。CPM 計算に使用する |
| サマリータスク | `—`（子タスクの合計を自動算出） |
| 例 | `30m`, `2h`, `1d`, `—` |

---

## サンプル

```markdown
---
updated: 2026-05-15
---

## Inbox
<!-- 思いついたことをここに自由に書く。形式は問わない。後でAIに処理させる。 -->

## WBS

| wbs | title | status | due | depends_on | tags | estimate |
|-----|-------|--------|-----|------------|------|----------|
| 1   | 発表資料を作る | In-Progress | 2026-05-20 | — | work | — |
| 1.1 | 構成案を作る | Done | 2026-05-14 | — | work | 1h |
| 1.2 | スライド作成 | In-Progress | 2026-05-16 | 1.1 | work | 3h |
| 1.3 | レビュー依頼 | Waiting | 2026-05-17 | 1.2 | work | 30m |
| 1.4 | 発表練習 | Todo | 2026-05-19 | 1.3 | work | 1h |
| 2   | 本番環境を構築する | Waiting | 2026-05-22 | 1 | infra | — |
| 2.1 | サーバー設定 | Todo | 2026-05-21 | — | infra | 2h |
| 2.2 | デプロイ確認 | Todo | 2026-05-22 | 2.1 | infra | 30m |

## Backlog
- 本棚を整理する
```

---

← [ドキュメント一覧](../index.md)
