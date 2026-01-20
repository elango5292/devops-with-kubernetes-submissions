from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# 1. Connection Configuration
# "postgresql+psycopg://" tells SQLAlchemy to use the psycopg driver we installed earlier
DB_URL = "postgresql+psycopg://admin:postgres@localhost:5432/mdb"

# 2. Setup the "Engine" (The core connection manager)
engine = create_engine(DB_URL)

# 3. Define the "Base" class
# All your table models will inherit from this
Base = declarative_base()

# 4. Define your Table as a Python Class
class Usage(Base):
    __tablename__ = 'usage_orm_test'  # Name of the table in DB

    id = Column(Integer, primary_key=True)
    info = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Usage(id={self.id}, info='{self.info}')>"

def run_orm_demo():
    print("Connecting via SQLAlchemy...")

    # --- THIS ANSWERS YOUR QUESTION ---
    # 5. Create Tables
    # This command looks at all classes inheriting from 'Base' (like Usage)
    # and checks if their __tablename__ exists in the DB.
    # If it does NOT exist, it issues the CREATE TABLE SQL for you.
    # If it DOES exist, it does typically nothing.
    print("Checking/Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables ready.")

    # 6. Create a Session
    # The session is your handle for one "conversation" with the DB
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # 7. Insert Data
        # Notice we just create a Python object. No SQL!
        print("Inserting new record...")
        new_record = Usage(info="Created with SQLAlchemy magic!")
        session.add(new_record)
        session.commit()
        print("Commited.")

        # 8. Query Data
        # We ask for "Usage" objects, not rows.
        print("Querying data...")
        # Get the input we just made (order by id desc, get first)
        latest = session.query(Usage).order_by(Usage.id.desc()).first()
        print(f"Found record: {latest}")
        print(f"Accessing attributes directly: Info = {latest.info}")

    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    run_orm_demo()
