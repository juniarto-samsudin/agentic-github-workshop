# 💻 Act 2 — Client-Side & Hybrid: Agent Works *With* You

> In Act 2, you'll experience GitHub Copilot as an **interactive collaborator** that works alongside you in real-time. You'll use VS Code Agent Mode, Copilot CLI, and hybrid workflows that combine cloud and client capabilities.

[← Back to Workshop Overview](../README.md)

## 🎯 What You'll Learn

By completing Act 2, you will be able to:
- Use VS Code Agent Mode for interactive, multi-file code generation
- Use Copilot CLI for terminal-first development workflows
- Combine cloud and client tools in a relay development pattern
- Verify that Custom Instructions apply consistently across all surfaces

## How Act 2 Differs from Act 1

| | Act 1 (Cloud) | Act 2 (Client & Hybrid) |
|---|---|---|
| **Model** | Agent works *for* you, asynchronously | Agent works *with* you, in real-time |
| **Where** | GitHub.com / Actions | VS Code / Terminal / Hybrid |
| **Feedback** | Review results in PR | See results instantly in editor/terminal |
| **Best for** | Large tasks (full test suites, etc.) | Medium/small tasks, refactoring, DevOps |

## 📋 Prerequisites

Before starting Act 2, ensure you have:
- [ ] Completed the [Workshop Setup](../setup.md)
- [ ] VS Code (Insiders) open with the repository loaded
- [ ] Copilot Chat and Agent Mode available in VS Code
- [ ] Copilot CLI installed (`copilot --version`)
- [ ] Docker installed and running (Chapter 10)
- [ ] Familiarity with Act 1 concepts (recommended but not required)

## ⏱️ Estimated Total Time: ~50 minutes

## Chapters

| Chapter | Theme | What You'll Do | Time |
|---------|-------|---------------|------|
| 9 | [VS Code Agent Mode](chapter-09-vscode-agent.md) | @workspace analysis → Agent Mode → add validation → Accept/Reject → local test | ~15 min |
| 10 | [Copilot CLI](chapter-10-copilot-cli.md) | CLI analysis → generate Dockerfile → docker-compose → build & test → commit | ~12 min |
| 11 | [Hybrid Workflow](chapter-11-hybrid-workflow.md) | CLI→Cloud→Mission Control→VS Code relay → Code Review | ~15 min |
| 12 | [Context Consistency](chapter-12-context-consistency.md) | Same request across 3 surfaces → compare → verify consistency | ~10 min |

## Key Concept: Three Surfaces, One Experience

```
┌──────────────────────────────────────────────────────────────┐
│  GitHub.com Chat       VS Code Chat/Agent       Copilot CLI  │
│  ──────────────        ──────────────────       ──────────── │
│  Browser-based         Editor-integrated        Terminal-native│
│  Issue → Agent         Agent Mode → local       Natural lang → exec│
│  PR results            Instant in-editor        Instant in-terminal│
│  Managers & PMs        Daily development        DevOps & CLI lovers│
└──────────────────────────────────────────────────────────────┘
                              │
                    All share the same:
                    • Custom Instructions
                    • Repository context
                    • Copilot capabilities
```

## How Chapters Connect

- **Chapter 9** (VS Code Agent Mode) — Standalone exercise using VS Code
- **Chapter 10** (Copilot CLI) — Standalone exercise using the terminal
- **Chapter 11** (Hybrid) — Capstone that combines CLI, Cloud, and VS Code in one workflow
- **Chapter 12** (Context Consistency) — Proof exercise showing all 3 surfaces follow the same rules

> **Note:** Chapters 9 and 10 are independent and can be done in either order. Chapter 11 builds on concepts from both. Chapter 12 is best done last as a synthesis exercise.

---

**Ready to begin?** Start with [Chapter 9: VS Code Agent Mode →](chapter-09-vscode-agent.md)
