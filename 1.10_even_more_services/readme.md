## 1.10 Even More Services

Multi-container pod with shared volume for inter-container communication.

- **src-1-generate-hash**: Generates a random SHA256 hash and writes it with a timestamp to a shared file every 5 seconds
- **src-2-respond-hash**: FastAPI service that reads and returns the hash from the shared file at `/`

### Usage

```bash
# Build images
docker build -t src-1-generate-hash:v1 ./1.10_even_more_services/src-1-generate-hash/
docker build -t src-2-respond-hash:v1 ./1.10_even_more_services/src-2-respond-hash/

# Deploy to Kubernetes
kubectl apply -f ./1.10_even_more_services/manifest/
```

### Endpoints

- `GET /` → Returns the current hash with timestamp from shared volume
- `GET /health` → Health check endpoint

### Access

NodePort service available at `http://localhost:30002`
