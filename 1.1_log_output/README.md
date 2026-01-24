1.1 Log Output - Python app logging random hash every 5 seconds

Usage
```
# Build image 
docker build -t log-output:v1 ./1.1_log_output  

# Deploy to Kubernetes 
kubectl apply -f 1.1_log_output/manifests/deployment.yaml
```
Output:

<img width="890" height="696" alt="image" src="https://github.com/user-attachments/assets/ea3515ca-59a3-4d96-85e9-046305a5807f" />