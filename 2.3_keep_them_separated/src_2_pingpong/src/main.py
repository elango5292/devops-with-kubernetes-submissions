import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

count = None


@app.on_event("startup")
def startup_event():
    global count
    count = 0
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")


@app.get("/pings", response_class=PlainTextResponse)
def ping():
    return f"Ping / Pongs: {count}"


@app.get("/pingpong")
def pingpong():
    global count
    if count is not None and count >= 0:
        count += 1
    else:
        count = 0
    return "pong " + str(count)


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
