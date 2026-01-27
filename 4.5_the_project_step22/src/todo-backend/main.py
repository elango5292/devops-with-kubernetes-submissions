import os
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import text
import db

from prometheus_fastapi_instrumentator import Instrumentator

from prometheus_client import Counter

import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def root():
    return {"status": "alive"}

@app.get("/healthz")
def healthz():
    try:
        with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return JSONResponse(status_code=200, content={"status": "ready", "database": "connected"})
    except Exception as e:
        print(f"Readiness check failed: {e}")
        return JSONResponse(status_code=503, content={"status": "not ready", "database": "disconnected", "error": str(e)})

# Create a manual metric
REJECTED_TODOS = Counter("todos_rejected_total", "Total count of todos rejected due to length")

Instrumentator().instrument(app).expose(app)

class TodoItem(BaseModel):
    todo: str

class TodoUpdate(BaseModel):
    done: bool

@app.get("/todos")
def get_todos():
    db_todos = db.get_todos()
    return [{"id": todo.id, "todo": todo.content, "done": bool(todo.done)} for todo in db_todos]

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

@app.put("/todos/{id}")
def update_todo(id: str, item: TodoUpdate):
    logger.info(f"Updating todo {id}: done={item.done}")
    success = db.update_todo(id, item.done)
    if not success:
         raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo updated successfully"}
