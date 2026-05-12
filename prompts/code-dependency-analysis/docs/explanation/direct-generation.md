[code-dependency-analysis/](../index.md) > explanation

# Explanation: なぜ直接生成方式か

コード → Mermaid 図の直接生成を採用し、「コード → metadata.json（中間層）→ Mermaid 図」の 2 フェーズ構成を採用しなかった理由。

---

## 直接生成の利点

- **真実の源が 1 つ**: マスタ Mermaid ファイル = 唯一の正。中間 JSON と図の間で乖離が生じない
- **コンテキスト効率**: 大規模コードで中間 JSON が肥大化すると対話 UI のコンテキスト制限に引っかかる。直接生成なら入出力は常に 1 コンテキスト分に収まる
- **更新サイクルが短い**: コード → 図の変換が 1 往復で完結する

## 直接生成の制約

- **AI の抽出精度に依存**: 静的解析ツールのような完全性は保証できない
- **チャンク跨ぎの補完**: チャンクを跨ぐ呼び出し関係は途中のチャンクでスタブとして保持し、後続チャンクで補完される

---

## 関連

← [code-dependency-analysis/ に戻る](../index.md)

- ツールの背景と全体設計 → [architecture-overview.md](architecture-overview.md)
- なぜ 2 枚構成か → [two-diagram-design.md](two-diagram-design.md)
