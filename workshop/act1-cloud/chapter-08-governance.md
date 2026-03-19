# Chapter 8: Governance — Mission Control and Agent Oversight

> **Key takeaway:** Mission Control is your command center for all Agent tasks — monitor progress, steer running Agents in real-time, and maintain full visibility across all autonomous work.

| | |
|---|---|
| **Navigation** | [← Chapter 7: Context](chapter-07-context.md) · [Back to Act 1](README.md) · [Next: Act 2 →](../act2-client-hybrid/README.md) |

---

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- **Navigate Mission Control** to view all Agent tasks in one dashboard
- **Explore the task detail view** — session log, overview, and files changed in a single screen
- **Send real-time instructions** to a running Agent (steering)
- **Identify multiple launch methods** for Agent tasks (Issue, Chat, Mission Control, Mobile)

## 📋 Prerequisites

| Requirement | How to Verify |
|---|---|
| Chapters 3–7 completed | Tasks from earlier chapters should appear in Mission Control |
| Browser open to GitHub.com | You'll navigate to `github.com/copilot` |

## ⏱️ Estimated Time: ~10 minutes

---

## Workshop Flow

```
Open Mission Control  →  Review task list  →  Explore task detail  →  Real-time steering  →  Discover launch methods
        ↓                       ↓                     ↓                      ↓                        ↓
 github.com/copilot      All task statuses     Single-screen view     Instruct running Agent    Issue / Chat / Mobile
```

---

## Exercise 1: View Task List in Mission Control

### What You'll Do

Open Mission Control and review the centralized task dashboard — the single place where all Agent tasks are visible.

### Steps

1. **Navigate to Mission Control:**
   - Go to **[github.com/copilot](https://github.com/copilot)**
   - Alternatively: click the **Copilot icon** in the top navigation bar → select the task view

2. **Review the task list:**
   - Tasks from today's workshop should be visible:
     - 📋 The Issue from Chapter 3 (unit tests) → check its status
     - 📋 The Issue from Chapter 7 (Custom Agent / Spaces) → check its status
   - Each task displays a quick-link to its associated PR

3. **Understand the status indicators:**

   | Status | Meaning |
   |--------|---------|
   | 🟡 **In progress** | Agent is currently executing |
   | ✅ **Completed** | Agent has created a PR |
   | 🔴 **Needs input** | Agent is waiting for your feedback |

<details>
<summary>💡 <strong>Instructor Note: Setting the Scene</strong></summary>

> **Key message:** *"Mission Control is the control tower for Agent tasks. Even when running multiple tasks simultaneously, you get a bird's-eye view of everything here. Which tasks are in progress, which ones are waiting for human input — it's all visible at a glance."*
>
> If participants don't see any tasks yet, reassure them that tasks may take a few minutes to appear after creation. Have them refresh the page.

</details>

### ✅ Verification Checkpoint

- [ ] You can see Mission Control at `github.com/copilot`
- [ ] At least one task from previous chapters is visible in the list
- [ ] You can identify the status of each task (In progress / Completed / Needs input)

---

## Exercise 2: Explore Task Detail View

### What You'll Do

Click into a task to experience the unified detail view — session log, overview, and code diff all on one screen with no page-hopping.

### Steps

1. **Click any task** in the list to open its detail view

2. **Observe the unified interface:**

   **Left panel — Session Log:**
   - Which files the Agent read
   - What decisions it made
   - Commit reasoning displayed in real-time

   **Right panel — Tabs:**
   - **Overview** — Task summary, progress status, link to the created PR
   - **Files changed** — Full diff of all files the Agent modified

3. **Appreciate the single-screen design:**
   - ✅ All information visible without navigating away
   - ✅ Session log and code changes side-by-side
   - ✅ Agent's reasoning is shown in context with the code

<details>
<summary>💡 <strong>Instructor Note: Before vs. After</strong></summary>

> **Key message:** *"Previously, you had to hop between Issue → Actions → PR → Files changed to piece together what happened. Mission Control consolidates everything into one screen — the Agent's thinking process and code changes are visible simultaneously."*
>
> Walk participants through each panel. Point out how the session log shows the Agent's "thought process" — this is observability in action.

</details>

### ✅ Verification Checkpoint

- [ ] You can see the session log on the left side of the task detail view
- [ ] You can switch between the **Overview** and **Files changed** tabs on the right
- [ ] You can read the Agent's reasoning alongside the code diff — all on one page

---

## Exercise 3: Real-Time Steering

### What You'll Do

Send instructions to a running Agent directly from Mission Control — no need to wait for a PR or post comments.

### Steps

1. **Find a running task:**
   - Look for a task with 🟡 **In progress** status
   - If no Agent is currently running, see the note below — you can still explore the interface

2. **Open the running task** and locate the **chat input** at the bottom of the session log

3. **Send a steering instruction:**

   > **"Make sure all test files include descriptive docstrings. Follow the Custom Instructions."**

4. **Observe the result:**
   - The Agent incorporates your instruction after completing its current tool call
   - The session log reflects the new instruction
   - Subsequent work aligns with your direction

5. **Bonus: Comment on code directly:**
   - Switch to the **Files changed** tab
   - Click on a specific line of code and add a comment
   - No need to navigate to the PR page — it works right here

> **💡 No running Agent?** That's fine! You can still see where the steering input would be. To try it live, create a new task using one of the methods in Exercise 4 (e.g., the `/task` command in Copilot Chat).

<details>
<summary>💡 <strong>Instructor Note: Real-Time Steering</strong></summary>

> **Key message:** *"This is real-time steering. You can redirect the Agent while it's actively working — no waiting for a PR. Previously, you had to post a PR comment with @copilot to communicate. In Mission Control, you chat directly with the Agent. Feedback is incorporated immediately."*
>
> If no Agent is currently running, demonstrate the input field and explain what would happen. Consider creating a quick task with `/task` to show the live experience.

</details>

### ✅ Verification Checkpoint

- [ ] You can locate the chat input for steering in the task detail view
- [ ] You understand that instructions are incorporated into the Agent's ongoing work
- [ ] You know you can comment on code in the **Files changed** tab without leaving Mission Control

---

## Exercise 4: Discover Task Launch Methods

### What You'll Do

Explore the multiple ways to start Agent tasks and learn about IDE handoff capabilities.

### Steps

1. **Locate the "New task" button** in Mission Control

2. **Review all launch methods:**

   | Method | Where | Notes |
   |--------|-------|-------|
   | **Issue Assignment** | Issue page → Assignees → Copilot | Used in Chapter 3 |
   | **Mission Control** | `github.com/copilot` → New task button | Direct creation from dashboard |
   | **Chat `/task` command** | Copilot Chat → type `/task` | Quick inline task creation |
   | **GitHub Mobile** | Mobile app → Task page | Start tasks on the go |

3. **Note the IDE handoff buttons:**
   - Look for **"Open in Codespaces"** and **"Open in VS Code"** on any task
   - These let you take over Agent work in your IDE at any point
   - The Agent's branch and changes are ready for you to continue

<details>
<summary>💡 <strong>Instructor Note: Governance = Flexibility + Control</strong></summary>

> **Key message:** *"Governance isn't just about restrictions. Being able to create tasks from anywhere and hand off work seamlessly — that flexibility is part of governance too. Administrators control policy, developers operate efficiently through Mission Control."*
>
> Emphasize that the IDE handoff is a powerful escape hatch — participants are never locked into the Agent's workflow. They can always take over manually.

</details>

### ✅ Verification Checkpoint

- [ ] You can identify at least **3 different ways** to launch an Agent task
- [ ] You know where the IDE handoff buttons are located (Codespaces / VS Code)
- [ ] You understand that you can start a task from Issue, Chat, Mission Control, or Mobile

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Tasks not visible in Mission Control | Tasks may take a few minutes to appear. Refresh the page. Try `github.com/copilot/agents` as an alternative URL. |
| No running Agent for real-time steering | Create a new task using the `/task` command in Copilot Chat to see the steering interface live. |
| Mission Control URL not working | Try these URLs: `github.com/copilot` or `github.com/copilot/agents`. The exact path may vary. |
| Task detail view looks different | The UI may have been updated. Look for session log on the left and tabs (Overview / Files changed) on the right. |
| IDE handoff buttons not visible | These appear on completed or in-progress tasks. Check that the Agent has created a branch. |

---

## 📝 Recap

In this chapter, you:

| What You Did | Why It Matters |
|---|---|
| **Opened Mission Control** | Centralized dashboard — see all Agent tasks at a glance |
| **Explored task detail view** | Single-screen visibility — session log + overview + code diff, no page-hopping |
| **Sent real-time steering instructions** | Redirect a running Agent instantly without waiting for a PR |
| **Discovered multiple launch methods** | Flexible entry points — Issue, Chat, Mission Control, Mobile |
| **Learned about IDE handoff** | Seamlessly transition from cloud Agent to local development anytime |

---

## 🔑 Key Concepts

| Concept | Description |
|---------|-------------|
| **Centralized Task Management** | All Agent tasks visible in Mission Control — status, progress, and PR links at a glance |
| **Real-Time Steering** | Send instructions to a running Agent immediately — no need to wait for PR creation |
| **Single-Screen Visibility** | Session log + Overview + Files changed in one view — eliminates page-hopping |
| **Flexible Launch Points** | Start Agent tasks from Issue, Chat, Mission Control, or GitHub Mobile |
| **IDE Handoff** | Take over Agent work in Codespaces or VS Code at any point |
| **Observability** | Track the Agent's thinking process in real-time through session logs |

---

## 🎉 Act 1 Complete!

You've completed all of Act 1 — Cloud-Side Agent workflows. You've experienced the full lifecycle:

```
Entry → Execution → Collaboration → Review → Context → Governance
  ↓         ↓            ↓            ↓         ↓          ↓
Create    Observe      Iterate      Quality   Customize   Oversee
 task      Agent       with PR      gates     behavior    everything
```

**[Continue to Act 2: Client-Side & Hybrid Workflows →](../act2-client-hybrid/README.md)**

---

| | |
|---|---|
| **Navigation** | [← Chapter 7: Context](chapter-07-context.md) · [Back to Act 1](README.md) · [Next: Act 2 →](../act2-client-hybrid/README.md) |
