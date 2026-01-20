## 2.7 Stateful applications

Run a Postgres database as a StatefulSet and persist Ping-pong application counters.

### Usage

**1. Create Namespace**
```bash
kubectl create namespace exercises
```

**2. Build Images**
```bash
docker build -t src-1-log-output:v1 ./2.7_stateful_applications/src_1_log_output/
docker build -t src-2-pingpong:v1 ./2.7_stateful_applications/src_2_pingpong/
```

**3. Install Ingress Controller (if not present)**
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
```

**4. Deploy App**
```bash
kubectl apply -f ./2.7_stateful_applications/manifest/
```

**5. Verify**
```bash
kubectl get statefulsets -n exercises
kubectl get pods -n exercises
```

### Additional Details

- **Database Interaction**: Uses `psycopg[binary]` and `sqlalchemy` to connect to PostgreSQL.
- **Testing**: A standalone Postgres pod configuration is available in `2.7_stateful_applications/manifests_for_testing/db_external.yaml` to verify connectivity before full deployment.

