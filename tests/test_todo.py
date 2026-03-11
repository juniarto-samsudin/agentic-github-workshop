import pytest
from fastapi.testclient import TestClient

from app.main import app
from app import database as db


@pytest.fixture(autouse=True)
def reset_db():
    """Reset the in-memory database before each test."""
    db.reset_database()
    yield
    db.reset_database()


@pytest.fixture
def client():
    """Return a TestClient for the FastAPI app."""
    with TestClient(app) as c:
        yield c


# ---------------------------------------------------------------------------
# GET /todos
# ---------------------------------------------------------------------------

class TestListTodos:
    def test_list_todos_empty(self, client):
        response = client.get("/todos")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_todos_returns_all(self, client):
        client.post("/todos", json={"title": "First"})
        client.post("/todos", json={"title": "Second"})
        response = client.get("/todos")
        assert response.status_code == 200
        assert len(response.json()) == 2


# ---------------------------------------------------------------------------
# POST /todos
# ---------------------------------------------------------------------------

class TestCreateTodo:
    def test_create_todo_minimal(self, client):
        response = client.post("/todos", json={"title": "Buy milk"})
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Buy milk"
        assert data["description"] is None
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data

    def test_create_todo_with_description(self, client):
        response = client.post(
            "/todos",
            json={"title": "Buy groceries", "description": "Milk, eggs, bread"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Buy groceries"
        assert data["description"] == "Milk, eggs, bread"

    def test_create_todo_missing_title_returns_422(self, client):
        response = client.post("/todos", json={"description": "No title here"})
        assert response.status_code == 422

    def test_create_todo_empty_body_returns_422(self, client):
        response = client.post("/todos", json={})
        assert response.status_code == 422

    def test_create_todo_empty_string_title_returns_422(self, client):
        response = client.post("/todos", json={"title": ""})
        assert response.status_code == 422

    def test_create_todo_very_long_title(self, client):
        long_title = "a" * 1_000
        response = client.post("/todos", json={"title": long_title})
        assert response.status_code == 201
        assert response.json()["title"] == long_title


# ---------------------------------------------------------------------------
# GET /todos/{id}
# ---------------------------------------------------------------------------

class TestGetTodo:
    def test_get_existing_todo(self, client):
        created = client.post("/todos", json={"title": "Test todo"}).json()
        response = client.get(f"/todos/{created['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == created["id"]
        assert response.json()["title"] == "Test todo"

    def test_get_nonexistent_todo_returns_404(self, client):
        response = client.get("/todos/9999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Todo not found"


# ---------------------------------------------------------------------------
# PUT /todos/{id}
# ---------------------------------------------------------------------------

class TestUpdateTodo:
    def test_update_todo_title(self, client):
        created = client.post("/todos", json={"title": "Old title"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"title": "New title"}
        )
        assert response.status_code == 200
        assert response.json()["title"] == "New title"

    def test_update_todo_completed(self, client):
        created = client.post("/todos", json={"title": "Task"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"completed": True}
        )
        assert response.status_code == 200
        assert response.json()["completed"] is True

    def test_update_todo_description(self, client):
        created = client.post("/todos", json={"title": "Task"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"description": "New description"}
        )
        assert response.status_code == 200
        assert response.json()["description"] == "New description"

    def test_update_nonexistent_todo_returns_404(self, client):
        response = client.put("/todos/9999", json={"title": "Ghost"})
        assert response.status_code == 404
        assert response.json()["detail"] == "Todo not found"


# ---------------------------------------------------------------------------
# DELETE /todos/{id}
# ---------------------------------------------------------------------------

class TestDeleteTodo:
    def test_delete_existing_todo(self, client):
        created = client.post("/todos", json={"title": "To delete"}).json()
        response = client.delete(f"/todos/{created['id']}")
        assert response.status_code == 204

        # Verify that the todo no longer exists
        get_response = client.get(f"/todos/{created['id']}")
        assert get_response.status_code == 404

    def test_delete_nonexistent_todo_returns_404(self, client):
        response = client.delete("/todos/9999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Todo not found"

    def test_delete_same_todo_twice_returns_404_on_second(self, client):
        created = client.post("/todos", json={"title": "Delete me twice"}).json()
        first = client.delete(f"/todos/{created['id']}")
        assert first.status_code == 204
        second = client.delete(f"/todos/{created['id']}")
        assert second.status_code == 404
        assert second.json()["detail"] == "Todo not found"
