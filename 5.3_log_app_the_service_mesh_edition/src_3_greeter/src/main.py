import os

from fastapi import FastAPI

app = FastAPI()

# Get version from environment variable
VERSION = os.getenv("GREETER_VERSION", "v1")
GREETING = os.getenv("GREETING", "Hello")


@app.get("/")
async def greet():
    return {"greeting": f"{GREETING} from greeter {VERSION}!"}


@app.get("/healthz")
async def health():
    return {"status": "ok"}
