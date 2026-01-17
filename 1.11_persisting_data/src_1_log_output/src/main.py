from fastapi import FastAPI
import uvicorn
import os

import hashlib
import uuid
import time
from datetime import datetime,timezone

PERSISTENT_PONG_COUNT_PATH = os.getenv("PERSISTENT_PONG_COUNT_PATH", "./count.txt")

app = FastAPI()

cache_string = ""

def read_pong_count():
    try:
        with open(PERSISTENT_PONG_COUNT_PATH, "r") as f:
            pong_count = f.read()
    except Exception as e:
        print(f"Error: read_pong_count : {e}")
        return f'Ping / Pongs: 0'
    return pong_count

@app.on_event("startup")
def startup_event():
    global cache_string
    random_string = str(uuid.uuid4())
    cache_string = hashlib.sha256(random_string.encode()).hexdigest()
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")

@app.get("/health")
def health():
    return {"status": "Healthy"}

@app.get("/")
def root():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{datetime.now(timezone.utc).microsecond // 1000:03d}Z"
    pong_count=read_pong_count()
    response_string = f'{timestamp}: {cache_string} . {pong_count}'
    return response_string

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

