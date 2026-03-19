---
layout: default
title: "Act 1 — Cloud-Side: Agent Works For You"
permalink: /act1-overview/
---

# ☁️ Act 1 — Cloud-Side: Agent Works *For* You

> In Act 1, you'll experience GitHub Copilot as an **autonomous agent** that works asynchronously on your behalf. You'll assign tasks via Issues, and the Agent will plan, code, test, and deliver results as Pull Requests — all running on GitHub Actions.

[← Back to Workshop Overview](../README.md)

## 🎯 What You'll Learn

By completing Act 1, you will be able to:
- Use Copilot Chat to understand codebases and create Issues
- Trigger the Coding Agent by assigning Copilot to an Issue
- Collaborate with the Agent through PR comments
- Understand how Copilot Code Review works
- Configure Custom Instructions to enforce team standards
- Monitor and steer Agent tasks through Mission Control

## 📋 Prerequisites

Before starting Act 1, ensure you have:
- [ ] Completed the [Workshop Setup](../setup.md)
- [ ] Access to a GitHub repository with Copilot enabled
- [ ] A browser open to your repository on GitHub.com

## ⏱️ Estimated Total Time: ~60 minutes

## Chapters

| Chapter | Theme | What You'll Do | Time |
|---------|-------|---------------|------|
| 3 | [Entry](chapter-03-entry.md) | Chat with Copilot → discover gaps → create Issue → assign Copilot as agent | ~10 min |
| 4 | [Execution](chapter-04-execution.md) | Observe the Agent on Actions → read session log → review the completed PR | ~10 min |
| 5 | [Collaboration](chapter-05-collaboration.md) | Post @copilot comments on the PR → request edge cases → see iterative commits | ~10 min |
| 6 | [Review](chapter-06-review.md) | Examine auto code review → explore suggestions → trigger review→fix loop | ~10 min |
| 7 | [Context](chapter-07-context.md) | Examine Custom Instructions → verify compliance → explore Agents & Spaces | ~10 min |
| 8 | [Governance](chapter-08-governance.md) | Open Mission Control → monitor tasks → steer a running Agent → explore launch methods | ~10 min |

## Key Concept: Asynchronous Autonomous Execution

```
You (Issue)  ──→  Coding Agent (Actions)  ──→  Pull Request
    │                    │                         │
    │              Plans, codes,                    │
    │              tests, commits               You review,
    │                    │                    comment, merge
    └────────────────────┴─────────────────────────┘
                  Feedback loop via PR
```

The Agent runs on GitHub Actions runners — no new infrastructure needed. Your existing Actions policies, secrets, and runner configurations all apply.

## How Chapters Connect

```
Chapter 3 (Entry)
    │  Creates Issue, assigns Copilot
    ▼
Chapter 4 (Execution)
    │  Agent runs, creates PR
    ▼
Chapter 5 (Collaboration)
    │  You refine the PR with @copilot
    ▼
Chapter 6 (Review)
    │  Code Review provides feedback
    ▼
Chapter 7 (Context)
    │  Understanding WHY the Agent followed your rules
    ▼
Chapter 8 (Governance)
       Monitoring and steering all of the above
```

> **Note:** Chapters 3→4→5→6 form a continuous flow using the same PR. Chapters 7 and 8 can be done somewhat independently, but are best experienced after 3–6.

---

**Ready to begin?** Start with [Chapter 3: Entry →](chapter-03-entry.md)
