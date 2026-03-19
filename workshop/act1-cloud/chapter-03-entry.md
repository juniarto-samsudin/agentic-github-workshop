---
layout: step
title: "Entry — From Chat to Agent"
step_number: 1
estimated_minutes: 10
permalink: /chapter/03/
---

# Chapter 3: Entry — From Chat to Agent

> **Key takeaway:** Copilot Chat is the most natural entry point — understand code, discover gaps, create Issues, and trigger the Agent, all from a single conversation.

[← Back to Act 1 Overview](README.md) | [Next: Chapter 4 →](chapter-04-execution.md)

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Use Copilot Chat on GitHub.com to understand an entire repository
- [ ] Ask Copilot to identify project improvements
- [ ] Create a GitHub Issue directly from a Chat conversation
- [ ] Assign Copilot to an Issue to trigger autonomous execution

## 📋 Prerequisites

- [ ] Completed [Workshop Setup](../setup.md)
- [ ] Browser open to your forked repository on GitHub.com

## ⏱️ Estimated Time: ~10 minutes

---

## Overall Flow

```
Understand code with Chat → Discover improvements → Create Issue → Assign Copilot
         ↓                          ↓                    ↓               ↓
    "Explain this"          "No tests exist"       Issue is created   Continue to
                                                                     Chapter 4
```

---

## Exercise 1: Understand the Codebase with Chat

### Background

Copilot Chat on GitHub.com has full repository context — it can read and understand all files in the repo. This makes it ideal for quickly grasping a new project's architecture.

### Instructions

1. Open your repository on GitHub.com
2. Click the **Copilot Chat icon** (top right)
3. Ask:
   > "What does this project do? Explain the architecture and the relationships between files."

### ✅ Verification

- [ ] Copilot reads the entire repository and responds
- [ ] Copilot identifies this as a FastAPI-based Todo API
- [ ] Copilot describes the 3-layer structure: `main.py` (routes) → `models.py` (schemas) → `database.py` (storage)
- [ ] Copilot lists the 5 CRUD endpoints

<details>
<summary>💡 Instructor Notes</summary>

- Chat is the most casual entry point — just open a repo and ask questions
- Emphasize that Chat reads the ENTIRE repository, not just one file
- This is useful for onboarding new team members to an unfamiliar codebase

</details>

---

## Exercise 2: Discover Improvement Opportunities

### Instructions

1. Continue in the same Chat session
2. Ask:
   > "What improvements would you suggest for this project?"

### ✅ Verification

- [ ] Copilot identifies multiple gaps, including:
  - ⚠️ No unit tests
  - ⚠️ No input validation
  - ⚠️ No Dockerfile
  - ⚠️ No CI/CD pipeline
  - ⚠️ No logging

<details>
<summary>💡 Instructor Notes</summary>

- Copilot doesn't just understand code content — it identifies what's MISSING
- This is like a project health check before a code review
- The gaps are intentional in this workshop app — they give Copilot something to fix

</details>

---

## Exercise 3: Create an Issue from Chat

### Background

One of Copilot Chat's powerful features is the ability to create GitHub Issues directly from the conversation. This means you can go from discovery to action without leaving the chat window — zero context switching.

### Instructions

1. Based on Copilot's suggestions, ask in Chat:
   > "Create a GitHub Issue about the missing unit tests. It should request pytest and httpx tests for all endpoints."
2. Copilot will generate an Issue title and body
3. Click the **"Create Issue"** button or link when it appears
4. Review the pre-filled Issue and click **Submit new issue**

### ✅ Verification

- [ ] An Issue is created with a descriptive title
- [ ] The Issue body includes testing requirements (pytest, httpx, all endpoints)
- [ ] The Issue appears in your repository's Issues tab

### 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Chat doesn't offer to create an Issue | Copy Copilot's suggestion, go to the Issues tab, and create it manually using the backup content below |
| Issue creation button not visible | Your Copilot plan may not support this feature. Create the Issue manually using the backup content below |
| Chat generates an Issue but it looks incomplete | Edit the Issue body before submitting to include the requirements listed in the backup content |

<details>
<summary>📋 Backup: Manual Issue Content</summary>

If you need to create the Issue manually, use the following:

**Title:**
```
Add unit tests for the Todo API endpoints
```

**Body:**
```markdown
We need unit tests for all CRUD endpoints in the Todo API.

## Requirements
- Use `pytest` and `httpx` for testing
- Test all endpoints: GET /todos, GET /todos/{id}, POST /todos, PUT /todos/{id}, DELETE /todos/{id}
- Test both success and error cases (e.g., 404 for missing todo)
- Add a `tests/` directory with proper structure
- Include a `conftest.py` with shared test fixtures
```

</details>

<details>
<summary>💡 Instructor Notes</summary>

- The key message here is the seamless flow: understanding → discovery → Issue creation, all in one screen
- Emphasize zero context switching — from thought to action in a single conversation
- If participants have trouble with the Chat-to-Issue feature, the manual backup is perfectly fine — the important thing is that the Issue exists for the next step

</details>

---

## Exercise 4: Assign Copilot to the Issue

### Background

Assigning Copilot to an Issue triggers the Coding Agent — it will autonomously plan, write code, and create a Pull Request. This is the bridge from human intent (the Issue) to autonomous execution (the Agent).

### Instructions

1. Open the Issue you just created
2. Click **Assignees** in the right sidebar
3. Select **Copilot** from the assignee list
4. Confirm that Copilot starts working — you should see a "Copilot is working..." indicator

### ✅ Verification

- [ ] Copilot appears as an assignee on the Issue
- [ ] A "working" indicator appears (this means the Agent has been triggered)

> ⏳ **The Agent will take 1–3 minutes to complete.** Continue to [Chapter 4](chapter-04-execution.md) where you'll observe the Agent's execution.

<details>
<summary>💡 Instructor Notes</summary>

- The assignment triggers a GitHub Actions workflow behind the scenes
- While waiting, you can explain the architecture or take questions from participants
- The key message: Issue → assign Copilot → Agent runs autonomously
- Participants don't need to wait here — Chapter 4 covers observing the Agent's work

</details>

---

## 📝 Chapter Recap

In this chapter, you:
- Used **Copilot Chat** to understand the full codebase from GitHub.com
- Asked Copilot to identify **improvement opportunities** in the project
- Created a **GitHub Issue** directly from a Chat conversation — zero context switching
- **Assigned Copilot** to the Issue, triggering autonomous Agent execution

### Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Full repository context** | Chat understands all files, not just one |
| **Chat → Issue pipeline** | Seamless flow from discovery to action |
| **Structured Issue generation** | Copilot writes requirements based on project understanding |
| **Agent trigger** | Assigning Copilot = starting autonomous execution |

---

## 📎 Solution Reference

If the Agent completes before you reach Chapter 4, or if you want to compare results later, these branches were created by Copilot during previous workshop runs:

- `copilot/add-pytest-unit-tests` — Full test suite with CI workflow
- `copilot/add-unit-tests-todo-api` — Alternative, simpler test implementation
- `copilot/explain-codebase-structure` — Example of Copilot's codebase analysis

---

**Next:** [Chapter 4: Execution →](chapter-04-execution.md) — Watch the Agent work and review its output.
