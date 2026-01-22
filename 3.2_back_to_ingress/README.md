## 3.2 Back to Ingress

Run "Log output" and "Ping-pong" applications into GKE and expose it with Ingress.

### Usage

**1. Prerequisite: Google Kubernetes Engine (GKE)**
Ensure you are connected to your GKE cluster via **Google Cloud Shell**.
```bash
gcloud container clusters get-credentials <YOUR_CLUSTER_NAME> --zone <YOUR_ZONE> --project <YOUR_PROJECT_ID>
```

**2. Create Namespace**
```bash
kubectl create namespace exercises
```

**3. Deploy App**
The application uses the following pre-built images hosted on Docker Hub:

| Component | Image Tag |
| :--- | :--- |
| **Log Output (Main App)** | `elango5292/src-1-log-output:v2` |
| **Ping-pong (Counter)** | `elango5292/src-2-pingpong:v3` |

**Note:** To satisfy the Ingress requirement of a successful response from the `/` path, a new route has been added to the `main.py` of the "Ping-pong" application.

```bash
kubectl apply -f ./3.2_back_to_ingress/manifest/
```

**4. Verify**
```bash
kubectl get statefulsets -n exercises
kubectl get pods -n exercises
kubectl get svc -n exercises
```

**5. Test Database Connectivity (Optional)**
To expose the Postgres database externally for testing purposes:

```bash
kubectl apply -f ./3.2_back_to_ingress/manifests_for_testing
kubectl get svc -n exercises postgres-db-external
```

### 6. Services & Access

| Service | Type | Purpose | Access Command |
| :--- | :--- | :--- | :--- |
| `src-1-log-output` | NodePort | Main Application | `kubectl get svc -n exercises src-1-log-output` |
| `src-2-pingpong` | NodePort | Counter Service | `kubectl get svc -n exercises src-2-pingpong` |
| `postgres-db-external` | LoadBalancer | **Testing Only** | `kubectl get svc -n exercises postgres-db-external` |

**Database Note:** The application uses `psycopg[binary]` and `sqlalchemy` for PostgreSQL connections.

---

### 7. Evidence

**1. Cluster Status (Terminal)**
*Applying manifests*
![Terminal Output](./screenshots/cloud_terminal_apply_manifests.png)
<br/>

**2. GKE Workloads (Console)**
*Verification of Pods running in Google Cloud Console.*
![GKE Workloads](./screenshots/gconsole_workload_pods_tab.png)
<br/>

**3. GKE Services (Console)**
*Verification of Services.*
![GKE Services](./screenshots/gconsole_services_tab.png)
<br/>

**4. GKE Ingress (Console)**
*Ingress details.*
![GKE Ingress](./screenshots/gconsole_ingress_view.png)
<br/>

**5. Application Access (Ingress)**
*Ping-pong Service (Counter):*
![PingPong Access](./screenshots/browser_ping_pong_access.png)
<br/>

*Log Output Service (Main App):*
![Log Output Access](./screenshots/browser_logout_access.png)
<br/>


