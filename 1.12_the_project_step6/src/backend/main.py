import os
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from asset_manager import AssetManager

app = FastAPI()

# Initialize Asset Manager
storage_path = os.getenv("IMAGE_STORE_PATH", "/usr/src/mount/image-store")
manager = AssetManager(storage_path)

# Register the daily image asset
manager.register_asset(
    name="daily_image",
    url="https://picsum.photos/1200",
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


app.mount("/", StaticFiles(directory="dist", html=True), name="static")