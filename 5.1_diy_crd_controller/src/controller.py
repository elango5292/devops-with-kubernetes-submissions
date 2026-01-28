import kopf
import kubernetes
import requests


@kopf.on.create("dwk.io", "v1", "dummy-sites")
def create_fn(spec, name, **kwargs):
    website_url = spec.get("website_url")
    replicas = spec.get("replicas", 1)
    dummy_port = spec.get("dummy_port")
    if not website_url:
        return {"message": "No website_url provided"}
    if not dummy_port:
        return {"message": "No dummy_port provided"}

    namespace = "default"

    print(f"Creating DummySite {name} for {website_url} with {replicas} replicas")

    # Fetch content
    headers = {"User-Agent": "DummySiteController/1.0 (Kubernetes CRD Controller)"}
    try:
        response = requests.get(website_url, timeout=10, headers=headers)
        content = response.text
    except Exception as e:
        print(f"Error fetching website: {e}")
        content = f"<html><body><h1>Error fetching website</h1><p>{e}</p></body></html>"

    api = kubernetes.client.CoreV1Api()
    apps_api = kubernetes.client.AppsV1Api()

    # ConfigMap for the HTML
    cm_name = f"{name}-html"
    cm = {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {"name": cm_name, "namespace": namespace},
        "data": {"index.html": content},
    }

    # Deployment
    dep = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": name, "namespace": namespace},
        "spec": {
            "replicas": replicas,
            "selector": {"matchLabels": {"app": name}},
            "template": {
                "metadata": {"labels": {"app": name}},
                "spec": {
                    "containers": [
                        {
                            "name": "web",
                            "image": "docker.io/library/nginx:alpine",
                            "ports": [{"containerPort": 80}],
                            "volumeMounts": [
                                {"name": "html", "mountPath": "/usr/share/nginx/html"},
                            ],
                        },
                    ],
                    "volumes": [{"name": "html", "configMap": {"name": cm_name}}],
                },
            },
        },
    }

    # Service
    svc = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": name, "namespace": namespace},
        "spec": {
            "selector": {"app": name},
            "ports": [{"protocol": "TCP", "port": dummy_port, "targetPort": 80}],
            "type": "LoadBalancer",
        },
    }

    # Link the resources to the DummySite for automatic cleanup
    kopf.adopt(cm)
    kopf.adopt(dep)
    kopf.adopt(svc)

    try:
        api.create_namespaced_config_map(namespace=namespace, body=cm)
        apps_api.create_namespaced_deployment(namespace=namespace, body=dep)
        api.create_namespaced_service(namespace=namespace, body=svc)
        print(f"Resources created for DummySite {name}")
    except kubernetes.client.exceptions.ApiException as e:
        print(f"Exception when creating resources: {e}")


@kopf.on.update("dwk.io", "v1", "dummy-sites")
def update_fn(spec, name, **kwargs):
    website_url = spec.get("website_url")
    replicas = spec.get("replicas", 1)
    namespace = "default"

    print(f"Updating DummySite {name} to {website_url} with {replicas} replicas")

    # Update ConfigMap
    headers = {"User-Agent": "DummySiteController/1.0 (Kubernetes CRD Controller)"}
    try:
        response = requests.get(website_url, timeout=10, headers=headers)
        content = response.text
    except Exception as e:
        print(f"Error fetching website: {e}")
        content = f"<html><body><h1>Error fetching website</h1><p>{e}</p></body></html>"

    api = kubernetes.client.CoreV1Api()
    cm_name = f"{name}-html"

    cm = {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {"name": cm_name, "namespace": namespace},
        "data": {"index.html": content},
    }

    try:
        api.patch_namespaced_config_map(name=cm_name, namespace=namespace, body=cm)
        print(f"ConfigMap updated for DummySite {name}")
    except kubernetes.client.exceptions.ApiException as e:
        print(f"Exception when updating ConfigMap: {e}")

    # Update Deployment Replicas
    apps_api = kubernetes.client.AppsV1Api()
    dep_patch = {
        "spec": {
            "replicas": replicas,
        },
    }
    try:
        apps_api.patch_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=dep_patch,
        )
        print(f"Deployment updated for DummySite {name}")
    except kubernetes.client.exceptions.ApiException as e:
        print(f"Exception when updating Deployment: {e}")
