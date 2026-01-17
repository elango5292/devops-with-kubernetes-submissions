## 1.12 The Project - Step 6

Adding a persistent daily image to the project using a shared volume that survives container restarts.

- **Frontend**: Displays a daily "To-do" image, fetched via a proxy API to ensure freshness.
- **Backend (FastAPI)**: Manages image caching logic. Checks usage of a local image file in the shared persistent volume; if missing or stale (>10 mins), it fetches a new random image from Lorem Picsum and updates the cache.

### Usage

```bash
# Build unified image (Multistage: React build -> FastAPI serve)
docker build -t project-step6:v3 ./1.12_the_project_step6/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
# Note: deploy persistent volume (admin manifest) first
kubectl apply -f ./1.12_the_project_step6/admin_manifest/
kubectl apply -f ./1.12_the_project_step6/manifests/
```

### Features

- **Image Persistance**: Images are stored in `/usr/src/mount/image-store` backed by a PersistentVolume.
- **Auto-Refresh**: Backend automatically refreshes the image if it is older than 10 minutes.
- **Container Resilience**: If the pod crashes, the new pod mounts the same volume and serves the existing image without re-fetching.
