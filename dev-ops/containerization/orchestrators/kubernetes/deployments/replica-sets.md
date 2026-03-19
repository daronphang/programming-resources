## ReplicaSet

ReplicaSets are used to ensure a fixed number of Pods are running. However, it does not manage updates, i.e. no versioning or rolling updates. ReplicaSets are usually created by Deployments and not directly.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
```
