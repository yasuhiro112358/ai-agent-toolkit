# 解説: 全体フロー

[ドキュメント](../index.md) > 全体フロー

> **Diataxis: Explanation** — prompt-distiller の全体フローと2ステップ構成の概観。


```mermaid
sequenceDiagram
    participant U as 利用者
    participant A as 生成AI

    Note over U,A: ステップ1
    U->>A: requirements-extract.md を同一セッションの末尾に貼り付け
    A->>A: 要件定義書を作成 → 自己チェック → 修正
    A->>U: 要件定義書を出力
    U->>U: 要件定義書をレビュー・修正
    Note over U,A: ステップ2
    U->>A: prompts-generate.md を同一または新規セッションに貼り付け
    A->>A: 汎用プロンプトを作成 → 自己チェック → 修正
    A->>U: 汎用プロンプトを出力
    U->>U: 汎用プロンプトをファイルに保存
```

## 関連する解説

- [なぜ同一セッションで実行するか](why-same-session.md)
- [なぜ直接生成ではなく2ステップ構成か](why-two-steps.md)
- [なぜ要件定義書を中間層に置くか](why-requirements-middle-layer.md)

---

[← ドキュメント一覧](../index.md)
