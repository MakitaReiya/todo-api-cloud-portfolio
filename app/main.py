from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

app = FastAPI()

todos = []
next_id = 1


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    status: Literal["todo", "doing", "done"]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/todos")
def create_todo(todo: TodoCreate):
    global next_id

    now = datetime.now().isoformat()

    new_todo = {
        "id": next_id,
        "title": todo.title,
        "description": todo.description,
        "status": todo.status,
        "created_at": now,
        "updated_at": now,
    }

    todos.append(new_todo)
    next_id += 1

    return new_todo


@app.get("/todos")
def get_todos():
    return todos