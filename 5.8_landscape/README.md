# Exercise 5.8: CNCF Landscape

![CNCF Landscape](screenshots/landscape_project_product.png)


## Tools and Projects Used

### Direct Usage (Red Circles)
- **Depot**: Used local CLI to build and push images to registry faster.
- **Argo CD**: Used in **Exercise 4.4** (Argo Rollouts) to deploy canary releases.
- **Postgres**: Used in **Exercise 1.11**, **2.7**, and throughout the project application for persistence.
- **GitHub Actions**: Used in **Exercise 1.4** and onwards to deploy CI/CD pipelines.
- **NATS**: Used in **Exercise 4.6** (Todo Broadcaster) for messaging between services.
- **AWS Kinesis**: Used **outside of the course** to learn about streaming.
- **Knative**: Used in **Exercise 5.6** and **5.7** to deploy serverless functions.
- **Kubernetes**: Used throughout the course, specifically for deployments and rollouts starting from **Exercise 1.1**.
- **Istio**: Used in **Exercise 5.2** and **5.3** to deploy a service mesh.
- **Caddy**: Used **outside of the course** for on-demand SSL in one project.
- **ETCD**: Used **outside of the course** to learn about distributed systems.
- **Terraform**: Used **outside of the course** to learn about Infrastructure as Code.
- **Amazon ECR**: Used **outside of the course** to store built images.
- **Google Container Registry**: Used **outside of the course** to learn about container registries.
- **SOPS**: Used **outside of the course** to encrypt configurations.
- **Prometheus**: Used in **Exercise 4.3** and onwards for monitoring.
- **Grafana**: Used in **Exercise 4.3** and onwards for visualization.
- **OpenTelemetry**: Used in **Exercise 4.6** in the todo-backend to trace requests.
- **Kiali**: Used in **Exercise 5.3** to visualize the Istio service mesh.
- **Grafana Loki**: Used in **Exercise 2.10** for log aggregation.

### Indirect usage (Green Circles)
* **Traefik**: Used indirectly as the default Ingress controller in **k3d** (**Exercise 1.1**).
* **Containerd**: Used indirectly as the runtime in **k3d** and **GKE** (**Exercise 3.1**).
