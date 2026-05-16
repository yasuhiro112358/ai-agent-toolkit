# Explanation: なぜ変数名を src / dest にしたか

[diagram-keeper/](../index.md) > explanation


入出力のペアとして `root`/`out` から `src`/`dest` に変更した。

`src`/`dest` は Gulp をはじめ多くのビルドツールで定着した慣用ペアであり、「ソースから出力先へ」という方向性が直感的に伝わる。`root` は「ファイルツリーの根」か「プロジェクトルート」か曖昧で、`out` は短すぎて `src` との対応が見えにくかった。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
