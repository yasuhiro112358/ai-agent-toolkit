# チュートリアル: 初めてのセッション

`templates/tasks.md` を使って最初のタスク管理セッションを体験する手順。

## 前提

- Claude.ai / ChatGPT 等のチャットUIのアカウント
- テキストエディタ

## セッションのフロー

```mermaid
flowchart TD
    S([開始])
    E([終了])

    S --> Copy["templates/tasks.md を開いて\n全文をコピーする"]
    Copy --> Paste["チャットUIに貼り付けて送信する"]
    Paste --> Auto["AIが自動処理を実行する\n変更サマリーが返ってくる"]
    Auto --> Review["変更サマリーを確認する"]
    Review --> Instruction{指示がある?}
    Instruction -- Yes --> Give["自然言語で指示を出す\n例: 「資料作成を始めた」"]
    Give --> Response["AIが変更サマリーを返す"]
    Response --> Review
    Instruction -- No --> Finish{作業終了?}
    Finish -- No --> Review
    Finish -- Yes --> Output["「出力して」と入力する"]
    Output --> Save["返ってきた全文を\ntemplates/tasks.md に上書き保存する"]
    Save --> E
```

AIの自動処理の詳細は [explanation/inbox-processing.md](../explanation/inbox-processing.md) を参照。

## 次のステップ

- セッションの外で思いついたことは `templates/tasks.md` の `## Inbox` にメモを書いておくだけでよい。次回セッション開始時にAIが自動処理する
- タスクが増えてきたら [アーカイブ](../how-to/archive.md) を参照

---

← [ドキュメント一覧](../index.md)
