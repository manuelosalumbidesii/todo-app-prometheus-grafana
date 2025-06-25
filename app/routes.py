# app/routes.py

from fastapi import APIRouter, HTTPException
from app.models import ToDoItem
from app.metrics import REQUEST_COUNT, REQUEST_LATENCY

router = APIRouter()

todos = []  # In-memory list (no DB for now)

@router.get("/todos")
@REQUEST_LATENCY.time()
def get_todos():
    REQUEST_COUNT.labels(method="GET", endpoint="/todos").inc()
    return todos

@router.post("/todos")
@REQUEST_LATENCY.time()
def create_todo(item: ToDoItem):
    REQUEST_COUNT.labels(method="POST", endpoint="/todos").inc()
    todos.append(item)
    return item

@router.delete("/todos/{item_id}")
@REQUEST_LATENCY.time()
def delete_todo(item_id: int):
    REQUEST_COUNT.labels(method="DELETE", endpoint="/todos/{item_id}").inc()
    for todo in todos:
        if todo.id == item_id:
            todos.remove(todo)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="To-do not found")
