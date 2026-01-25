import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from sqlalchemy import text

from db import put_pingpong, get_pingpong, engine

app = FastAPI()


@app.get("/healthz")
def healthz():
    """Readiness probe - checks database connectivity"""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return JSONResponse(status_code=200, content={"status": "ready", "database": "connected"})
    except Exception as e:
        return JSONResponse(status_code=503, content={"status": "not ready", "database": "disconnected", "error": str(e)})

@app.on_event("startup")
def startup_event():
    put_pingpong("count", "0")
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")


@app.get("/pings", response_class=PlainTextResponse)
def ping():
    count = get_pingpong("count").value
    return f"Ping / Pongs: {count}"


@app.get("/version")
def version():
    return {"version": "v5"}


@app.get("/")
def pingpong():
    count = int(get_pingpong("count").value)
    if count is not None and count >= 0:
        count += 1
    else:
        count = 0
    put_pingpong("count", str(count))
    return "pong " + str(count)


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
