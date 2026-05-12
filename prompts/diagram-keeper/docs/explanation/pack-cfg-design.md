[diagram-keeper/](../index.md) > explanation

# Explanation: なぜ設定ファイル方式（pack.cfg）を採用したか

当初はシェルスクリプト（`bundle.sh` / `bundle.cmd`）の中に設定値を埋め込む方式を検討した。しかし以下の問題があった：

- bash 版と Windows 版の2ファイルに同じ設定を重複して書く必要がある
- 設定変更のたびに2ファイルを修正しなければならない

Python が PATH に入っていれば `python scripts/pack.py` をどの OS からでも直接呼べるため、ラッパースクリプト自体が不要と判断した。設定は `pack.cfg`（INI 形式）に分離し、`pack.py` が自動的に読み込む設計とした。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
