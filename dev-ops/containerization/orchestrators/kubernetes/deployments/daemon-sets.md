## DaemonSet

DaemonSets are used to run exactly one Pod per node. They are often used for:

- Logging agents (Fluentd)
- Monitoring agents (Prometheus Node Exporter)
- Network proxies (Calico, Cilium)

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-agent
spec:
  selector:
    matchLabels:
      app: node-agent
  template:
    metadata:
      labels:
        app: node-agent
    spec:
      containers:
        - name: agent
          image: my-agent:latest
```
