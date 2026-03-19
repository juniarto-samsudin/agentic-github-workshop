# Agentic GitHub Copilot — Workshop Guide

> Chapter-by-chapter hands-on exercises exploring the 6-layer agentic architecture across Cloud, VS Code, and CLI surfaces.

---

## Workshop Overview

This workshop walks you through each layer of Copilot's agentic architecture — from simple chat interactions to full governance controls — using a real codebase as your playground.

### Demo Application

The workshop uses a **Python FastAPI Todo API** with basic CRUD operations:

```
app/
├── main.py          # FastAPI route handlers (5 endpoints)
├── models.py        # Pydantic schemas (TodoCreate / TodoUpdate / Todo)
└── database.py      # In-memory storage (dict-based)
requirements.txt     # fastapi, uvicorn, pydantic
```

### Intentional Gaps

The codebase ships with deliberate gaps that you will fix throughout the workshop using Copilot's agentic capabilities:

| Gap | Fixed In |
|-----|----------|
| ❌ No unit tests | Ch 3 / 4 (Cloud — Entry & Execution) |
| ❌ No input validation | Ch 9 (VS Code Agent Mode) |
| ❌ No Dockerfile | Ch 10 (Copilot CLI) |
| ❌ No CI/CD workflow | Ch 11 (Hybrid Workflow) |

---

## 6-Layer Architecture

```
┌─────────────────────────────────────────────────┐
│                  GOVERNANCE                       │
│          Mission Control · Policies               │
│  ┌─────────────────────────────────────────────┐ │
│  │               CONTEXT                        │ │
│  │    Custom Instructions · Spaces              │ │
│  │  ┌────────────────────────────────────────┐  │ │
│  │  │             REVIEW                      │  │ │
│  │  │      Copilot Code Review                │  │ │
│  │  │  ┌─────────────────────────────────┐    │  │ │
│  │  │  │         COLLABORATION             │    │  │ │
│  │  │  │    PR Comments · @copilot          │    │  │ │
│  │  │  │  ┌──────────────────────────┐     │    │  │ │
│  │  │  │  │       EXECUTION           │     │    │  │ │
│  │  │  │  │  Coding Agent · Actions    │     │    │  │ │
│  │  │  │  │  ┌───────────────────┐    │     │    │  │ │
│  │  │  │  │  │     ENTRY          │    │     │    │  │ │
│  │  │  │  │  │  Chat · Issues     │    │     │    │  │ │
│  │  │  │  │  └───────────────────┘    │     │    │  │ │
│  │  │  │  └──────────────────────────┘     │    │  │ │
│  │  │  └─────────────────────────────────┘    │  │ │
│  │  └────────────────────────────────────────┘  │ │
│  └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

---

## Two-Act Structure

### Act 1 — ☁️ Cloud-Side: Agent Works *For* You

The agent runs asynchronously on GitHub Actions, working on your behalf. You create issues, assign Copilot, and review the results — the agent handles the coding autonomously.

| Chapter | Theme | What You'll Practice | Est. Time |
|---------|-------|---------------------|-----------|
| 3 | [Entry](act1-cloud/chapter-03-entry.md) | Chat → discover gaps → Issue → assign Copilot | ~10 min |
| 4 | [Execution](act1-cloud/chapter-04-execution.md) | Observe Agent on Actions → session log → PR review | ~10 min |
| 5 | [Collaboration](act1-cloud/chapter-05-collaboration.md) | @copilot on PR → edge case requests → iteration | ~10 min |
| 6 | [Review](act1-cloud/chapter-06-review.md) | Auto code review → suggestions → fix loop | ~10 min |
| 7 | [Context](act1-cloud/chapter-07-context.md) | Custom Instructions → verify compliance → Spaces | ~10 min |
| 8 | [Governance](act1-cloud/chapter-08-governance.md) | Mission Control → steering → task management | ~10 min |

### Act 2 — 💻 Client-Side & Hybrid: Agent Works *With* You

The agent works alongside you in real-time with immediate feedback. You interact directly through VS Code Agent Mode and Copilot CLI, collaborating in a tight loop.

| Chapter | Theme | What You'll Practice | Est. Time |
|---------|-------|---------------------|-----------|
| 9 | [VS Code Agent Mode](act2-client-hybrid/chapter-09-vscode-agent.md) | Agent Mode → validation → Accept/Reject → test | ~15 min |
| 10 | [Copilot CLI](act2-client-hybrid/chapter-10-copilot-cli.md) | CLI → Dockerfile → build → test → commit | ~12 min |
| 11 | [Hybrid Workflow](act2-client-hybrid/chapter-11-hybrid-workflow.md) | CLI→Cloud→VS Code relay development | ~15 min |
| 12 | [Context Consistency](act2-client-hybrid/chapter-12-context-consistency.md) | Same request × 3 surfaces → consistent rules | ~10 min |

---

## Intentional Gaps × Surface Mapping

| Gap | Cloud (Act 1) | Client (Act 2) |
|-----|--------------|----------------|
| ❌ No unit tests | ✅ Ch 3/4: Issue → Agent → PR | — |
| ❌ No input validation | — | ✅ Ch 9: VS Code Agent Mode |
| ❌ No Dockerfile | — | ✅ Ch 10: Copilot CLI |
| ❌ No CI/CD workflow | — | ✅ Ch 11: Hybrid Workflow |

---

## 6-Layer × 3-Surface Mapping

| Layer | Cloud (Act 1) | VS Code (Act 2) | CLI (Act 2) |
|-------|--------------|-----------------|-------------|
| **Entry** | Chat → Issue | @workspace → Agent Mode | CLI analysis → gh issue |
| **Execution** | Actions (Coding Agent) | Agent Mode (interactive) | CLI Agentic Mode |
| **Collaboration** | PR comments @copilot | VS Code PR comments | — |
| **Review** | Copilot Code Review | VS Code Review | — |
| **Context** | Custom Instructions / Spaces | Same Instructions apply | Same Instructions apply |
| **Governance** | Mission Control | "Open in VS Code" handoff | CLI task status check |

---

## Preparation Checklist

### Environment

- [ ] VS Code Insiders installed with Copilot extension enabled
- [ ] Copilot CLI installed (`copilot --version` to verify)
- [ ] Repository cloned locally
- [ ] Python 3.11+ installed
- [ ] `pip install -r requirements.txt` done
- [ ] Docker installed (Chapter 10)
- [ ] `gh` CLI installed and authenticated (Chapter 11)

### Before Starting

- [ ] Open repository in VS Code
- [ ] Open Copilot Chat panel
- [ ] Have 2+ terminals open
- [ ] Open GitHub.com repository page in browser
- [ ] Start Docker Desktop (Chapter 10)
