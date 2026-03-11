from datetime import datetime
from app.models import Todo

# In-memory storage
_todos: dict[int, Todo] = {}
_next_id: int = 1


def get_all_todos() -> list[Todo]:
    return list(_todos.values())


def get_todo(todo_id: int) -> Todo | None:
    return _todos.get(todo_id)


def create_todo(title: str, description: str | None = None) -> Todo:
    global _next_id
    now = datetime.utcnow()
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
    todo = _todos.get(todo_id)
    if todo is None:
        return None

    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    todo.updated_at = datetime.utcnow()

    _todos[todo_id] = todo
    return todo


def delete_todo(todo_id: int) -> bool:
    if todo_id in _todos:
        del _todos[todo_id]
        return True
    return False


def reset_database() -> None:
    global _next_id
    _todos.clear()
    _next_id = 1
