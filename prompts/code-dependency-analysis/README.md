# 対話型生成AIによるコード依存関係分析ツール

大規模な C++ / Java / C# コードベースの依存関係を、対話型 AI（UI のみ）＋ VS Code ローカルプレビューで可視化するツール。API キー・GitHub・外部アカウント不要。詳細は [requirements.md](requirements.md) 参照。

## アーキテクチャ

**マスタ直接生成 + CRUD プロンプト構成**。コードから 2 枚のマスタ図（クラス図・コールグラフ）を直接生成し、Git 管理の真実の源とする。マスタの保守はバンドルを小分けに投入する Upsert 運用。シーケンス図はマスタに含めず、開発時にマスタ 2 枚から AI にオンデマンド派生させる。

```
マスタ Upsert (C+U):  既存マスタ + コードバンドル + prompt-master-upsert.md
                     → AI → 更新された class-diagram.md + call-graph.md

マスタ Delete  (D):  既存マスタ + 削除指示 + prompt-master-delete.md
                     → AI → エントリを除去した class-diagram.md + call-graph.md

シーケンス派生 (R):  class-diagram.md + call-graph.md + シナリオ指示 + prompt-derive-sequence.md
                     → AI → 一時的な sequenceDiagram
```

v1 の「metadata.json 中心 2 フェーズ方式」は [`legacy/`](./legacy/) に退避済み。経緯は [`requirements.md` §1.1](./requirements.md) 参照。

## ファイル構成

| ファイル | 役割 |
|---------|------|
| `requirements.md` | 要件確認書（SRS-lite、v2） |
| `bundle.py` | ソースツリーを MANIFEST 形式に変換する Python スクリプト |
| `prompt-master-upsert.md` | マスタ 2 枚の Upsert（Create + Update） |
| `prompt-master-delete.md` | マスタ 2 枚の Delete |
| `prompt-derive-sequence.md` | マスタ 2 枚からシーケンス図を派生 |
| `legacy/` | v1 の設計資産退避先 |

各 `prompt-*.md` ファイルは**全文をそのまま AI に貼り付けて使える**プロンプト本文のみを記載している。使い方・指示例は本 README にまとめる。

### 生成される成果物

| パス | 役割 |
|------|------|
| `diagrams/class-diagram.md` | マスタ 1: クラス図（プロジェクト全体、静的構造） |
| `diagrams/call-graph.md` | マスタ 2: コールグラフ（プロジェクト全体、呼び出し関係網） |
| `diagrams/sequences/<name>.md` | 保存したい派生シーケンス図（任意・必要時のみ） |

## 前提環境

- Python 3.8 以上（標準ライブラリのみ使用）
- VS Code + [Mermaid Chart 拡張](https://marketplace.visualstudio.com/items?itemName=MermaidChart.vscode-mermaid-chart)（`MermaidChart.vscode-mermaid-chart`、アカウント登録不要）
- 対話型 AI（Claude.ai / ChatGPT 等の UI）

## 運用フロー

### マスタ Upsert（初回生成・継続更新の共通フロー）

```
1. bundle.py で対象ソースを MANIFEST 形式に変換（必要ならチャンク分割）
2. 対話 AI に以下をまとめて貼り付け:
   - prompt-master-upsert.md の全文
   - 既存マスタ 2 枚の全文（初回は「マスタ未作成」と明記）
   - バンドル（1 チャンク）
3. 応答から class-diagram.md / call-graph.md のコピー用ブロックを取り出し
   diagrams/ 配下に保存（既存ファイルを上書き）
4. 次のチャンクがあれば 2 に戻る（既存マスタは前ステップの出力を使う）
5. 全チャンクを投入し終えたら VS Code でプレビュー確認 → Git コミット
```

**重要**: Upsert はバンドル内のファイル／クラスだけを上書き対象とする。バンドル外のエントリには触れないため、複数回に分けて投入してもマスタが失われない。

### マスタ Delete（不要になったコードの掃除）

コードリポジトリからファイルやクラスを削除したとき、マスタから対応エントリを除く。

```
1. 対話 AI に以下を貼り付け:
   - prompt-master-delete.md の全文
   - 既存マスタ 2 枚の全文
   - 削除指示（自然言語）
2. 応答からコピー用ブロックを取り出し diagrams/ 配下に保存
3. VS Code でプレビュー確認 → Git コミット
```

削除指示の例:
- 「`src/auth/OldAuthManager.cpp` を削除」
- 「クラス `LegacyUser` を削除」
- 「`AuthManager.oldLogin` を削除」
- 「`src/legacy/` 配下を一括削除」

### シーケンス図派生（開発時オンデマンド）

```
1. 対話 AI に以下を貼り付け:
   - prompt-derive-sequence.md の全文
   - マスタ 2 枚（class-diagram.md + call-graph.md）の全文
   - シナリオ指示（自然言語）
2. AI がコピー用コードブロックで sequenceDiagram を返す
3. 一時用途なら保存せず、残したいものだけ diagrams/sequences/<name>.md に保存
```

シナリオ指示の例:
- 「`AuthController.login` から始まる処理の時系列を描いて」
- 「auth パッケージ内部の相互作用だけ」
- 「例外パス（認証失敗）のシナリオ」
- 「起点は `Main.run`、深さは 3 階層まで」

### 分割・統合切替

プロジェクトが大きくなりマスタが 1 枚で扱いにくくなった場合、`prompt-master-upsert.md` のフローでバンドル投入時に粒度指示を添えて再生成する。

- 分割したい: 「パッケージ単位に分割して、`class-<packageName>.md` と `call-graph-<packageName>.md` で返して。あわせて `package-diagram.md` も」
- 統合したい: 「全パッケージを 1 枚に統合して」

マスタはテキスト（Mermaid .md）なので手動編集でのマージ／分割も容易。詳細は [`requirements.md` §5.3](./requirements.md) 参照。

## bundle.py の使い方

```bash
# 最小
python bundle.py --root /path/to/src

# 出力先とチャンク分割
python bundle.py --root /path/to/src --out bundle.txt --max-chars 60000

# include/exclude
python bundle.py --root /path/to/src \
  --include 'src/auth/*' --include 'src/core/*' \
  --exclude '*/test/*' --exclude '*/generated/*'

# 拡張子を限定
python bundle.py --root /path/to/src --ext .cpp --ext .h
```

### 主なオプション

| オプション | 説明 |
|-----------|------|
| `--root` | 解析対象ルートディレクトリ（必須） |
| `--out` | 出力ファイル（既定: `bundle.txt`） |
| `--include` | 含めるグロブパターン（相対パス、複数可） |
| `--exclude` | 除外グロブパターン（相対パス、複数可） |
| `--max-chars` | 1 チャンクの上限文字数。超えたら `bundle-001.txt, bundle-002.txt, ...` に分割 |
| `--ext` | 対象拡張子を上書き（既定は C++/Java/C# 一式） |

### チャンクサイズの決め方

`--max-chars` に絶対的な正解値はない。以下を目安に運用しながら調整する。

- **大きすぎる弊害**: AI がクラスやエッジを取りこぼす / 応答が途切れる
- **小さすぎる弊害**: 往復回数が増え、Upsert の集約ミスが起きやすい
- **推奨の決め方**:
  1. まずは `--max-chars` 指定なし（または十分大きい値）で小さなサブディレクトリを投入
  2. 応答品質が劣化または途切れる閾値を観測
  3. その **7〜8 割** を本番値に設定
- **初期の目安**: 30,000〜60,000 字（概ね 10〜30 ファイル相当）から試すと扱いやすい

## 未確定事項（運用しながら調整）

- Python 実行環境の最終確認（職場 PC で 3.8+ が使えるか）
- `--max-chars` の適切な値
- チャンク分割時の Upsert 累積による品質劣化の有無（応答を何回か行き来させると抽出漏れが起きないか）
