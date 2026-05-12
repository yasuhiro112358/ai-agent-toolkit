[diagram-keeper/](../index.md) > how-to

# How-to: チャンク分割して更新する

コードが大きく1回の貼り付けに収まらない場合、`--max-chars` でチャンク分割してから繰り返し投入する。

---

## 概要フロー

```mermaid
sequenceDiagram
    actor 管理者
    participant AI as 生成 AI
    participant Repo as diagrams/

    管理者->>管理者: bundle.py --max-chars でチャンクを生成
    loop チャンクがある間
        管理者->>AI: diagrams-upsert.md + 前ステップのマスタ + bundle-00N.txt を貼り付け
        AI-->>管理者: class-diagram.md + call-graph.md を返す
        管理者->>Repo: 上書き保存
    end
    管理者->>管理者: VS Code でプレビュー確認・Git コミット
```

---

## 手順

```bash
python scripts/bundle.py --root ./src --out bundle.txt --max-chars 50000
# → bundle-001.txt, bundle-002.txt, ... が生成される
```

投入手順:

```text
1. bundle-001.txt を Upsert → class-diagram.md, call-graph.md を保存
2. 前ステップの出力をマスタとして bundle-002.txt を Upsert → 上書き保存
3. 全チャンクが終わるまで繰り返す
4. VS Code でプレビュー確認 → Git コミット
```

各チャンクで AI に貼り付けるもの:

| 項目 | 初回 | 2回目以降 |
| --- | --- | --- |
| プロンプト | `prompts/diagrams-upsert.md` の全文 | `prompts/diagrams-upsert.md` の全文 |
| マスタ2枚 | 既存の `diagrams/` 内のファイル | **前ステップの AI 出力** |
| バンドル | `bundle-001.txt` | `bundle-00N.txt` |

> チャンクごとに「既存マスタ = 前ステップの出力」を使うこと。初回投入のマスタを使い回すとエントリが失われる。

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- 通常の更新手順（1回で収まる場合） → [update-diagrams.md](update-diagrams.md)
- bundle.py の全オプション → [../reference/bundle-py.md](../reference/bundle-py.md)
