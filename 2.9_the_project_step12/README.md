## 2.9 The Project - Step 12

Implemented a `CronJob` that automatically adds a random Wikipedia article to the Todo list once every hour.

### Changes
1.  **New Component (todo-cron)**: A simple Python script (`src/todo-cron`) that:
    - Fetches a random Wikipedia URL (redirects from `https://en.wikipedia.org/wiki/Special:Random`).
    - Sends the URL as a new Todo item to the `todo-backend`.
2.  **Manifest**: Defined a `CronJob` resource in `manifests/cronjob.yaml`.

### Usage

**1. Create Namespace**

```bash
kubectl create namespace project
```

**2. Build Images**

```bash
# Run from repository root

# Main App (Frontend)
docker build -t project-step12:v1 2.9_the_project_step12/src/todo-app/

# Todo Backend
docker build -t todo-backend:v1 2.9_the_project_step12/src/todo-backend/

# Todo Cron
docker build -t todo-cron:v1 2.9_the_project_step12/src/todo-cron/
```

**3. Ensure NGINX Ingress Controller is installed**

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
```

**4. Deploy**

```bash
kubectl apply -f ./2.9_the_project_step12/manifests/
```
