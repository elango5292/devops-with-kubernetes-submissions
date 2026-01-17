## 1.11 Persisting Data

Using PersistentVolumes and PersistentVolumeClaims to maintain state across pod restarts between two services.

- **src-1-log-output**: Generates a random hash and combines it with a timestamp and the current pong count from a shared persistent file.
- **src-2-pingpong**: FastAPI service that increments a pong count and persists it to a shared file at `/usr/src/mount/count.txt`.

### Usage

```bash
# Build images
docker build -t src-1-log-output:v1 ./1.11_persisting_data/src_1_log_output/
docker build -t src-2-pingpong:v1 ./1.11_persisting_data/src_2_pingpong/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
# Note: deploy persistent volume (admin manifest) first
kubectl apply -f ./1.11_persisting_data/admin_manifest/
kubectl apply -f ./1.11_persisting_data/manifest/
```

### Endpoints

- `GET /` (src-1) → Returns timestamp, hash, and current pong count.
- `GET /pingpong` (src-2) → Increments and returns the pong count, persisting it.

### Access

- **Log Output**: Available via Ingress at `http://localhost:8081/` (or your configured Ingress host)
- **Ping Pong**: Available via Ingress at `http://localhost:8081/pingpong`
