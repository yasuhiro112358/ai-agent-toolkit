# Reference: プロンプトファイル

[diagram-keeper/](../index.md) > reference


`prompts/` ディレクトリに格納された3つのプロンプトファイルはそれぞれ CRUD の1操作に対応する。ファイル全文をそのまま AI に貼り付けて使う自己完結型。

---

## 対比表

| ファイル | 操作 | 入力 | 出力 |
| --- | --- | --- | --- |
| `prompts/diagrams-upsert.md` | Create + Update | 既存マスタ2枚（任意）+ pack.py の出力 | 更新された `class-diagram.md` + `call-graph.md` |
| `prompts/diagrams-delete.md` | Delete | 既存マスタ2枚 + 削除指示（自然言語） | 削除後の `class-diagram.md` + `call-graph.md` |
| `prompts/diagrams-convert-to-sequence.md` | Read / 派生 | マスタ2枚 + シナリオ指示（自然言語） | `sequenceDiagram` を含む `.md` |

---

## diagrams-upsert.md

**用途**: コードの追加・変更をマスタに反映する。初回生成にも使う。

**Upsert の挙動**:

- バンドル内のファイル・クラス → コード現状で全面上書き
- バンドル外のファイル・クラス → 既存マスタをそのまま保持
- バンドルに新規のファイル・クラス → マスタに追加

**初回生成時**: 「マスタ未作成」と宣言する（既存マスタの貼り付け不要）。

---

## diagrams-delete.md

**用途**: コードから削除されたファイル・クラス・メソッドをマスタから除去する。

**Delete の挙動**:

- 指定クラスのノード・属性・メソッド宣言を削除
- 削除クラスに紐づく関係エッジ（継承・実装・合成・集約・依存）を全て削除
- コールグラフでは削除メソッドのノードと入出エッジを全て削除
- 孤立スタブノードを連鎖削除
- 削除対象が片方のマスタにしかない場合でも両マスタを全文で返す
- 応答末尾に「削除済み」サマリーを付与

**注意**: Upsert では削除が行われない。コード削除後は必ず Delete プロンプトを使うこと。

---

## diagrams-convert-to-sequence.md

**用途**: 特定シナリオのシーケンス図を開発時オンデマンドで生成する。

**派生の挙動**:

- コールグラフのエッジに沿って呼び出しチェーンを時系列化
- クラス図から参加者（ライフライン）のクラス情報を補強
- コールグラフに存在しないメソッド呼び出しは創作しない
- マスタ自体は変更しない

---

## 共通: 出力フォーマット

すべてのプロンプトは以下の形式でファイル内容を返す。

````text
### file: diagrams/class-diagram.md
```markdown
---
（フロントマター）
---

（Mermaid ブロック）
```
````

- 外側コードブロックは `markdown` タグ付き
- 差分ではなく**全文**を返す
- ファイル名は見出しで明示

---

## 関連

← [diagram-keeper/ に戻る](../index.md)

- クラス図・コールグラフの仕様 → [diagram-spec.md](diagram-spec.md)
- Upsert 手順 → [../how-to/update-diagrams.md](../how-to/update-diagrams.md)
- Delete 手順 → [../how-to/delete-entries.md](../how-to/delete-entries.md)
- シーケンス派生手順 → [../how-to/derive-sequence.md](../how-to/derive-sequence.md)
