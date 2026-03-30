from fastapi import FastAPI, HTTPException
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


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoCreate):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = updated_todo.title
            todo["description"] = updated_todo.description
            todo["status"] = updated_todo.status
            todo["updated_at"] = datetime.now().isoformat()
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(index)
            return {
                "message": "Todo deleted",
                "deleted_todo": deleted_todo
            }

    raise HTTPException(status_code=404, detail="Todo not found")