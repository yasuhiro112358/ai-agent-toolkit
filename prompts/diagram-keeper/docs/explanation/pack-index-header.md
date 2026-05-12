[diagram-keeper/](../index.md) > explanation

# Explanation: なぜ出力ヘッダを === INDEX === にしたか

当初 `=== MANIFEST ===` というヘッダを使っていた。`MANIFEST` は Java の JAR や Python パッケージングで使われる用語を借用したものだが、このツール独自のフォーマット名として定着しにくく、一般的な意味からも少しずれていた。

`INDEX` は「目次・索引」として直感的で、「パックの中身のリスト」という役割を正確に表す。AI がフォーマットを解釈する際にヘッダ名に強く依存するわけではないが、ドキュメント・コードを読む人間にとっての明快さを優先した。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
