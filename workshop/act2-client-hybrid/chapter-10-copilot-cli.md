---
layout: step
title: "Copilot CLI — Terminal-First Development"
step_number: 8
estimated_minutes: 12
permalink: /chapter/10/
---

# Chapter 10: Copilot CLI — Terminal-First Development

> **Key takeaway:** Copilot CLI brings the full Copilot experience to the terminal — analyze projects, generate code, build, test, and commit without leaving the command line.

[← Chapter 9](chapter-09-vscode-agent.md) | [Back to Act 2](README.md) | [Next: Chapter 11 →](chapter-11-hybrid-workflow.md)

## 🎯 Learning Objectives
- [ ] Use Copilot CLI to analyze a project's structure and dependencies
- [ ] Generate a production-ready Dockerfile from natural language
- [ ] Generate a docker-compose.yml with development configuration
- [ ] Build, run, and test containers through the CLI
- [ ] Create meaningful Git commits with auto-generated messages

## 📋 Prerequisites
- [ ] Copilot CLI installed (`copilot --version`)
- [ ] Docker installed and running (`docker info`)
- [ ] Terminal open in the repository root directory

## ⏱️ Estimated Time: ~12 minutes

---

## Three Surfaces at a Glance

Before diving in, note where Copilot CLI fits among Copilot's three surfaces:

| | GitHub.com Chat | VS Code Chat / Agent | **Copilot CLI** |
|---|---|---|---|
| **Interface** | Browser | Editor | Terminal |
| **Interaction** | Issue → Agent | Agent Mode → local files | Natural language → execution |
| **Feedback** | Results in PR | Instant in-editor | Instant in-terminal |
| **Best for** | Managers & PMs | Daily development | DevOps & CLI lovers |

---

## Exercise 1: Analyze the Project

### Background
Copilot CLI can read your project's files and provide intelligent analysis — right from the terminal. No browser or IDE needed.

### Instructions
1. Open a terminal and navigate to your project directory
2. Ask Copilot CLI to analyze your project:

   ```
   "What do I need to containerize this project? Analyze the file structure and dependencies."
   ```

3. Review the CLI's response — it should identify:
   - `requirements.txt` and its dependencies
   - FastAPI + Uvicorn as the application framework
   - The need for a `Dockerfile` and `docker-compose.yml`
   - Port 8000 as the application port

### ✅ Verification
- [ ] CLI correctly identifies the project as a FastAPI application
- [ ] CLI notes `requirements.txt` as the dependency source
- [ ] CLI recommends creating Dockerfile and docker-compose.yml
- [ ] CLI identifies port 8000

<details>
<summary>💡 Instructor Notes</summary>

"Copilot CLI is terminal-native. It works without a browser or IDE — even over SSH to a remote server. This makes it ideal for DevOps workflows, server administration, and headless environments."

Let participants take a moment to explore the CLI response. Point out that it reads the actual project files — this isn't generic advice but context-aware analysis.

</details>

---

## Exercise 2: Generate a Dockerfile

### Background
Instead of manually writing Docker configuration, you can describe what you want in natural language and let Copilot CLI generate best-practice files.

### Instructions
1. Ask Copilot CLI to create a Dockerfile:

   ```
   "Create a production-ready Dockerfile for this FastAPI app. Include multi-stage build, non-root user, and health check."
   ```

2. Review the generated Dockerfile. It should include:

   ```dockerfile
   # Build stage
   FROM python:3.11-slim AS builder
   WORKDIR /build
   COPY requirements.txt .
   RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

   # Production stage
   FROM python:3.11-slim
   # Non-root user
   RUN useradd --create-home appuser
   WORKDIR /home/appuser/app
   COPY --from=builder /install /usr/local
   COPY app/ ./app/
   USER appuser
   EXPOSE 8000
   HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
       CMD curl -f http://localhost:8000/ || exit 1
   CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

3. Confirm that the CLI writes the file to disk

### ✅ Verification
- [ ] `Dockerfile` exists in the project root
- [ ] Contains a multi-stage build (builder + production stages)
- [ ] Creates and uses a non-root user (`appuser`)
- [ ] Includes a `HEALTHCHECK` directive
- [ ] `CMD` runs uvicorn on port 8000

<details>
<summary>💡 Instructor Notes</summary>

"Natural language → best-practice Dockerfile. You said 'multi-stage build, non-root user, health check' and got a production-ready Dockerfile without memorizing Docker syntax."

Highlight the security best practices the CLI included automatically:
- Multi-stage build keeps the final image small (no build tools)
- Non-root user follows the principle of least privilege
- Health check enables container orchestration readiness

</details>

---

## Exercise 3: Generate docker-compose.yml

### Background
Now extend the setup with a docker-compose configuration that includes development-friendly features like hot-reload.

### Instructions
1. Ask Copilot CLI:

   ```
   "Create a docker-compose.yml for this Dockerfile. Include development hot-reload configuration."
   ```

2. Review the generated file. It should include:

   ```yaml
   services:
     api:
       build: .
       ports:
         - "8000:8000"
       volumes:
         - ./app:/home/appuser/app/app  # Hot-reload for development
       environment:
         - UVICORN_RELOAD=true
       healthcheck:
         test: ["CMD", "curl", "-f", "http://localhost:8000/"]
         interval: 30s
         timeout: 5s
         retries: 3
   ```

3. Confirm that the CLI writes the file to disk

### ✅ Verification
- [ ] `docker-compose.yml` exists in the project root
- [ ] Port mapping is `8000:8000`
- [ ] Volume mount enables hot-reload of the `app/` directory
- [ ] Health check is configured

<details>
<summary>💡 Instructor Notes</summary>

"Notice that the CLI understood the project context — it got the port number, the app directory path, and the volume mount correct without you specifying them. It read the codebase before generating the config."

</details>

---

## Exercise 4: Build and Test

### Background
Copilot CLI doesn't just generate code — it can also help you build, run, and verify your containers in one flow.

### Instructions
1. Ask Copilot CLI:

   ```
   "Build the Docker image, start the container, and verify the health check passes."
   ```

2. Run the suggested commands (or let the CLI execute them):

   ```bash
   # Build the image
   docker compose build

   # Start the container in detached mode
   docker compose up -d

   # Test the root endpoint
   curl http://localhost:8000/

   # Test the todos endpoint
   curl http://localhost:8000/todos

   # Clean up
   docker compose down
   ```

3. Observe the output at each step — the API should respond successfully

### ✅ Verification
- [ ] `docker compose build` completes without errors
- [ ] `docker compose up -d` starts the container
- [ ] `curl http://localhost:8000/` returns a response
- [ ] `curl http://localhost:8000/todos` returns a JSON response
- [ ] `docker compose down` stops the container cleanly

<details>
<summary>💡 Instructor Notes</summary>

"The CLI handles the full cycle: code generation → build → test → verification. You haven't left the terminal once. For DevOps workflows, this is extremely powerful — containerization from zero to verified in minutes."

If Docker is slow to build, explain the multi-stage build process while waiting. Point out the layer caching that will make subsequent builds faster.

</details>

---

## Exercise 5: Commit with Auto-Generated Message

### Background
Copilot CLI can also handle Git operations — staging files and generating meaningful commit messages based on the actual changes.

### Instructions
1. Ask Copilot CLI:

   ```
   "Stage the new files and commit with an appropriate message."
   ```

2. The CLI should execute something like:

   ```bash
   git add Dockerfile docker-compose.yml
   git commit -m "Add Dockerfile and docker-compose.yml for containerization

   - Multi-stage build for smaller image size
   - Non-root user for security
   - Health check endpoint configuration
   - Development hot-reload support via docker-compose"
   ```

3. Review the generated commit message

### ✅ Verification
- [ ] New files are staged (`git status` shows them committed)
- [ ] Commit message accurately summarizes what was added
- [ ] Commit message includes details about key features (multi-stage, non-root, health check)

<details>
<summary>💡 Instructor Notes</summary>

"Even the commit message is auto-generated. The CLI understands *what* changed and *why*, producing a meaningful commit history. The entire cycle — analysis → generation → build → test → commit — completed without leaving the terminal."

</details>

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Docker not installed | Skip Exercise 4 — review the generated Dockerfile and docker-compose.yml instead |
| Docker permission denied | Add your user to the docker group: `sudo usermod -aG docker $USER` (then restart terminal) |
| Port 8000 already in use | Stop the other service, or edit `docker-compose.yml` to use a different port (e.g., `8001:8000`) |
| Copilot CLI not responding | Verify with `copilot --version` — try restarting the terminal if it hangs |
| Container build fails | Check that Dockerfile paths match the actual project structure (`app/`, `requirements.txt`) |
| Health check fails | Ensure the app has a root endpoint (`/`) that returns a response |

---

## 📝 Recap

In this chapter you completed a **full development cycle entirely in the terminal**:

1. **Analyzed** the project structure and dependencies
2. **Generated** a production-ready Dockerfile with best practices
3. **Generated** a docker-compose.yml with development configuration
4. **Built and tested** the container to verify everything works
5. **Committed** with an auto-generated, meaningful commit message

## 🔑 Key Concepts

| Concept | What It Means |
|---------|--------------|
| **Terminal-complete workflow** | No browser or IDE needed — works over SSH too |
| **Natural language → execution** | Describe your intent, get best-practice output |
| **Context-aware generation** | CLI reads the project to generate correct configs |
| **Build & test integration** | From code generation through deployment verification in one flow |
| **Git integration** | Meaningful auto-generated commit messages |
| **DevOps strength** | Ideal for Dockerfiles, CI/CD, shell scripts, infrastructure configs |

---

**Next up:** [Chapter 11: Hybrid Workflow →](chapter-11-hybrid-workflow.md) — Combine CLI, Cloud, and VS Code in a relay development pattern.
