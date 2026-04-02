from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    status: Literal["todo", "doing", "done"]


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    status: Literal["todo", "doing", "done"]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
