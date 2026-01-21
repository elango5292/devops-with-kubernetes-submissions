# Exercise 2.10: Project Step 13 – Monitoring & Logging

## Changes Implemented

- **140 Character Limit**: The backend now validates todo length.
- **Request Logging**: All incoming requests are logged.
- **Loki Integration**: Invalid todos (exceeding length limit) generate error logs viewable in Grafana via Loki.

---

## 1. Quick Start

### Install Monitoring Stack
```bash
# Prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install mooc-prometheus prometheus-community/prometheus --version 28.6.0 -n prometheus --create-namespace

# Grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm install mooc-grafana grafana/grafana --version 10.5.8 -n grafana --create-namespace

# Loki
helm repo add grafana https://grafana.github.io/helm-charts
helm install mooc-loki grafana/loki --version 6.49.0 -f 2.10_the_project_step13/loki_config/loki-values.yaml -n loki --create-namespace

# Promtail
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install mooc-promtail grafana/promtail -n promtail --create-namespace --set "config.clients[0].url=http://mooc-loki.loki:3100/loki/api/v1/push"
```

### Build & Deploy
```bash
# Build
docker build -t project-step13:v1 2.10_the_project_step13/src/todo-app/
docker build -t todo-backend:v1 2.10_the_project_step13/src/todo-backend/
docker build -t todo-cron:v1 2.10_the_project_step13/src/todo-cron/

# Deploy
kubectl create namespace project
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
kubectl apply -f ./2.10_the_project_step13/manifests/
```

---

## 2. Testing & Validation

### Backend Validation (140-Character Limit)

To verify that the backend rejects long todos, use the provided testing manifests to expose the service.

**Example:**
```bash
curl -X POST http://localhost:9092/todos \
  -H "Content-Type: application/json" \
  -d '{"todo": "This is a very long todo that exceeds the 140 character limit and should be rejected by the backend validation logic implemented in this exercise. This will trigger a 400 error and an ERROR log in Grafana."}'
```
**Expected Response:** `{"detail":"Todo exceeds 140 characters"}`

### Viewing Logs in Grafana

1. **Access Grafana**:
   - Apply the `grafana_lb.yaml` manifest (see below).
   - URL: `http://localhost:9091`
2. **Credentials**:
   - User: `admin`
   - Password: Run `kubectl get secret mooc-grafana -n grafana -o jsonpath="{.data.admin-password}" | base64 -d`
3. **Check Logs**:
   - Navigate to **Explore** -> Select **Loki** data source.
   - Query: `{app="todo-backend"}`
   - Observe `INFO` logs for requests and `ERROR` logs for rejected todos.

---

## 3. Testing Manifests

A set of extra manifests is provided in `manifests_for_testing/` to help with local debugging by exposing services via LoadBalancer.

| Manifest File | Description | Port Mapping | Command to Apply |
| :--- | :--- | :--- | :--- |
| `todo_backend_lb.yaml` | Exposes the Go Backend directly to localhost. | `9092` -> `8001` | `kubectl apply -f 2.10_the_project_step13/manifests_for_testing/todo_backend_lb.yaml` |
| `grafana_lb.yaml` | Exposes the Grafana UI. | `9091` -> `3000` | `kubectl apply -f 2.10_the_project_step13/manifests_for_testing/grafana_lb.yaml` |
| `prometheus_lb.yaml` | Exposes the Prometheus UI. | `9090` -> `9090` | `kubectl apply -f 2.10_the_project_step13/manifests_for_testing/prometheus_lb.yaml` |
| `db_external.yaml` | Exposes the Postgres Database. | `5432` -> `5432` | `kubectl apply -f 2.10_the_project_step13/manifests_for_testing/db_external.yaml` |
