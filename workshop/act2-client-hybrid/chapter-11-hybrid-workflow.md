---
layout: step
title: "Hybrid Workflow — Cloud ⇔ Client Relay Development"
step_number: 9
estimated_minutes: 15
permalink: /chapter/11/
---

# Chapter 11: Hybrid Workflow — Cloud ⇔ Client Relay Development

> **Key takeaway:** The right tool for each phase — CLI for rapid analysis, Cloud Agent for autonomous heavy lifting, Mission Control for oversight, VS Code for precision refinement. Seamless handoffs between all of them.

[← Chapter 10](chapter-10-copilot-cli.md) | [Back to Act 2](README.md) | [Next: Chapter 12 →](chapter-12-context-consistency.md)

## 🎯 Learning Objectives

- [ ] Use Copilot CLI to analyze requirements and create a GitHub Issue from the terminal
- [ ] Trigger the Cloud Coding Agent by assigning Copilot to the Issue
- [ ] Monitor Agent progress in real time through Mission Control
- [ ] Hand off from cloud to VS Code for precision improvements
- [ ] Complete the full cycle with automatic Copilot Code Review

## 📋 Prerequisites

- [ ] Completed [Chapter 9](chapter-09-vscode-agent.md) and [Chapter 10](chapter-10-copilot-cli.md) concepts
- [ ] `gh` CLI authenticated (`gh auth status`)
- [ ] VS Code (Insiders) open with the repository loaded
- [ ] Copilot Chat and Agent Mode available in VS Code
- [ ] Copilot CLI installed (`copilot --version`)

## ⏱️ Estimated Time: ~15 minutes

---

## Relay Development Overview

This capstone exercise chains **five surfaces** into a single development flow. Each surface handles the phase it does best:

```
[CLI] Analyze & Issue  →  [Cloud] Agent Execution  →  [Mission Control] Monitor  →  [VS Code] Refine  →  [Cloud] Review
     ↓                          ↓                           ↓                          ↓                      ↓
 Fast analysis            Async, autonomous           Real-time visibility        Precision editing       Quality assurance
```

```
┌────────────────────────────────────────────────────────────────────────────┐
│                          Relay Development Flow                            │
│                                                                            │
│  🖥️ CLI            ☁️ Cloud            🖥️ VS Code          ☁️ Cloud       │
│  ┌──────────┐     ┌──────────┐        ┌──────────┐        ┌──────────┐   │
│  │ Analyze   │ ──→ │  Agent   │ ──→    │ Take over │ ──→   │  Review  │   │
│  │ Create    │     │ Autonomous│  ↓     │ Refine    │       │  Quality │   │
│  │ Issue     │     │ Execution │  │     │ Improve   │       │  Check   │   │
│  └──────────┘     └──────────┘  │     └──────────┘        └──────────┘   │
│                                  │                                         │
│                        📊 Mission Control                                  │
│                        (Real-time monitoring)                              │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Exercise 1: [CLI] Analyze and Create Issue

### Background

The relay starts at the terminal. Copilot CLI analyzes the project and helps you create a structured GitHub Issue — no browser needed.

### Instructions

1. In your terminal, ask Copilot CLI to help you plan a CI/CD pipeline:

   ```
   This project needs a CI/CD pipeline. Create a GitHub Issue requesting a GitHub
   Actions workflow with pytest, code linting with ruff, Docker image build, and
   pip dependency caching.
   ```

2. Copilot CLI will analyze the project structure and propose a `gh issue create` command with a structured title and body:

   ```bash
   gh issue create \
     --title "Add CI/CD pipeline with GitHub Actions" \
     --body "## Requirements
   - Run pytest on every push and PR
   - Python linting with ruff
   - Build Docker image on main branch
   - Cache pip dependencies for faster builds

   ## Acceptance Criteria
   - [ ] .github/workflows/ci.yml created
   - [ ] Tests pass in CI environment
   - [ ] Lint checks pass
   - [ ] Docker build succeeds"
   ```

3. Review the command Copilot suggests, then execute it to create the Issue

### ✅ Verification

- [ ] Issue was created in your repository
- [ ] Issue has a clear title and structured body with requirements
- [ ] Issue includes acceptance criteria as a checklist
- [ ] You did not need to open a browser at any point

<details>
<summary>💡 Instructor Notes</summary>

"Terminal → GitHub Issue in one step. No context switching. The CLI is your fast lane for analysis and Issue creation — it reads the project, understands the structure, and generates actionable requirements. Now we pass the baton to the cloud."

If participants' Copilot CLI output varies, that's fine. The key is that an Issue gets created with meaningful requirements. They can also write the `gh issue create` command manually.

</details>

---

## Exercise 2: [Cloud] Assign Copilot to the Issue

### Background

Now the Issue exists, hand it off to the Coding Agent for autonomous execution — the same workflow you learned in Act 1.

### Instructions

1. Choose one of two methods to assign Copilot:

   **Option A — From the CLI (recommended for this flow):**

   ```bash
   gh issue edit <issue_number> --add-assignee @copilot
   ```

   > Replace `<issue_number>` with the number from Exercise 1.

   **Option B — From the browser:**
   - Open the Issue on GitHub.com
   - Click **Assignees** → select **Copilot**

2. The Coding Agent starts autonomous execution — the same experience as [Chapter 4](../act1-cloud/chapter-04-execution.md)
3. A GitHub Actions workflow is triggered to run the Agent

### ✅ Verification

- [ ] Copilot appears as an assignee on the Issue
- [ ] A working indicator or Actions workflow starts (may take a moment)

<details>
<summary>💡 Instructor Notes</summary>

"We defined the requirements with the CLI and handed them to the Cloud Agent — just like you'd assign a task to a team member. The Agent will now autonomously read the codebase, plan the implementation, and create a PR. While it works, we'll watch from Mission Control."

This is the same assign-to-Copilot flow from Chapter 3/4. If participants have done Act 1, they'll recognize it.

</details>

---

## Exercise 3: [Mission Control] Monitor the Agent

### Background

While the Agent works autonomously, Mission Control gives you real-time visibility into its progress — governance and observability without interrupting the Agent.

### Instructions

1. Open **Mission Control** at [github.com/copilot](https://github.com/copilot)
2. Find the task created from your Issue
3. Observe the real-time session log. Watch for:
   - 📖 Agent reading the project structure
   - ✍️ Agent creating `.github/workflows/ci.yml`
   - 🔧 Agent configuring ruff linting
   - ✅ Agent verifying test execution
4. Note how the Agent's reasoning is fully visible — what it reads, plans, and decides

### ✅ Verification

- [ ] Task is visible in Mission Control
- [ ] Session log shows real-time Agent activity
- [ ] You can trace the Agent's reasoning (files read → plan → implementation)

<details>
<summary>💡 Instructor Notes</summary>

"CLI sent the task, Cloud Agent is executing it, and Mission Control gives us eyes on the process. Three surfaces working in concert. Next comes the highlight — handing off from cloud to VS Code."

If the Agent hasn't finished yet, use this time to explore Mission Control's interface. Point out that the same session log is available from the Actions tab. Continue to Exercise 4 once a PR appears.

</details>

---

## Exercise 4: [VS Code] Take Over and Refine

> **This is the key exercise** — the handoff from cloud to local development.

### Background

The Cloud Agent does the heavy lifting (80%), and you refine the details that need human judgment (20%). This exercise demonstrates the seamless transition from autonomous cloud execution to precision local editing.

### Instructions

1. Once the Agent has created a PR, check out its branch locally:

   ```bash
   gh pr checkout <pr_number>
   ```

   > Replace `<pr_number>` with the PR number from the Agent's work.

2. Open `.github/workflows/ci.yml` in VS Code and review what the Agent created

3. Use **Agent Mode** in VS Code to improve the workflow:

   ```
   Add matrix testing for Python 3.11 and 3.12, and optimize the pip caching
   configuration in this workflow file.
   ```

4. Review the changes Agent Mode proposes:
   - Matrix strategy added for multiple Python versions
   - pip caching configuration optimized
   - Accept the changes when satisfied

5. Commit and push your improvements:

   ```bash
   git add .github/workflows/ci.yml
   git commit -m "Optimize CI/CD: add matrix testing and pip cache"
   git push
   ```

### ✅ Verification

- [ ] You successfully checked out the Agent's PR branch
- [ ] `.github/workflows/ci.yml` now includes a matrix strategy for Python 3.11 and 3.12
- [ ] pip caching configuration is present and optimized
- [ ] Your changes are committed and pushed to the PR branch

<details>
<summary>💡 Instructor Notes</summary>

"The Cloud Agent built the entire CI/CD pipeline — workflow file, linting config, test execution. We refined the last 20%: matrix testing and cache optimization. That's the 80/20 principle in action. The Agent automates the bulk, the developer handles the nuanced decisions."

Emphasize the zero-friction handoff: `gh pr checkout` is all it takes to go from cloud to local. No special tools, no export/import steps.

</details>

---

## Exercise 5: [Cloud] Observe Code Review

### Background

After pushing, Copilot Code Review automatically runs on the PR — covering both the Agent-generated code and your manual improvements as a unified whole.

### Instructions

1. Go to the PR on GitHub.com (or use `gh pr view --web`)
2. Observe that Copilot Code Review runs automatically
3. Note that the PR now contains **both**:
   - Code generated by the Cloud Agent
   - Your manual improvements from VS Code
4. Code Review treats it all as one cohesive change

5. **Reflect on the complete relay flow:**

   ```
   [CLI] Analyze & Issue        — terminal strength (fast analysis)
      ↓
   [Cloud] Agent execution      — cloud strength (async, autonomous)
      ↓
   [Mission Control] Monitor    — governance strength (observability)
      ↓
   [VS Code] Refine             — IDE strength (precision editing)
      ↓
   [Cloud] Code Review          — automated quality assurance
   ```

### ✅ Verification

- [ ] Copilot Code Review appears on the PR
- [ ] Review covers both Agent-generated and manually-added code
- [ ] You can trace the entire journey: Issue → Agent → Mission Control → VS Code → Code Review

<details>
<summary>💡 Instructor Notes</summary>

"Five surfaces, one continuous flow. CLI → Cloud → Mission Control → VS Code → Code Review. But here's the key insight: none of this was forced. You chose which tool to use at each phase. The developer is always in control of the workflow."

This is the capstone moment — make sure to pause and let participants appreciate the full loop before moving on.

</details>

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent hasn't finished yet | Review Mission Control while waiting. Continue to Exercise 4 once the PR appears |
| `gh pr checkout` fails | Try manually: `git fetch origin && git checkout <branch-name>` |
| Mission Control doesn't show the task | May take a few minutes to appear. Refresh, or check [github.com/copilot](https://github.com/copilot) directly |
| "Open in VS Code" button not available | Use `gh pr checkout <pr_number>` as the alternative (works reliably) |
| Code Review doesn't trigger | Check that Copilot Code Review is enabled for the repository in Settings → Copilot |
| Agent created unexpected file structure | That's OK — the refinement step (Exercise 4) is where you correct and improve |

---

## 📝 Chapter Recap

In this chapter, you completed a **full relay development cycle** across five Copilot surfaces:

1. **CLI** — Analyzed the project and created a GitHub Issue from the terminal
2. **Cloud Agent** — Autonomously implemented the CI/CD pipeline
3. **Mission Control** — Monitored the Agent's progress in real time
4. **VS Code** — Took over the Agent's work and refined it with precision
5. **Code Review** — Automated quality assurance on the combined result

### Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Right tool for the job** | Each surface has its strength — use the best one for each phase |
| **Seamless handoffs** | CLI → Cloud → VS Code transitions with zero friction |
| **80/20 principle** | Agent automates the bulk; human handles the important 20% |
| **All surfaces unified** | CLI, Cloud, Mission Control, VS Code, Code Review in one flow |
| **Developer choice** | You decide which tool to use at each phase — nothing is forced |

---

**Next:** [Chapter 12: Context Consistency →](chapter-12-context-consistency.md) — Verify that Custom Instructions apply identically across all surfaces.
