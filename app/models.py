from datetime import datetime

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str | None = None


class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = None
    completed: bool | None = None


class Todo(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False
    created_at: datetime
    updated_at: datetime
