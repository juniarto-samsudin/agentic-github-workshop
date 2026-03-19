---
layout: step
title: "Review — Automated Code Review and Fix Loops"
step_number: 4
estimated_minutes: 10
permalink: /chapter/06/
---

# Chapter 6: Review — Automated Code Review and Fix Loops

> **Key takeaway:** Copilot Code Review autonomously reviews PR diffs — not just style, but logic, test quality, and best practices — and the review→fix loop creates a continuous improvement cycle.

[← Chapter 5: Collaboration](chapter-05-collaboration.md) | [Back to Act 1](README.md) | [Next: Chapter 7 — Context →](chapter-07-context.md)

---

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Examine Copilot Code Review results on a Pull Request
- Understand the types of feedback Copilot provides (bugs, improvements, suggestions)
- Use the "Apply suggestion" feature to apply fixes as commits
- Trigger a review→fix→re-review loop by asking `@copilot` to address findings

## 📋 Prerequisites

- [Chapter 5](chapter-05-collaboration.md) completed — you have a PR with commits from the Coding Agent

## ⏱️ Estimated Time: ~10 minutes

---

## Exercise 1: Check Automatic Review Results

When a PR is opened, Copilot Code Review runs automatically — just like a human reviewer.

### Steps

1. Open the **PR** you've been working with (from Chapters 4–5).
2. Go to the **Conversation** tab.
3. Look for **Copilot** listed as a reviewer:
   - The 🤖 icon identifies Copilot in the reviewers list.
   - Note the review status — it will show **Changes requested** or **Commented**.
4. Read the **review summary** at the top of Copilot's review:
   - Copilot summarizes what it understood about the changes.
   - It lists the number of comments and their severity.

<details>
<summary>🎤 <strong>Instructor Note</strong></summary>

Point out that Copilot appears in exactly the same place as any human reviewer — no special UI or separate tool. This is important: the Agent integrates into existing PR review workflows, so there's nothing new to learn.

</details>

### ✅ Verification Checkpoint

- [ ] Copilot appears as a reviewer on the PR
- [ ] A review status is visible (Changes requested or Commented)
- [ ] A review summary is present

---

## Exercise 2: Examine Review Comments

Copilot doesn't just flag lint issues — it reads the code logic and provides context-aware feedback.

### Steps

1. Go to the **Files changed** tab on your PR.
2. Find Copilot's inline review comments on specific code lines.
3. Look for different types of feedback:

   **Bug reports** (⚠️):
   - Example: *"Database state is shared between tests — reset before each test for isolation"*
   - Example: *"Only the status code is checked; also validate the response body content"*

   **Improvement suggestions** (💡):
   - Example: *"Use `pytest.fixture` to share test setup across tests"*
   - Example: *"Make test names more specific (e.g., `test_create_todo` → `test_create_todo_with_valid_data_returns_201`)"*

4. Notice that each comment **references a specific code line** — this is not generic advice.

<details>
<summary>🎤 <strong>Instructor Note</strong></summary>

Emphasize the difference between Copilot's feedback and traditional linters. Copilot understands the *logic* of the code — it can identify that tests lack isolation, that assertions are incomplete, or that naming doesn't follow project conventions. This is the kind of feedback you'd expect from an experienced human reviewer.

</details>

### ✅ Verification Checkpoint

- [ ] At least one review comment points to a specific code issue
- [ ] Comments demonstrate understanding of test logic (not just syntax)
- [ ] You can distinguish between bug reports and improvement suggestions

---

## Exercise 3: Explore Code Suggestions

Beyond identifying problems, Copilot can propose concrete fixes as code diffs.

### Steps

1. In the **Files changed** tab, find a review comment that includes a **"Suggested change"** block.
2. Examine the suggestion:
   - It shows a diff format: the original code (red) and the proposed replacement (green).
   - The fix is specific to the exact lines being discussed.
3. Notice the **"Apply suggestion"** button:
   - Clicking it would apply the fix directly as a new commit on the PR branch.
   - This is a one-click fix — no local checkout needed.
4. **Don't apply it yet** — we'll use a different approach in Exercise 4.

<details>
<summary>🎤 <strong>Instructor Note</strong></summary>

The "Apply suggestion" button is useful for small, isolated fixes. For multiple changes, the approach in Exercise 4 (asking `@copilot` to fix everything) is more efficient. Make sure participants understand both options: manual one-at-a-time apply vs. automated batch fix.

</details>

### ✅ Verification Checkpoint

- [ ] You can see a suggested code change in diff format
- [ ] The "Apply suggestion" button is visible
- [ ] You understand the one-click apply mechanism

---

## Exercise 4: Trigger the Review → Fix Loop

This is where the 6-layer architecture comes full circle: the review layer feeds back into the execution layer.

### Steps

1. Go to the **Conversation** tab of your PR.
2. Post a comment:

   > **@copilot Please fix all the issues raised in the code review.**

3. Wait for Copilot to respond. The Agent will:
   - Read all the review comments
   - Understand the requested fixes
   - Make code changes addressing the feedback
   - Push a new commit to the PR branch

4. Observe the loop in action:

   ```
   ┌──────────────┐     ┌───────────┐     ┌──────────────┐
   │    Review     │ ──→ │  @copilot  │ ──→ │  New Commit   │
   │  (findings)  │     │ fix request │     │   (fixes)     │
   └──────────────┘     └───────────┘     └──────────────┘
          ↑                                       │
          └───────────────────────────────────────┘
                    Re-review → Re-fix loop
   ```

5. Once the new commit appears, Copilot Code Review will automatically re-review the updated code — continuing the cycle.

<details>
<summary>🎤 <strong>Instructor Note</strong></summary>

This is the key "aha moment" of Act 1. The 6-layer architecture is not a linear pipeline — it's a cycle. Review feeds back to execution, execution produces new code for review. This is what makes the system *agentic*: continuous, autonomous improvement rather than one-shot generation.

Draw attention to the fact that no human intervention was required between the review findings and the fixes being committed.

</details>

### ✅ Verification Checkpoint

- [ ] Your `@copilot` comment was posted
- [ ] A new commit appears on the PR addressing review feedback
- [ ] You can see the review→fix→re-review cycle in the PR timeline

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Copilot Code Review didn't run automatically | Go to the PR's **Reviewers** section and manually request a review from **Copilot**. |
| Very few or no review comments | Less feedback means higher code quality — this is a positive signal. If you want more comments for demonstration, you can add intentionally imperfect code. |
| `@copilot` doesn't respond to the fix request | Wait 1–2 minutes — AI processing takes time. Check the PR timeline for any pending status indicators. |
| Copilot's suggestions don't match the project style | Custom Instructions (Chapter 7) will address this — Copilot learns team conventions when configured. |

---

## 📝 Recap

In this chapter, you:

- ✅ **Observed** automatic code review running on your PR
- ✅ **Examined** context-aware feedback that goes beyond lint — understanding test logic, isolation, and best practices
- ✅ **Explored** code suggestions with one-click apply capability
- ✅ **Triggered** the review→fix→re-review loop using `@copilot`

## 🔑 Key Concepts

| Concept | What It Means |
|---------|---------------|
| **Automatic Review** | Copilot Code Review runs when a PR is opened — no manual trigger needed |
| **Context-Aware Feedback** | Not just lint — Copilot understands code logic and provides substantive feedback |
| **Code Suggestions** | Copilot proposes concrete fixes as diffs with one-click apply |
| **Review → Execution Loop** | Findings → `@copilot` fix request → new commit → re-review |
| **6-Layer Cycles** | The architecture creates feedback loops, not linear pipelines — quality improves iteratively |

---

**Next up:** In [Chapter 7](chapter-07-context.md), you'll explore how Custom Instructions shape the Agent's behavior to match your team's coding standards.
