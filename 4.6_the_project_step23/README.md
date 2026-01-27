# Exercise: 4.6. The project, step 23

## Installation

### Nats:
```
helm repo add nats https://nats-io.github.io/k8s/helm/charts/
helm install mooc-nats nats/nats -n nats --create-namespace
```

### Images used in different deployments:
*   **Backend**: `elango5292/todo-project-backend:v8`
*   **Broadcaster**: `elango5292/todo-project-broadcaster:v2`
*   **Frontend**: `elango5292/todo-project-app:v3`
*   **Cron**: `elango5292/todo-project-cron:v1`

## Implementation Highlights

*   **NATS Integration**: The backend (`todo-backend`) now connects to a NATS server and publishes messages (`todo_updates`) whenever a Todo is created or updated.
*   **Broadcaster Service**: A new `todo-broadcaster` service was created to listen to these NATS messages.
    *   **Scaling**: It uses NATS Queue Groups (`broadcaster_workers`) to ensure that even with **6 replicas**, each message is processed only once (load balanced).
    *   **Discord Webhook**: The broadcaster formats the messages into rich Discord Embeds (Green for Create, Orange/Red for Update) and sends them to a configured Webhook.

## Evidence of Testing

[Watch the video demonstration of the working application](https://youtu.be/z6yUjghZXEo)

<iframe width="560" height="315" src="https://www.youtube.com/embed/z6yUjghZXEo?si=rLYEEysI8mlUbM2i" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
