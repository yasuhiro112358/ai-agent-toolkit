---
title: Legacy (metadata.json 中心 2フェーズ方式)
created: 2026-04-17
status: 退避・参照用
supersedes: 新方式（コード → Mermaid 図への直接変換、図自体をマスタとする）
---

# legacy/ — 旧方式のアーカイブ

本ディレクトリは、本プロジェクトが 2026-04-17 に「コード → metadata.json → Mermaid 図」の 2 フェーズ構成から、「コード → Mermaid 図（直接生成）」の 1 フェーズ構成に方針転換した際、旧方式の設計資産を退避するために作られた。

## 旧方式の概要

- **アーキテクチャ**: 2 フェーズ構成
  - Phase 1: コードチャンク + `metadata.json` → AI → `metadata.json`（Upsert / Delete）
  - Phase 2: `metadata.json` + 図指示 → AI → Mermaid `.md` ファイル群
- **中心データ**: `metadata.json`（クラス・属性・メソッド・呼び出し関係・継承関係・パッケージ所属を網羅した JSON）
- **生成対象**: Tier 1（クラス図・パッケージ図・シーケンス図）＋ Tier 2（状態機械図・コンポーネント図・ER 図）

## 採用を見送った理由

1. **コンテキスト超過**: `metadata.json` のサイズがコードベース規模に比例して増大し、対話 UI 型 AI（API 不使用）のコンテキストウィンドウを超える事例が発生した
2. **運用コスト**: パッケージ単位の JSON 分割で回避する設計だったが、手順が煩雑で利用者体験を損ねた
3. **真実の源の二重化**: コードと `metadata.json` の両方が真実の源候補になり、不整合検出が人手で必要だった

## 現方式（置き換え後）

- マスタ 2 枚（`diagrams/class-diagram.md` と `diagrams/call-graph.md`）をコードから直接生成し、Git 管理の唯一の真実の源とする
- シーケンス図はシナリオ選択が必要なためマスタに含めず、開発時にマスタ 2 枚から AI にオンデマンド派生させる
- 詳細はプロジェクト直下の [`requirements.md`](../requirements.md) を参照

## 再参照が有効になる契機

以下の条件が揃ったときに、本 legacy のロジックを再評価する価値がある。

- 職場環境で CLI ベース / API ベースの AI 利用が解禁された（メタデータ JSON のコンテキスト超過問題が解消する）
- 同一ソースから 6 種類以上の図を大量・繰り返し生成する需要が発生した（JSON 中間層の再利用メリットが勝る）
- Tier 2 図（状態機械図・コンポーネント図・ER 図）を恒常的に生成する必要が出た（予約セクション `components` / `entities` / `states` の設計が活きる）

## 退避ファイル一覧

| ファイル | 元の役割 |
|---------|---------|
| `metadata.json` | 状態ストア。Phase 1 の出力 / Phase 2 の入力（空スキーマで初期化済み） |
| `prompt-phase1-upsert.md` | Phase 1 Upsert (Create + Update)。コードチャンク → metadata.json の蓄積・更新 |
| `prompt-phase1-delete.md` | Phase 1 Delete。metadata.json の削除・連鎖整理 |
| `prompt-phase2.md` | Phase 2 Read。metadata.json + 図指示 → Mermaid 図群（6 種のテンプレート埋め込み） |
| `prompt-legacy.md` | さらに前の単一フェーズ構成プロンプト（後方互換のため旧方式時点でも保持されていた） |

## 注意事項

- 本 legacy のファイルは Git 履歴として残すことが目的であり、日常運用では参照不要
- 新方式の設計判断に迷ったときの参照資料としてのみ有効
