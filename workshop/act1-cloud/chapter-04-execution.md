# Chapter 4: Execution — Observing the Agent at Work

> **Key takeaway:** The Coding Agent runs on GitHub Actions, and everything it does — every file it reads, every decision it makes — is fully observable through session logs.

[← Chapter 3](chapter-03-entry.md) | [Back to Act 1](README.md) | [Next: Chapter 5 →](chapter-05-collaboration.md)

## 🎯 Learning Objectives
- [ ] Navigate to the Actions tab to observe a running Coding Agent
- [ ] Read session logs to understand the Agent's reasoning process
- [ ] Review a completed PR created by the Agent (description, files, Issue link)

## 📋 Prerequisites
- [ ] Completed [Chapter 3](chapter-03-entry.md) — Copilot assigned to an Issue

## ⏱️ Estimated Time: ~10 minutes

---

## Exercise 1: Observe the Agent on GitHub Actions

### Background
The Coding Agent runs as a GitHub Actions workflow. No special infrastructure is needed — it uses your existing Actions runners and policies.

### Instructions
1. Navigate to the **Actions** tab in your repository
2. Find the Copilot Coding Agent workflow run
3. Note the workflow status (🟡 In progress or ✅ Completed) and execution time
4. Click the workflow run to expand the logs — observe:
   - 📖 Which files the Agent read
   - 🌿 Branch creation
   - ✍️ File creation and editing
   - ✅ Any automated test execution

### ✅ Verification
- [ ] You can see the Coding Agent workflow in the Actions tab
- [ ] The workflow log shows which files the Agent analyzed
- [ ] A branch was created for the changes

<details>
<summary>💡 Instructor Notes</summary>

Emphasize that Actions is the existing infrastructure — no new setup needed. The same org policies and runner configs apply. This is a key selling point: zero additional infrastructure cost.

</details>

---

## Exercise 2: Read the Session Log

### Background
The session log is a detailed record of the Agent's entire thought process — what it read, how it planned, and what it decided.

### Instructions
1. Open the Agent's execution detail page
2. Review the session log, looking for:
   - Which files the Agent read (e.g., "Read app/main.py — identified 5 endpoints")
   - How it interpreted the codebase structure
   - What plan it formed
   - Which files it created or modified

### ✅ Verification
- [ ] You can trace the Agent's reasoning from file reading → planning → code generation
- [ ] The Agent correctly identified the project structure (main.py, models.py, database.py)

<details>
<summary>💡 Instructor Notes</summary>

"This is not a black box. Everything the Agent reads, thinks, and creates is traceable in the session log. This is what observability means."

Highlight specific log entries to show:
- `app/main.py` was read and 5 endpoints were recognized
- `app/models.py` was analyzed to understand Pydantic model structures
- `tests/` directory was created with `conftest.py` and `test_main.py`

</details>

---

## Exercise 3: Review the Completed Pull Request

### Instructions
1. Go to the **Pull Requests** tab and find the PR created by Copilot
2. Review these elements:

   **PR Description:**
   - Auto-generated description explaining what was done
   - Reference link to the original Issue (`Closes #XX`)
   - Summary of changes

   **Files Changed:**
   - `tests/` directory created
   - `tests/conftest.py` — shared fixtures (TestClient setup, etc.)
   - `tests/test_main.py` — tests for all endpoints

   **Test Code Quality:**
   - Success cases (normal CRUD operations)
   - Error cases (404 for non-existent IDs)
   - Correct imports (referencing `app.main` and `app.database`)
   - Appropriate assertions (status codes, response bodies)

### ✅ Verification
- [ ] PR exists and references the original Issue
- [ ] Test files were created in a `tests/` directory
- [ ] Tests cover both success and error scenarios
- [ ] PR description explains what was done and why

<details>
<summary>💡 Instructor Notes</summary>

"The result is a normal PR. Not a special format or a proprietary UI — it fits directly into your existing PR review workflow. That's the point: you don't need to learn a new process."

</details>

### 🔧 Troubleshooting
| Problem | Solution |
|---------|----------|
| Agent is still running | Wait 1–3 min. In the meantime, review the session log (Exercise 2) |
| PR doesn't reference the Issue | This can happen — check the PR description for mentions of the Issue content |
| Tests look incomplete | AI output varies — check if the core CRUD operations are covered |

---

## 📝 Chapter Recap

In this chapter, you:
- Observed the Coding Agent running on **GitHub Actions** — your existing CI infrastructure
- Read **session logs** to trace the Agent's reasoning process
- Reviewed a completed **Pull Request** with auto-generated tests and description

### Key Concepts
| Concept | What It Means |
|---------|--------------|
| **GitHub Actions execution** | Agent uses existing infra — no new setup needed |
| **Asynchronous execution** | Agent works while you do other things |
| **Observability** | Session logs reveal the full thought process |
| **Standard PR output** | Results integrate into your normal review workflow |
| **Issue ↔ PR traceability** | Automatic links between Issue and PR |

---

## 📎 Solution Reference

These branches were created by Copilot during previous runs and show example outputs for Chapters 3–4:

| Branch | What It Contains |
|--------|-----------------|
| `copilot/add-pytest-unit-tests` | Full test suite + CI workflow + Custom Instructions compliance |
| `copilot/add-unit-tests-todo-api` | Alternative test implementation (simpler) |

To inspect a solution branch:
```bash
git log --oneline origin/copilot/add-pytest-unit-tests
git diff main..origin/copilot/add-pytest-unit-tests --stat
```

> **Note:** Your Agent's output will differ — AI results vary between runs. Use these as reference points, not exact expectations.

---

**Next:** [Chapter 5: Collaboration →](chapter-05-collaboration.md) — Interact with the Agent on the PR.
