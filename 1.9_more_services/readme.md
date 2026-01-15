## 1.9 More Services

Multiple microservices with shared Ingress routing.

- **service-1-log-hash**: Generates a random SHA256 hash on startup and returns it with a timestamp at `/`
- **service-2-ping-pong**: Returns "pong" with an incrementing counter at `/pingpong`

### Usage

```bash
# Build images
docker build -t service-1-log-hash:v1 ./1.9_more_services/service-1-log-hash/
docker build -t service-2-ping-pong:v1 ./1.9_more_services/service-2-ping-pong/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
kubectl apply -f ./1.9_more_services/manifest/
```

### Endpoints

- `GET /` → log-hash service (timestamp + hash)
- `GET /pingpong` → ping-pong service (pong counter)
