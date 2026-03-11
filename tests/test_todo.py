"""Todo APIのユニットテスト。

全エンドポイントの正常系・異常系・エッジケースをカバーする。
"""

import pytest
from fastapi.testclient import TestClient

from app import database as db
from app.main import app

# テスト用定数
NONEXISTENT_TODO_ID: int = 9999
LONG_TITLE_LENGTH: int = 1_000


@pytest.fixture(autouse=True)
def reset_db():
    """各テスト前後にインメモリデータベースをリセットする。"""
    db.reset_database()
    yield
    db.reset_database()


@pytest.fixture
def client():
    """FastAPIアプリのTestClientを返す。"""
    with TestClient(app) as c:
        yield c


# ---------------------------------------------------------------------------
# GET /
# ---------------------------------------------------------------------------


class TestRoot:
    def test_root_returns_welcome_message(self, client: TestClient) -> None:
        """ルートエンドポイントがウェルカムメッセージを返すことを確認する。"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Welcome to the Todo API"
        assert data["docs"] == "/docs"


# ---------------------------------------------------------------------------
# GET /todos
# ---------------------------------------------------------------------------


class TestListTodos:
    def test_list_todos_with_empty_db_returns_empty_list(self, client: TestClient) -> None:
        """データベースが空の場合、空リストが返ることを確認する。"""
        response = client.get("/todos")
        assert response.status_code == 200
        assert response.json() == []
        assert response.headers["X-Total-Count"] == "0"

    def test_list_todos_with_multiple_items_returns_all(self, client: TestClient) -> None:
        """複数のTodoが登録されている場合、全件返ることを確認する。"""
        client.post("/todos", json={"title": "First"})
        client.post("/todos", json={"title": "Second"})
        response = client.get("/todos")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.headers["X-Total-Count"] == "2"

    def test_list_todos_with_pagination_returns_subset(self, client: TestClient) -> None:
        """ページネーションパラメータで部分的な結果が返ることを確認する。"""
        for i in range(5):
            client.post("/todos", json={"title": f"Todo {i}"})
        response = client.get("/todos", params={"skip": 1, "limit": 2})
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.headers["X-Total-Count"] == "5"

    def test_list_todos_with_skip_beyond_total_returns_empty(self, client: TestClient) -> None:
        """skipが全件数を超える場合、空リストが返ることを確認する。"""
        client.post("/todos", json={"title": "Only one"})
        response = client.get("/todos", params={"skip": 10})
        assert response.status_code == 200
        assert response.json() == []
        assert response.headers["X-Total-Count"] == "1"


# ---------------------------------------------------------------------------
# POST /todos
# ---------------------------------------------------------------------------


class TestCreateTodo:
    def test_create_todo_with_title_only_returns_201(self, client: TestClient) -> None:
        """タイトルのみでTodoを作成できることを確認する。"""
        response = client.post("/todos", json={"title": "Buy milk"})
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Buy milk"
        assert data["description"] is None
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data
        assert "updated_at" in data

    def test_create_todo_with_description_returns_201(self, client: TestClient) -> None:
        """タイトルと説明でTodoを作成できることを確認する。"""
        response = client.post(
            "/todos",
            json={"title": "Buy groceries", "description": "Milk, eggs, bread"},
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Buy groceries"
        assert data["description"] == "Milk, eggs, bread"

    def test_create_todo_without_title_returns_422(self, client: TestClient) -> None:
        """タイトルなしでPOSTした場合、422が返ることを確認する。"""
        response = client.post("/todos", json={"description": "No title here"})
        assert response.status_code == 422

    def test_create_todo_with_empty_body_returns_422(self, client: TestClient) -> None:
        """空のJSONボディでPOSTした場合、422が返ることを確認する。"""
        response = client.post("/todos", json={})
        assert response.status_code == 422

    def test_create_todo_with_empty_title_returns_422(self, client: TestClient) -> None:
        """空文字列のタイトルでPOSTした場合、422が返ることを確認する。"""
        response = client.post("/todos", json={"title": ""})
        assert response.status_code == 422

    def test_create_todo_with_very_long_title_returns_201(self, client: TestClient) -> None:
        """非常に長いタイトル（1000文字以上）でTodoを作成できることを確認する。"""
        long_title = "a" * LONG_TITLE_LENGTH
        response = client.post("/todos", json={"title": long_title})
        assert response.status_code == 201
        assert response.json()["title"] == long_title


# ---------------------------------------------------------------------------
# GET /todos/{id}
# ---------------------------------------------------------------------------


class TestGetTodo:
    def test_get_todo_with_valid_id_returns_200(self, client: TestClient) -> None:
        """存在するIDでTodoを取得できることを確認する。"""
        created = client.post("/todos", json={"title": "Test todo"}).json()
        response = client.get(f"/todos/{created['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == created["id"]
        assert response.json()["title"] == "Test todo"

    def test_get_todo_with_invalid_id_returns_404(self, client: TestClient) -> None:
        """存在しないIDで404とエラーレスポンスが返ることを確認する。"""
        response = client.get(f"/todos/{NONEXISTENT_TODO_ID}")
        assert response.status_code == 404
        error = response.json()["error"]
        assert error["code"] == "TODO_NOT_FOUND"
        assert error["details"]["todo_id"] == NONEXISTENT_TODO_ID


# ---------------------------------------------------------------------------
# PUT /todos/{id}
# ---------------------------------------------------------------------------


class TestUpdateTodo:
    def test_update_todo_title_with_valid_id_returns_200(self, client: TestClient) -> None:
        """タイトルを更新できることを確認する。"""
        created = client.post("/todos", json={"title": "Old title"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"title": "New title"}
        )
        assert response.status_code == 200
        assert response.json()["title"] == "New title"

    def test_update_todo_completed_with_valid_id_returns_200(self, client: TestClient) -> None:
        """完了状態を更新できることを確認する。"""
        created = client.post("/todos", json={"title": "Task"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"completed": True}
        )
        assert response.status_code == 200
        assert response.json()["completed"] is True

    def test_update_todo_description_with_valid_id_returns_200(self, client: TestClient) -> None:
        """説明を更新できることを確認する。"""
        created = client.post("/todos", json={"title": "Task"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"description": "New description"}
        )
        assert response.status_code == 200
        assert response.json()["description"] == "New description"

    def test_update_todo_with_invalid_id_returns_404(self, client: TestClient) -> None:
        """存在しないIDで更新した場合、404が返ることを確認する。"""
        response = client.put(
            f"/todos/{NONEXISTENT_TODO_ID}", json={"title": "Ghost"}
        )
        assert response.status_code == 404
        error = response.json()["error"]
        assert error["code"] == "TODO_NOT_FOUND"
        assert error["details"]["todo_id"] == NONEXISTENT_TODO_ID

    def test_update_todo_with_empty_title_returns_422(self, client: TestClient) -> None:
        """空文字列のタイトルで更新した場合、422が返ることを確認する。"""
        created = client.post("/todos", json={"title": "Task"}).json()
        response = client.put(
            f"/todos/{created['id']}", json={"title": ""}
        )
        assert response.status_code == 422


# ---------------------------------------------------------------------------
# DELETE /todos/{id}
# ---------------------------------------------------------------------------


class TestDeleteTodo:
    def test_delete_todo_with_valid_id_returns_204(self, client: TestClient) -> None:
        """存在するTodoを削除できることを確認する。"""
        created = client.post("/todos", json={"title": "To delete"}).json()
        response = client.delete(f"/todos/{created['id']}")
        assert response.status_code == 204

        # 削除後に取得すると404が返ることを確認
        get_response = client.get(f"/todos/{created['id']}")
        assert get_response.status_code == 404

    def test_delete_todo_with_invalid_id_returns_404(self, client: TestClient) -> None:
        """存在しないIDで削除した場合、404が返ることを確認する。"""
        response = client.delete(f"/todos/{NONEXISTENT_TODO_ID}")
        assert response.status_code == 404
        error = response.json()["error"]
        assert error["code"] == "TODO_NOT_FOUND"
        assert error["details"]["todo_id"] == NONEXISTENT_TODO_ID

    def test_delete_todo_twice_returns_404_on_second(self, client: TestClient) -> None:
        """同じTodoを2回削除した場合、2回目に404が返ることを確認する。"""
        created = client.post("/todos", json={"title": "Delete me twice"}).json()
        first = client.delete(f"/todos/{created['id']}")
        assert first.status_code == 204
        second = client.delete(f"/todos/{created['id']}")
        assert second.status_code == 404
        error = second.json()["error"]
        assert error["code"] == "TODO_NOT_FOUND"
