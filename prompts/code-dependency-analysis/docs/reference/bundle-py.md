[code-dependency-analysis/](../index.md) > reference

# Reference: bundle.py

指定ディレクトリのソースファイルを MANIFEST 形式に変換する Python スクリプト（Python 3.8 以上、標準ライブラリのみ）。

---

## 基本構文

```bash
python scripts/bundle.py --root <dir> [options]
```

## オプション

| オプション | 必須 | 既定値 | 説明 |
| --- | --- | --- | --- |
| `--root <dir>` | 必須 | — | 解析対象ルートディレクトリ |
| `--out <file>` | 任意 | `bundle.txt` | 出力ファイルパス |
| `--include <glob>` | 任意 | — | 含めるパターン（相対パス、複数可） |
| `--exclude <glob>` | 任意 | — | 除外するパターン（相対パス、複数可） |
| `--max-chars <n>` | 任意 | 制限なし | 1チャンクの上限文字数。超えたら自動分割 |
| `--ext <.ext>` | 任意 | 下表参照 | 対象拡張子を上書き（複数可） |

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

## 使用例

```bash
# 最小構成
python scripts/bundle.py --root /path/to/src

# 出力ファイルを指定
python scripts/bundle.py --root /path/to/src --out bundle.txt

# チャンク分割（50,000 字ずつ）
python scripts/bundle.py --root /path/to/src --max-chars 50000

# ディレクトリを絞り込む
python scripts/bundle.py --root /path/to/src \
  --include 'src/auth/*' --include 'src/core/*' \
  --exclude '*/test/*' --exclude '*/generated/*'

# 拡張子を限定
python scripts/bundle.py --root /path/to/src --ext .cpp --ext .h
```

## 出力フォーマット（MANIFEST 形式）

```text
=== MANIFEST ===
File: src/auth/AuthManager.cpp
Classes: AuthManager, TokenService

File: src/auth/IAuthProvider.h
Classes: IAuthProvider

=== FILE: src/auth/AuthManager.cpp ===
（ファイルの全内容）

=== FILE: src/auth/IAuthProvider.h ===
（ファイルの全内容）
```

## チャンク分割時の出力

`--max-chars` を指定して上限を超えた場合、自動的に連番ファイルに分割される。

```text
bundle-001.txt
bundle-002.txt
bundle-003.txt
```

各ファイルを順番に Upsert する。手順は [../how-to/update-diagrams.md](../how-to/update-diagrams.md) 参照。

## チャンクサイズの決め方

| 弊害 | 対処 |
| --- | --- |
| AI がクラスやエッジを取りこぼす / 応答が途切れる | `--max-chars` を小さくする（現在値の 7〜8 割） |
| 往復回数が増えて Upsert の集約ミスが起きやすい | `--max-chars` を大きくする |

初期の目安: `--max-chars 50000`（概ね 10〜30 ファイル相当）から試す。

## 入力サイズ制約への対応

このツールは「コードチャンク + プロンプト + 既存マスタ2枚」を 1 コンテキストに収める設計になっている。

- 中間 JSON を持たないため、入出力は常に 1 コンテキスト分に収まる
- 複数チャンクにまたがる場合は「1 チャンク Upsert → 次チャンクで再 Upsert」を繰り返す。バンドル外エントリは保持されるため安全
- マスタ2枚はファイルが独立しており、累積してもコンテキストを圧迫しない

---

## 関連

← [code-dependency-analysis/ に戻る](../index.md)

- チャンク Upsert の手順 → [../how-to/update-diagrams.md](../how-to/update-diagrams.md)
- 対応言語・制約条件の詳細 → [constraints.md](constraints.md)
