from fastapi import FastAPI
import uvicorn
import os

import hashlib
import uuid
import time
from datetime import datetime,timezone

app = FastAPI()

count = None

@app.get("/pingpong")
def health():
    global count
    if count is not None and count >= 0:
        count +=1
    else:
        count = 0
    return "pong "+ str(count)

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

