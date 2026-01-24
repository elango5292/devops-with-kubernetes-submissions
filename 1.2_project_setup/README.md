## 1.2 Project Setup

FastAPI web application with Docker and Kubernetes deployment

### Usage

```bash
# Build image
docker build -t todo-app:v1 ./1.2_project_setup

# Deploy to Kubernetes
kubectl apply -f 1.2_project_setup/manifests/deployment.yaml
```

<img width="1160" height="826" alt="Screenshot 2026-01-14 at 10 16 00 AM" src="https://github.com/user-attachments/assets/a96d3301-d474-44ee-9a08-698672516294" />