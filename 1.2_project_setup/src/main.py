from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.on_event("startup")
def startup_event():
    port = str(os.getenv("APP_PORT", 8000))
    print(f"Server started in port {port}")

@app.get("/")
def root():
    return {"status": "Healthy"}

if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

