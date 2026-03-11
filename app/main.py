"""Todo APIのメインモジュール。

FastAPIアプリケーションのルート定義とエラーハンドリングを提供する。
"""

import logging
import time

from fastapi import FastAPI, Query, Request, Response
from fastapi.responses import JSONResponse

from app import database as db
from app.exceptions import AppException, TodoNotFoundException
from app.models import ErrorResponse, RootResponse, Todo, TodoCreate, TodoUpdate

# ロガー設定
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Todo API",
    description="Todo管理のためのシンプルなREST API",
    version="1.0.0",
)


@app.middleware("http")
async def logging_middleware(request: Request, call_next) -> Response:
    """リクエストのログを出力するミドルウェア。

    Args:
        request: HTTPリクエスト
        call_next: 次のミドルウェアまたはルートハンドラ

    Returns:
        HTTPレスポンス
    """
    start_time = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start_time) * 1000
    logger.info(
        "[%s] %s - %s (%.1fms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    """カスタム例外を統一エラーフォーマットで返すハンドラ。

    Args:
        request: HTTPリクエスト
        exc: 発生したアプリケーション例外

    Returns:
        統一フォーマットのJSONエラーレスポンス
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details,
            }
        },
    )


@app.get("/", response_model=RootResponse)
def root() -> dict:
    """ルートエンドポイント。ウェルカムメッセージを返す。

    Returns:
        ウェルカムメッセージとドキュメントパス
    """
    return {"message": "Welcome to the Todo API", "docs": "/docs"}


@app.get("/todos", response_model=list[Todo])
def list_todos(
    skip: int = Query(default=0, ge=0, description="スキップするアイテム数"),
    limit: int = Query(
        default=db.DEFAULT_LIMIT,
        ge=1,
        le=db.MAX_LIMIT,
        description="取得する最大アイテム数",
    ),
) -> Response:
    """全Todoをリストで取得する（ページネーション対応）。

    Args:
        skip: スキップするアイテム数
        limit: 取得する最大アイテム数（デフォルト20、最大100）

    Returns:
        Todoリストと総件数ヘッダーを含むレスポンス
    """
    todos, total = db.get_all_todos(skip=skip, limit=limit)
    return JSONResponse(
        content=[todo.model_dump(mode="json") for todo in todos],
        headers={"X-Total-Count": str(total)},
    )


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    """指定されたIDのTodoを取得する。

    Args:
        todo_id: 取得するTodoのID

    Returns:
        Todoオブジェクト

    Raises:
        TodoNotFoundException: 指定されたIDのTodoが見つからない場合
    """
    todo = db.get_todo(todo_id)
    if todo is None:
        raise TodoNotFoundException(todo_id)
    return todo


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(payload: TodoCreate) -> Todo:
    """新しいTodoを作成する。

    Args:
        payload: Todo作成リクエストデータ

    Returns:
        作成されたTodoオブジェクト
    """
    return db.create_todo(title=payload.title, description=payload.description)


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate) -> Todo:
    """指定されたIDのTodoを更新する。

    Args:
        todo_id: 更新するTodoのID
        payload: Todo更新リクエストデータ

    Returns:
        更新されたTodoオブジェクト

    Raises:
        TodoNotFoundException: 指定されたIDのTodoが見つからない場合
    """
    todo = db.update_todo(
        todo_id,
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
    )
    if todo is None:
        raise TodoNotFoundException(todo_id)
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    """指定されたIDのTodoを削除する。

    Args:
        todo_id: 削除するTodoのID

    Raises:
        TodoNotFoundException: 指定されたIDのTodoが見つからない場合
    """
    if not db.delete_todo(todo_id):
        raise TodoNotFoundException(todo_id)
