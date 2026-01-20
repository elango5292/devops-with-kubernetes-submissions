## 2.8 The Project - Step 11

Implemented a persistent PostgreSQL database for Todos using a StatefulSet and configured the backend to communicate with it using ConfigMaps.

### Changes
1.  **Database**: Deployed PostgreSQL 15 as a StatefulSet (`manifests/db_deployment.yaml`) with a persistent volume claim.
2.  **Configuration**: Updated `configmap.yaml` to include database connection details (`DB_SERVICE_NAME`, `DB_USER`, `DB_NAME`, etc.).
3.  **Backend Logic**: Refactored `todo-backend` (`src/todo-backend/db.py`) to use `SQLAlchemy` for persistent storage instead of an in-memory list.

### Usage

**1. Create Namespace**

```bash
kubectl create namespace project
```

**2. Build Images**

```bash
# Run from repository root

# Main App (Frontend)
docker build -t project-step11:v1 2.8_the_project_step11/src/todo-app/

# Todo Backend
docker build -t todo-backend:v1 2.8_the_project_step11/src/todo-backend/
```

**3. Ensure NGINX Ingress Controller is installed**

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
```

**4. Deploy**

```bash
kubectl apply -f ./2.8_the_project_step11/manifests/
```
