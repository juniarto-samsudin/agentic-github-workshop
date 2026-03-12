# 🎬 Agentic GitHub Copilot — Demo Scenario

> **スライドごとのライブデモシナリオ**
> 各スライド（3〜12）に対応するデモを実施し、6層アーキテクチャを体験的に示す
> Act 1（Cloud-Side: Slides 3-8）＋ Act 2（Client-Side & Hybrid: Slides 9-12）

---

## 📋 全体構成

### Act 1 — ☁️ Cloud-Side：Agent があなたの代わりに非同期で自律実行する

| スライド | テーマ | デモ内容 | 所要時間 |
|---------|--------|---------|---------|
| 3 | [入口（Entry）](#-スライド-3入口entry) | Chat でコード理解 → Issue 作成 → Copilot アサイン | ~3 min |
| 4 | [実行（Execution）](#-スライド-4実行execution) | Actions 上の実行過程 → セッションログ → 完成 PR 確認 | ~4 min |
| 5 | [協働（Collaboration）](#-スライド-5協働collaboration) | PR 上で @copilot にエッジケース追加を依頼 → 反復 | ~3 min |
| 6 | [レビュー（Review）](#-スライド-6レビューreview) | 自動レビュー確認 → コメント＆提案 → 修正ループ | ~3 min |
| 7 | [文脈（Context）](#-スライド-7文脈context) | Custom Instructions → Chat 効果確認 → Agent 選択 → Spaces | ~3 min |
| 8 | [統制（Governance）](#-スライド-8統制governance) | Mission Control でタスク管理 → リアルタイムステアリング | ~3 min |

### Act 2 — 💻 Client-Side & Hybrid：Agent があなたと一緒にリアルタイムで協働する

| スライド | テーマ | デモ内容 | 所要時間 |
|---------|--------|---------|---------|
| 9 | [VS Code Agent Mode](#-スライド-9vs-code-agent-mode--インタラクティブ実行) | Agent Mode で入力バリデーション追加 → リアルタイム協働 → ローカルテスト | ~5 min |
| 10 | [Copilot CLI](#-スライド-10copilot-cli--ターミナルファースト開発) | CLI で Dockerfile 生成 → ビルド＆テスト → コミット（全てターミナル完結） | ~4 min |
| 11 | [Hybrid ワークフロー](#-スライド-11ハイブリッド--クラウドクライアント連携) | CLI 分析 → Issue → Cloud Agent → VS Code 引き継ぎ → Cloud Review | ~5 min |
| 12 | [コンテキスト一貫性](#-スライド-12コンテキスト一貫性--どこでも同じルール) | 同じリクエストを 3 サーフェスで実行 → Custom Instructions の一貫適用を証明 | ~3 min |

### 意図的なギャップ × サーフェス マッピング

| Gap | Cloud Demo（Act 1） | Client Demo（Act 2） |
|-----|---------------------|---------------------|
| ❌ ユニットテストなし | ✅ Slide 3/4: Issue → Agent → PR | — |
| ❌ 入力バリデーションなし | — | ✅ Slide 9: VS Code Agent Mode |
| ❌ Dockerfile なし | — | ✅ Slide 10: Copilot CLI |
| ❌ CI/CD ワークフローなし | — | ✅ Slide 11: Hybrid ワークフロー |

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

---

## ⚙️ スライド 4：実行（Execution）

> **メッセージ:** Coding Agent は GitHub Actions 上で非同期に自律実行し、その過程はすべて観察可能

### 全体の流れ

```
Issue アサイン済み → Actions で実行過程を観察 → セッションログ確認 → 完成 PR を確認
       ↓                    ↓                         ↓                    ↓
  スライド 3 から      Agent の動きを見る        思考過程を追う       成果物レビュー
```

---

### ステップ 1：Actions タブで実行過程を観察する

> ⏳ スライド 3 で Issue に Copilot をアサイン済み。Agent が裏で動いている。

1. リポジトリの **Actions タブ** を開く
2. Copilot Coding Agent のワークフロー実行を確認：
   - ワークフロー名とステータス（🟡 In progress / ✅ Completed）
   - 実行時間

3. ワークフロー実行をクリックしてログを展開：
   - 📖 コードベースの分析（どのファイルを読んだか）
   - 🌿 ブランチの作成
   - ✍️ ファイルの作成・編集
   - ✅ 自動テスト実行（もしあれば）

🗣️ **トーク:**
*「Coding Agent は GitHub Actions のランナー上で動きます。新しいインフラは不要で、既存の Actions 環境をそのまま活用します。組織の Actions ポリシーもそのまま適用されます」*

---

### ステップ 2：セッションログで思考過程を確認する

1. Agent の実行詳細ページを開く
2. **セッションログ** を確認する：
   - Copilot がどのファイルを読み込んだか
   - コードベースをどう解釈したか
   - どのような計画を立てたか
   - どのファイルを作成・編集したか

3. 具体例をハイライト：
   - 「`app/main.py` を読んで、5つのエンドポイントを認識した」
   - 「`app/models.py` から Pydantic モデルの構造を理解した」
   - 「`tests/` ディレクトリを作成し、`conftest.py` と `test_main.py` を生成した」

🗣️ **トーク:**
*「ブラックボックスではありません。Agent が何を読み、何を考え、何を作ったか——すべてセッションログで追跡できます。これが『観察可能性』です」*

---

### ステップ 3：完成した PR を確認する

1. Agent が作成した **Pull Request** を開く
2. 確認ポイント：

   **PR 説明文：**
   - ✅ 自動生成された説明文
   - ✅ Issue への参照リンク（`Closes #XX`）
   - ✅ 変更内容のサマリー

   **作成されたファイル：**
   - ✅ `tests/` ディレクトリ
   - ✅ `tests/conftest.py` — 共通フィクスチャ（TestClient の設定等）
   - ✅ `tests/test_main.py` — 全エンドポイントのテスト

   **テストコードの品質：**
   - ✅ 成功ケース（正常なCRUD操作）
   - ✅ エラーケース（存在しない ID で 404）
   - ✅ 正しいインポート（`app.main` と `app.database` を参照）
   - ✅ 適切なアサーション（ステータスコード、レスポンスボディ）

🗣️ **トーク:**
*「結果は普通の PR です。特別なフォーマットや独自のUIではなく、既存のPRレビューワークフローにそのまま乗ります。これがポイントです——新しいプロセスを覚える必要はありません」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **GitHub Actions 上で実行** | 既存インフラ活用、追加セットアップ不要 |
| **非同期実行** | Agent が動く間、開発者は他の作業ができる |
| **観察可能性** | セッションログで Agent の思考過程を追跡可能 |
| **結果は普通の PR** | 既存のレビューワークフローにシームレスに統合 |
| **Issue との自動リンク** | PR が Issue を自動的に参照、トレーサビリティ確保 |

---

### バックアップ（Agent の実行が遅い場合）

- スライドの内容説明や Q&A で時間を埋める
- 事前に別の Issue でテスト実行しておき、完成済みの PR を見せる準備をしておく
- 「実際の環境では 1〜3 分で完了します」と補足する

---

## 🤝 スライド 5：協働（Collaboration）

> **メッセージ:** PR を媒介に人と Copilot が対話し、反復的にコードを改善する

### 全体の流れ

```
PR を開いている状態 → @copilot にフィードバック → Copilot が追加コミット → 反復を確認
       ↓                       ↓                         ↓                    ↓
  スライド 4 から        エッジケース依頼          新しいコミット追加     タイムラインで可視化
```

---

### ステップ 1：PR 上で @copilot にエッジケース追加を依頼する

> スライド 4 で確認した PR をそのまま使う

1. PR の **Conversation タブ** を開く
2. コメント欄に `@copilot` 宛てのフィードバックを書く：

   > **「@copilot エッジケースのテストを追加してください。以下のケースをカバーしてください：**
   > - **空文字列のタイトルで POST した場合**
   > - **非常に長い文字列（1000文字以上）のタイトル**
   > - **存在しない ID で PUT（更新）した場合の 404**
   > - **同じ todo を2回削除した場合」**

3. コメントを **Submit** する

🗣️ **トーク:**
*「普通のコードレビューと同じ体験です。PR のコメント欄で @copilot にフィードバックするだけ。特別なツールや UI は必要ありません」*

---

### ステップ 2：Copilot の応答を確認する

1. Copilot がコメントに反応する：
   - 💬 応答コメント（「追加のテストケースを作成します」等）
   - ✍️ 新しいコミットが PR に追加される

2. **Commits タブ** を開いて、追加コミットを確認：
   - 最初のコミット：スライド 4 で作成されたテスト一式
   - 追加コミット：エッジケースのテスト

3. **Files changed** で差分を確認：
   - 新しいテスト関数が追加されている
   - 既存のテストは変更されていない（安全な追加）

🗣️ **トーク:**
*「Copilot は指示を理解して、必要な部分だけを追加しました。既存のコードを壊さずに、ピンポイントで改善できます」*

---

### ステップ 3：タイムラインで反復の流れを確認する

1. PR の **Conversation タブ** に戻る
2. タイムラインを上から下にスクロールして流れを見せる：

   ```
   [Copilot]  PR を作成（テスト一式）          ← スライド 4
       ↓
   [人]       @copilot エッジケースを追加して    ← 今のステップ
       ↓
   [Copilot]  応答 + 新しいコミット追加
       ↓
   [人]       確認 → レビュー → マージ           ← スライド 6 へ
   ```

3. この **人 ↔ Agent の双方向対話** が PR 上で完全に可視化されていることを強調

🗣️ **トーク:**
*「PR がコラボレーションのハブになっています。人が方向性を示し、Agent が実行する。このサイクルが PR 上で何度でも回せます。しかも全部のやり取りが履歴として残ります」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **既存ワークフローそのまま** | PR コメントで指示するだけ、新しいツール不要 |
| **反復的な改善** | フィードバック → 修正 → 確認のサイクルを何度でも回せる |
| **安全な変更** | 既存コードを壊さず、追加・修正のみ |
| **完全な履歴** | すべてのやり取りが PR タイムラインに記録される |
| **人が主導権を持つ** | Agent は実行するが、判断と方向性は人が決める |

---

### バックアップ（Copilot の応答が遅い場合）

- 「Agent は通常 1〜2 分で応答します」と補足
- コメントを送った状態で「応答を待つ間に、次のスライドに進みましょう」とスライド 6 へ移行
- 後でスライド 6 のデモ中に結果を確認することもできる

---

## 🔍 スライド 6：レビュー（Review）

> **メッセージ:** Copilot Code Review が PR diff を自律的に査読し、レビュー → 実行のループが回る

### 全体の流れ

```
自動レビュー結果を確認 → コメント＆コード提案 → @copilot に修正依頼 → 新コミットで修正
       ↓                       ↓                       ↓                    ↓
  Copilot Review         バグ指摘・改善提案        レビュー→実行ループ    スライド 4 に戻る
```

---

### ステップ 1：自動レビュー結果を確認する

> スライド 5 で作業していた PR をそのまま使う

1. PR の **Conversation タブ** を確認
2. Copilot Code Review が自動で実行されていることを見せる：
   - 🤖 **Copilot** がレビュアーとして表示されている
   - レビューステータス（「Changes requested」や「Commented」）

3. レビューのサマリーを確認：
   - Copilot が変更内容を理解した上でのフィードバック
   - コメント数と重要度

🗣️ **トーク:**
*「PR が開かれると、Copilot Code Review が自動的に走ります。人のレビュアーと同じように、PR にレビューとして表示されます」*

---

### ステップ 2：レビューコメントを確認する（バグ指摘・改善提案）

1. **Files changed** タブを開く
2. Copilot のレビューコメントを確認する：

   **バグ指摘の例：**
   - ⚠️ 「このテストではデータベースの状態がテスト間で共有されています。テストの独立性を確保するために、各テストの前にデータベースをリセットしてください」
   - ⚠️ 「ステータスコードの確認だけでなく、レスポンスボディの内容も検証すべきです」

   **改善提案の例：**
   - 💡 「`pytest.fixture` を使ってテストデータのセットアップを共通化できます」
   - 💡 「テスト関数名をより具体的にすると可読性が向上します（例: `test_create_todo` → `test_create_todo_with_valid_data_returns_201`）」

3. コメントが **具体的なコード行** を指しているのことを強調

🗣️ **トーク:**
*「汎用的な lint 警告ではありません。Copilot はテストコードのロジックを理解して、テストの独立性やアサーションの網羅性といった、実践的なフィードバックを返します」*

---

### ステップ 3：コード提案（Suggestion）を確認する

1. レビューコメントの中に **具体的なコード修正の提案** があることを見せる：
   - 「Suggested change」ブロックが表示される
   - 修正前 → 修正後のコードが diff 形式で見える

2. **「Apply suggestion」ボタン** があることを見せる（クリックはしない）：
   - ワンクリックで提案を適用できる
   - コミットとして PR に追加される

🗣️ **トーク:**
*「Copilot は問題を指摘するだけでなく、具体的な修正コードも提示します。Apply suggestion をクリックするだけで修正が適用されます」*

---

### ステップ 4：レビュー → 実行のループ

1. Copilot のレビュー指摘に対して、PR のコメントで依頼する：

   > **「@copilot レビューで指摘された問題をすべて修正してください」**

2. **期待結果:**
   - Copilot がレビューコメントを読み取る
   - 指摘事項に基づいてコードを修正
   - 新しいコミットとして PR に追加

3. この流れを図示：

   ```
   ┌──────────┐     ┌──────────┐     ┌──────────┐
   │  レビュー  │ ──→ │  @copilot │ ──→ │  新コミット │
   │ (指摘)    │     │ 修正依頼   │     │  (修正)    │
   └──────────┘     └──────────┘     └──────────┘
        ↑                                   │
        └───────────────────────────────────┘
                  再レビュー → 再修正ループ
   ```

🗣️ **トーク:**
*「レビュー層と実行層がループでつながっています。6層アーキテクチャは一方通行ではなく、レビュー → 実行 → 再レビューという循環が自然に回ります。これが『agentic』の本質です」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **自動レビュー** | PR が開かれると Copilot が自動的に査読を実行 |
| **文脈を理解したフィードバック** | 汎用的な lint ではなく、コードのロジックを理解した指摘 |
| **コード提案（Suggestion）** | 問題の指摘だけでなく、具体的な修正コードを提示 |
| **レビュー → 実行ループ** | 指摘 → `@copilot` で修正依頼 → 新コミット → 再レビュー |
| **6層の循環** | レビュー層と実行層が双方向でつながり、品質が反復的に向上 |

---

### バックアップ

- Copilot Code Review が自動で走っていない場合：
  - PR の **Reviewers** から **Copilot** を手動で選んでレビューをリクエスト
- レビューコメントが少ない場合：
  - 「コードの品質が高いほどコメントは少なくなります。これ自体がポジティブなシグナルです」と補足

---

## 🧠 スライド 7：文脈（Context）

> **メッセージ:** Custom Instructions / Spaces でリポジトリ固有の知識を Copilot に持たせ、チームの規約を自動的に適用する

### 全体の流れ

```
Custom Instructions を見せる → Chat でコード生成 → Agent 選択 → Spaces を紹介
         ↓                          ↓                    ↓                  ↓
  .github/ のファイル          規約に従った出力     専門 Agent を選ぶ     複数リポの知識統合
```

---

### ステップ 1：Custom Instructions ファイルを見せる

1. リポジトリの **Code タブ** → `.github/copilot-instructions.md` を開く
2. 内容をスクロールしながら、主要なルールをハイライト：

   | ルール | 効果 |
   |--------|------|
   | 🇯🇵 コメントと docstring は日本語 | 生成コードで一目瞭然 |
   | 📐 統一エラーフォーマット (`error.code`, `error.message`) | 現在の `HTTPException` とは別構造 |
   | 📄 リスト系にページネーション (`skip`, `limit`) | 現在のコードにはない機能 |
   | 🏷️ テスト命名 `test_<対象>_<条件>_<期待結果>` | 汎用的な名前と明らかに異なる |
   | 📝 全エンドポイントにログ出力 | 現在のコードにはない |

🗣️ **トーク:**
*「`.github/copilot-instructions.md` をリポジトリに置くだけで、Copilot の Chat・Coding Agent・Code Review すべてに反映されます。チームの規約を一度書けば、全員の Copilot が自動的に従います」*

---

### ステップ 2：Chat で Custom Instructions の効果を確認する

1. Copilot Chat を開く
2. 質問する：

   > **「このプロジェクトに /todos の検索エンドポイント（キーワードで todo を検索）を追加するコードを書いてください」**

3. **期待結果** — Custom Instructions に従ったコードが生成される：

   ```python
   @app.get("/todos/search", response_model=list[Todo])
   def search_todos(
       keyword: str,
       skip: int = 0,          # ← ページネーション（Custom Instructions）
       limit: int = 20,        # ← デフォルト値 20（Custom Instructions）
   ) -> list[Todo]:
       """キーワードで Todo を検索する。

       Args:
           keyword: 検索キーワード
           skip: スキップする件数
           limit: 取得する最大件数

       Returns:
           検索条件に一致する Todo のリスト

       Raises:
           AppError: 検索処理に失敗した場合
       """
       # ← 日本語 docstring（Custom Instructions）
       # ← Google スタイル（Custom Instructions）
       # ← 型ヒント付き（Custom Instructions）
   ```

4. **確認ポイントを聴衆に示す：**
   - ✅ docstring が**日本語**で書かれている
   - ✅ **Google スタイル**（Args / Returns / Raises セクション）
   - ✅ ページネーション（`skip`, `limit`）が**自動的に追加**されている
   - ✅ `limit` のデフォルト値が **20**（Custom Instructions で指定した値）
   - ✅ すべての引数に**型ヒント**がある

🗣️ **トーク:**
*「何も指示していないのに、日本語の docstring、ページネーション、型ヒントが自動的に含まれています。これは Custom Instructions が効いている証拠です。現在のコード（`app/main.py`）にはこれらの規約は適用されていません——つまり、Copilot は既存コードのパターンではなく、Custom Instructions を優先しています」*

---

### ステップ 3：Coding Agent で Custom Agent を選択する

> Issue アサイン時に使用する Agent を選べることを見せる

1. 新しい Issue を作成する（または既存の Issue を開く）
2. **Assignees** → **Copilot** を選択する際に、**Agent の選択肢**が表示されることを見せる：
   - デフォルトの Copilot Agent
   - Organization やリポジトリで設定されたカスタム Agent（存在する場合）

3. Agent 選択画面で説明：

   > 「ここでプロジェクトに最適化されたカスタム Agent を選べます。例えば、特定のフレームワーク（FastAPI）に精通した Agent や、社内の開発規約を深く理解した Agent を設定できます」

4. **デフォルトの Copilot** を選択して Issue をアサインする

🗣️ **トーク:**
*「Custom Instructions が『ルールブック』だとすれば、Custom Agent は『そのルールを熟知した専門家』を選ぶようなものです。チームごと、プロジェクトごとに最適な Agent を用意できます。例えば、フロントエンド専用 Agent、セキュリティ特化 Agent、テスト専門 Agent といった使い分けが可能です」*

---

### ステップ 4：Copilot Spaces を紹介する

1. GitHub.com の **Copilot** メニューから **Spaces** を開く（利用可能な場合）
2. UI をナビゲーションしながら説明：

   - 📁 **リポジトリの追加** — 複数のリポジトリをまとめて参照可能
   - 📄 **ドキュメントの追加** — 設計書・仕様書を文脈として追加
   - 👥 **チーム共有** — ナレッジベースをチームで共有

3. デモリポジトリとの関連で説明：

   > 「例えばこの Todo API がマイクロサービスの一部だった場合、他のサービスのリポジトリも Space にまとめることで、Copilot がサービス間の依存関係を理解した上でコードを生成できます」

🗣️ **トーク:**
*「Custom Instructions はリポジトリ単位の文脈、Spaces はリポジトリの枠を超えた文脈です。組織のアーキテクチャ全体の知識を Copilot に持たせることができます」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **一度書けば全機能に反映** | Custom Instructions は Chat・Coding Agent・Code Review すべてに適用 |
| **既存コードより Instructions を優先** | 現在のコードにないルールでも Instructions に従う |
| **目に見える効果** | 日本語 docstring、ページネーション等、出力で即座に確認可能 |
| **Custom Agent で専門家を選択** | プロジェクトに最適化された Agent を Issue アサイン時に選べる |
| **Spaces で横断的な文脈** | 複数リポジトリの知識を統合して Copilot に持たせられる |
| **チーム規約の自動適用** | 個人の知識ではなく、チームのルールとして定着 |

---

### バックアップ

- Chat でルールが完全に反映されない場合：
  - 反映されている部分をハイライトし「主要なルールが適用されています」と補足
  - 「Coding Agent ではより厳密に適用されます」と説明
- Spaces が利用できない場合：
  - スライドで概念を説明し「現在プレビュー提供中です」と補足

---

## 🔒 スライド 8：統制（Governance）

> **メッセージ:** Mission Control で Agent タスクを一元管理し、リアルタイムで監視・介入・追跡する

### 全体の流れ

```
Mission Control を開く → タスク一覧を確認 → リアルタイムステアリング → セッションログ確認
         ↓                     ↓                      ↓                       ↓
  github.com/copilot     全タスクの状態一覧     実行中 Agent に介入       思考過程を追跡
```

---

### ステップ 1：Mission Control でタスク一覧を確認する

1. **github.com/copilot** を開く（または右上の Copilot アイコン → タスクビュー）
2. **Mission Control のタスク一覧** を見せる：

   **今日のデモで作成したタスクが表示されていることを確認：**
   - 📋 スライド 3 で作成した Issue（ユニットテスト追加）→ ステータス表示
   - 📋 スライド 7 で作成した Issue（Custom Agent デモ用）→ ステータス表示

3. 各タスクのステータスを説明：
   - 🟡 **In progress** — Agent が現在実行中
   - ✅ **Completed** — Agent が PR を作成済み
   - 🔴 **Needs input** — Agent がフィードバックを待っている
   - 各タスクから PR へのクイックリンク

🗣️ **トーク:**
*「Mission Control は Agent タスクの管制塔です。複数のタスクを同時に走らせても、ここで全体を一望できます。どのタスクが進行中で、どれが人の入力を待っているか——一目でわかります」*

---

### ステップ 2：タスク詳細画面 — Overview と Files changed を見る

1. タスク一覧から **1つのタスクをクリック** して詳細画面を開く
2. **一画面で全情報を見せる：**

   **左側：セッションログ**
   - Agent がどのファイルを読んだか
   - どのような判断をしたか
   - コミットの理由がリアルタイムで表示される

   **右側タブ：**
   - **Overview** — タスクの概要、進捗、作成された PR
   - **Files changed** — Agent が変更したファイルの diff

3. 確認ポイント：
   - ✅ ページを移動せずに全情報を確認できる
   - ✅ セッションログとコード変更を並べて見られる
   - ✅ Agent のコミット理由がコンテキスト内に表示される

🗣️ **トーク:**
*「従来は Issue → Actions → PR → Files changed とページを行き来する必要がありましたが、Mission Control ではすべてが一画面に集約されています。Agent の思考過程とコード変更を同時に確認できます」*

---

### ステップ 3：リアルタイムステアリング — 実行中の Agent に介入する

> スライド 7 で新しい Issue をアサインしていれば、Agent が実行中の可能性がある。そうでなければ、新規タスクを作成する。

1. **実行中のタスク**（🟡 In progress）を開く
2. **チャット入力欄** からリアルタイムで指示を送る：

   > **「テストファイルには必ず日本語の docstring を含めてください。Custom Instructions に従ってください」**

3. **期待結果：**
   - Agent が現在のツールコール完了後に指示を取り込む
   - セッションログに新しい指示が反映される
   - 以降の作業が指示に沿って変更される

4. **Files changed タブ** からも直接コメント可能であることを見せる：
   - コードの特定行にコメントを追加
   - PR ページに移動する必要がない

🗣️ **トーク:**
*「これがリアルタイムステアリングです。Agent が作業している最中でも、方向修正ができます。従来は PR コメントで @copilot に伝える必要がありましたが、Mission Control ではチャットで直接指示できます。即座にフィードバックが反映されます」*

---

### ステップ 4：タスクの起動方法の多様性を見せる

1. Mission Control 画面で **新しいタスクの作成** ボタンを見せる
2. 複数の起動方法を説明：

   | 起動方法 | 場所 |
   |---------|------|
   | **Issue アサイン** | Issue ページで Copilot をアサイン（スライド 3 で実演済み） |
   | **github.com/copilot** | Mission Control から直接タスク作成 |
   | **Chat で `/task`** | Copilot Chat で `/task` コマンド |
   | **GitHub Mobile** | モバイルアプリのタスクページから |

3. **IDE への引き継ぎ** にも言及：
   - 「Codespaces で開く」「VS Code で開く」ボタン
   - Agent の作業途中でも、人が IDE で引き継げる

🗣️ **トーク:**
*「統制とは制限するだけではありません。どこからでもタスクを作成でき、どこでも作業を引き継げる——その柔軟性も統制の一部です。管理者はポリシーで制御し、開発者は Mission Control で効率的に運用できます」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **一元的なタスク管理** | 全 Agent タスクを Mission Control で一望。状態・進捗が一目でわかる |
| **リアルタイムステアリング** | 実行中の Agent に即座に介入・方向修正が可能 |
| **一画面での全情報確認** | セッションログ + Overview + Files changed がページ遷移なしで見える |
| **柔軟な起動方法** | Issue / Chat / Mission Control / Mobile — どこからでもタスクを開始 |
| **IDE への引き継ぎ** | Agent の作業を Codespaces / VS Code でシームレスに引き継ぎ |
| **観察可能性** | Agent の思考過程をセッションログでリアルタイム追跡 |

---

### バックアップ

- 実行中の Agent がない場合（リアルタイムステアリング不可）：
  - 新しいタスクを `/task` で作成し、ステアリングの入力欄を見せる
  - 「実行中のタスクがあれば、ここからリアルタイムで指示を送れます」と説明
- Mission Control にタスクが表示されていない場合：
  - github.com/copilot/agents からタスク一覧にアクセスしてみる
  - 「タスクの反映に数分かかることがあります」と補足

---
---

# 🎬 Act 2 — Client-Side & Hybrid Demo Scenarios

> **Act 1 との対比**
>
> | | Act 1（Cloud） | Act 2（Client & Hybrid） |
> |--|---------------|------------------------|
> | **メッセージ** | Agent があなたの**代わりに**非同期で自律実行する | Agent があなたと**一緒に**リアルタイムで協働する |
> | **実行場所** | GitHub.com / Actions | VS Code / ターミナル / ハイブリッド |
> | **フィードバック** | PR で結果を確認 | エディタ・ターミナルで即座に確認 |
> | **適したタスク** | 大きなタスク（テスト一式追加等） | 中〜小のタスク・リファクタ・DevOps |

---

## 💻 スライド 9：VS Code Agent Mode — インタラクティブ実行

> **メッセージ:** VS Code Agent Mode は「自分と一緒にコードを書く」体験。リアルタイムで Agent の作業を確認し、即座に方向修正できる

### 全体の流れ

```
VS Code で開く → @workspace で理解 → Agent Mode 起動 → バリデーション追加 → ローカルテスト → 確認
      ↓                ↓                  ↓                    ↓                  ↓            ↓
  既に開いている    コード把握        インタラクティブ実行    複数ファイル編集    即座にフィードバック   完成
```

### Cloud Agent との対比

```
┌─────────────────────────────────────────────────────────────┐
│  Cloud Agent（Slide 4）         VS Code Agent Mode（Slide 9）│
│  ─────────────────────         ────────────────────────────  │
│  非同期・自律実行               同期・インタラクティブ実行      │
│  結果を待つ                    リアルタイムで見守る            │
│  PR で結果を確認               エディタで即座に確認           │
│  大きなタスク向き              中〜小のタスク・リファクタ向き  │
│  Issue → Agent → PR           Chat → Agent → ローカル確認    │
└─────────────────────────────────────────────────────────────┘
```

---

### ステップ 1：@workspace でコードベースを理解する（Cloud Chat との対比）

1. VS Code で `demo-ghec` が開いている状態（デモ冒頭で実施済み）
2. Copilot Chat パネルを開く（`Ctrl+Shift+I` または サイドバーの Copilot アイコン）
3. **@workspace** を使ってリポジトリを理解する：

   > **「@workspace このプロジェクトの構造と各ファイルの役割を説明してください」**

4. **期待結果:**
   - VS Code がローカルのファイルインデックスを使って高速に回答
   - `app/main.py`、`app/models.py`、`app/database.py` の関係を説明
   - GitHub.com Chat と同等の回答が、ローカルで即座に得られる

5. 続けて改善点を聞く：

   > **「@workspace 入力バリデーションが不足しているエンドポイントはどれですか？具体的に何が足りないか教えてください」**

6. **期待結果:**
   - `POST /todos`: タイトルの空文字チェックなし
   - `PUT /todos/{id}`: 更新値のバリデーションなし
   - `TodoCreate`/`TodoUpdate` モデルに Pydantic validator がない

🗣️ **トーク:**
*「スライド 3 では GitHub.com の Chat で同じことをしました。VS Code でも @workspace を使えば、ローカルのファイルインデックスを活用して同じ品質の回答が得られます。違いは速度——ローカルファイルなので、応答が非常に高速です」*

---

### ステップ 2：Agent Mode を起動して入力バリデーションを追加する

1. Copilot Chat で **Agent Mode** に切り替える（チャット入力欄のモードセレクターで「Agent」を選択）
2. Agent に指示する：

   > **「入力バリデーションを追加してください。TodoCreate と TodoUpdate モデルに Pydantic のフィールドバリデーションを追加し、タイトルが空文字でないこと、文字列の最大長を制限してください。Custom Instructions に従って実装してください」**

3. **Agent Mode の動きを実演（ここが見せ場）：**

   ⚡ **リアルタイムで見える Agent の行動：**
   - 📖 `app/models.py` を開いて分析
   - 📖 `app/main.py` を開いてエンドポイントを確認
   - 📖 `.github/copilot-instructions.md` を読み込み
   - ✏️ `app/models.py` を編集（バリデーション追加）
   - ✏️ `app/main.py` を編集（カスタム例外ハンドラ追加）
   - 🆕 新しいファイル `app/exceptions.py` を作成（カスタム例外クラス）
   - 🖥️ ターミナルでコマンド実行（依存関係確認等）

4. **重要な実演ポイント — インタラクティブ性：**
   - 各ファイルの変更に対して **Accept / Reject** が選べることを見せる
   - Agent がターミナルコマンドを実行しようとしたとき、**承認を求める** ことを見せる
   - 途中で方向修正ができることを強調

🗣️ **トーク:**
*「Cloud Agent との決定的な違いがここです。Cloud Agent は結果だけを PR で返しますが、VS Code Agent Mode は一つ一つのファイル変更を目の前で見せてくれます。気に入らない変更があれば、その場で却下できます。Agent を完全にコントロールしながら作業を進められます」*

---

### ステップ 3：Agent の生成コードを確認する

1. Agent が生成したコードを確認する。**期待される変更：**

   **`app/models.py`（バリデーション追加）:**
   ```python
   from pydantic import BaseModel, Field, field_validator

   # タイトルの最大文字数
   MAX_TITLE_LENGTH = 100
   # 説明の最大文字数
   MAX_DESCRIPTION_LENGTH = 500

   class TodoCreate(BaseModel):
       """Todo 作成リクエストのスキーマ。"""
       title: str = Field(..., min_length=1, max_length=MAX_TITLE_LENGTH)
       description: str | None = Field(None, max_length=MAX_DESCRIPTION_LENGTH)

       @field_validator('title')
       @classmethod
       def title_must_not_be_blank(cls, v: str) -> str:
           """タイトルが空白のみでないことを検証する。"""
           if not v.strip():
               raise ValueError('タイトルは空白のみにはできません')
           return v.strip()
   ```

   **`app/exceptions.py`（新規作成 — Custom Instructions に従ったカスタム例外）:**
   ```python
   class AppError(Exception):
       """アプリケーション共通のエラークラス。"""
       def __init__(self, code: str, message: str, status_code: int, details: dict | None = None):
           self.code = code
           self.message = message
           self.status_code = status_code
           self.details = details or {}
   ```

2. **Custom Instructions が効いていることを確認：**
   - ✅ 日本語のコメント・docstring
   - ✅ `X | None` 形式（`Optional` ではなく）
   - ✅ カスタム例外クラス（`HTTPException` ではなく）
   - ✅ マジックナンバーではなく定数定義（`MAX_TITLE_LENGTH`）

🗣️ **トーク:**
*「Custom Instructions はクラウドだけでなく、VS Code でも有効です。日本語 docstring、カスタム例外、型ヒント——すべてのルールが自動的に適用されています。スライド 7 で見せたのと同じ効果が、ローカル開発でも得られます」*

---

### ステップ 4：ローカルでテストを実行する

1. Agent Mode に続けて指示する：

   > **「追加したバリデーションのテストも書いてください。tests/ ディレクトリに追加してください」**

2. Agent が `tests/test_validation.py` を生成
3. Agent がターミナルで pytest を実行：

   ```bash
   pytest tests/test_validation.py -v
   ```

4. テスト結果がターミナルに表示される：
   - ✅ `test_create_todo_with_empty_title_returns_422`
   - ✅ `test_create_todo_with_blank_title_returns_422`
   - ✅ `test_create_todo_with_long_title_returns_422`
   - ✅ `test_create_todo_with_valid_data_returns_201`

🗣️ **トーク:**
*「Agent がコードを書くだけでなく、テストも書いて、実行まで自動的にやってくれます。テストが通らなければ Agent が自分で修正を試みます。このフィードバックループがローカルで即座に回るのが VS Code Agent Mode の強みです」*

---

### ステップ 5：（オプション）Next Edit Suggestions を見せる

1. Agent Mode のセッションを終了し、手動編集モードに切り替える
2. `app/main.py` を開く
3. 一つのエンドポイントに日本語 docstring を手動で追加する
4. **Next Edit Suggestions（NES）** が次のエンドポイントにも同じパターンの docstring を提案することを見せる
5. `Tab` キーで提案を受け入れ、連鎖的に全エンドポイントに適用

🗣️ **トーク:**
*「Next Edit Suggestions はパターンを学習します。一つ修正すれば、同じパターンの修正が他の箇所にも自動的に提案されます。Agent Mode は大きなタスク、NES は細かな反復作業——使い分けがポイントです」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **インタラクティブな実行** | Agent の各ステップを目の前で確認、Accept/Reject で制御 |
| **即座のフィードバック** | ローカル実行なので結果がすぐ見える、テストも即座に回せる |
| **Custom Instructions の一貫性** | クラウドと同じルールが VS Code でも自動適用 |
| **複数ファイル編集** | Agent Mode が models.py, main.py, exceptions.py を横断的に編集 |
| **ターミナル統合** | Agent がコマンドを実行し、結果に基づいて次の行動を判断 |
| **NES との補完** | Agent Mode（大タスク）+ NES（パターン反復）の使い分け |

---

### バックアップ

- Agent Mode の応答が遅い場合：
  - Chat モード（Agent ではなく Ask/Edit モード）で個別にコード生成を見せる
  - 「Agent Mode は複数ステップを自動化しますが、Chat でも一つずつ同じことができます」と補足
- Custom Instructions が反映されない場合：
  - `.github/copilot-instructions.md` が開かれていることを確認
  - Chat で明示的に「Custom Instructions に従って」と指示する

---

## 🖥️ スライド 10：Copilot CLI — ターミナルファースト開発

> **メッセージ:** ターミナルから一歩も出ずに、自然言語でコード生成・テスト・コミットまで完結する

### 全体の流れ

```
CLI でプロジェクト分析 → Dockerfile 生成 → docker-compose 生成 → ビルド＆テスト → コミット
         ↓                    ↓                    ↓                   ↓              ↓
   「何が足りない？」     マルチステージビルド    サービス構成定義      動作確認       Git 操作
```

### 3つのサーフェスの対比

```
┌───────────────────────────────────────────────────────────────────┐
│  GitHub.com Chat      VS Code Chat/Agent      Copilot CLI        │
│  ──────────────       ──────────────────      ───────────        │
│  ブラウザで質問        エディタで編集           ターミナルで全完結  │
│  Issue → Agent        Agent Mode → ローカル    自然言語 → 実行    │
│  PR で結果確認         エディタで即確認         ターミナルで即確認  │
│  管理者・PM 向き      開発者の日常             DevOps・CLI 愛好者  │
└───────────────────────────────────────────────────────────────────┘
```

---

### ステップ 1：Copilot CLI でプロジェクトを分析する

1. ターミナルで `demo-ghec` ディレクトリにいることを確認
2. Copilot CLI を起動：

   > **「このプロジェクトをコンテナ化するために何が必要ですか？現在のファイル構成を分析して教えてください」**

3. **期待結果:**
   - Copilot CLI がプロジェクト構造を分析
   - `requirements.txt` の依存関係を確認
   - FastAPI + Uvicorn の構成を認識
   - Dockerfile と docker-compose.yml が必要と判断
   - ポート 8000 の公開が必要と判断

🗣️ **トーク:**
*「Copilot CLI はターミナルネイティブの体験です。ブラウザも VS Code も開かずに、ターミナルの中で Copilot と対話できます。SSH でリモートサーバーに接続しているときにも使えます」*

---

### ステップ 2：Dockerfile を生成する

1. Copilot CLI に指示する：

   > **「このFastAPIアプリケーション用の本番向け Dockerfile を作成してください。マルチステージビルド、非 root ユーザー、ヘルスチェックを含めてください」**

2. **期待結果 — Copilot CLI が Dockerfile を生成：**

   ```dockerfile
   # ビルドステージ
   FROM python:3.11-slim AS builder
   WORKDIR /build
   COPY requirements.txt .
   RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

   # 実行ステージ
   FROM python:3.11-slim
   # 非rootユーザーの作成
   RUN useradd --create-home appuser
   WORKDIR /home/appuser/app
   COPY --from=builder /install /usr/local
   COPY app/ ./app/
   USER appuser
   EXPOSE 8000
   HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
       CMD curl -f http://localhost:8000/ || exit 1
   CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

3. Copilot CLI がファイルをディスクに書き込むことを見せる

🗣️ **トーク:**
*「自然言語で『マルチステージビルド、非rootユーザー、ヘルスチェック』と言うだけで、ベストプラクティスに沿った Dockerfile が生成されます。Docker の細かい構文を覚える必要がありません」*

---

### ステップ 3：docker-compose.yml を生成する

1. 続けて指示する：

   > **「この Dockerfile を使った docker-compose.yml も作成してください。開発用のホットリロード設定も含めてください」**

2. **期待結果:**

   ```yaml
   services:
     api:
       build: .
       ports:
         - "8000:8000"
       volumes:
         - ./app:/home/appuser/app/app  # 開発用ホットリロード
       environment:
         - UVICORN_RELOAD=true
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:8000/"]
         interval: 30s
         timeout: 5s
         retries: 3
   ```

🗣️ **トーク:**
*「プロジェクトの文脈を理解しているので、ポート番号やパスを間違えません。Copilot CLI はコードベースを読んだ上で、適切な設定を生成します」*

---

### ステップ 4：ビルドしてテストする

1. Copilot CLI に指示する：

   > **「Docker イメージをビルドして、コンテナを起動し、ヘルスチェックが通ることを確認してください」**

2. **期待結果 — CLI が一連のコマンドを提案・実行：**

   ```bash
   docker compose build
   docker compose up -d
   curl http://localhost:8000/
   curl http://localhost:8000/todos
   docker compose down
   ```

3. 各コマンドの実行結果がターミナルに表示される

🗣️ **トーク:**
*「CLI はコード生成だけでなく、ビルド・テスト・確認まで一気通貫です。ターミナルから一歩も出ずに、コンテナ化からデプロイ確認まで完了しました」*

---

### ステップ 5：Git コミットしてプッシュする

1. Copilot CLI に指示する：

   > **「変更をステージングして、適切なコミットメッセージでコミットしてください」**

2. **期待結果:**

   ```bash
   git add Dockerfile docker-compose.yml
   git commit -m "Add Dockerfile and docker-compose.yml for containerization

   - Multi-stage build for smaller image size
   - Non-root user for security
   - Health check endpoint configuration
   - Development hot-reload support via docker-compose"
   ```

🗣️ **トーク:**
*「コミットメッセージも自動生成です。変更内容を理解した上で、意味のあるメッセージを書いてくれます。ターミナルだけで分析→生成→テスト→コミットの全サイクルが完了しました」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **ターミナル完結** | ブラウザも IDE も不要、SSH 環境でも使える |
| **自然言語 → 実行** | Docker の構文を覚える必要なし、意図を伝えるだけ |
| **コンテキスト認識** | プロジェクト構造を理解した上で適切な設定を生成 |
| **ビルド＆テスト統合** | コード生成からテスト実行まで一気通貫 |
| **Git 統合** | コミットメッセージも自動生成、意味のある履歴 |
| **DevOps タスクに強い** | Dockerfile、CI/CD、シェルスクリプトなどインフラ系に最適 |

---

### バックアップ

- Docker が利用できない環境の場合：
  - Dockerfile の生成と内容説明だけ見せる
  - 「実際の環境では即座にビルド・テストまでできます」と補足
- CLI の応答が遅い場合：
  - 事前に生成済みのファイルを用意しておく

---

## 🔄 スライド 11：ハイブリッド — クラウド⇔クライアント連携

> **メッセージ:** 適材適所——分析はCLI、自律実行はCloud、精緻な調整はVS Code。各ツールの強みを活かしたリレー開発

### 全体の流れ

```
[CLI] 分析＆Issue作成 → [Cloud] Agent 実行 → [Mission Control] 監視 → [VS Code] 引き継ぎ → [Cloud] Review
       ↓                     ↓                      ↓                     ↓                    ↓
  ターミナルで発見      Actions で自動実行      進捗をリアルタイム監視   ローカルで精緻化      品質を自動チェック
```

### リレー開発の全体像

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        リレー開発フロー                                   │
│                                                                          │
│  🖥️ CLI          ☁️ Cloud           🖥️ VS Code        ☁️ Cloud          │
│  ┌────────┐     ┌────────┐         ┌────────┐        ┌────────┐        │
│  │ 分析    │ ──→ │ Agent  │ ──→     │ 引継ぎ  │ ──→    │ Review │        │
│  │ Issue作成│     │ 自律実行│  ↓      │ 精緻化  │        │ 品質確認│        │
│  └────────┘     └────────┘  │      └────────┘        └────────┘        │
│                              │                                           │
│                     📊 Mission Control                                   │
│                     （リアルタイム監視）                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### ステップ 1：[CLI] Copilot CLI で CI/CD の要件を分析する

1. ターミナルで Copilot CLI に質問：

   > **「このプロジェクトに CI/CD パイプラインを追加したい。GitHub Actions で pytest の実行、コードリントチェック、Docker イメージのビルドを含むワークフローを設計してください。要件を GitHub Issue にまとめてください」**

2. **期待結果:**
   - Copilot CLI がプロジェクト構造を分析
   - 必要な CI/CD ステップを整理
   - GitHub Issue の内容を生成
   - `gh issue create` コマンドで Issue を直接作成

3. CLI が提案するコマンド：

   ```bash
   gh issue create \
     --title "Add CI/CD pipeline with GitHub Actions" \
     --body "## Requirements
   - Run pytest on every push and PR
   - Python linting with ruff
   - Build Docker image on main branch
   - Cache pip dependencies for faster builds

   ## Acceptance Criteria
   - [ ] .github/workflows/ci.yml created
   - [ ] Tests pass in CI environment
   - [ ] Lint checks pass
   - [ ] Docker build succeeds"
   ```

🗣️ **トーク:**
*「ターミナルから直接 GitHub Issue を作成しました。ブラウザを開く必要はありません。CLI は分析 → 要件定義 → Issue 作成まで一気通貫です。ここからはクラウドにバトンを渡します」*

---

### ステップ 2：[Cloud] Issue に Copilot をアサインして Agent に実行させる

1. **2つの方法のどちらかを選択：**

   **方法 A — CLI から直接：**
   ```bash
   gh issue edit <issue_number> --add-assignee @copilot
   ```

   **方法 B — GitHub.com で操作：**
   - Issue ページを開く → Assignees → Copilot を選択

2. Coding Agent が自律実行を開始
3. **スライド 4 と同じ体験** — Actions で実行過程を観察

🗣️ **トーク:**
*「CLI で作った Issue を Cloud Agent が拾って自律実行します。ターミナルで要件を定義し、クラウドで非同期実行——人間の開発チームと同じリレーです」*

---

### ステップ 3：[Mission Control] 実行中の Agent を監視する

1. **github.com/copilot** で Mission Control を開く
2. 先ほど作成したタスクが表示されていることを確認
3. セッションログでリアルタイム進捗を見る：
   - Agent が `.github/workflows/ci.yml` を作成中
   - Agent が `ruff` の設定を追加中
   - Agent がテスト実行を確認中

🗣️ **トーク:**
*「CLI で投げたタスクを Mission Control で監視しています。Agent がどこまで進んでいるかリアルタイムで確認できます。ここからが今回のハイライト——VS Code への引き継ぎです」*

---

### ステップ 4：[VS Code] Agent の作業を VS Code で引き継ぐ

> **ここがハイブリッドワークフローの最大の見せ場**

1. Mission Control で **「Open in VS Code」** ボタンを見せる（または PR ページから）
2. Agent が作成した PR のブランチをローカルにチェックアウト：

   ```bash
   gh pr checkout <pr_number>
   ```

3. VS Code で Agent が作成したファイルを確認：
   - `.github/workflows/ci.yml` を開く
   - Agent の生成内容をレビュー

4. **VS Code Agent Mode で改良を加える：**

   > **「@workspace この CI/CD ワークフローにキャッシュの最適化とマトリックステストの設定（Python 3.11 と 3.12）を追加してください」**

5. **期待結果:**
   - Agent Mode がワークフローファイルを編集
   - matrix strategy で複数 Python バージョンを追加
   - pip キャッシュの設定を最適化

6. 変更をコミットしてプッシュ：

   ```bash
   git add .github/workflows/ci.yml
   git commit -m "Optimize CI/CD: add matrix testing and cache"
   git push
   ```

🗣️ **トーク:**
*「Cloud Agent が 80% の仕事をし、残りの 20%——マトリックステストやキャッシュ最適化といった細かな調整——を VS Code で行いました。大枠は Agent に任せ、仕上げは人が VS Code で。これが適材適所のリレー開発です」*

---

### ステップ 5：[Cloud] Code Review で品質を確認する

1. プッシュ後、Copilot Code Review が自動で走る
2. PR ページでレビュー結果を確認：
   - Cloud Agent のコードと人の修正、両方が含まれた PR
   - Code Review が全体を通してレビュー

3. **フロー全体を振り返る：**

   ```
   [CLI] 分析＆Issue作成        — ターミナルの強み（高速な分析）
      ↓
   [Cloud] Agent 自律実行      — クラウドの強み（非同期・自律）
      ↓
   [Mission Control] 監視      — ガバナンスの強み（可観測性）
      ↓
   [VS Code] 引き継ぎ＆改良    — IDE の強み（精緻な編集）
      ↓
   [Cloud] Code Review         — 自動品質保証
   ```

🗣️ **トーク:**
*「CLI → Cloud → Mission Control → VS Code → Cloud Review。5つのサーフェスを横断しましたが、体験は一貫しています。どのツールを使うかは開発者が選べます。強制されるワークフローはありません」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **適材適所** | 分析は CLI、自律実行は Cloud、精緻化は VS Code、品質は Code Review |
| **シームレスなハンドオフ** | CLI → Cloud → VS Code の切り替えに摩擦がない |
| **80/20 の法則** | Agent が 80% を自動化、人が 20% の重要な判断を行う |
| **全サーフェスの統合** | CLI, Cloud, Mission Control, VS Code, Code Review が一つのフローに |
| **開発者の選択肢** | どのツールをどの場面で使うか、開発者が自由に選べる |

---

### バックアップ

- Agent の実行が間に合わない場合：
  - 事前に完成済みの PR を用意しておき、VS Code 引き継ぎの部分から見せる
  - 「通常は数分で Agent が PR を作成するので、そこから VS Code で引き継げます」と補足
- Mission Control の「Open in VS Code」が利用できない場合：
  - `gh pr checkout` コマンドで直接チェックアウトする

---

## 🌐 スライド 12：コンテキスト一貫性 — どこでも同じルール

> **メッセージ:** Custom Instructions を一度定義すれば、GitHub.com / VS Code / CLI のすべてで同じルールが適用される

### 全体の流れ

```
同じリクエストを 3 サーフェスで実行 → 出力を比較 → 一貫性を確認
     ↓                                   ↓               ↓
GitHub.com / VS Code / CLI           並べて見せる      エンタープライズ品質
```

---

### ステップ 1：3つのサーフェスで同じリクエストを送る

**共通リクエスト：**
> **「/todos の検索エンドポイント（キーワードで todo をフィルタ）を追加するコードを書いてください」**

このリクエストを以下の 3 箇所で実行する（事前に準備しておき、結果を並べて見せる）：

#### サーフェス A：GitHub.com Chat

1. GitHub.com のリポジトリで Copilot Chat を開く
2. リクエストを送信
3. 生成されたコードをコピーして比較用に保存

#### サーフェス B：VS Code Chat

1. VS Code で Copilot Chat を開く
2. 同じリクエストを送信
3. 生成されたコードを確認

#### サーフェス C：Copilot CLI

1. ターミナルで Copilot CLI を起動
2. 同じリクエストを送信
3. 生成されたコードを確認

---

### ステップ 2：出力を並べて比較する

1. 3つの出力を並べて見せる（VS Code のスプリットビュー等を使用）
2. **全サーフェスで共通して適用されている Custom Instructions：**

   | ルール | GitHub.com | VS Code | CLI |
   |--------|-----------|---------|-----|
   | 🇯🇵 日本語 docstring | ✅ | ✅ | ✅ |
   | 📐 Google スタイル docstring | ✅ | ✅ | ✅ |
   | 📄 ページネーション (`skip`, `limit`) | ✅ | ✅ | ✅ |
   | 🔢 `limit` デフォルト値 20 | ✅ | ✅ | ✅ |
   | 🏷️ 型ヒント | ✅ | ✅ | ✅ |
   | ⚠️ `X \| None` 形式 | ✅ | ✅ | ✅ |

🗣️ **トーク:**
*「3つの全く異なるサーフェス——ブラウザ、エディタ、ターミナル——で同じコードが生成されました。Custom Instructions は `.github/copilot-instructions.md` という 1 つのファイルで定義していますが、それがチームの全メンバーの、すべてのツールで、自動的に適用されます」*

---

### ステップ 3：エンタープライズ観点での意味を説明する

1. スライドまたは口頭で、組織規模での意味を説明：

   ```
   ┌──────────────────────────────────────────────────┐
   │            Custom Instructions の効果              │
   │                                                    │
   │  開発者 A（VS Code 派）  ──→  同じルール適用      │
   │  開発者 B（CLI 派）      ──→  同じルール適用      │
   │  開発者 C（GitHub.com 派）──→  同じルール適用      │
   │  Coding Agent            ──→  同じルール適用      │
   │  Code Review             ──→  同じルール基準      │
   │                                                    │
   │  結果：コードスタイルの統一、レビューコストの削減   │
   └──────────────────────────────────────────────────┘
   ```

🗣️ **トーク:**
*「個人の好みやツールの選択に関係なく、チーム全体で一貫したコードが生成されます。これはコードレビューの効率化だけでなく、オンボーディングの加速にも直結します。新しいメンバーが使うツールが何であっても、最初からチームの規約に沿ったコードが書けるのです」*

---

### この Demo のポイント

| ポイント | 説明 |
|---------|------|
| **一度定義、全面適用** | `.github/copilot-instructions.md` 1ファイルで全サーフェスをカバー |
| **ツール非依存** | どのツールを使っても同じルールが適用される |
| **チーム規約の自動適用** | 個人ではなくリポジトリ単位でルールを管理 |
| **レビューコスト削減** | スタイルの議論が不要、レビューはロジックに集中 |
| **オンボーディング加速** | 新メンバーでも初日から規約に沿ったコードを生成 |

---

### バックアップ

- 3つのサーフェスすべてでデモする時間がない場合：
  - GitHub.com と VS Code の 2つだけで比較
  - 「CLI でも同じ結果が得られます」と補足
- 出力が完全に同一でない場合：
  - 「生成AIなので表現は毎回異なりますが、Custom Instructions のルール——日本語、ページネーション、型ヒント——は全サーフェスで一貫しています」と補足

---

## 📊 全体マッピング — 6層 × 3サーフェス

| 層 | Cloud（Act 1） | VS Code（Act 2） | CLI（Act 2） |
|-----|---------------|-----------------|--------------|
| **Entry** | Chat → Issue | @workspace → Agent Mode | CLI で分析 → gh issue |
| **Execution** | Actions (Coding Agent) | Agent Mode（インタラクティブ） | CLI Agentic Mode |
| **Collaboration** | PR コメント @copilot | VS Code で PR コメント | — |
| **Review** | Copilot Code Review | VS Code で Review 確認 | — |
| **Context** | Custom Instructions / Spaces | 同一 Instructions 適用 | 同一 Instructions 適用 |
| **Governance** | Mission Control | "Open in VS Code" で引き継ぎ | CLI でタスク状態確認 |

---

## 🔧 デモ準備チェックリスト

### 環境要件

- [ ] VS Code Insiders がインストール済み、Copilot 拡張機能が有効
- [ ] Copilot CLI がインストール済み（`copilot --version` で確認）
- [ ] `demo-ghec` リポジトリがローカルにクローン済み
- [ ] `demo/agentic-copilot-0311` ブランチにチェックアウト済み
- [ ] Python 3.11+ がインストール済み
- [ ] `pip install -r requirements.txt` 実行済み
- [ ] Docker がインストール済み（Slide 10 用）
- [ ] `gh` CLI がインストール済み・認証済み（Slide 11 用）

### 事前準備

- [ ] VS Code Insiders でリポジトリを開いておく
- [ ] Copilot Chat パネルを表示しておく
- [ ] ターミナルを2つ以上開いておく（CLI デモ用）
- [ ] ブラウザで GitHub.com のリポジトリページを開いておく
- [ ] Docker Desktop を起動しておく（Slide 10 用）

### バックアップ資料

- [ ] 各スライドの「期待結果」のスクリーンショットを用意
- [ ] 事前に生成した Dockerfile、docker-compose.yml のバックアップコピー
- [ ] 事前に作成した CI/CD ワークフローの PR（Slide 11 バックアップ用）
