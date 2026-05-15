# task-streamliner

自然言語でタスクを管理するプロンプト駆動システム。
`templates/tasks.md` 1ファイルをチャットUIに貼り付けるだけで動く。APIキー・サーバー・カスタムアプリ不要。

[English version](README.md)

## 使い方

1. `templates/tasks.md` をテキストエディタで開く
2. 全文をコピーしてチャットUI（Claude.ai / ChatGPT 等）に貼り付ける
3. 送信する — AIが Inbox 処理と CPM スケジューリングを自動実行する
4. 自然言語で指示を出す
5. 「出力して」と入力して返ってきた全文を `templates/tasks.md` に上書き保存する

## 動作環境

- Claude.ai / ChatGPT 等の対話型チャットUI（アカウントのみ必要）
- テキストエディタ

## ドキュメント

→ [docs/index.md](docs/index.md)

## ファイル構成

| パス | 役割 |
| --- | --- |
| `templates/tasks.md` | タスクデータ兼AIへの振る舞い定義（単一情報源） |
| `prompts/tasks-operate.md` | 振る舞い定義の単体ファイル（復旧用） |
| `docs/` | ドキュメント（Diataxis 構成） |
