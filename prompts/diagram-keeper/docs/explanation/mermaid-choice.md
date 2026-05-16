# Explanation: なぜ Mermaid か

[diagram-keeper/](../index.md) > explanation


図の記法として Mermaid を採用した根拠。

---

## 選定結果

| ツール | 判定 | 理由 |
| --- | --- | --- |
| **Mermaid** | **採用** | ブラウザのみで動作。GitHub / Obsidian / Markdown ネイティブ対応。LLM 生成の成功率が高い |
| PlantUML | 不採用 | ローカルに Java + Graphviz のインストールが必要 |
| Graphviz / DOT | 不採用 | VS Code 公式エクステンションのサポートが弱い |

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- ツールの背景と全体設計 → [architecture-overview.md](architecture-overview.md)
- 制約条件・対象外 → [../reference/constraints.md](../reference/constraints.md)
