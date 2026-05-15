# AIの振る舞いルール

`templates/tasks.md` の末尾 `## AI Instructions` セクションに定義されている内容の早引き。

## セッション開始時の自動処理

詳細は [explanation/inbox-processing.md](../explanation/inbox-processing.md) を参照。

## 操作ルール

| 操作 | ルール |
| --- | --- |
| wbs 採番 | 同一階層内で連番。削除後も再利用しない |
| status 遷移 | `Todo` → `In-Progress` → `Waiting` / `Done` / `Cancelled`。`depends_on` が未完了なら `Waiting` |
| depends_on 整合性 | 参照先 wbs が WBS テーブルに存在しない場合はユーザーに確認する |
| estimate 不足 | estimate が未入力のリーフタスクをユーザーに通知し、暫定値（`—`）のタスクは due 近い順に並べてフロート計算済みタスクの後に配置する |
| アーカイブ | `Done` / `Cancelled` を対象。アーカイブ用内容と整理後の `tasks.md` を両方返す |
| 図の更新 | Gantt Chart・Dependency Graph は常に WBS テーブルと整合させる |

## 出力ルール

| 条件 | 出力 |
| --- | --- |
| 通常の指示 | 変更サマリーのみ（ファイル全文は返さない） |
| 「出力して」「終了」 | ファイル全文をコードブロックで返す |

全文出力時はセクション構成・フィールド名・フォーマットを変えず、フロントマターの `updated` を実行日に書き換える。

---

← [ドキュメント一覧](../index.md)
