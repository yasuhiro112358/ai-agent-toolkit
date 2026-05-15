# AI Instructions の復旧

`tasks.md` の末尾にある `## AI Instructions` セクションが破損・消失し、AIが正しく動作しなくなった場合の対処手順。

## 方法 A: テキストエディタで直接修復（推奨）

```mermaid
flowchart TD
    S([開始])
    E([終了])

    S --> Open["prompts/tasks-operate.md を開く"]
    Open --> Copy["--- より下の AI Instructions\n全体をコピーする"]
    Copy --> Edit["tasks.md を開き\n## AI Instructions 以降を選択する"]
    Edit --> Paste["コピーした内容で上書きする"]
    Paste --> Save["tasks.md を保存する"]
    Save --> E
```

`prompts/tasks-operate.md` は `templates/tasks.md` の AI Instructions と同一内容を保持している復旧用ファイル。

## 方法 B: AI セッション経由で修復

```mermaid
flowchart TD
    S([開始])
    E([終了])

    S --> Open["prompts/tasks-operate.md を開く"]
    Open --> Paste["チャットUIに以下の順で貼り付けて送信する\n① tasks-operate.md の全文\n② tasks.md の全文"]
    Paste --> Session["通常どおりセッションを進める"]
    Session --> Output["「出力して」と入力する"]
    Output --> Save["出力された全文を tasks.md に上書き保存する"]
    Save --> E
```

AI Instructions を含む完全な `tasks.md` が再構成される。Inbox の処理も同時に行いたい場合に適している。

---

← [ドキュメント一覧](../index.md)
