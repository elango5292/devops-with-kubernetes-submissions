1.3 Declarative Setup

Usage
```
# Build image 
docker build -t log-output:v2 ./1.3_declarative_setup

# Deploy to Kubernetes 
kubectl apply -f 1.3_declarative_setup/manifests/deployment.yaml
```
Output:
<img width="962" height="854" alt="image" src="https://github.com/user-attachments/assets/9d78b0ec-616c-4a4a-854e-ac0347441d65" />