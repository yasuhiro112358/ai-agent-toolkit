# データスキーマ

`templates/tasks.md` のデータ形式の仕様。

---

## ファイル構造

```text
{frontmatter}
## Inbox
## WBS
## Backlog
## Gantt Chart
## Dependency Graph
---
## AI Instructions
```

セクション順は固定。`---` より前がユーザーデータ領域、以降がプロンプト領域。

ユーザーデータ領域の前半（Inbox・WBS・Backlog）はユーザーが記入するセクション、後半（Gantt Chart・Dependency Graph）は AI が自動生成するセクション。

---

## フロントマター

```yaml
---
updated: YYYY-MM-DD
---
```

| フィールド | 型 | 制約 |
| --- | --- | --- |
| `updated` | string | ISO 8601 date。全文出力時にAIが自動書き換え |

---

## セクション定義

### `## Inbox`

形式自由のキャプチャ領域。Markdown リスト・文章・走り書きすべて可。AIがセッション開始時に処理する。

### `## WBS`

WBS 構造でタスクを管理するテーブル。フィールド定義は [reference/wbs-fields.md](wbs-fields.md) を参照。

### `## Backlog`

未コミット候補リスト。形式自由。スコープ・期日が定まっていないため CPM の対象外。

### `## Gantt Chart`

mermaid gantt ブロック。AIが WBS テーブルの内容から自動生成・更新する。

### `## Dependency Graph`

mermaid graph ブロック。AIが `depends_on` から自動生成・更新する。

---

← [ドキュメント一覧](../index.md)
