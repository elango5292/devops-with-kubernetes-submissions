import os
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
import db

from prometheus_fastapi_instrumentator import Instrumentator

from prometheus_client import Counter

import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

app = FastAPI()

# Create a manual metric
REJECTED_TODOS = Counter("todos_rejected_total", "Total count of todos rejected due to length")

Instrumentator().instrument(app).expose(app)

class TodoItem(BaseModel):
    todo: str

@app.get("/todos")
def get_todos():
    db_todos = db.get_todos()
    return [todo.content for todo in db_todos]

@app.post("/todos")
def create_todo(item: TodoItem):
    logger.info(f"Received todo: {item.todo}")
    if len(item.todo) > 140:
         logger.error(f"Rejected todo (too long): value was {len(item.todo)} chars")
         REJECTED_TODOS.inc() # MANUALLY INCREMENT HERE
         raise HTTPException(status_code=400, detail="Todo exceeds 140 characters")
    db.add_todo(item.todo)
    logger.info(f"Created todo: {item.todo[:15]}...")
    return {"message": "Todo added successfully"}
