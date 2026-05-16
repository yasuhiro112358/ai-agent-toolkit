# ドキュメント

prompt-distiller の利用者向けドキュメント。[Diataxis](https://diataxis.fr/) の4象限で構成されている。

## チュートリアル — まず動かす

| ドキュメント | 内容 |
| ---------- | ---- |
| [会話からプロンプトを蒸留する](tutorials/extract-prompt.md) | ステップ1（要件定義書の生成）〜ステップ2（汎用プロンプトの生成）までの全体ウォークスルー |

## ハウツー — 特定の作業をこなす

| ドキュメント | 内容 |
| ---------- | ---- |
| [要件定義書の最終確認](how-to/verify-requirements.md) | ステップ2に進む前のレビューチェックリスト |
| [ゴール記述を修正する](how-to/fix-goal-statement.md) | ゴールが「何をしたか」に留まっている場合の修正 |
| [アクター記述を修正する](how-to/fix-actor-description.md) | アクターが抽象的な場合の修正 |
| [変数化を修正する](how-to/fix-variable-extraction.md) | 変数化が不十分な場合の修正 |
| [暗黙の制約条件を補足する](how-to/fix-missing-constraints.md) | 制約条件から暗黙のルールが抜けている場合の修正 |

## リファレンス — 正確な仕様を調べる

| ドキュメント | 内容 |
| ---------- | ---- |
| [requirements-extract.md 仕様](reference/requirements-extract.md) | ステップ1プロンプトの入出力・挙動・セクション仕様 |
| [prompts-generate.md 仕様](reference/prompts-generate.md) | ステップ2プロンプトの入出力・挙動・セクション仕様 |

## 解説 — なぜこうなっているかを理解する

| ドキュメント | 内容 |
| ---------- | ---- |
| [全体フロー](explanation/architecture.md) | 2ステップ構成の全体像（シーケンス図） |
| [なぜ同一セッションで実行するか](explanation/why-same-session.md) | 同一セッション実行を標準とした理由 |
| [なぜ2ステップ構成か](explanation/why-two-steps.md) | 直接生成を採用しなかった理由 |
| [なぜ要件定義書を中間層に置くか](explanation/why-requirements-middle-layer.md) | 「何をするか」と「なぜするか」を分離する設計 |
| [なぜ自己チェック＋修正を要件に含めるか](explanation/why-self-check.md) | 確認だけでなく修正まで AI に行わせる理由 |
| [なぜ特定のAIサービスに依存しないか](explanation/why-ai-agnostic.md) | 移植性を確保するための制約 |

---

[← README に戻る](../README.md)
