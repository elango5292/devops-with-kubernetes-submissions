## 2.4 The Project - Step 9

Moved all project resources (Main App, Todo Backend, PVC, Ingress) to a dedicated namespace called `project`.

### Usage

**1. Create Namespace**

```bash
kubectl create namespace project
```

**2. Build Images**

```bash
# Main App
docker build -t project-step9:v1 ./2.4_the_project_step9/

# Todo Backend
docker build -t todo-backend:v1 ./2.4_the_project_step9/src/todo-backend/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy manifests
kubectl apply -f ./2.4_the_project_step9/admin_manifest/
kubectl apply -f ./2.4_the_project_step9/manifests/
```
