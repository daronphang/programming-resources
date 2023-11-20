## Liveness probe

he kubelet uses liveness probes to know when to **restart a container**. For example, liveness probes could catch a deadlock, where an application is running, but unable to make progress. Restarting a container in such a state can help to make the application more available despite bugs.

However, it should be used with caution and must be configured carefully to ensure that they truly indicate unrecoverable application failure i.e. deadlock.

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-exec
spec:
  containers:
    - name: liveness
      image: registry.k8s.io/busybox
      args:
        - /bin/sh
        - -c
        - touch /tmp/healthy; sleep 30; rm -f /tmp/healthy; sleep 600
      livenessProbe:
        exec:
          command:
            - cat
            - /tmp/healthy
        initialDelaySeconds: 5
        periodSeconds: 5

---
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

## Readiness probe

The kubelet uses readiness probes to know when a container is **ready to start accepting traffic**. A Pod is considered ready when all of its containers are ready. One use of this signal is to control which Pods are used as backends for Services. When a Pod is not ready, it is removed from Service load balancers.

```yaml
readinessProbe:
  exec:
    command:
      - cat
      - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```
