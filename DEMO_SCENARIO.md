# 🎬 Agentic GitHub Copilot — Demo Scenario

> **スライドごとのライブデモシナリオ**
> 各スライド（3〜8）に対応するデモを実施し、6層アーキテクチャを体験的に示す

---

## 📋 全体構成

| スライド | テーマ | デモ内容 | 所要時間 |
|---------|--------|---------|---------|
| 3 | [入口（Entry）](#-スライド-3入口entry) | Chat でコード理解 → Issue 作成 → Copilot アサイン | ~3 min |
| 4 | 実行（Execution） | TBD | TBD |
| 5 | 協働（Collaboration） | TBD | TBD |
| 6 | レビュー（Review） | TBD | TBD |
| 7 | 文脈（Context） | TBD | TBD |
| 8 | 統制（Governance） | TBD | TBD |

### デモアプリケーション

Python FastAPI で構築した **Todo API**（CRUD 操作）をデモ対象とする。

```
demo-ghec/
├── app/
│   ├── main.py          # FastAPI ルートハンドラ（5 エンドポイント）
│   ├── models.py         # Pydantic モデル（TodoCreate / TodoUpdate / Todo）
│   └── database.py       # インメモリストレージ（dict ベース）
├── requirements.txt      # fastapi, uvicorn, pydantic
└── README.md
```

**意図的なギャップ（Copilot が埋める対象）:**
- ❌ ユニットテストなし
- ❌ Dockerfile なし
- ❌ 入力バリデーションなし
- ❌ CI/CD ワークフローなし

---

## 💬 スライド 3：入口（Entry）

> **メッセージ:** Chat がコードベース理解の入口となり、そこから Issue 作成・Agent 起動まで一気通貫でつながる

### 全体の流れ

```
Chat でコード理解 → 改善点の発見 → Issue として作成 → Copilot をアサイン
       ↓                  ↓                ↓                  ↓
  「説明して」       「テストがない」    Issue が作られる    スライド 4 へ
```

---

### ステップ 1：Chat でコードベースを理解する

1. GitHub.com でリポジトリ（`shinyay/demo-ghec`）を開く
2. 右上の **Copilot Chat アイコン** をクリック
3. 質問する：

   > **「このプロジェクトは何をするものですか？アーキテクチャとファイル間の関係を説明してください」**

4. **期待結果:**
   - Copilot がリポジトリ全体を読み込む
   - FastAPI ベースの Todo API であること
   - `main.py`（ルート） → `models.py`（スキーマ） → `database.py`（ストレージ）の3層構造
   - 5つの CRUD エンドポイントの一覧

🗣️ **トーク:**
*「Chat は最もカジュアルな入口です。リポジトリを開いて質問するだけで、全ファイルを理解した回答が得られます。新しいチームメンバーのオンボーディングにも使えます」*

---

### ステップ 2：改善点を聞く

1. 続けて Chat で質問する：

   > **「このプロジェクトの改善すべき点は何ですか？」**

2. **期待結果:**
   Copilot が複数の改善点を指摘する。例：
   - ⚠️ ユニットテストがない
   - ⚠️ 入力バリデーションがない
   - ⚠️ Dockerfile がない
   - ⚠️ CI/CD パイプラインがない
   - ⚠️ ログ出力がない

🗣️ **トーク:**
*「Copilot はコードの中身だけでなく、プロジェクトに足りないものも指摘できます。コードレビューの前段階として、プロジェクト全体の健全性チェックにも使えます」*

---

### ステップ 3：Chat から Issue を作成する

1. Copilot の改善提案を受けて、Chat で依頼する：

   > **「ユニットテストがないという改善点について、GitHub Issue を作成してください。pytest と httpx を使って、全エンドポイントのテストを追加する内容にしてください」**

2. **期待結果:**
   - Copilot が Issue のタイトルと本文を生成する
   - 「Create Issue」ボタン（またはリンク）が表示される
   - クリックすると Issue 作成画面にプリフィルされる

3. Issue を確認して **Submit** する

🗣️ **トーク:**
*「Chat で理解 → 改善点の発見 → Issue 化。この流れが一つの画面で完結します。コンテキストスイッチなしで、思考からアクションに直結できます」*

---

### ステップ 4：Issue に Copilot をアサインする

1. 作成された Issue ページで **Assignees** をクリック
2. **Copilot** を選択してアサインする
3. Copilot が作業を開始する：
   - 「Copilot is working...」の表示を確認

🗣️ **トーク:**
*「Issue に Copilot をアサインするだけで、Agent が自律的にコードを書き始めます。ここから先はスライド 4『実行』で詳しく見ていきます」*

> ⏳ **Agent の実行には 1〜3 分かかる。この間にスライドの説明に戻り、スライド 4 の説明を開始する。**

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **フルリポジトリコンテキスト** | Chat は1ファイルではなく、リポジトリ全体を理解している |
| **Chat → Issue のシームレスな接続** | 思考からアクションへのコンテキストスイッチがゼロ |
| **構造化された Issue 生成** | Copilot がプロジェクトを理解した上で要件を記述する |
| **Agent 起動への自然な流れ** | Issue 作成 → アサイン → 自律実行が一直線 |

---

### バックアップ（Chat → Issue がうまくいかない場合）

手動で Issue を作成する：

**Title:**
```
Add unit tests for the Todo API endpoints
```

**Body:**
```markdown
We need unit tests for all CRUD endpoints in the Todo API.

## Requirements
- Use `pytest` and `httpx` for testing
- Test all endpoints: GET /todos, GET /todos/{id}, POST /todos, PUT /todos/{id}, DELETE /todos/{id}
- Test both success and error cases (e.g., 404 for missing todo)
- Add a `tests/` directory with proper structure
- Include a `conftest.py` with shared test fixtures
```
