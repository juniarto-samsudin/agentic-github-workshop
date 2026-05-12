from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import TodoNotFoundError
from app.models import Todo, TodoCreate, TodoUpdate
from app import database as db

app = FastAPI(
    title="Todo API",
    description="A simple REST API for managing todos",
    version="1.0.0",
)

TODO_NOT_FOUND_BODY = {
    "error": {
        "code": "TODO_NOT_FOUND",
        "message": "Todo not found",
        "details": {},
    }
}


@app.exception_handler(TodoNotFoundError)
async def todo_not_found_handler(_request: Request, _exc: TodoNotFoundError) -> JSONResponse:
    """Return a unified 404 error response when a todo is not found.

    Args:
        _request: The incoming HTTP request (unused).
        _exc: The raised TodoNotFoundError instance (unused).

    Returns:
        A JSONResponse with status 404 and the unified error body.

    Example:
        curl -X GET http://localhost:8000/todos/9999
        # {"error": {"code": "TODO_NOT_FOUND", "message": "Todo not found", "details": {}}}
    """
    return JSONResponse(status_code=404, content=TODO_NOT_FOUND_BODY)


@app.get("/")
def root():
    return {"message": "Welcome to the Todo API", "docs": "/docs"}


@app.get("/todos", response_model=list[Todo])
def list_todos():
    return db.get_all_todos()


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = db.get_todo(todo_id)
    if todo is None:
        raise TodoNotFoundError()
    return todo


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(payload: TodoCreate):
    return db.create_todo(title=payload.title, description=payload.description)


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate):
    todo = db.update_todo(
        todo_id,
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
    )
    if todo is None:
        raise TodoNotFoundError()
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if not db.delete_todo(todo_id):
        raise TodoNotFoundError()
