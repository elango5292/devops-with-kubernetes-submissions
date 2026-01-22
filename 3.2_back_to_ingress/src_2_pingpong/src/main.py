import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from db import put_pingpong, get_pingpong

app = FastAPI()

@app.on_event("startup")
def startup_event():
    put_pingpong("count", "0")
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")


@app.get("/pings", response_class=PlainTextResponse)
def ping():
    count = get_pingpong("count").value
    return f"Ping / Pongs: {count}"


@app.get("/pingpong")
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
