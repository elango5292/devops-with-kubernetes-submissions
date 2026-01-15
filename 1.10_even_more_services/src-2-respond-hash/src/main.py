from fastapi import FastAPI
import uvicorn
import os

READ_PATH = os.getenv("SHARED_HASH_PATH", "./hash.txt")

app = FastAPI()

@app.on_event("startup")
def startup_event():
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")

@app.get("/health")
def health():
    return {"status": "Healthy"}

@app.get("/")
def root():
    try:
        with open(READ_PATH, 'r') as f:
            hash_string = f.read()
        return hash_string
    except Exception as e:
        return {"error": str(e)}
    

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

