## 2.6 The Project - Step 10

Refactored the application structure and moved all hardcoded configurations (ports, URLs, paths) to Kubernetes ConfigMaps and Environment Variables.

### Changes
1.  **Folder Structure**: Source code organized into `src/todo-app` (Frontend/Backend) and `src/todo-backend`.
2.  **Configuration**: Introduced `configmap.yaml` to centralize configuration.
3.  **Environment Variables**: Updated helper scripts and manifests to use `valueFrom` ConfigMap.

### Usage

**1. Create Namespace**

```bash
kubectl create namespace project
```

**2. Build Images**

```bash
# Main App
# Run from repository root
docker build -t project-step10:v1 2.6_the_project_step10/src/todo-app/


# Todo Backend
docker build -t todo-backend:v1 2.6_the_project_step10/src/todo-backend/
```

**3. Ensure NGINX Ingress Controller is installed**

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
```

**4. Deploy**

```bash
kubectl apply -f ./2.6_the_project_step10/admin_manifest/
kubectl apply -f ./2.6_the_project_step10/manifests/
```
