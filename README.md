# Todo API

> A simple REST API for managing todo items, built with Python and FastAPI.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

A lightweight Todo REST API built with **FastAPI** and **Pydantic**. It provides full CRUD operations for managing todo items with in-memory storage — perfect for learning, prototyping, and demos.

---

## 🚀 Quick Start

**Prerequisites:**

- **Python 3.11+** (`python3 --version`)
- **pip** (`pip --version`)

### 1. Clone and install

```bash
git clone https://github.com/shinyay/demo-ghec.git
cd demo-ghec
pip install -r requirements.txt
```

### 2. Run the server

```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs to see the interactive API documentation.

---

## 💡 Overview

### Architecture

```
Client (curl / browser / frontend)
        │
        ▼
  ┌─────────────┐
  │  FastAPI     │  ← app/main.py (routes & error handling)
  │  Endpoints   │
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │  Pydantic    │  ← app/models.py (request/response schemas)
  │  Models      │
  └──────┬──────┘
         │
  ┌──────▼──────┐
  │  In-Memory   │  ← app/database.py (dict-based storage)
  │  Database    │
  └─────────────┘
```

---

## ✨ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/todos` | List all todos |
| `GET` | `/todos/{id}` | Get a specific todo |
| `POST` | `/todos` | Create a new todo |
| `PUT` | `/todos/{id}` | Update an existing todo |
| `DELETE` | `/todos/{id}` | Delete a todo |

---

## 📖 Usage Examples

### Create a todo

```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

### List all todos

```bash
curl http://localhost:8000/todos
```

### Update a todo

```bash
curl -X PUT http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

### Delete a todo

```bash
curl -X DELETE http://localhost:8000/todos/1
```

---

## 🧪 Running Tests

The test suite uses [pytest](https://docs.pytest.org/) and FastAPI's built-in `TestClient`.

```bash
# Install dependencies (includes test dependencies)
pip install -r requirements.txt

# Run all tests
pytest tests/ -v
```

Tests are located in the `tests/` directory and cover every API endpoint — including normal cases, empty results, validation errors, and 404 scenarios.

---

## 🏗️ Project Structure

```
demo-ghec/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and route handlers
│   ├── models.py         # Pydantic models for request/response
│   └── database.py       # In-memory data storage layer
├── tests/
│   ├── __init__.py
│   └── test_todo.py      # pytest unit tests for all API endpoints
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 📚 References

| Resource | Link |
|----------|------|
| FastAPI Documentation | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| Pydantic Documentation | [docs.pydantic.dev](https://docs.pydantic.dev) |
| Uvicorn | [uvicorn.org](https://www.uvicorn.org) |

---

## Licence

Released under the [MIT license](https://gist.githubusercontent.com/shinyay/56e54ee4c0e22db8211e05e70a63247e/raw/f3ac65a05ed8c8ea70b653875ccac0c6dbc10ba1/LICENSE)

## Author

- github: <https://github.com/shinyay>
- bluesky: <https://bsky.app/profile/yanashin.bsky.social>
- twitter: <https://twitter.com/yanashin18618>
- mastodon: <https://mastodon.social/@yanashin>
- linkedin: <https://www.linkedin.com/in/yanashin/>
