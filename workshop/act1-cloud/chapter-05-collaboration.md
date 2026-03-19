---
layout: step
title: "Collaboration — Human ↔ Agent Dialogue on Pull Requests"
step_number: 3
estimated_minutes: 10
permalink: /chapter/05/
---

# Chapter 5: Collaboration — Human ↔ Agent Dialogue on Pull Requests

> **Key takeaway:** The PR is a collaboration hub where you and Copilot iterate — you provide direction, the Agent executes, and the entire conversation is preserved as history.

[← Chapter 4](chapter-04-execution.md) | [Back to Act 1](README.md) | [Next: Chapter 6 →](chapter-06-review.md)

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Post `@copilot` comments on a PR to request changes
- [ ] Observe how the Agent adds commits in response to feedback
- [ ] Understand the human ↔ Agent iteration cycle visible in the PR timeline

## 📋 Prerequisites

- [ ] Completed [Chapter 4](chapter-04-execution.md) — A PR created by the Coding Agent exists

## ⏱️ Estimated Time: ~10 minutes

---

## Overall Flow

```
PR is open from Ch.4 → Post @copilot feedback → Copilot adds commits → Confirm iteration
        ↓                       ↓                        ↓                      ↓
  Open the PR            Request edge cases        New commit pushed      Visible in timeline
```

---

## Exercise 1: Request Edge Cases via @copilot

### Background

You interact with the Coding Agent the same way you'd interact with a human teammate — by posting comments on the PR. No special tools or UI required. The `@copilot` mention tells the Agent to pick up your feedback and act on it.

### Instructions

1. Open the **PR created by Copilot** in Chapter 4
2. Go to the **Conversation** tab
3. In the comment box, type the following and click **Comment**:

   > **@copilot Please add edge case tests for the following scenarios:**
   > - **Empty string title on POST**
   > - **Very long title (1000+ characters)**
   > - **PUT with a non-existent ID returning 404**
   > - **Deleting the same todo twice**

4. Submit the comment

### ✅ Verification

- [ ] Your comment is posted on the PR and mentions `@copilot`
- [ ] Copilot acknowledges the comment (a reaction or initial reply appears)

<details>
<summary>💡 Instructor Notes</summary>

"This is exactly the same experience as a normal code review. You post a comment on the PR mentioning `@copilot`, and it picks up the feedback. No special tools, no new UI — just the PR comment box you already use every day."

Emphasize the key point: **existing workflow integration**. Participants don't need to learn anything new — if they've reviewed a PR before, they already know how to collaborate with the Agent.

</details>

---

## Exercise 2: Review the Agent's Response

### Background

When the Agent receives your feedback, it reads your comment, plans the changes, and pushes a new commit to the same PR branch. This is the same additive pattern a human collaborator would follow — no force-pushes, no rewriting history.

### Instructions

1. Wait for Copilot to respond (typically 1–2 minutes):
   - 💬 A reply comment (e.g., "I'll add those edge case tests")
   - ✍️ A new commit pushed to the PR branch

2. Open the **Commits** tab on the PR:
   - **First commit:** The original tests created in Chapter 4
   - **New commit:** Edge case tests added in response to your feedback

3. Open the **Files changed** tab and review the diff:
   - New test functions have been added
   - Existing tests remain unchanged (safe, additive change)

### ✅ Verification

- [ ] A new commit has been added to the PR
- [ ] New test functions exist for the edge cases you requested
- [ ] Existing test functions from Chapter 4 are untouched

<details>
<summary>💡 Instructor Notes</summary>

"Copilot understood the request and added exactly what was needed — nothing more, nothing less. Notice that the existing tests are completely untouched. The Agent makes safe, additive changes, just like a careful human collaborator would."

Point out in the diff:
- New test functions for empty title, long title, non-existent ID, and double-delete
- The original test functions from Chapter 4 remain unmodified
- AI output may vary in details, but the intent should be captured

</details>

---

## Exercise 3: Trace the Collaboration Timeline

### Background

One of the most powerful aspects of PR-based collaboration is the **complete audit trail**. Every interaction between you and the Agent is recorded in the PR timeline — who said what, when, and what changed as a result.

### Instructions

1. Go back to the **Conversation** tab on the PR
2. Scroll through the full timeline from top to bottom and observe the flow:

   ```
   [Copilot]  Creates PR (tests from Chapter 4)
       ↓
   [You]      @copilot — "Add edge case tests for..."
       ↓
   [Copilot]  Responds + pushes new commit
       ↓
   [You]      Review → approve → merge (Chapter 6)
   ```

3. Note that the **entire dialogue** is preserved — anyone on the team can see exactly how the code evolved and why

### ✅ Verification

- [ ] The PR timeline shows the full conversation: Copilot's initial PR → your feedback → Copilot's response and commit
- [ ] You can trace every change back to a specific request
- [ ] The collaboration history is visible to any team member who opens this PR

<details>
<summary>💡 Instructor Notes</summary>

"The PR has become a collaboration hub. The human sets the direction, the Agent executes, and this cycle can repeat as many times as needed. Most importantly — every single interaction is preserved as history. There's no hidden chat window, no ephemeral conversation. It's all right here in the PR timeline."

This is the key message of the chapter: **the feedback loop is visible, repeatable, and auditable**. Compare this to pair programming where the conversation is lost — here, the full reasoning chain is preserved.

</details>

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Copilot doesn't respond to your comment | Wait 1–2 minutes — response time varies depending on load. Ensure you typed `@copilot` (not `@Copilot` or `copilot`) |
| Response doesn't exactly match your request | AI output varies between runs. Check if the **intent** was captured even if the specific details differ |
| No new commit appears | Check if Copilot posted a text-only response first. It may take another minute to push the commit after replying |
| Copilot says it can't make the changes | The Agent may hit edge cases with certain repo configurations. Review its response for details and try rephrasing the request |

> **Tip:** If the Agent is slow to respond, you can continue to [Chapter 6](chapter-06-review.md) and come back to verify the results later. The commit will be added to the PR whenever the Agent finishes.

---

## 📝 Chapter Recap

In this chapter, you:
- Posted a `@copilot` comment on the PR to **request edge case tests**
- Observed the Agent **respond with a new commit** — additive, non-destructive changes
- Traced the **full collaboration timeline** showing the human ↔ Agent iteration cycle

### Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Existing workflow integration** | PR comments are the interface — no new tools to learn |
| **Iterative refinement** | Feedback → Agent action → review, repeatable as many times as needed |
| **Safe additive changes** | Agent adds to the codebase without modifying existing code |
| **Complete audit trail** | Every interaction is recorded in the PR timeline |
| **Human retains control** | The Agent executes, but you decide the direction and approve the results |

---

**Next:** [Chapter 6: Review →](chapter-06-review.md) — Explore Copilot Code Review and the review → fix loop.
