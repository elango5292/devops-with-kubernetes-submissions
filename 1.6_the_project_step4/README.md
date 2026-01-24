## 1.6 The Project Step-4

Full-stack application with Kubernetes Service for external access.

### Usage

```bash
# Build image
docker build -t project-step4:v1 ./1.6_the_project_step4/

# Deploy to Kubernetes
kubectl apply -f ./1.6_the_project_step4/manifests/
```

# Access the application
curl http://localhost:30080

<img width="2558" height="1440" alt="Screenshot 2026-01-14 at 11 50 09 PM" src="https://github.com/user-attachments/assets/3257dbd5-72a0-4e6e-8440-0060ed97a765" />
<img width="899" height="900" alt="image" src="https://github.com/user-attachments/assets/65e5ae7b-3b3d-41e0-9d56-0ed7f996d368" />