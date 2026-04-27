[ドキュメント](../README.md) > [ハウツー](README.md) > エントリを削除する

> **Diataxis: How-to** — コードを削除したとき、マスタから対応エントリを除去する。

# ハウツー: エントリを削除する（Delete）

ソースコードからファイルやクラスを削除したとき、マスタ 2 枚（クラス図・コールグラフ）から対応エントリを除去する手順。

## 手順

```
1. AI に以下を 1 メッセージで貼り付ける
   - diagrams-delete.md の全文
   - 既存の class-diagram.md の全文
   - 既存の call-graph.md の全文
   - 削除指示（自然言語）

2. 応答から class-diagram.md / call-graph.md を diagrams/ に上書き保存

3. VS Code でプレビュー確認 → Git コミット
```

## 削除指示の書き方

削除指示は自然言語で書く。粒度は問わない。

| 粒度 | 指示の例 |
|------|---------|
| ファイル単位 | 「`src/auth/OldAuthManager.cpp` を削除」 |
| クラス単位 | 「クラス `LegacyUser` を削除」 |
| メソッド単位 | 「`AuthManager.oldLogin` を削除」 |
| パッケージ単位 | 「`src/legacy/` 配下を一括削除」 |
| 複数指定 | 「クラス `LegacyUser` と `DeprecatedToken` を削除」 |

## 注意

- Upsert（`diagrams-upsert.md`）はエントリの「更新」であり、削除は行わない。コード削除後にそのまま Upsert しても古いエントリがマスタに残る。削除は必ず Delete プロンプトで行うこと。
- 削除指示が曖昧な場合、AI は「どれを削除対象と解釈したか」を冒頭で宣言してから処理する。意図と異なればメッセージで修正指示を出すこと。

## 関連

- [図を更新する（Upsert）](update-diagrams.md)
- [プロンプトファイル仕様](../reference/prompts.md)（Delete の詳細な挙動はこちら）

---

[← ハウツー一覧](README.md) | [ドキュメント一覧](../README.md)
