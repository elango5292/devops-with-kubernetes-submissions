## 1.8 The Project Step 5

Full-stack application with Kubernetes Ingress for external HTTP routing.

### Usage

```
# Build image
docker build -t project-step5:v1 ./1.8_the_project_step5/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
kubectl apply -f ./1.8_the_project_step5/manifests/
```

<img width="1440" height="900" alt="image" src="https://github.com/user-attachments/assets/e4e47240-6c63-4b57-ac90-6c19b0c7ef8c" />
<img width="926" height="895" alt="Screenshot 2026-01-15 at 2 45 44 PM" src="https://github.com/user-attachments/assets/aa5218af-9eaa-434f-a9e8-7f6a6f1358a7" />