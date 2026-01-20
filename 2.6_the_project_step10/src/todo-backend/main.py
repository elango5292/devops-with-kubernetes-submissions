import os
from fastapi import FastAPI, Response

app = FastAPI()

todos = []

from pydantic import BaseModel

class Todo(BaseModel):
    todo: str

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(item: Todo):
    todos.append(item.todo)
    return {"message": "Todo added successfully"}


