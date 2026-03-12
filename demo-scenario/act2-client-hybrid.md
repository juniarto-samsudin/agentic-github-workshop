# 💻 Act 2 — Client-Side & Hybrid Demo Scenarios

> **Agent があなたと一緒にリアルタイムで協働する**
>
> スライド 9〜12：VS Code / Copilot CLI / ハイブリッドのデモシナリオ
>
> 📋 [全体構成に戻る](README.md)

---

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

