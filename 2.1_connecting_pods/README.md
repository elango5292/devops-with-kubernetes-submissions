## 2.1 Connecting Pods

Connecting the **Log output** application and the **Ping pong** application via HTTP. The Log output application requests the current pong count from the Ping pong application's API.

- **Ping pong app**: Exposes `/pings` (status) and `/pingpong` (increment) endpoints.
- **Log output app**: Calls the Ping pong app using the Kubernetes Service DNS.
- **Networking**: Uses ClusterIP services for internal communication and NGINX Ingress for external access.

### Usage

```bash
# From the project root
docker build -t src-1-log-output:v1 ./2.1_connecting_pods/src_1_log_output/
docker build -t src-2-pingpong:v1 ./2.1_connecting_pods/src_2_pingpong/

# Ensure NGINX Ingress Controller is installed
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

# Apply the manifests (Deployment, Service, Ingress)
kubectl apply -f ./2.1_connecting_pods/manifest/
```
