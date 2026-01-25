from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

import os

DB_SERVICE_NAME = os.getenv("DB_SERVICE_NAME", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "mdb")

DB_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_SERVICE_NAME}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URL)

Base = declarative_base()

class PingPong(Base):
    __tablename__ = "pingpong"
    key = Column(String, primary_key=True)
    value = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PingPong(key={self.key}, value='{self.value}')>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def put_pingpong(key, value):
    existing = session.query(PingPong).filter(PingPong.key == key).first()
    if existing:
        existing.value = value
    else:
        pingpong = PingPong(key=key, value=value)
        session.add(pingpong)
    session.commit()


def get_pingpong(key):
    return session.query(PingPong).filter(PingPong.key == key).first()


if __name__ == "__main__":
    put_pingpong("count", "1")
    print(get_pingpong("count").value)
    put_pingpong("count", "2")
    print(get_pingpong("count").value)
    session.close()

