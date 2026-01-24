## 1.4 The Project Step-2

FastAPI web application with Docker and Kubernetes deployment

### Changes
Based on the 1.2 project setup with the following updates:
- Bumped deployment version to `2.0.0`
- Updated container image to `todo-app:v2`

### Usage

```bash
# Build image
docker build -t todo-app:v2 ./1.4_the_project_step2/

# Deploy to Kubernetes
kubectl apply -f ./1.4_the_project_step2//manifests/deployment.yaml
```

<img width="1100" height="737" alt="image" src="https://github.com/user-attachments/assets/41e1319b-86e8-4f2a-b172-f8be75ecce6c" />