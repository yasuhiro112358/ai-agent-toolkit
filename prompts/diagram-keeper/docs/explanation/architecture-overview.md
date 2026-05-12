[diagram-keeper/](../index.md) > explanation

# Explanation: ツールの背景と全体設計

このツールを作った動機・制約条件・全体アーキテクチャ。各設計判断の出発点となる文脈。

---

## 背景と目的

コードベースの依存関係を可視化し、設計レビュー・オンボーディング・アーキテクチャ分析に活用できる資料を作りたかった。職場環境においてインターネット接続・API キー利用・外部アカウント登録に制約があるため、対話型生成 AI（UI のみ）とローカルツールで完結する構成を前提として設計した。

## 全体アーキテクチャ

```mermaid
sequenceDiagram
    actor 管理者
    participant Script as bundle.py
    participant AI as 対話型 AI
    participant Repo as diagrams/

    管理者->>Script: python bundle.py --root ./src
    Script-->>管理者: bundle.txt（MANIFEST形式）
    管理者->>AI: diagrams-upsert.md + 既存マスタ + bundle.txt
    AI-->>管理者: class-diagram.md + call-graph.md
    管理者->>Repo: 保存（Git管理）

    actor 開発者
    開発者->>Repo: マスタ2枚を読み込み
    Repo-->>開発者: class-diagram.md + call-graph.md
    開発者->>AI: diagrams-convert-to-sequence.md + マスタ2枚 + シナリオ指示
    AI-->>開発者: sequenceDiagram ブロック
```

2 つのロール:

- **管理者**: `bundle.py` でコードをバンドルし、AI でマスタを更新する
- **開発者（利用者）**: マスタを読み、AI でシーケンス図をオンデマンド派生させる

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- なぜ直接生成方式か → [direct-generation.md](direct-generation.md)
- なぜ 2 枚構成か → [two-diagram-design.md](two-diagram-design.md)
- シーケンス図をマスタに含めない理由 → [sequence-as-derived.md](sequence-as-derived.md)
- なぜ一括投入型か → [batch-input.md](batch-input.md)
- なぜ Mermaid か → [mermaid-choice.md](mermaid-choice.md)
