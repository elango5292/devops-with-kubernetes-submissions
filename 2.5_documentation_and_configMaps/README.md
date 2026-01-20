## 2.5 Documentation and ConfigMaps

This exercise demonstrates:
1.  Using **ConfigMaps** to inject environment variables and files into Pods.

### Usage

**1. Create Namespace**

```bash
kubectl create namespace exercises
```

**2. Build Images**

```bash
docker build -t src-1-log-output:v1 ./2.5_documentation_and_configMaps/src_1_log_output/
docker build -t src-2-pingpong:v1 ./2.5_documentation_and_configMaps/src_2_pingpong/
```

**3. Deploy**

```bash
kubectl apply -f ./2.5_documentation_and_configMaps/manifest/
```

**4. Verification**

Checking logs:
```bash
kubectl -n exercises logs -f -l app=src-1-log-output
```

Checking output (port-forward or ingress, here via port-forward example or simple curl if local):
```bash
# Assuming port-forwarding or direct access
curl localhost:8000
```

