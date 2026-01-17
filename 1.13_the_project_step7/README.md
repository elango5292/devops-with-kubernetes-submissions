## 1.13 The Project - Step 7

Adding basic Todo list functionality to the project.

- **Frontend**: 
  - Added Todo Input field (max 140 characters).
  - Added "Send" button (placeholder functionality).
  - Added Todo List display with hardcoded items.
- **Backend**: Same as Step 6 (Image caching).
- **Persistence**: Daily image persists across restarts.

### Usage

```bash
# Build unified image
docker build -t project-step7:v1 ./1.13_the_project_step7/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
# Note: deploy persistent volume (admin manifest) first
kubectl apply -f ./1.13_the_project_step7/admin_manifest/
kubectl apply -f ./1.13_the_project_step7/manifests/
```
