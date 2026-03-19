# Agentic GitHub Copilot Workshop

> Hands-on workshop to master GitHub Copilot's agentic capabilities across Cloud, VS Code, and CLI.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## 🎯 What You'll Learn

This workshop guides you through GitHub Copilot's **6-layer agentic architecture** using a real FastAPI Todo API as your playground:

| Layer | What It Does | You'll Practice |
|-------|-------------|----------------|
| **Entry** | Start tasks via Chat or Issues | Chat → Issue → Agent trigger |
| **Execution** | Agent runs autonomously on Actions | Observe Agent's reasoning and output |
| **Collaboration** | Human ↔ Agent dialogue on PRs | @copilot feedback loops |
| **Review** | Automated code review | Review → fix → re-review cycles |
| **Context** | Custom Instructions & Spaces | Configure team-wide coding standards |
| **Governance** | Mission Control for Agent oversight | Real-time monitoring and steering |

## 📋 Prerequisites

- **GitHub account** with Copilot access (Copilot Business or Enterprise)
- **Python 3.11+** and **pip**
- **VS Code** (or VS Code Insiders) with GitHub Copilot extension
- **Copilot CLI** installed (`copilot --version`)
- **GitHub CLI** (`gh`) installed and authenticated
- **Docker** (for Chapter 10)
- **Git** configured with push access to a fork of this repo

## 🚀 Quick Setup

1. **Fork and clone** this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify the API runs:
   ```bash
   uvicorn app.main:app --reload
   # Open http://localhost:8000/docs
   ```

## 📚 Workshop Structure

The workshop is divided into two acts, covering 10 chapters (~2 hours total):

### Act 1 — ☁️ Cloud-Side: Agent Works *For* You

> Chapters 3–8 · ~60 minutes · GitHub.com & Actions

The Agent runs asynchronously in the cloud, working on your behalf while you observe and steer.

| Chapter | Theme | What You'll Do | Time |
|---------|-------|---------------|------|
| 3 | [Entry](workshop/act1-cloud/chapter-03-entry.md) | Chat → discover gaps → create Issue → assign Copilot | ~10 min |
| 4 | [Execution](workshop/act1-cloud/chapter-04-execution.md) | Observe Agent on Actions → read session log → review PR | ~10 min |
| 5 | [Collaboration](workshop/act1-cloud/chapter-05-collaboration.md) | @copilot on PR → request edge cases → iterative refinement | ~10 min |
| 6 | [Review](workshop/act1-cloud/chapter-06-review.md) | Auto code review → suggestions → review→fix loop | ~10 min |
| 7 | [Context](workshop/act1-cloud/chapter-07-context.md) | Custom Instructions → verify compliance → Spaces | ~10 min |
| 8 | [Governance](workshop/act1-cloud/chapter-08-governance.md) | Mission Control → real-time steering → task management | ~10 min |

### Act 2 — 💻 Client-Side & Hybrid: Agent Works *With* You

> Chapters 9–12 · ~50 minutes · VS Code, CLI, and cross-surface workflows

The Agent works alongside you in real-time, with immediate feedback and interactive control.

| Chapter | Theme | What You'll Do | Time |
|---------|-------|---------------|------|
| 9 | [VS Code Agent Mode](workshop/act2-client-hybrid/chapter-09-vscode-agent.md) | Agent Mode → add validation → Accept/Reject → local test | ~15 min |
| 10 | [Copilot CLI](workshop/act2-client-hybrid/chapter-10-copilot-cli.md) | CLI → Dockerfile → docker-compose → build → commit | ~12 min |
| 11 | [Hybrid Workflow](workshop/act2-client-hybrid/chapter-11-hybrid-workflow.md) | CLI→Cloud→Mission Control→VS Code relay development | ~15 min |
| 12 | [Context Consistency](workshop/act2-client-hybrid/chapter-12-context-consistency.md) | Same request × 3 surfaces → verify consistent rules | ~10 min |

## 🏗️ The Demo Application

A deliberately simple **Todo API** built with FastAPI — your workshop playground:

```
app/
├── main.py       # FastAPI routes (5 CRUD endpoints)
├── models.py     # Pydantic schemas (TodoCreate, TodoUpdate, Todo)
└── database.py   # In-memory dict storage
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/todos` | List all todos |
| `GET` | `/todos/{id}` | Get a specific todo |
| `POST` | `/todos` | Create a new todo |
| `PUT` | `/todos/{id}` | Update a todo |
| `DELETE` | `/todos/{id}` | Delete a todo |

### Intentional Gaps (What Copilot Will Fix)

| Gap | Fixed In |
|-----|----------|
| ❌ No unit tests | Chapters 3–4 (Cloud Agent) |
| ❌ No input validation | Chapter 9 (VS Code Agent Mode) |
| ❌ No Dockerfile | Chapter 10 (Copilot CLI) |
| ❌ No CI/CD pipeline | Chapter 11 (Hybrid Workflow) |

## 📎 Solution References

These branches were created by Copilot during previous workshop runs and serve as reference solutions:

| Branch | Contains |
|--------|----------|
| `copilot/add-pytest-unit-tests` | Full test suite + CI workflow + Custom Instructions compliance |
| `copilot/add-unit-tests-todo-api` | Alternative test implementation |
| `copilot/explain-codebase-structure` | Codebase analysis output |

## ❓ FAQ

**Q: Do I need Copilot Business/Enterprise?**
A: Yes. The Coding Agent (cloud-side execution) requires Copilot Business or Enterprise. VS Code Agent Mode and Copilot CLI work with any Copilot plan.

**Q: Can I do the chapters out of order?**
A: Within each Act, chapters build on each other (especially Act 1 chapters 3→4→5→6). Act 2 chapters are more independent. We recommend following the order on your first run.

**Q: What if Copilot generates different code than expected?**
A: That's normal! AI outputs vary between runs. Focus on whether the *structural rules* (from Custom Instructions) are applied, not the exact code.

## 📄 License

Released under the [MIT License](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## Author

- GitHub: [@shinyay](https://github.com/shinyay)
