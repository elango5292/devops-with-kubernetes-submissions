# 5.6 Knative Serverless

My manifests are in the `manifests/` directory.

### Knative Installation & Pods
Running serverless workloads on k3d with Knative serving.

![Lens Pods View](screenshots/lens_view_pods_hello.png)

### Accessing the Service
Verifying the service works via `curl` using the `sslip.io` domain.

![Curl Output](screenshots/curl_slip_io_domain.png)

### Revisions & Traffic Splitting
Demonstrating traffic splitting between two revisions (v1 and v2) and autoscaling behavior.

![Traffic Split](screenshots/terminal_traffic_split_v1_v2.png)
![Autoscaling Terminal](screenshots/scalling_terminal_split_curl_pods_terminals.png)
