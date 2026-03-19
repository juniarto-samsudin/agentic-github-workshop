# Chapter 7: Context — Custom Instructions, Agents, and Spaces

> **Key takeaway:** Custom Instructions let you define team standards in a single file — and every Copilot feature (Chat, Coding Agent, Code Review) automatically follows those rules.

[← Chapter 6](chapter-06-review.md) | [Back to Act 1](README.md) | [Next: Chapter 8 →](chapter-08-governance.md)

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:
- [ ] Examine the Custom Instructions file and understand each rule
- [ ] Verify that Chat-generated code follows Custom Instructions (not just existing code patterns)
- [ ] Understand Custom Agent selection for Issue assignment
- [ ] Explore Copilot Spaces for cross-repository context

## 📋 Prerequisites

- [ ] Completed [Workshop Setup](../setup.md)
- [ ] Familiar with the `app/` code structure (from earlier chapters)

## ⏱️ Estimated Time: ~10 minutes

---

## Overall Flow

```
Examine Custom Instructions → Verify in Chat → Agent Selection → Tour Spaces
           ↓                        ↓                 ↓                ↓
  .github/ file rules       Rules appear in output   Pick an Agent   Cross-repo context
```

---

## Exercise 1: Examine Custom Instructions

### Background

Custom Instructions live in `.github/copilot-instructions.md` at the root of your repository. Every Copilot feature — Chat, Coding Agent, and Code Review — reads this file and applies the rules automatically. This is how you encode team standards once and have them enforced everywhere.

### Instructions

1. Open your repository on GitHub.com
2. Navigate to **Code** tab → `.github/copilot-instructions.md`
3. Read through the file and identify the key rules
4. Compare each rule against the **current code** in `app/` — note which rules the existing code does NOT follow:

   | Rule | Current Code Follows It? | Effect When Applied |
   |------|--------------------------|---------------------|
   | Google-style docstrings with Args/Returns/Raises/Example sections | ❌ No docstrings at all | Docstrings appear on all functions |
   | Structured error format `{"error": {"code":…, "message":…, "details":…}}` | ❌ Uses `HTTPException` directly | New error shape in responses |
   | Pagination parameters (`skip`, `limit`) on list endpoints | ❌ No pagination | New parameters on list endpoints |
   | `X-Total-Count` header in list responses | ❌ Not present | New header in list responses |
   | Custom exception classes instead of `HTTPException` | ❌ Uses `HTTPException` directly | New exception module created |
   | Test naming: `test_<target>_<condition>_<expected>` | ❌ No tests exist | Tests follow the naming convention |
   | Request logging with specific format | ❌ No logging | Log output appears |

### ✅ Verification

- [ ] You found the `.github/copilot-instructions.md` file in the repository
- [ ] You can identify at least **3 rules** that the current `app/` code does NOT follow
- [ ] You understand that these rules will apply to Chat, Coding Agent, AND Code Review

<details>
<summary>💡 Instructor Notes</summary>

The critical insight here is the **gap between instructions and current code**. The existing code has none of these features — no docstrings, no pagination, no structured errors, no logging. This gap is intentional: it makes it easy to prove that Copilot follows the instructions rather than just mimicking existing patterns.

Point out the file location: `.github/copilot-instructions.md` — this is a convention. Just placing the file in this path is enough; no additional configuration is required.

</details>

---

## Exercise 2: Verify Custom Instructions in Chat Output

### Background

This exercise proves that Custom Instructions actively influence Copilot's output. Since the current code has none of the features specified in the instructions, any features that appear in Chat-generated code must come from the instructions — not from pattern-matching the existing codebase.

### Instructions

1. Open **Copilot Chat** on GitHub.com
2. Ask:
   > "Write a search endpoint for /todos that filters by keyword"
3. Examine the generated code carefully for Custom Instructions compliance:

   ```python
   @app.get("/todos/search", response_model=list[Todo])
   def search_todos(
       keyword: str,
       skip: int = 0,          # ← Pagination (Custom Instructions)
       limit: int = 20,        # ← Default 20 (Custom Instructions)
   ) -> list[Todo]:
       """Search todos by keyword.

       Args:
           keyword: Search keyword to filter todos.
           skip: Number of records to skip.
           limit: Maximum number of records to return.

       Returns:
           List of Todo items matching the keyword.

       Raises:
           AppError: If the search operation fails.

       Example:
           curl http://localhost:8000/todos/search?keyword=meeting
       """
   ```

4. Check for these markers — each one comes from Custom Instructions, NOT from the existing code:

   - ✅ **Google-style docstring** with Args / Returns / Raises / Example sections
   - ✅ **Pagination parameters** (`skip: int = 0`, `limit: int = 20`)
   - ✅ **Type hints** on all parameters and return value
   - ✅ **`response_model`** specified on the decorator
   - ✅ **`limit` default of 20** (the exact value from Custom Instructions)

### ✅ Verification

- [ ] Chat generated code that includes a Google-style docstring
- [ ] Pagination parameters (`skip`, `limit`) appear — even though current code has none
- [ ] You can identify at least **3 features** in the generated code that do NOT exist in the current codebase
- [ ] You understand that these features come from Custom Instructions, not from existing patterns

<details>
<summary>💡 Instructor Notes</summary>

This is the key "aha" moment of the chapter. Drive the point home:

> "The key insight — Copilot follows Custom Instructions OVER existing code patterns. The current code has no docstrings, no pagination, no structured errors. Yet the generated code has all of them. This proves that Custom Instructions actively shape the output."

If the generated code doesn't include ALL the expected features, that's okay — highlight the ones that ARE present. Custom Instructions are influential but not deterministic. You can mention:
- "In Coding Agent mode, compliance tends to be even stricter since the Agent reads the instructions as part of its planning phase."

</details>

---

## Exercise 3: Explore Custom Agent Selection

### Background

When assigning Copilot to an Issue, you may have the option to choose which Agent handles the task. This is where teams can configure specialized agents — for example, a FastAPI expert, a security specialist, or a test-focused agent.

### Instructions

1. Create a new Issue or open an existing one in your repository
2. Click **Assignees** in the right sidebar
3. Look for **Copilot** in the assignee list
4. Note: depending on your organization configuration, you may see options to select different Agents:
   - Default Copilot Agent
   - Custom agents configured for your organization or repository

5. Consider the possibilities:
   - A **FastAPI expert** Agent for backend API work
   - A **security specialist** Agent for vulnerability fixes
   - A **test expert** Agent for comprehensive test generation
   - Each agent can have different skills and instructions

### ✅ Verification

- [ ] You can see the Agent selection interface (or understand where it would appear)
- [ ] You understand that Custom Agents = specialized experts selectable per task

> 💡 **Note:** You do not need to actually assign an Agent here — just explore the selection interface.

<details>
<summary>💡 Instructor Notes</summary>

> "If Custom Instructions are the 'rulebook,' Custom Agents are 'specialists who deeply know those rules.' You can set up different agents per team or per project — a frontend agent, a security agent, a testing agent — each optimized for their domain."

If Custom Agent selection is not visible for participants:
- This feature depends on organization/repository configuration
- Explain the concept and show the interface location
- Focus on the value: specialized agents for specialized tasks

</details>

---

## Exercise 4: Tour Copilot Spaces

### Background

Custom Instructions provide per-repository context. Copilot Spaces extend that concept across repository boundaries — you can group multiple repositories, add documentation, and share knowledge bases with your team.

### Instructions

1. Navigate to **Copilot** > **Spaces** on GitHub.com (if available in your plan)
2. Explore the Spaces UI:

   - 📁 **Adding repositories** — group multiple repos into a single Space
   - 📄 **Adding documentation** — include design docs, specifications, and architecture diagrams as context
   - 👥 **Team sharing** — share a Space with your team so everyone's Copilot has the same organizational knowledge

3. Think about how this applies to the workshop app:

   > "If this Todo API were one microservice among many, you could add all related service repositories to a Space. Copilot would then understand cross-service dependencies when generating code or reviewing PRs."

### ✅ Verification

- [ ] You can navigate the Spaces UI (or understand the concept if not yet available)
- [ ] You understand how Spaces differ from Custom Instructions (per-repo vs. cross-repo context)

<details>
<summary>💡 Instructor Notes</summary>

> "Custom Instructions are per-repository context. Spaces are context that spans across repositories. Together, they let you give Copilot knowledge of your entire organization's architecture."

If Spaces is not available for participants:
- This feature is currently in preview and may not be available in all plans
- Explain the concept: "Imagine giving Copilot a map of your entire microservice architecture — every service, every API contract, every shared library — so it can generate code that fits the bigger picture."
- Focus on the value proposition rather than hands-on exploration

</details>

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Chat doesn't fully follow Custom Instructions | Highlight the parts that ARE followed; instructions are influential but not deterministic. Coding Agent mode tends to follow them more strictly. |
| Generated code uses `HTTPException` instead of custom exceptions | Some rules are followed more consistently than others. Point out the rules that ARE applied (docstrings, pagination, etc.) |
| Custom Agent selection not visible | This depends on organization configuration. Explain the concept and its value. |
| Spaces not available in your plan | Currently in preview. Explain the concept: cross-repo context for organizational knowledge. |
| Custom Instructions file not found | Verify the file exists at `.github/copilot-instructions.md` — the path must be exact. |

---

## 📝 Chapter Recap

In this chapter, you:
- Examined the **Custom Instructions** file and identified rules the current code does not follow
- Verified that **Chat-generated code** includes features from Custom Instructions — proving it follows instructions over existing patterns
- Explored **Custom Agent selection** for assigning specialized agents to Issues
- Toured **Copilot Spaces** for cross-repository context sharing

### Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Write once, apply everywhere** | A single `.github/copilot-instructions.md` file governs Chat, Coding Agent, and Code Review |
| **Instructions override existing patterns** | New rules appear in generated code even when the current codebase doesn't use them |
| **Structural proof markers** | Docstrings, pagination, error format — visible evidence that instructions are working |
| **Custom Agents** | Specialized experts selectable per task during Issue assignment |
| **Copilot Spaces** | Cross-repository context — give Copilot organizational knowledge beyond a single repo |

---

**Next:** [Chapter 8: Governance →](chapter-08-governance.md) — Monitor and steer Agent tasks through Mission Control.
