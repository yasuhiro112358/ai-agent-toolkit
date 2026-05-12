[diagram-keeper/](../index.md) > reference

# Reference: pack.py / pack.cfg

ソースファイルを1つのテキストにまとめる Python スクリプト（Python 3.8 以上、標準ライブラリのみ）。

---

## 基本的な使い方

プロジェクトルートに `pack.cfg` を置いて設定を書き、引数なしで実行する。

```bash
python scripts/pack.py
```

---

## pack.cfg（設定ファイル）

`[pack]` セクションに設定値を書く。コメント行は `#` で始める。

```ini
[pack]
# スキャン対象ディレクトリ（必須）
src = ./src

# 出力ファイルパス
dest = pack.txt

# チャンク上限文字数（空欄 = 制限なし）
chunk_size = 50000

# ホワイトリスト、スペース区切り
# マッチしたファイルだけをパック。空欄 = src 配下の全ファイルを対象
# exclude と併用した場合、include で絞った結果をさらに exclude で除く
include =

# ブラックリスト、スペース区切り
# マッチしたファイルをスキップ。空欄 = 除外なし
# include と併用した場合、include フィルタの後に適用される
exclude =

# 対象拡張子、スペース区切り
# 組み込みデフォルト（C/C++, Java, C#, Python, TypeScript 等）を置き換える（追加ではない）
# 例: ext = .py .ts  -> .py と .ts のみをスキャン
# 空欄 = 組み込みデフォルトを使用
ext =
```

`pack.cfg` は `python scripts/pack.py` を実行したカレントディレクトリから読まれる（通常はプロジェクトルート）。

---

## コマンドラインオプション

CLI 引数は `pack.cfg` の値を上書きする。

| オプション | 説明 |
| --- | --- |
| `--src <dir>` | スキャン対象ディレクトリ |
| `--dest <file>` | 出力ファイルパス |
| `--include <glob>` | 含めるパターン（複数指定可） |
| `--exclude <glob>` | 除外するパターン（複数指定可） |
| `--chunk-size <n>` | チャンク上限文字数 |
| `--ext <.ext>` | 対象拡張子の上書き（複数指定可） |
| `--config <file>` | pack.cfg 以外の設定ファイルを指定 |

---

## デフォルト対象拡張子

| 言語 | 拡張子 |
| --- | --- |
| C / C++ | `.c` `.cpp` `.cxx` `.cc` `.c++` `.h` `.hpp` `.hxx` `.hh` |
| Java | `.java` |
| C# | `.cs` |
| Visual Basic | `.vb` |
| Python | `.py` |
| TypeScript | `.ts` `.tsx` |
| JavaScript | `.js` `.jsx` |
| PHP | `.php` |
| Rust | `.rs` |

---

## 出力フォーマット

```text
=== INDEX ===
File: src/auth/AuthManager.cpp
Classes: AuthManager, TokenService

File: src/auth/IAuthProvider.h
Classes: IAuthProvider

=== FILE: src/auth/AuthManager.cpp ===
（ファイルの全内容）

=== FILE: src/auth/IAuthProvider.h ===
（ファイルの全内容）
```

---

## チャンク分割

`chunk_size` を指定して上限を超えた場合、自動的に連番ファイルに分割される。

```text
pack-001.txt
pack-002.txt
pack-003.txt
```

各ファイルを順番に Upsert する。手順と調整の目安は [../how-to/update-with-chunks.md](../how-to/update-with-chunks.md) 参照。

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- チャンク Upsert の手順 → [../how-to/update-with-chunks.md](../how-to/update-with-chunks.md)
- 対応言語・制約条件の詳細 → [constraints.md](constraints.md)
