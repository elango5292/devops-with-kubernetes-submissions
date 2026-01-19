## 2.2 The Project - Step 8

Introduced microservices architecture by separating Todo logic into a dedicated backend service.

- **Frontend**: Connects to the main backend to fetch and save todos.
- **Main Backend**: Proxies `/api/todos` requests to the internal `todo-backend` service.
- **Todo Backend**: New separate service handling Todo Create/Read operations (in-memory storage).
- **Communication**: Main App connects to Todo Backend via `http://todo-backend-svc:2345`.

### Usage

```bash
# Build Main App image
docker build -t project-step8:v1 ./2.2_the_project_step8/

# Build Todo Backend image
docker build -t todo-backend:v1 ./2.2_the_project_step8/src/todo-backend/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
# Note: deploy persistent volume (admin manifest) first
kubectl apply -f ./2.2_the_project_step8/admin_manifest/
kubectl apply -f ./2.2_the_project_step8/manifests/
```
