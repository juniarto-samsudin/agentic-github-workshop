---
layout: workshop
title: "Agentic GitHub Workshop"
permalink: /
---

## 🎯 Workshop Overview

Master **GitHub Copilot's 6-layer agentic architecture** through hands-on exercises across three surfaces — GitHub.com, VS Code, and Copilot CLI. You'll work with a deliberately incomplete FastAPI Todo API and watch Copilot autonomously fix gaps: adding tests, input validation, Docker support, and CI/CD pipelines.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/shinyay/agentic-github-workshop)

---

## 🏗️ 6-Layer Architecture

This workshop teaches Copilot's agentic capabilities as six nested layers, from user entry to enterprise governance:

```
┌─────────────────────────────────────────────┐
│  Layer 6: Governance (Mission Control)      │
│  ┌─────────────────────────────────────┐    │
│  │  Layer 5: Context (Custom Instr.)   │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  Layer 4: Review (Auto)     │    │    │
│  │  │  ┌─────────────────────┐    │    │    │
│  │  │  │  Layer 3: Collab    │    │    │    │
│  │  │  │  ┌─────────────┐    │    │    │    │
│  │  │  │  │ L2: Execute │    │    │    │    │
│  │  │  │  │ ┌─────────┐ │    │    │    │    │
│  │  │  │  │ │ L1:Entry │ │    │    │    │    │
│  │  │  │  │ └─────────┘ │    │    │    │    │
│  │  │  │  └─────────────┘    │    │    │    │
│  │  │  └─────────────────────┘    │    │    │
│  │  └─────────────────────────────┘    │    │
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

---

## 📚 Two-Act Structure

### ☁️ Act 1 — Cloud-Side: Agent Works *For* You (~60 min)

The Coding Agent runs **asynchronously on GitHub Actions**. You assign tasks via Issues, the Agent executes autonomously, and you review and steer via Pull Requests.

| Step | Chapter | Topic | Duration |
|------|---------|-------|----------|
| 1 | [Chapter 3: Entry](/chapter/03/) | Chat → Understand codebase → Create Issue → Assign Agent | ~10 min |
| 2 | [Chapter 4: Execution](/chapter/04/) | Observe Actions workflow → Read session logs → Review PR | ~10 min |
| 3 | [Chapter 5: Collaboration](/chapter/05/) | Post @copilot comments → Request edge cases → See commits | ~10 min |
| 4 | [Chapter 6: Review](/chapter/06/) | Examine auto code review → Apply suggestions → Fix loops | ~10 min |
| 5 | [Chapter 7: Context](/chapter/07/) | Custom Instructions → Verify compliance → Explore Spaces | ~10 min |
| 6 | [Chapter 8: Governance](/chapter/08/) | Mission Control → Monitor tasks → Steer running agents | ~10 min |

### 💻 Act 2 — Client-Side & Hybrid: Agent Works *With* You (~50 min)

The Agent works **interactively in real-time** via VS Code and Copilot CLI. Immediate feedback, local testing, and precise control.

| Step | Chapter | Topic | Duration |
|------|---------|-------|----------|
| 7 | [Chapter 9: VS Code Agent Mode](/chapter/09/) | @workspace analysis → Agent Mode → Add validation → Accept/Reject | ~15 min |
| 8 | [Chapter 10: Copilot CLI](/chapter/10/) | CLI project analysis → Generate Dockerfile → docker-compose → Build | ~12 min |
| 9 | [Chapter 11: Hybrid Workflow](/chapter/11/) | CLI → Cloud Agent → Mission Control → VS Code → Code Review | ~15 min |
| 10 | [Chapter 12: Context Consistency](/chapter/12/) | Same request × 3 surfaces → Compare outputs → Verify consistency | ~10 min |

---

## 🧩 The Demo Application

A **deliberately incomplete** FastAPI Todo API — Copilot fills the gaps during the workshop:

| Intentional Gap | Fixed In | Copilot Surface |
|----------------|----------|-----------------|
| ❌ No unit tests | Chapters 3–4 | ☁️ Cloud Coding Agent |
| ❌ No input validation | Chapter 9 | 💻 VS Code Agent Mode |
| ❌ No Dockerfile | Chapter 10 | 🖥️ Copilot CLI |
| ❌ No CI/CD pipeline | Chapter 11 | 🔄 Hybrid Workflow |

---

## 🛤️ Learning Paths

Choose your path based on interest and time:

| Path | Chapters | Duration | Focus |
|------|----------|----------|-------|
| **🚀 Quick Start** | 3 → 4 → 9 | ~35 min | Core Cloud + VS Code experience |
| **☁️ Cloud Deep Dive** | 3 → 4 → 5 → 6 → 7 → 8 | ~60 min | Full autonomous agent lifecycle |
| **💻 Client Mastery** | 9 → 10 → 11 | ~42 min | VS Code + CLI + hybrid relay |
| **🏆 Complete Workshop** | All (3–12) | ~110 min | Full 6-layer architecture mastery |

---

## 📖 Supplementary Resources

- [Workshop Architecture Guide](/workshop-guide/) — Detailed 6-layer architecture explanation and surface mapping
- [Act 1 Overview](/act1-overview/) — Cloud-side asynchronous Agent execution concepts
- [Act 2 Overview](/act2-overview/) — Client-side interactive and hybrid workflow concepts
