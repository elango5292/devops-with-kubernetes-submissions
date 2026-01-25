# Exercise 4.1: Readiness Probes

## Implementation

### Ping-pong Application (`/healthz` endpoint)
- Checks **database connectivity** by executing a `SELECT 1` query
- Returns `200 OK` when PostgreSQL is connected
- Returns `503 Service Unavailable` when database is unreachable

### Log Output Application (`/healthz` endpoint)
- Checks if it can **receive data from Ping-pong** by calling `GET /pings`
- Returns `200 OK` when Ping-pong service is reachable
- Returns `503 Service Unavailable` when Ping-pong is unreachable

## Readiness Probe Configuration

Both deployments use HTTP GET readiness probes:

```yaml
readinessProbe:
  initialDelaySeconds: 30
  periodSeconds: 5
  httpGet:
    path: /healthz
    port: 80
```

## Images

| Application | Image Tag |
|-------------|-----------|
| Log Output | `elango5292/src-1-log-output:v3` |
| Ping-pong | `elango5292/src-2-pingpong:v6` |

Both images are built for `linux/amd64` platform for GKE compatibility.
