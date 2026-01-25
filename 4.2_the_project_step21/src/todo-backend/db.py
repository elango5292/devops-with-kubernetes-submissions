import uuid
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

DB_SERVICE_NAME = os.getenv("DB_SERVICE_NAME", "localhost")
DB_PORT = os.getenv("DB_SERVICE_PORT", "5432")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "mdb")

DB_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_SERVICE_NAME}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Todo(id={self.id}, content='{self.content}')>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = scoped_session(Session)

def add_todo(content):
    todo = Todo(content=content)
    session.add(todo)
    session.commit()

def get_todos():
    return session.query(Todo).all()


if __name__ == "__main__":
    add_todo("Buy milk")
    todos = get_todos()
    for todo in todos:
        print(todo.content)
    session.close()
