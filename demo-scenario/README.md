# 🎬 Agentic GitHub Copilot — Demo Scenario

> **スライドごとのライブデモシナリオ**
> 各スライド（3〜12）に対応するデモを実施し、6層アーキテクチャを体験的に示す
> Act 1（Cloud-Side: Slides 3-8）＋ Act 2（Client-Side & Hybrid: Slides 9-12）

---

## 📋 全体構成

### Act 1 — ☁️ Cloud-Side：Agent があなたの代わりに非同期で自律実行する

📄 **[act1-cloud.md](act1-cloud.md)**

| スライド | テーマ | デモ内容 | 所要時間 |
|---------|--------|---------|---------|
| 3 | [入口（Entry）](act1-cloud.md#-スライド-3入口entry) | Chat でコード理解 → Issue 作成 → Copilot アサイン | ~3 min |
| 4 | [実行（Execution）](act1-cloud.md#-スライド-4実行execution) | Actions 上の実行過程 → セッションログ → 完成 PR 確認 | ~4 min |
| 5 | [協働（Collaboration）](act1-cloud.md#-スライド-5協働collaboration) | PR 上で @copilot にエッジケース追加を依頼 → 反復 | ~3 min |
| 6 | [レビュー（Review）](act1-cloud.md#-スライド-6レビューreview) | 自動レビュー確認 → コメント＆提案 → 修正ループ | ~3 min |
| 7 | [文脈（Context）](act1-cloud.md#-スライド-7文脈context) | Custom Instructions → Chat 効果確認 → Agent 選択 → Spaces | ~3 min |
| 8 | [統制（Governance）](act1-cloud.md#-スライド-8統制governance) | Mission Control でタスク管理 → リアルタイムステアリング | ~3 min |

### Act 2 — 💻 Client-Side & Hybrid：Agent があなたと一緒にリアルタイムで協働する

📄 **[act2-client-hybrid.md](act2-client-hybrid.md)**

| スライド | テーマ | デモ内容 | 所要時間 |
|---------|--------|---------|---------|
| 9 | [VS Code Agent Mode](act2-client-hybrid.md#-スライド-9vs-code-agent-mode--インタラクティブ実行) | Agent Mode で入力バリデーション追加 → リアルタイム協働 → ローカルテスト | ~5 min |
| 10 | [Copilot CLI](act2-client-hybrid.md#-スライド-10copilot-cli--ターミナルファースト開発) | CLI で Dockerfile 生成 → ビルド＆テスト → コミット（全てターミナル完結） | ~4 min |
| 11 | [Hybrid ワークフロー](act2-client-hybrid.md#-スライド-11ハイブリッド--クラウドクライアント連携) | CLI 分析 → Issue → Cloud Agent → VS Code 引き継ぎ → Cloud Review | ~5 min |
| 12 | [コンテキスト一貫性](act2-client-hybrid.md#-スライド-12コンテキスト一貫性--どこでも同じルール) | 同じリクエストを 3 サーフェスで実行 → Custom Instructions の一貫適用を証明 | ~3 min |

---

### 意図的なギャップ × サーフェス マッピング

| Gap | Cloud Demo（Act 1） | Client Demo（Act 2） |
|-----|---------------------|---------------------|
| ❌ ユニットテストなし | ✅ Slide 3/4: Issue → Agent → PR | — |
| ❌ 入力バリデーションなし | — | ✅ Slide 9: VS Code Agent Mode |
| ❌ Dockerfile なし | — | ✅ Slide 10: Copilot CLI |
| ❌ CI/CD ワークフローなし | — | ✅ Slide 11: Hybrid ワークフロー |

---

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
