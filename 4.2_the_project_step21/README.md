# Exercise 4.2: The Project Step 21 - Readiness and Liveness Probes

This directory contains the solution for Exercise 4.2, adding health checks to the Todo application.

## Probe Logic

We implemented **Readiness** and **Liveness** probes for both the Backend and Frontend services.

### Backend (`todo-backend`)

*   **Liveness Probe** (`/healthz`):
    *   Checks system health including **Database Connectivity**.
    *   If the database is unreachable, the pod will be restarted.
*   **Readiness Probe** (`/healthz`):
    *   Checks **Database Connectivity**.
    *   Ensures traffic is only sent to the backend when it can access the database.

### Frontend (`todo-app`)

*   **Liveness Probe** (`/healthz`):
    *   Checks system health including **Backend Connectivity**.
    *   If the backend is unreachable, the pod will be restarted.
*   **Readiness Probe** (`/healthz`):
    *   Checks **Backend Connectivity**.
    *   Ensures traffic is only sent when the backend is reachable.

## Dependency Chain

The probes create a dependency chain that ensures the entire system starts up in the correct order:

```
PostgreSQL DB -> Backend (Ready when DB is up) -> Frontend (Ready when Backend is reachable)
```

## Testing

To verify the probes work, you can simulate a failure:

1.  **Stop the Database**: Delete the PostgreSQL StatefulSet.
    *   Result: Backend Readiness Probe fails (`503`). Backend pod goes "Not Ready".
    *   Result: Frontend Readiness Probe fails (`503`, can't reach Backend). Frontend pod goes "Not Ready".
    *   Result: Liveness probes pass (pods stay "Running", no crash loop).

2.  **Start the Database**: Re-apply PostgreSQL manifest.
    *   Result: Backend connects, probe passes (`200`). Backend becomes "Ready".
    *   Result: Frontend connects to Backend, probe passes (`200`). Frontend becomes "Ready".
