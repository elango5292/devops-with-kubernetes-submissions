import os
from fastapi import FastAPI, Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from asset_manager import AssetManager
import requests

app = FastAPI()

@app.get("/healthz")
def healthz():
    try:
        response = requests.get(f"{TODO_BACKEND_URL}/healthz", timeout=5)
        if response.status_code == 200:
             return JSONResponse(status_code=200, content={"status": "ready", "backend": "reachable"})
        else:
             return JSONResponse(status_code=503, content={"status": "not ready", "backend": "unreachable"})
    except Exception as e:
        print(f"Readiness check failed: {e}")
        return JSONResponse(status_code=503, content={"status": "not ready", "backend": "unreachable", "error": str(e)})

# Initialize Asset Manager
storage_path = os.getenv("IMAGE_STORE_PATH", "/usr/src/mount/image-store")
manager = AssetManager(storage_path)
TODO_BACKEND_URL = os.getenv("TODO_BACKEND_URL", "http://localhost:8001")

# Register the daily image asset
daily_image_url = os.getenv("DAILY_IMAGE_URL", "https://picsum.photos/1200")
manager.register_asset(
    name="daily_image",
    url=daily_image_url,
    refresh_interval_seconds=600, # 10 minutes
    filename="daily_image.jpg"
)

@app.get("/config")
def get_config():
    return {"image_store_path": os.getenv("IMAGE_STORE_PATH", "default")}

@app.get("/api/image")
def get_image():
    file_path = manager.get_asset_path("daily_image")
    if file_path and file_path.exists():
        return FileResponse(file_path)
    return Response(status_code=404, content="Image not available")

@app.get("/api/todos")
def get_todos():
    try:
        response = requests.get(f"{TODO_BACKEND_URL}/todos")
        return response.json()
    except Exception as e:
        print(f"Error fetching todos: {e}")
        return []

@app.post("/api/todos")
async def add_todo(request: Request):
    try:
        data = await request.json()
        response = requests.post(f"{TODO_BACKEND_URL}/todos", json=data)
        return response.json()
    except Exception as e:
        print(f"Error adding todo: {e}")
        return {"error": str(e)}

@app.put("/api/todos/{id}")
async def update_todo(id: str, request: Request):
    try:
        data = await request.json()
        response = requests.put(f"{TODO_BACKEND_URL}/todos/{id}", json=data)
        return response.json()
    except Exception as e:
        print(f"Error updating todo: {e}")
        return {"error": str(e)}

app.mount("/", StaticFiles(directory="dist", html=True), name="static")
