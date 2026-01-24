## 1.5 The Project Step-3

Full-stack application with React frontend and FastAPI backend, using multi-stage Docker build.


### Usage

```bash
# Build image
docker build -t project-step3:v1 ./1.5_the_project_step3/

# Deploy to Kubernetes
kubectl apply -f ./1.5_the_project_step3/manifests/deployment.yaml

# Port forward
kubectl port-forward project-step3-5548499774-2ddm4 3002:80
```

<img width="2560" height="1437" alt="Screenshot 2026-01-14 at 9 30 13 PM" src="https://github.com/user-attachments/assets/e44fd720-2420-45be-8539-ab1becc91bbf" />
<img width="991" height="731" alt="Screenshot 2026-01-14 at 9 30 30 PM" src="https://github.com/user-attachments/assets/4ec2b1ab-5bd1-465b-b6cf-7be00e9d37ec" />