"""Tests for all Todo API endpoints."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app import database


@pytest.fixture(autouse=True)
def reset_db() -> None:
    """Reset the in-memory database before each test to ensure isolation."""
    database.reset_database()


client = TestClient(app)


# ---------------------------------------------------------------------------
# GET /
# ---------------------------------------------------------------------------

def test_root_returns_welcome_message() -> None:
    """GET / should return a welcome message and a docs link."""
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Welcome to the Todo API"
    assert "docs" in body


# ---------------------------------------------------------------------------
# GET /todos
# ---------------------------------------------------------------------------

def test_list_todos_with_empty_database_returns_empty_list() -> None:
    """GET /todos should return an empty list when no todos exist."""
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_list_todos_with_existing_items_returns_list() -> None:
    """GET /todos should return all todos that have been created."""
    client.post("/todos", json={"title": "First"})
    client.post("/todos", json={"title": "Second"})

    response = client.get("/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) == 2
    titles = {t["title"] for t in todos}
    assert titles == {"First", "Second"}


# ---------------------------------------------------------------------------
# GET /todos/{id}
# ---------------------------------------------------------------------------

def test_get_todo_with_valid_id_returns_todo() -> None:
    """GET /todos/{id} should return the todo that matches the given ID."""
    created = client.post("/todos", json={"title": "My Todo"}).json()
    todo_id = created["id"]

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["title"] == "My Todo"


def test_get_todo_with_invalid_id_returns_404() -> None:
    """GET /todos/{id} should return 404 when the todo does not exist."""
    response = client.get("/todos/9999")
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# POST /todos
# ---------------------------------------------------------------------------

def test_create_todo_with_valid_data_returns_201() -> None:
    """POST /todos with a valid payload should create a todo and return 201."""
    response = client.post("/todos", json={"title": "New Todo", "description": "Details"})
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "New Todo"
    assert body["description"] == "Details"
    assert body["completed"] is False
    assert "id" in body


def test_create_todo_with_missing_title_returns_422() -> None:
    """POST /todos without a title should be rejected with 422 Unprocessable Entity."""
    response = client.post("/todos", json={"description": "No title here"})
    assert response.status_code == 422


# ---------------------------------------------------------------------------
# PUT /todos/{id}
# ---------------------------------------------------------------------------

def test_update_todo_with_valid_id_returns_updated_todo() -> None:
    """PUT /todos/{id} should update an existing todo and return the updated data."""
    created = client.post("/todos", json={"title": "Original"}).json()
    todo_id = created["id"]

    response = client.put(
        f"/todos/{todo_id}",
        json={"title": "Updated", "completed": True},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Updated"
    assert body["completed"] is True


def test_update_todo_with_invalid_id_returns_404() -> None:
    """PUT /todos/{id} should return 404 when the todo does not exist."""
    response = client.put("/todos/9999", json={"title": "Doesn't matter"})
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# DELETE /todos/{id}
# ---------------------------------------------------------------------------

def test_delete_todo_with_valid_id_returns_204() -> None:
    """DELETE /todos/{id} should delete an existing todo and return 204 No Content."""
    created = client.post("/todos", json={"title": "To be deleted"}).json()
    todo_id = created["id"]

    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    # Confirm it is gone
    assert client.get(f"/todos/{todo_id}").status_code == 404


def test_delete_todo_with_invalid_id_returns_404() -> None:
    """DELETE /todos/{id} should return 404 when the todo does not exist."""
    response = client.delete("/todos/9999")
    assert response.status_code == 404
