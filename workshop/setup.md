# Workshop Setup Guide

> Complete these steps before starting the workshop. Estimated setup time: **~15 minutes**.
>
> This guide covers macOS, Linux, and Windows. OS-specific differences are noted where applicable.

---

## System Requirements

### Required Software

| Tool | Minimum Version | Check Command | Install Link |
|------|----------------|---------------|--------------|
| Python | 3.11+ | `python3 --version` | [python.org](https://www.python.org/downloads/) |
| pip | latest | `pip --version` | Included with Python |
| Git | 2.30+ | `git --version` | [git-scm.com](https://git-scm.com/downloads) |
| VS Code | Latest Insiders | `code-insiders --version` | [VS Code Insiders](https://code.visualstudio.com/insiders/) |
| GitHub CLI | 2.0+ | `gh --version` | [cli.github.com](https://cli.github.com/) |
| Docker | 20.10+ | `docker --version` | [docker.com](https://www.docker.com/get-started/) (Chapter 10 only) |

> **Note for Windows users:** Use `python` instead of `python3`. We recommend using Git Bash or WSL.

### Required Accounts & Access

| Requirement | Why | How to Verify |
|------------|-----|---------------|
| GitHub account | All exercises | `gh auth status` |
| GitHub Copilot (Business or Enterprise) | Coding Agent, Code Review | Check at [github.com/settings/copilot](https://github.com/settings/copilot) |
| Copilot Chat (GitHub.com) | Chapter 3, 7 | Open any repo and verify the Copilot icon is visible |

---

## Step 1: Fork and Clone the Repository

### 1-1. Fork the Repository

```bash
gh repo fork shinyay/agentic-github-workshop --clone=false
```

Or go to [github.com/shinyay/agentic-github-workshop](https://github.com/shinyay/agentic-github-workshop) and click the **Fork** button in the top right.

### 1-2. Clone Your Forked Repository

```bash
gh repo clone <your-username>/agentic-github-workshop
cd agentic-github-workshop
```

> Replace `<your-username>` with your GitHub username.

---

## Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

> **Tip:** We recommend using a virtual environment.
>
> ```bash
> # macOS / Linux
> python3 -m venv .venv
> source .venv/bin/activate
>
> # Windows (PowerShell)
> python -m venv .venv
> .venv\Scripts\Activate.ps1
> ```
>
> Activate the virtual environment, then run `pip install -r requirements.txt`.

Packages that will be installed:

- **FastAPI** 0.115.0 — Web framework
- **Uvicorn** 0.30.0 — ASGI server
- **Pydantic** 2.9.0 — Data validation

---

## Step 3: Verify the API Runs

### 3-1. Start the Server

```bash
uvicorn app.main:app --reload
```

### 3-2. Verify the Swagger UI

Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser and verify that the Swagger UI is displayed.

### 3-3. Test with curl

Open a separate terminal and run the following:

```bash
# Root endpoint
curl http://localhost:8000/
# Expected: {"message": "Welcome to the Todo API", "docs": "/docs"}
```

```bash
# Create a todo
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Test todo"}'
# Expected: 201 status code with a todo object
```

```bash
# List all todos
curl http://localhost:8000/todos
# Expected: An array containing the todo you created
```

> **Windows (PowerShell) users:** Use `Invoke-RestMethod` instead of `curl`, or run the commands from Git Bash.
>
> ```powershell
> Invoke-RestMethod -Uri http://localhost:8000/
> Invoke-RestMethod -Uri http://localhost:8000/todos -Method Post -ContentType "application/json" -Body '{"title": "Test todo"}'
> ```

### 3-4. Stop the Server

Stop the server with `Ctrl+C`.

---

## Step 4: Verify VS Code & Copilot

1. Open the repo in VS Code Insiders:

   ```bash
   code-insiders .
   ```

2. **Verify the Copilot extension:** Confirm the Copilot icon appears in the status bar. If it does not, install "GitHub Copilot" from the Extensions marketplace.

3. **Verify Copilot Chat:** Open Copilot Chat with `Ctrl+Shift+I` (macOS: `Cmd+Shift+I`), type the following, and verify you get a response:

   ```
   What is 2+2?
   ```

4. **Verify Agent Mode:** In the Chat input area, check that the mode selector allows you to select "Agent" mode.

---

## Step 5: Verify GitHub CLI

```bash
gh auth status
```

You should see output similar to the following:

```
✓ Logged in to github.com as <your-username> (...)
✓ Git operations for github.com configured to use https protocol.
✓ Token: gho_****
✓ Token scopes: gist, read:org, repo, workflow
```

If you are not logged in, run the following:

```bash
gh auth login
```

Follow the prompts and select `GitHub.com` → `HTTPS` → `Login with a web browser`.

---

## Step 6: Verify Copilot CLI

```bash
copilot --version
```

You should see a version number displayed.

### If Copilot CLI Is Not Installed

```bash
# Install as a GitHub CLI extension
gh extension install github/gh-copilot

# Verify installation
gh copilot --version
```

> **Note:** Copilot CLI requires an active GitHub Copilot subscription.

---

## Step 7: Verify Docker (Chapter 10 only)

> Docker is only used in Chapter 10. You can skip this step if you want to start with the other chapters first.

```bash
docker --version
# Expected: Docker version 20.10.x or higher

docker compose version
# Expected: Docker Compose version v2.x.x
```

If Docker is not installed, download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

---

## Smoke Test Checklist

Once all setup steps are complete, run through this final checklist:

- [ ] `python3 --version` shows 3.11+
- [ ] `pip install -r requirements.txt` completes successfully
- [ ] `uvicorn app.main:app --reload` starts the server
- [ ] [http://localhost:8000/docs](http://localhost:8000/docs) shows the Swagger UI
- [ ] `curl http://localhost:8000/` returns a valid response
- [ ] VS Code Insiders Copilot Chat responds to questions
- [ ] VS Code Insiders Agent Mode is selectable
- [ ] `gh auth status` shows you are authenticated
- [ ] `copilot --version` or `gh copilot --version` shows a version number
- [ ] `docker --version` shows 20.10+ (optional — Chapter 10 only)

---

## Common Issues

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'fastapi'` | Run `pip install -r requirements.txt`. If using a virtual environment, make sure it is activated. |
| Copilot Chat does not respond | Check your Copilot subscription at [github.com/settings/copilot](https://github.com/settings/copilot). |
| `gh auth status` shows not logged in | Run `gh auth login` and follow the prompts. |
| Port 8000 already in use | Kill the existing process or use a different port: `uvicorn app.main:app --reload --port 8001`. |
| Docker permission denied | Add your user to the `docker` group or use `sudo`: `sudo usermod -aG docker $USER` (re-login required). |
| VS Code does not show Agent Mode | Update VS Code Insiders and the Copilot extension to the latest version. |
| Windows: `python3` not found | Use the `python` command instead. If you installed Python from the Microsoft Store, `python3` may also work. |
| `gh extension install` fails | Verify `gh --version` is 2.0 or higher and authenticate with `gh auth login`. |

---

## Need Help?

If you run into issues that you cannot resolve, please reach out to the workshop facilitator for help.
