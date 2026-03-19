# Chapter 9: VS Code Agent Mode — Interactive Real-Time Collaboration

> **Key takeaway:** VS Code Agent Mode is "coding together" — the Agent edits files in real-time while you watch, approve, reject, or redirect each change. Unlike the Cloud Agent, you're in the driver's seat.

[← Back to Act 2 Overview](README.md) | [Next: Chapter 10 →](chapter-10-copilot-cli.md)

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Use `@workspace` to analyze code in VS Code
- [ ] Switch to Agent Mode and give multi-file instructions
- [ ] Interact with Agent Mode: Accept/Reject changes, approve terminal commands
- [ ] Verify Custom Instructions compliance in generated code
- [ ] Run tests locally through the Agent
- [ ] (Optional) Experience Next Edit Suggestions (NES)

## 📋 Prerequisites

- [ ] Completed [Workshop Setup](../setup.md)
- [ ] VS Code (Insiders recommended) open with the repository loaded
- [ ] GitHub Copilot Chat extension installed and active
- [ ] Agent Mode available in Copilot Chat (mode selector visible)

## ⏱️ Estimated Time: ~15 minutes

---

## Comparison: Cloud Agent vs VS Code Agent Mode

Before we begin, understand where VS Code Agent Mode fits compared to the Cloud Agent from Act 1:

| | Cloud Agent (Chapter 4) | VS Code Agent Mode (Chapter 9) |
|---|---|---|
| **Execution model** | Asynchronous, autonomous | Synchronous, interactive |
| **Feedback loop** | Wait for results | Watch in real-time |
| **Results delivered via** | Pull Request | In-editor changes |
| **Best for** | Large tasks (full test suites, CI/CD) | Medium/small tasks, refactoring |
| **Workflow** | Issue → Agent → PR | Chat → Agent → Local verification |
| **Control** | Review after completion | Accept/Reject each change |

---

## Overall Flow

```
@workspace analysis → Agent Mode → Add validation → Review code → Run tests → Verify
       ↓                  ↓              ↓               ↓            ↓          ↓
  Understand code   Interactive    Multi-file edits   Custom      Instant     Complete
                    collaboration                     Instructions feedback
```

---

## Exercise 1: Understand the Codebase with @workspace

### Background

The `@workspace` participant in VS Code Copilot Chat uses a local file index to answer questions about your project. It gives the same quality answers as GitHub.com Chat (Chapter 3), but often responds faster because it works with local files.

### Instructions

1. Open the Copilot Chat panel in VS Code (`Ctrl+Shift+I` or click the Copilot icon in the sidebar)
2. Ask:
   > "@workspace Explain the project structure and each file's role."
3. Review the response — Copilot should describe the `app/` directory structure, `main.py` (routes), `models.py` (schemas), and `database.py` (storage)

4. Follow up with a more targeted question:
   > "@workspace Which endpoints lack input validation? What specifically is missing?"

### ✅ Verification

- [ ] Copilot identifies this as a FastAPI-based Todo API and describes the file relationships
- [ ] Copilot finds validation gaps, such as:
  - `POST /todos` has no empty-title check
  - `PUT /todos/{id}` has no update-value validation
  - `TodoCreate` / `TodoUpdate` models have no Pydantic field validators

<details>
<summary>💡 Instructor Notes</summary>

- `@workspace` uses local file indexing — it is often faster than cloud-based Chat for large repos
- Compare this to Chapter 3: same quality of analysis, different surface (VS Code vs GitHub.com)
- Point out that the validation gaps are intentional — they give us something to fix with Agent Mode in the next exercise

</details>

---

## Exercise 2: Add Input Validation with Agent Mode

### Background

Agent Mode is a step beyond regular Copilot Chat. Instead of generating code snippets for you to copy, the Agent **directly edits files** in your workspace. You watch each action in real-time and decide whether to accept or reject each change.

### Instructions

1. In the Copilot Chat panel, switch to **Agent Mode** using the mode selector dropdown (click the mode name at the top of the chat input area and select **"Agent"**)

2. Give the Agent a multi-file instruction:
   > "Add input validation to the TodoCreate and TodoUpdate models. Add Pydantic field validators to ensure titles are not empty or blank and have a max length. Follow the Custom Instructions for this project."

3. **Watch the Agent work in real-time.** You should see it:
   - 📖 Open and read `app/models.py`
   - 📖 Open and read `app/main.py`
   - 📖 Read `.github/copilot-instructions.md` (Custom Instructions)
   - ✏️ Edit `app/models.py` — adding validators
   - ✏️ Edit `app/main.py` — adding custom error handling
   - 🆕 Possibly create `app/exceptions.py` — custom exception class
   - 🖥️ Possibly run terminal commands

4. **Key interaction point:** For each file change, you will see **Accept** and **Reject** buttons. For terminal commands, the Agent asks for your **approval** before executing.

### ✅ Verification

- [ ] Agent Mode begins editing files — you can see the changes happening in real-time
- [ ] Each file change shows Accept / Reject controls
- [ ] Terminal commands (if any) require your explicit approval before running

<details>
<summary>💡 Instructor Notes</summary>

- **This is the key differentiator from the Cloud Agent.** The Cloud Agent delivers results via PR; VS Code Agent Mode shows you every change as it happens and lets you control the process.
- Remind participants: "You can reject any individual change without stopping the entire session."
- If Agent Mode takes a while, explain that it is reading Custom Instructions and planning multi-file edits — this is expected behavior.
- If Agent Mode is not visible in the mode selector, ensure the Copilot extension (and VS Code) are updated to the latest version.

</details>

---

## Exercise 3: Review Generated Code for Custom Instructions Compliance

### Background

In Chapter 7 (Custom Instructions), you configured rules like Google-style docstrings, `X | None` syntax, custom exception classes, and named constants. Now verify that VS Code Agent Mode follows the **same rules** as the Cloud Agent — proving that Custom Instructions are consistent across surfaces.

### Instructions

1. Examine the files the Agent modified or created. Look for the following structural markers:

   **In `app/models.py` — Validation logic:**
   - Field validators using `Field(...)` with `min_length` / `max_length`
   - A `@field_validator` to reject blank (whitespace-only) titles
   - Named constants (e.g., `MAX_TITLE_LENGTH`, `MAX_DESCRIPTION_LENGTH`) instead of magic numbers

   **In `app/exceptions.py` (if created) — Custom error class:**
   - A custom exception class matching the unified error format from Custom Instructions:
     ```json
     {
       "error": {
         "code": "ERROR_CODE",
         "message": "Human-readable error message",
         "details": {}
       }
     }
     ```

2. Check for Custom Instructions compliance:

| Rule | What to look for | ✅ / ❌ |
|------|-----------------|---------|
| Google-style docstrings | Functions have docstring with description, Args, Returns, Raises sections | |
| `X \| None` format | Uses `str \| None` instead of `Optional[str]` | |
| Custom exception classes | Uses custom error classes, not raw `HTTPException` | |
| Named constants | `MAX_TITLE_LENGTH = 100` instead of inline `100` | |
| Type hints on all functions | Every function has parameter and return type annotations | |

### ✅ Verification

- [ ] Generated code follows **at least 3** of the Custom Instructions rules listed above
- [ ] No magic numbers in validation logic
- [ ] Error responses use the unified format (if custom exceptions were created)

<details>
<summary>💡 Instructor Notes</summary>

- Custom Instructions apply in VS Code just as they do on GitHub.com — this is a key consistency point
- The structural markers (docstrings, `X | None`, custom exceptions, constants) serve as **proof** that the instructions are working
- If some rules are not followed, demonstrate how to tell the Agent: "Follow the Custom Instructions for this project" — the Agent will re-read `.github/copilot-instructions.md` and adjust
- Compare with the Cloud Agent's output from Act 1 — the patterns should be the same

</details>

---

## Exercise 4: Run Tests Locally Through the Agent

### Background

One of Agent Mode's most powerful features is its ability to write code, write tests, and run them — all in a single session. If tests fail, the Agent can attempt to fix them automatically, creating a tight local feedback loop.

### Instructions

1. Continue in the same Agent Mode session
2. Instruct the Agent:
   > "Write tests for the validation you just added. Put them in the tests/ directory following the project's test naming conventions."

3. The Agent should:
   - Create a test file (e.g., `tests/test_validation.py`)
   - Write test functions following the naming pattern `test_<target>_<condition>_<expected_result>`
   - Run `pytest tests/test_validation.py -v` in the terminal (with your approval)

4. Expected tests (names may vary slightly):
   - `test_create_todo_with_empty_title_returns_422`
   - `test_create_todo_with_blank_title_returns_422`
   - `test_create_todo_with_long_title_returns_422`
   - `test_create_todo_with_valid_data_returns_201`

### ✅ Verification

- [ ] Agent creates a test file in the `tests/` directory
- [ ] Agent runs pytest in the integrated terminal
- [ ] All tests pass (or the Agent attempts to fix failures automatically)

<details>
<summary>💡 Instructor Notes</summary>

- Highlight the full loop: **write code → write tests → run tests → fix failures** — all within Agent Mode
- If tests fail, let participants watch the Agent diagnose and fix the issue. This self-healing loop is a major selling point.
- Compare to the Cloud Agent: the Cloud Agent also writes and runs tests, but you only see the results in a PR. Here you see everything live.
- The test naming pattern (`test_<target>_<condition>_<expected>`) comes from the Custom Instructions — another compliance proof point.

</details>

---

## Exercise 5: Accept / Reject Workflow — Understanding Control

### Background

Agent Mode is interactive by design. This exercise focuses on the **control mechanisms** — understanding how to accept, reject, or redirect the Agent's proposals. This is what makes VS Code Agent Mode fundamentally different from autonomous cloud execution.

### Instructions

1. Review the changes from Exercises 2–4 and take note of how each interaction worked:

   | Action | What happens |
   |--------|-------------|
   | **Accept** (click ✓ or "Accept") | The change is applied to the file |
   | **Reject** (click ✗ or "Reject") | The change is discarded; the file stays unchanged |
   | **Terminal command approval** | Agent shows the command and waits — you decide whether to run it |
   | **Redirect mid-task** | Type a new message to change the Agent's direction |

2. (Optional) Try rejecting one change and asking the Agent to try a different approach:
   > "Don't use a field_validator for this — use a model_validator instead."

3. Observe how the Agent adjusts based on your feedback.

### ✅ Verification

- [ ] You understand how to accept individual file changes
- [ ] You understand how to reject changes without stopping the session
- [ ] You understand that terminal commands require explicit approval
- [ ] You understand that you can redirect the Agent mid-task with new instructions

<details>
<summary>💡 Instructor Notes</summary>

- This exercise is more about awareness than hands-on coding
- If time is short, demonstrate Accept/Reject with a quick example rather than having participants try the optional rejection step
- Emphasize: "The Cloud Agent is fire-and-forget. Agent Mode is pair programming with an AI."

</details>

---

## Exercise 6 (Optional): Next Edit Suggestions

### Background

Next Edit Suggestions (NES) is a complementary feature to Agent Mode. While Agent Mode handles **large multi-file tasks**, NES detects **repetitive patterns** during manual editing and proposes similar changes across your codebase. Think of it as Tab-completion for refactoring.

### Instructions

1. Exit Agent Mode (switch back to a non-Agent chat mode, or simply start editing files manually)
2. Open `app/main.py`
3. Manually add a Google-style docstring to **one** endpoint function. For example:
   ```python
   @app.post("/todos", response_model=TodoResponse, status_code=201)
   def create_todo(todo: TodoCreate):
       """Create a new todo item.

       Args:
           todo: The todo creation request containing title and optional description.

       Returns:
           The created todo item with its assigned ID.
       """
       ...
   ```
4. Move your cursor to the **next** endpoint function
5. Watch: NES should propose a similar docstring pattern for this function
6. Press **Tab** to accept the suggestion
7. Continue to the next endpoint — NES chains the pattern through all remaining endpoints

### ✅ Verification

- [ ] After manually editing one function, NES suggests a similar edit for the next function
- [ ] Pressing Tab accepts and applies the suggestion
- [ ] The pattern chains across multiple endpoints

<details>
<summary>💡 Instructor Notes</summary>

- **Agent Mode** = large tasks spanning multiple files; **NES** = small pattern-based repetition within a file
- NES is context-aware: it learns the pattern from your first edit and applies it consistently
- If NES doesn't trigger immediately, it may need a moment to analyze the pattern. Try saving the file and moving to the next function.
- This is optional — skip if time is tight. The key takeaway can be stated verbally: "Agent Mode for big tasks, NES for small repetitive edits."

</details>

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Agent Mode not visible in the mode selector | Update VS Code (try Insiders edition) and the Copilot extension to the latest version. Agent Mode requires a recent version. |
| Agent Mode responds slowly | This is normal for complex multi-file edits. For simpler tasks, use **Ask** or **Edit** mode in Copilot Chat instead. |
| Custom Instructions not reflected in output | Verify `.github/copilot-instructions.md` exists in the repo root. Try explicitly saying _"Follow the Custom Instructions for this project"_ in your prompt. |
| Tests fail after Agent generates them | Let the Agent attempt to fix them (it often self-corrects). If it cannot, check for missing imports or incorrect test client setup. |
| `@workspace` gives incomplete answers | Ensure the workspace index is built — open the command palette (`Ctrl+Shift+P`) and search for "Copilot: Rebuild workspace index." |
| NES doesn't trigger (Exercise 6) | Save the file after your manual edit, then move the cursor to the next function. NES needs a moment to detect the pattern. |

---

## 📝 Recap

In this chapter you:

1. **Analyzed code with `@workspace`** — fast local indexing gives the same quality answers as GitHub.com Chat
2. **Used Agent Mode for interactive multi-file editing** — watched the Agent edit models, routes, and exceptions in real-time
3. **Verified Custom Instructions compliance** — the same rules from Chapter 7 apply in VS Code (docstrings, type hints, custom exceptions, constants)
4. **Ran tests locally through the Agent** — experienced the write → test → fix feedback loop
5. **Understood Accept/Reject control** — each change is individually controllable
6. **(Optional) Tried Next Edit Suggestions** — pattern-based repetition for manual editing

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Interactive execution** | See every Agent action in real-time; Accept or Reject each change individually |
| **Instant feedback** | Local execution = immediate test results, no waiting for CI |
| **Custom Instructions consistency** | The same rules apply in VS Code as on GitHub.com — proven by structural markers |
| **Multi-file editing** | Agent edits models, routes, exceptions, and tests across files in a single session |
| **Terminal integration** | Agent runs commands (e.g., pytest) in the integrated terminal, acting on results |
| **NES complement** | Agent Mode for large tasks + NES for pattern-based repetition — use both |

---

**Next up:** [Chapter 10: Copilot CLI →](chapter-10-copilot-cli.md) — take Copilot into the terminal for DevOps workflows.
