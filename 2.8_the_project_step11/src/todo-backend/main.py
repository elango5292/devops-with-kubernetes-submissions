import os
from fastapi import FastAPI, Response
from pydantic import BaseModel
import db

app = FastAPI()

class TodoItem(BaseModel):
    todo: str

@app.get("/todos")
def get_todos():
    db_todos = db.get_todos()
    return [todo.content for todo in db_todos]

@app.post("/todos")
def create_todo(item: TodoItem):
    if len(item.todo) > 140:
         return Response(status_code=400)
    db.add_todo(item.todo)
    return {"message": "Todo added successfully"}
