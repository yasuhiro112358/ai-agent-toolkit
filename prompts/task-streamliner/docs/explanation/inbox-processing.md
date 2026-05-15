# Inbox 処理のフロー

セッション開始時に AI が Inbox のメモを WBS タスクに変換する処理。

## 全体フロー

```mermaid
flowchart TD
    S([開始])
    E([終了])

    S --> HasInbox{Inbox に\nアイテムがある?}
    HasInbox -- No --> CPM
    HasInbox -- Yes --> ForEach["各アイテムを分類・処理する"]
    ForEach --> Clean["処理済みアイテムを\nInbox から削除する"]
    Clean --> CPM["CPM 計算"]
    CPM --> Summary["変更サマリーを返す"]
    Summary --> E
```

CPM 計算の詳細は [explanation/cpm-prioritization.md](cpm-prioritization.md) を参照。

## アイテムの分類

Inbox の各アイテムに対して順に実行する。

```mermaid
flowchart TD
    S([アイテム])
    E([完了])

    S --> AutoClassify{スコープと期日を\n推測できる?}
    AutoClassify -- "WBS へ（自動）" --> WBSProcess["WBS に分解する"]
    AutoClassify -- "Backlog へ（自動）" --> ToBacklog["Backlog に移す"]
    AutoClassify -- "判断不能" --> AskUser["ユーザーに確認\n（WBS / Backlog / 削除）"]
    AskUser --> UserDecision{ユーザーの回答}
    UserDecision -- "WBS へ" --> WBSProcess
    UserDecision -- "Backlog へ" --> ToBacklog
    UserDecision -- "削除" --> E
    WBSProcess --> E
    ToBacklog --> E
```

| 判断 | 条件 |
| --- | --- |
| WBS へ（自動） | スコープが読み取れ、期日を推測できる |
| Backlog へ（自動） | 「いつかやる」「そのうち」など明示的に先送りの意図がある |
| ユーザーに確認 | スコープまたは期日が不明で推測もできない |

## WBS への分解

WBS に追加するアイテムの詳細処理。

```mermaid
flowchart TD
    S([アイテム])
    E([完了])

    S --> Parse["メモを解析"]
    Parse --> CreateST["サマリータスクを作成\nWBS コード採番"]
    CreateST --> Atomic{1ステップで\n完了できるか?}
    Atomic -- Yes --> OneLeaf["リーフタスクを追加\nWBS: 親.1"]
    Atomic -- No --> MultiLeaf["リーフタスクに分解\ndepends_on を設定"]
    OneLeaf --> Fill["due・tags・estimate を補完"]
    MultiLeaf --> Fill
    Fill --> E
```

メモの解析では、ゴール・範囲・成果物を読み取る。`due`・`tags`・`estimate` が不明な場合は推測し、不確かなときはコメントを付記する。

WBS の構造定義は [explanation/wbs.md](wbs.md) を参照。
AIの操作ルール全体は [reference/ai-behavior.md](../reference/ai-behavior.md) を参照。

---

← [ドキュメント一覧](../index.md)
