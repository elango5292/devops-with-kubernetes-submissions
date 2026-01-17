from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

PERSISTENT_PONG_COUNT_PATH = os.getenv("PERSISTENT_PONG_COUNT_PATH", "./count.txt")
count = None

def write_pong_count(count):
    with open(PERSISTENT_PONG_COUNT_PATH, "w") as f:
        f.write(f'Ping / Pongs: {count}')

@app.on_event("startup")
def startup_event():
    write_pong_count(0)
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")

@app.get("/pingpong")
def health():
    global count
    if count is not None and count >= 0:
        count +=1
    else:
        count = 0
    write_pong_count(count)
    return "pong "+ str(count)

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

