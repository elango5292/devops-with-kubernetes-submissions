# 3.3 To the Gateway

Migration of the "Log output" and "Ping-pong" applications to use the **Kubernetes Gateway API** on GKE.

### Prerequisites
1. **GKE Cluster** with **Gateway API** enabled (Standard mode).
   > *Note: I enabled this via the Google Cloud Console UI.*

   ![Gateway API Enabled](./screenshots/enable_gateway_api_console.png)

### Deployment
Deploy the application and the Gateway resources:
```bash
kubectl create namespace exercises
kubectl apply -f manifest/
```

### Verification
Check the Gateway and Routes:
```bash
kubectl get gateway -n exercises
kubectl get httproute -n exercises
kubectl get svc -n exercises
```

### Evidence

**1. Gateway Resources (Terminal)**
![Gateway List](./screenshots/gcloud-list-api-gateways.png)

**2. HTTP Routes Configuration**
*Route for Ping Pong:*
![Ping Pong Route](./screenshots/http-rule-1-pingpong.png)

*Route for Log Output:*
![Log Output Route](./screenshots/http-rule-2-logoutput.png)

**3. Browser Verification**
*Accessing Log Output (/):*
![Log Output Browser](./screenshots/browser-output-logoutput.png)

*Accessing Ping Pong (/pingpong):*
![Ping Pong Browser](./screenshots/browser-output-pingpong.png)
