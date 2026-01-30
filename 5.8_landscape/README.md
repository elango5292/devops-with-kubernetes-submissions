# Exercise 5.8: CNCF Landscape

![CNCF Landscape](screenshots/landscape_project_product.png)


## Tools and Projects Used

### Direct Usage (Red Circles)
- I used **Depot** to build images faster (Ex 5.8) and **Argo CD** to deploy rollouts (Ex 4.4).
- I used **Postgres** (Ex 1.11, 2.7) and **GitHub Actions** (Ex 1.4+) to manage persistence and CI/CD.
- I used **NATS** and **OpenTelemetry** to handle messaging and tracing in exercise 4.6.
- I used **Knative** (Ex 5.6-7) and **Istio** (Ex 5.2-3) to deploy serverless functions and service meshes.
- I used **Kubernetes** since exercise 1.1 to manage all deployments and rollouts.
- I used **Prometheus**, **Grafana** (Ex 4.3+), and **Grafana Loki** (Ex 2.10) to monitor and log applications.
- I used **Kiali** to visualize the Istio service mesh in exercise 5.3.
- I used **AWS Kinesis**, **Caddy**, **ETCD**, **Terraform**, **Amazon ECR**, **Google Container Registry**, and **SOPS** outside the course for streaming, infrastructure, and security.

### Indirect usage (Green Circles)
- I used **Traefik** (Ex 1.1) and **Containerd** (Ex 3.1) indirectly as Ingress and runtime environments.
