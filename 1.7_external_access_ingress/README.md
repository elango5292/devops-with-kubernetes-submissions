## 1.7 External Access with Ingress

Hash generator application with Kubernetes Ingress for external HTTP routing.

### Usage
```
# Build image
docker build -t hash-external-ingress:v1 ./1.7_external_access_ingress/

# If no ingress controller is installed, install NGINX Ingress Controller by running
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Deploy to Kubernetes
kubectl apply -f ./1.7_external_access_ingress/manifest/

```

<img width="882" height="900" alt="image" src="https://github.com/user-attachments/assets/92c8854b-3b2f-4fa9-89cc-76e3943546bb" />
<img width="1440" height="900" alt="image" src="https://github.com/user-attachments/assets/eb64d8b0-89e2-4d17-9906-e64ffeb98088" />
<img width="1099" height="630" alt="image" src="https://github.com/user-attachments/assets/4efff738-62d3-4961-887c-c3f03a15725c" />