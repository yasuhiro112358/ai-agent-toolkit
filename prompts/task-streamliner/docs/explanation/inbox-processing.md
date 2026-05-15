# Inbox 処理のフロー

セッション開始時に AI が Inbox のメモを WBS タスクに変換する処理。

```mermaid
flowchart TD
    S([開始])
    E([終了])

    S --> HasInbox{Inbox に\nアイテムがある?}
    HasInbox -- No --> CPM
    HasInbox -- Yes --> AutoClassify{AIが判断:\nスコープと期日を\n推測できる?}
    AutoClassify -- "推測できる（WBS へ）" --> Parse["メモを解析\n（ゴール・範囲・成果物を読み取る）"]
    AutoClassify -- "明らかに先送り（Backlog へ）" --> ToBacklog["Backlog に移す"]
    AutoClassify -- "判断不能" --> AskUser["ユーザーに確認する\n（WBS / Backlog / 削除）"]
    AskUser --> UserDecision{ユーザーの回答}
    UserDecision -- "WBS へ" --> Parse
    UserDecision -- "Backlog へ" --> ToBacklog
    UserDecision -- "削除" --> NextItem
    ToBacklog --> NextItem{次のアイテムがある?}
    Parse --> CreateST["サマリータスクを作成\nWBS コード採番（1, 2, 3 …）"]
    CreateST --> Atomic{1ステップで\n完了できるか?}
    Atomic -- Yes --> OneLeaf["リーフタスクを1件追加\nWBS: 親.1"]
    Atomic -- No --> MultiLeaf["リーフタスクに分解\nWBS: 親.1, 親.2 …\ndepends_on を設定"]
    OneLeaf --> Fill["due・tags・estimate を補完\n（不明な場合は推測し、\n不確かなときはコメントを付記）"]
    MultiLeaf --> Fill
    Fill --> NextItem
    NextItem -- Yes --> AutoClassify
    NextItem -- No --> Clean["処理済みアイテムを Inbox から削除する"]
    Clean --> CPM["CPM 計算\nフロートを算出し WBS テーブルを実行優先順に並べ替える"]
    CPM --> Summary["変更サマリーを返す"]
    Summary --> E
```

## AI の判断基準

| 判断 | 条件 |
| --- | --- |
| WBS へ（自動） | スコープが読み取れ、期日を推測できる |
| Backlog へ（自動） | 「いつかやる」「そのうち」など明示的に先送りの意図がある |
| ユーザーに確認 | スコープまたは期日が不明で推測もできない |

WBS の構造定義は [explanation/wbs.md](wbs.md) を参照。
AIの操作ルール全体は [reference/ai-behavior.md](../reference/ai-behavior.md) を参照。

---

← [ドキュメント一覧](../index.md)
