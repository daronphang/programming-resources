## Liveness Probe

```yaml
livenessProbe:
  httpGet:
    path: /api/health-check
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
  failureThreshold: 8
---
livenessProbe:
  tcpSocket:
    port: 3306
---
livenessProbe:
  exec:
    command:
      - cat
      - /app/is_healthy
```
