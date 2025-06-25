# app/models.py

from pydantic import BaseModel

class ToDoItem(BaseModel):
    id: int
    title: str
    completed: bool = False
