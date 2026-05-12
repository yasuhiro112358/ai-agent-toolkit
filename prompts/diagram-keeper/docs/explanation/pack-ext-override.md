[diagram-keeper/](../index.md) > explanation

# Explanation: なぜ ext は追加ではなく置き換えか

`ext` に拡張子を指定すると、組み込みのデフォルト（C/C++・Java・C#・Python・TypeScript 等 9 言語）は**完全に置き換わる**。追加ではない。

デフォルトの 9 言語は意図した組み合わせとして設計されており、「一部だけ追加したい」という操作は「なぜその言語だけ対象にするのか」という疑問を招きやすい。対象言語を絞りたい場合は使用するものを全て明示することを要求し、意図の誤りを防ぐ設計とした。

---

## 関連

← [pack.py / pack.cfg の設計判断に戻る](pack-design.md)

- pack.py / pack.cfg のリファレンス → [../reference/pack.md](../reference/pack.md)
