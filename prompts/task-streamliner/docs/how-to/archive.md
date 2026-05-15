# アーカイブ

`tasks.md` が肥大化してきたら `Done` / `Cancelled` タスクをアーカイブして軽量化する。

```mermaid
flowchart TD
    S([開始])
    E([終了])

    S --> Trigger["「アーカイブして」と入力する"]
    Trigger --> Return["AIが2つの内容を返す\n① アーカイブ用\n② 整理後のファイル"]
    Return --> Exists{同月の archive\nファイルがある?}
    Exists -- Yes --> Append["① を末尾に追記する"]
    Exists -- No --> New["① で新規作成する"]
    Append --> CopyTasks
    New --> CopyTasks["② を tasks.md に\n上書き保存する"]
    CopyTasks --> E
```

| 出力 | 内容 | 保存先 |
| --- | --- | --- |
| ① アーカイブ用 | `Done` / `Cancelled` タスクの一覧 | `tasks-archive-YYYY-MM.md`（月単位） |
| ② 整理後のファイル | アーカイブ対象を除いた `tasks.md` 全文 | `templates/tasks.md` |

---

← [ドキュメント一覧](../index.md)
