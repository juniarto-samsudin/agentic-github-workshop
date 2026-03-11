"""Todo APIのインメモリデータベースモジュール。

辞書ベースのストレージでTodoデータのCRUD操作を提供する。
"""

from datetime import datetime, UTC

from app.models import Todo

# インメモリストレージ
_todos: dict[int, Todo] = {}
_next_id: int = 1

# ページネーション定数
DEFAULT_LIMIT: int = 20
MAX_LIMIT: int = 100


def get_all_todos(skip: int = 0, limit: int = DEFAULT_LIMIT) -> tuple[list[Todo], int]:
    """全Todoを取得する（ページネーション対応）。

    Args:
        skip: スキップするアイテム数
        limit: 取得する最大アイテム数

    Returns:
        Todoリストと全件数のタプル
    """
    all_items = list(_todos.values())
    total = len(all_items)
    return all_items[skip : skip + limit], total


def get_todo(todo_id: int) -> Todo | None:
    """指定されたIDのTodoを取得する。

    Args:
        todo_id: 取得するTodoのID

    Returns:
        Todoオブジェクト。見つからない場合はNone
    """
    return _todos.get(todo_id)


def create_todo(title: str, description: str | None = None) -> Todo:
    """新しいTodoを作成する。

    Args:
        title: Todoのタイトル
        description: Todoの説明（任意）

    Returns:
        作成されたTodoオブジェクト
    """
    global _next_id
    now = datetime.now(UTC)
    todo = Todo(
        id=_next_id,
        title=title,
        description=description,
        completed=False,
        created_at=now,
        updated_at=now,
    )
    _todos[_next_id] = todo
    _next_id += 1
    return todo


def update_todo(
    todo_id: int,
    title: str | None = None,
    description: str | None = None,
    completed: bool | None = None,
) -> Todo | None:
    """指定されたIDのTodoを更新する。

    Args:
        todo_id: 更新するTodoのID
        title: 更新するタイトル
        description: 更新する説明
        completed: 更新する完了状態

    Returns:
        更新されたTodoオブジェクト。見つからない場合はNone
    """
    todo = _todos.get(todo_id)
    if todo is None:
        return None

    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    todo.updated_at = datetime.now(UTC)

    _todos[todo_id] = todo
    return todo


def delete_todo(todo_id: int) -> bool:
    """指定されたIDのTodoを削除する。

    Args:
        todo_id: 削除するTodoのID

    Returns:
        削除に成功した場合はTrue、見つからない場合はFalse
    """
    if todo_id in _todos:
        del _todos[todo_id]
        return True
    return False


def reset_database() -> None:
    """データベースを初期状態にリセットする。

    テスト用にすべてのデータをクリアし、IDカウンターをリセットする。
    """
    global _next_id
    _todos.clear()
    _next_id = 1
