"""Todo APIのPydanticモデル定義。

リクエスト・レスポンスのスキーマをPydanticモデルで定義する。
"""

from datetime import datetime

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    """Todo作成リクエストのスキーマ。

    Args:
        title: Todoのタイトル（1文字以上必須）
        description: Todoの説明（任意）
    """

    title: str = Field(..., min_length=1)
    description: str | None = None


class TodoUpdate(BaseModel):
    """Todo更新リクエストのスキーマ。

    Args:
        title: 更新するタイトル（指定する場合は1文字以上）
        description: 更新する説明
        completed: 完了状態
    """

    title: str | None = Field(default=None, min_length=1)
    description: str | None = None
    completed: bool | None = None


class Todo(BaseModel):
    """Todoレスポンスのスキーマ。

    Args:
        id: TodoのユニークID
        title: Todoのタイトル
        description: Todoの説明
        completed: 完了状態
        created_at: 作成日時
        updated_at: 更新日時
    """

    id: int
    title: str
    description: str | None = None
    completed: bool = False
    created_at: datetime
    updated_at: datetime


class RootResponse(BaseModel):
    """ルートエンドポイントのレスポンススキーマ。

    Args:
        message: ウェルカムメッセージ
        docs: APIドキュメントのパス
    """

    message: str
    docs: str


class ErrorDetail(BaseModel):
    """統一エラーレスポンスの詳細スキーマ。

    Args:
        code: アッパースネークケースのエラーコード
        message: 人間が読めるエラーメッセージ
        details: エラーの追加情報
    """

    code: str
    message: str
    details: dict = Field(default_factory=dict)


class ErrorResponse(BaseModel):
    """統一エラーレスポンスのスキーマ。

    Args:
        error: エラー詳細
    """

    error: ErrorDetail
