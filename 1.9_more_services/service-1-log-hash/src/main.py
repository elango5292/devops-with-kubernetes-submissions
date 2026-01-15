from fastapi import FastAPI
import uvicorn
import os

import hashlib
import uuid
import time
from datetime import datetime,timezone

app = FastAPI()

cache_string = ""

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
    hash_string = f"{timestamp}: {cache_string}"
    return {"timestamp": timestamp, "cache_string": cache_string }

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

