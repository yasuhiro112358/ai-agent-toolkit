# AIの振る舞いルール

`templates/tasks.md` の末尾 `## AI Instructions` セクションに定義されている内容の早引き。

## セッション開始時の自動処理

詳細は [explanation/inbox-processing.md](../explanation/inbox-processing.md) を参照。

## 操作ルール

| 操作 | ルール |
| --- | --- |
| id 採番 | 既存の最大値 +1。削除・アーカイブ後も再利用しない |
| wbs 採番 | 同一階層内で連番。アーカイブ後に詰め直す（再採番） |
| status 遷移 | `Todo` → `In-Progress` → `Waiting` / `Done` / `Cancelled`。`depends_on` が未完了なら `Waiting` |
| サマリータスクの status | 子タスクから自動導出する。すべて Done/Cancelled → Done、1つでも In-Progress → In-Progress、1つでも Waiting → Waiting、それ以外 → Todo |
| depends_on 整合性 | 参照先 id が WBS テーブルに存在しない場合はユーザーに確認する |
| estimate 不足 | estimate が未入力のリーフタスクをユーザーに通知し、due 近い順でフロート計算済みタスクの後に配置する |
| アーカイブ | 全リーフが Done/Cancelled のサマリーを対象とする。サマリーと配下リーフをまとめて切り出し、WBS を再採番する。アーカイブ用内容と整理後の tasks.md を両方返す |
| 図の更新 | Gantt Chart・Dependency Graph は常に WBS テーブルと整合させる |

## 出力ルール

| 条件 | 出力 |
| --- | --- |
| 通常の指示 | 変更サマリーのみ（ファイル全文は返さない） |
| 「出力して」「終了」 | ファイル全文をコードブロックで返す |

全文出力時はセクション構成・フィールド名・フォーマットを変えず、フロントマターの `updated` を実行日に書き換える。

---

← [ドキュメント一覧](../index.md)
