import os
import time
import json
import logging
import threading
import requests
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AssetConfig:
    name: str
    url: str
    refresh_interval_seconds: int
    filename: str

class AssetManager:
    def __init__(self, storage_path: str):
        self.storage_path = Path(storage_path)
        self.assets: Dict[str, AssetConfig] = {}
        self.metadata_file = self.storage_path / "assets_metadata.json"
        
        # Ensure storage directory exists
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._load_metadata()

    def register_asset(self, name: str, url: str, refresh_interval_seconds: int, filename: str):
        """Register a new asset to be managed."""
        self.assets[name] = AssetConfig(name, url, refresh_interval_seconds, filename)
    
    def get_asset_path(self, name: str) -> Optional[Path]:
        """Get the path to the asset, refreshing it if necessary."""
        if name not in self.assets:
            return None
            
        config = self.assets[name]
        file_path = self.storage_path / config.filename
        
        if self._needs_refresh(name):
            if file_path.exists():
                threading.Thread(target=self._refresh_asset, args=(name,)).start()
                return file_path
            else:
                success = self._refresh_asset(name)
                return file_path if success else None
        
        return file_path

    def _needs_refresh(self, name: str) -> bool:
        """Check if an asset needs refreshing based on metadata."""
        if name not in self.metadata:
            return True
            
        last_fetched = self.metadata[name].get("last_fetched", 0)
        config = self.assets[name]
        
        # Check if file physically exists
        if not (self.storage_path / config.filename).exists():
            return True
            
        age = time.time() - last_fetched
        return age > config.refresh_interval_seconds

    def _refresh_asset(self, name: str) -> bool:
        """Downloads the asset and updates metadata."""
        config = self.assets[name]
        file_path = self.storage_path / config.filename
        temp_path = file_path.with_suffix(".tmp")
        
        try:
            logger.info(f"Refreshing asset: {name}")
            response = requests.get(config.url, stream=True)
            if response.status_code == 200:
                with open(temp_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                
                # Atomic rename to avoid partial reads
                os.replace(temp_path, file_path)
                
                # Update metadata
                self.metadata[name] = {
                    "last_fetched": time.time(),
                    "filename": config.filename
                }
                self._save_metadata()
                logger.info(f"Successfully refreshed asset: {name}")
                return True
            else:
                logger.error(f"Failed to fetch asset {name}: Status {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"Error refreshing asset {name}: {e}")
            if temp_path.exists():
                temp_path.unlink()
            return False

    def _load_metadata(self):
        """Load metadata from JSON file."""
        if self.metadata_file.exists():
            try:
                with open(self.metadata_file, 'r') as f:
                    self.metadata = json.load(f)
            except Exception:
                self.metadata = {}
        else:
            self.metadata = {}

    def _save_metadata(self):
        """Save metadata to JSON file."""
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(self.metadata, f)
        except Exception as e:
            logger.error(f"Failed to save metadata: {e}")

