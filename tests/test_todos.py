def test_list_todos_returns_200(client):
    response = client.get("/todos")
    assert response.status_code == 200


def test_list_todos_empty_initially(client):
    response = client.get("/todos")
    assert response.json() == []


def test_list_todos_returns_all_created(client):
    client.post("/todos", json={"title": "First"})
    client.post("/todos", json={"title": "Second"})
    response = client.get("/todos")
    titles = [t["title"] for t in response.json()]
    assert len(titles) == 2
    assert "First" in titles
    assert "Second" in titles


# ---------------------------------------------------------------------------
# GET /todos/{id}
# ---------------------------------------------------------------------------


def test_get_todo_returns_200(client):
    created = client.post("/todos", json={"title": "Test"}).json()
    response = client.get(f"/todos/{created['id']}")
    assert response.status_code == 200


def test_get_todo_returns_correct_payload(client):
    created = client.post("/todos", json={"title": "Test", "description": "Desc"}).json()
    response = client.get(f"/todos/{created['id']}")
    data = response.json()
    assert data["id"] == created["id"]
    assert data["title"] == "Test"
    assert data["description"] == "Desc"


def test_get_todo_returns_404_for_missing(client):
    response = client.get("/todos/9999")
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# POST /todos
# ---------------------------------------------------------------------------


def test_create_todo_returns_201(client):
    response = client.post("/todos", json={"title": "New todo"})
    assert response.status_code == 201


def test_create_todo_with_title_only(client):
    response = client.post("/todos", json={"title": "No description"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "No description"
    assert data["description"] is None


def test_create_todo_with_description(client):
    response = client.post("/todos", json={"title": "With desc", "description": "Details"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "With desc"
    assert data["description"] == "Details"


def test_create_todo_returns_generated_fields(client):
    response = client.post("/todos", json={"title": "Fields test"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data
    assert data["completed"] is False


# ---------------------------------------------------------------------------
# PUT /todos/{id}
# ---------------------------------------------------------------------------


def test_update_todo_returns_200(client):
    created = client.post("/todos", json={"title": "Original"}).json()
    response = client.put(f"/todos/{created['id']}", json={"title": "Updated"})
    assert response.status_code == 200


def test_update_todo_partial_update(client):
    created = client.post("/todos", json={"title": "Original", "description": "Desc"}).json()
    response = client.put(f"/todos/{created['id']}", json={"title": "Changed"})
    data = response.json()
    assert data["title"] == "Changed"
    assert data["description"] == "Desc"


def test_update_todo_can_complete(client):
    created = client.post("/todos", json={"title": "Task"}).json()
    response = client.put(f"/todos/{created['id']}", json={"completed": True})
    assert response.json()["completed"] is True


def test_update_todo_returns_404_for_missing(client):
    response = client.put("/todos/9999", json={"title": "Ghost"})
    assert response.status_code == 404


# ---------------------------------------------------------------------------
# DELETE /todos/{id}
# ---------------------------------------------------------------------------


def test_delete_todo_returns_204(client):
    created = client.post("/todos", json={"title": "Delete me"}).json()
    response = client.delete(f"/todos/{created['id']}")
    assert response.status_code == 204


def test_delete_todo_removes_from_list(client):
    created = client.post("/todos", json={"title": "Gone"}).json()
    client.delete(f"/todos/{created['id']}")
    response = client.get(f"/todos/{created['id']}")
    assert response.status_code == 404


def test_delete_todo_returns_404_for_missing(client):
    response = client.delete("/todos/9999")
    assert response.status_code == 404
