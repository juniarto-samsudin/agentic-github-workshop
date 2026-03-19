---
layout: step
title: "Context Consistency — Same Rules, Every Surface"
step_number: 10
estimated_minutes: 10
permalink: /chapter/12/
---

# Chapter 12: Context Consistency — Same Rules, Every Surface

> **Key takeaway:** Custom Instructions defined in a single file are automatically applied across GitHub.com Chat, VS Code, and Copilot CLI — ensuring consistent code quality regardless of which tool developers prefer.

**Navigation:** [← Chapter 11: Hybrid Workflow](chapter-11-hybrid-workflow.md) | [Back to Act 2](README.md)

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Send the same code generation request across 3 different Copilot surfaces
- Compare outputs to verify Custom Instructions are consistently applied
- Understand the enterprise implications of consistent tooling standards

## Prerequisites

- [ ] Access to GitHub.com Copilot Chat (in your repository)
- [ ] VS Code with GitHub Copilot Chat extension
- [ ] Copilot CLI installed and authenticated
- [ ] Custom Instructions file (`.github/copilot-instructions.md`) committed to the repository

## Time Estimate

~10 minutes

---

## Overview

```
Send the same request to 3 surfaces  →  Compare outputs  →  Confirm consistency
         ↓                                    ↓                     ↓
GitHub.com / VS Code / CLI            Side-by-side view     Enterprise-grade quality
```

The goal of this chapter is to prove — hands-on — that Custom Instructions are not limited to a single tool. One file controls code generation behavior everywhere Copilot operates.

---

## Exercise 1: Send the Same Request to 3 Surfaces

Use this **exact** request on all three surfaces:

> **"Write a search endpoint for /todos that filters todos by keyword"**

### Surface A: GitHub.com Chat

1. Open your repository on GitHub.com
2. Open Copilot Chat (click the Copilot icon)
3. Paste the request exactly as written above
4. Copy and save the generated code (you will compare it later)

### Surface B: VS Code Chat

1. Open the repository in VS Code
2. Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`)
3. Paste the same request
4. Copy and save the generated code

### Surface C: Copilot CLI

1. Open a terminal in the repository root
2. Send the same request to Copilot CLI
3. Copy and save the generated code

<details>
<summary>💡 Instructor Note</summary>

If running this live, prepare all 3 surfaces in advance so you can switch quickly. The key moment is the side-by-side comparison — spend your time there, not on setup.

If participants only have access to 2 of the 3 surfaces, that is sufficient to demonstrate the concept.

</details>

### ✅ Verification

- [ ] You have code output saved from all 3 surfaces for the same request

---

## Exercise 2: Compare Outputs Side by Side

Place the 3 outputs side by side. VS Code split view works well for this.

### Comparison Checklist

Check each Custom Instructions rule across all surfaces:

| Rule | GitHub.com | VS Code | CLI |
|------|-----------|---------|-----|
| Google-style docstring (with sections) | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| Example section in docstring | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| Pagination parameters (`skip`, `limit`) | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| `limit` default = 20 | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| Type hints on all functions | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| `X \| None` format (not `Optional[X]`) | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |
| `response_model` specified on endpoint | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ |

### Why These Rules Matter

None of these rules exist in the current `app/` code. The **only** way they appear in generated output is if Copilot is reading and applying the Custom Instructions file. Each checkmark is direct proof that `.github/copilot-instructions.md` is working on that surface.

<details>
<summary>💡 Instructor Note</summary>

Emphasize: "The exact code will differ — AI is non-deterministic, so wording and variable names may vary. But the **structural rules** from Custom Instructions should be consistent. Focus on whether the rules are present, not whether the code is identical."

If a rule appears on 2 out of 3 surfaces, that still demonstrates the mechanism. AI generation has some variance, so occasional misses are expected.

</details>

### ✅ Verification

- [ ] Custom Instructions rules appear consistently across all 3 surfaces
- [ ] You can identify which rules come from Custom Instructions (not from the existing codebase)

---

## Exercise 3: Reflect on Enterprise Implications

Consider what consistent Custom Instructions means at organization scale:

```
┌────────────────────────────────────────────────────┐
│          Custom Instructions Effect                 │
│                                                     │
│  Developer A (VS Code user)    → Same rules applied │
│  Developer B (CLI user)        → Same rules applied │
│  Developer C (GitHub.com user) → Same rules applied │
│  Coding Agent                  → Same rules applied │
│  Code Review                   → Same rules as base │
│                                                     │
│  Result: Consistent code style, reduced review cost │
└────────────────────────────────────────────────────┘
```

### Key Insights

Think through (or discuss with your group) these implications:

- **Write once, apply everywhere** — One file (`.github/copilot-instructions.md`) governs ALL Copilot interactions in the repository
- **Tool-independent compliance** — Developer tool preference doesn't affect code quality or style
- **Day-one productivity** — New team members produce compliant code from their first interaction with Copilot
- **Review cost reduction** — Code review shifts from style debates to logic discussions
- **Scalable governance** — Organization-level instructions can layer on top of repository-level ones

<details>
<summary>💡 Instructor Note</summary>

This is a good moment to connect to real-world experience: "Raise your hand if you've ever had a PR review that was mostly about style, not logic." Custom Instructions eliminate that entire category of review friction.

For enterprise audiences, emphasize the governance angle: security teams can mandate patterns (e.g., input validation, error handling format) that are automatically applied regardless of which developer or tool generates the code.

</details>

### ✅ Verification

- [ ] You understand how a single configuration file creates consistency across tools and team members
- [ ] You can explain why Custom Instructions rules appearing in generated code proves they are being applied (since those rules don't exist in the current codebase)

---

## Troubleshooting

<details>
<summary>Not enough time for all 3 surfaces</summary>

Compare just GitHub.com Chat and VS Code Chat — these two are sufficient to prove cross-surface consistency. Mention that CLI also applies the same rules.

</details>

<details>
<summary>Outputs aren't identical</summary>

This is expected! AI outputs vary in exact code, variable names, and wording. Focus on **structural rules**: Are Google-style docstrings present? Are pagination parameters included? Are type hints applied? The rules should be consistent even when the exact code differs.

</details>

<details>
<summary>One surface doesn't apply some rules</summary>

This occasionally happens due to AI variance. Note which rules **are** applied — even partial application demonstrates that Custom Instructions are being read. If most rules appear on most surfaces, the mechanism is working. Try regenerating the response on the surface that missed rules.

</details>

<details>
<summary>Custom Instructions not applied on any surface</summary>

Verify the file exists at `.github/copilot-instructions.md` in the repository's default branch. The file must be committed and pushed — local uncommitted changes won't be picked up by GitHub.com Chat. Run:

```bash
git log --oneline -1 -- .github/copilot-instructions.md
```

If no commits appear, the file hasn't been pushed yet.

</details>

---

## Recap

✅ Verified that Custom Instructions produce consistent results across GitHub.com, VS Code, and CLI surfaces by sending the same request and comparing outputs.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Write once, apply everywhere** | `.github/copilot-instructions.md` — one file covers all Copilot surfaces |
| **Tool-independent** | Developer choice of IDE, CLI, or web doesn't affect rule compliance |
| **Team standards automation** | Rules are managed per-repository, applied per-interaction |
| **Review cost reduction** | Style is handled automatically; reviews focus on logic and correctness |
| **Onboarding acceleration** | New members generate compliant code from day one |

---

**Navigation:** [← Chapter 11: Hybrid Workflow](chapter-11-hybrid-workflow.md) | [Back to Act 2](README.md)
