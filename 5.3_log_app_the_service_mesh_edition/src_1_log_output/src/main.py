import hashlib
import os
import uuid
from datetime import datetime, timezone

import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

PINGPONG_SERVICE_NAME = os.getenv("PINGPONG_SERVICE_NAME", "src-2-pingpong")
PINGPONG_SERVICE_PORT = os.getenv("PINGPONG_SERVICE_PORT", "1234")
GREETER_SERVICE_NAME = os.getenv("GREETER_SERVICE_NAME", "src-3-greeter")
GREETER_SERVICE_PORT = os.getenv("GREETER_SERVICE_PORT", "80")
MESSAGE = os.getenv("MESSAGE", "")
MESSAGE_FILE = ""
app = FastAPI()

cache_string = ""


def read_pong_count():
    try:
        response = requests.get(
            f"http://{PINGPONG_SERVICE_NAME}:{PINGPONG_SERVICE_PORT}/pings",
            timeout=5,
        )
        return response.text
    except Exception as e:
        print(f"Error: read_pong_count : {e}")
        return "Ping / Pongs: 0"


def read_greeting():
    try:
        response = requests.get(
            f"http://{GREETER_SERVICE_NAME}:{GREETER_SERVICE_PORT}/",
            timeout=5,
        )
        data = response.json()
        return data.get("greeting", "Hello!")
    except Exception as e:
        print(f"Error: read_greeting : {e}")
        return "Hello (fallback)!"


@app.on_event("startup")
def startup_event():
    global cache_string
    global MESSAGE_FILE
    random_string = str(uuid.uuid4())
    cache_string = hashlib.sha256(random_string.encode()).hexdigest()
    with open("/etc/config/message.env") as f:
        MESSAGE_FILE = f.read()
    print("MESSAGE: ", MESSAGE)
    print("MESSAGE_FILE: ", MESSAGE_FILE)
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")


@app.get("/health")
def health():
    return {"status": "Healthy"}


@app.get("/healthz")
def healthz():
    """Readiness probe - checks if Ping-pong service is reachable"""
    try:
        response = requests.get(
            f"http://{PINGPONG_SERVICE_NAME}:{PINGPONG_SERVICE_PORT}/pings",
            timeout=5,
        )
        if response.status_code == 200:
            return JSONResponse(
                status_code=200,
                content={"status": "ready", "pingpong": "reachable"},
            )
        return JSONResponse(
            status_code=503,
            content={"status": "not ready", "pingpong": "unreachable"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={"status": "not ready", "pingpong": "unreachable", "error": str(e)},
        )


@app.get("/")
def root():
    timestamp = (
        datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.")
        + f"{datetime.now(timezone.utc).microsecond // 1000:03d}Z"
    )
    greeting = read_greeting()
    pong_count = read_pong_count()
    message_file = f"file content: {MESSAGE_FILE}"
    message_env = f"env variable: {MESSAGE}"
    response_string = f"{timestamp}: {cache_string}.\n{pong_count}"
    return PlainTextResponse(
        f"{greeting}\n{message_file}\n{message_env}\n{response_string}",
    )


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
