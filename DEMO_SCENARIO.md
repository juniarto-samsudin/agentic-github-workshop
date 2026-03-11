# 🎬 Agentic GitHub Copilot — Demo Scenario

> **15-minute live demonstration** of GitHub Copilot's agentic capabilities on GitHub.com  
> Audience: Mixed (developers, managers, executives)

---

## 📋 Demo Overview

This demonstration showcases three agentic capabilities of GitHub Copilot directly on GitHub.com, using a **Python FastAPI Todo API** as the target application.

| # | Scenario | Feature | Duration |
|---|----------|---------|----------|
| 1 | [Copilot Chat](#-scenario-1-copilot-chat-on-githubcom) | Understand & generate code with full repo context | ~3 min |
| 2 | [Coding Agent (Issue → PR)](#-scenario-2-copilot-coding-agent-issue--pr) | Assign an Issue to Copilot → autonomous PR creation | ~6 min |
| 3 | [Code Review on PR](#-scenario-3-copilot-code-review-on-pr) | Automated intelligent PR review | ~5 min |
| 4 | [Wrap-up](#-wrap-up) | Recap & key takeaways | ~1 min |

### About the Demo App

A simple REST API for managing todo items:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/todos` | List all todos |
| `GET` | `/todos/{id}` | Get a specific todo |
| `POST` | `/todos` | Create a new todo |
| `PUT` | `/todos/{id}` | Update an existing todo |
| `DELETE` | `/todos/{id}` | Delete a todo |

**Intentional gaps** (for Copilot to fill during demo):
- ❌ No unit tests
- ❌ No Dockerfile
- ❌ No input validation

---

## 💬 Scenario 1: Copilot Chat on GitHub.com

> **Goal:** Show that Copilot understands the entire repository and generates contextually accurate code.

### Step 1-1: Explain the codebase

1. Open the repository on GitHub.com
2. Click the **Copilot Chat icon** (top-right corner)
3. Ask:

   > **"What does this project do? Explain the architecture and how the files are connected."**

4. **Expected result:** Copilot reads all files and gives a coherent summary — mentioning FastAPI, Pydantic models, in-memory database, and the CRUD endpoints.

🗣️ **Talking point:** *"Copilot has full repo context — it's not just looking at one file. This is like having an onboarding buddy who already read every line of code."*

### Step 1-2: Generate a Dockerfile

1. In the same chat, ask:

   > **"Write a Dockerfile for this project."**

2. **Expected result:** Copilot generates a production-ready Dockerfile that:
   - Uses `python:3.11-slim` as base
   - Copies `requirements.txt` and installs dependencies
   - Uses `uvicorn app.main:app` as the entrypoint
   - Exposes port 8000

🗣️ **Talking point:** *"Notice it referenced our actual requirements.txt and the correct uvicorn entry point — this isn't a generic template."*

### Step 1-3: Ask about deployment

1. Ask:

   > **"How would I deploy this to Azure App Service?"**

2. **Expected result:** Step-by-step deployment instructions specific to *this* project.

🗣️ **Talking point:** *"Great for reducing context-switching — no need to leave GitHub to search Stack Overflow."*

---

## 🤖 Scenario 2: Copilot Coding Agent (Issue → PR)

> **Goal:** Create a GitHub Issue, assign it to Copilot, and watch it autonomously produce a working Pull Request.

### Step 2-1: Create the Issue

1. Navigate to **Issues** → **New Issue**
2. Fill in:

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

3. Submit the Issue

### Step 2-2: Assign to Copilot

1. On the Issue page, click **Assignees** → select **Copilot**
2. Copilot begins working autonomously:
   - 📖 Reads and analyzes the entire codebase
   - 🌿 Creates a new branch
   - ✍️ Writes code changes
   - 📬 Opens a Pull Request linked to the Issue

3. **Wait ~1–3 minutes** for Copilot to complete

🗣️ **Talking point:** *"This is the 'agentic' part — Copilot isn't just suggesting a line of code. It's reading the project, understanding the structure, creating files, and delivering a complete solution."*

### Step 2-3: Review the Result

1. Open the Pull Request that Copilot created
2. Walk through:
   - **PR description** — auto-generated, references the Issue
   - **New files** — `tests/` directory with pytest structure
   - **Test cases** — covers success paths AND error cases (404s)
   - **Correct imports** — references actual `app.main` and `app.database`

🗣️ **Talking point:** *"This isn't toy code — it's production-quality tests that understand our actual API structure."*

### Backup Issue (if time is tight)

If the Coding Agent takes too long, use this pre-prepared alternative:

**Title:** `Add input validation with proper error messages`

```markdown
The API currently accepts any string for todo titles, including empty strings.

## Requirements
- Title must be between 1 and 100 characters
- Description must be at most 500 characters if provided
- Return 422 with clear error messages for invalid input
- Update the Pydantic models in `app/models.py` with field validators
```

---

## 🔍 Scenario 3: Copilot Code Review on PR

> **Goal:** Show how Copilot automatically reviews Pull Requests and provides actionable, intelligent feedback.

### Step 3-1: View the PR Summary

1. Open the PR created by Copilot (from Scenario 2) — or any other PR
2. Show the **Copilot-generated summary** in the PR description
3. **Expected result:** An accurate description of what changed and why

🗣️ **Talking point:** *"No more 'updated files' as a PR description. Copilot writes the summary so reviewers can understand the change at a glance."*

### Step 3-2: Review Comments

1. Go to the **Files changed** tab
2. Show Copilot's review comments:
   - 🐛 Identifies potential bugs
   - 💡 Suggests improvements
   - 🔒 Flags security concerns
3. **Expected result:** Comments are specific and actionable — referencing actual code lines and suggesting concrete fixes

🗣️ **Talking point:** *"These aren't generic lint warnings. Copilot understands the logic and catches issues that require understanding the business context."*

### Step 3-3: Ask Copilot in the PR

1. In the PR conversation tab, type a comment mentioning Copilot:

   > **"Are there any edge cases this PR doesn't handle?"**

2. **Expected result:** Copilot analyzes the diff and suggests additional test scenarios or missing edge cases

🗣️ **Talking point:** *"You can have a conversation with Copilot right in the PR — it's like having a senior engineer available 24/7 for code review."*

---

## 🎯 Wrap-up

### Three Agentic Capabilities Demonstrated

| Capability | What it does | Business value |
|------------|-------------|----------------|
| **💬 Chat** | Understand any codebase instantly, generate code with full context | Faster onboarding, reduced context-switching |
| **🤖 Coding Agent** | Turn Issues into working PRs autonomously | Accelerate feature delivery, handle routine tasks |
| **🔍 Code Review** | Automated, intelligent PR review | Catch bugs earlier, consistent quality bar |

### Key Messages

1. **Full repo context** — Copilot understands your entire codebase, not just the current file
2. **Autonomous execution** — From Issue to PR without human intervention
3. **Quality, not just speed** — Production-quality code with proper testing and error handling
4. **Complements humans** — Augments your team, doesn't replace code review or decision-making

---

## 🎁 Bonus Scenarios (if time permits)

### Bonus A: Multi-file Task

**Issue:** *"Add a `/health` endpoint and a GitHub Actions CI workflow"*

Shows Copilot creating files across different directories (`app/main.py` + `.github/workflows/ci.yml`).

### Bonus B: Bug Fix

1. Intentionally introduce a bug (e.g., wrong status code on delete)
2. **Issue:** *"Bug: DELETE /todos/{id} returns 200 instead of 204"*
3. Assign to Copilot → it finds and fixes the exact line

### Bonus C: Dockerfile via Coding Agent

**Issue:** *"Add a Dockerfile for containerized deployment"*

```markdown
## Requirements
- Use a multi-stage build for smaller image size
- Use Python 3.11-slim as the base image
- Expose port 8000
- Run with uvicorn in production mode
- Include a .dockerignore file
```
