## Resource in containers

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
    - name: app
      image: images.my-company.example/app:v4
      resources:
        requests:
          memory: "64Mi"
          cpu: "0.2"
        limits:
          memory: "128Mi"
          cpu: "500m"
    - name: log-aggregator
      image: images.my-company.example/log-aggregator:v6
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

## Resource Quotas

When several users or teams share a cluster with a fixed number of nodes, there is a concern that one team could use more than its fair share of resources. Resource quotas are a tool for administrators to address this concern.

A resource quota provides constraints that limit aggregate resource consumption **per namespace**. It can limit the quantity of objects that can be created in a namespace by type, as well as the total amount of compute resources that may be consumed by resources in that namespace.

If quota is enabled in a namespace for compute resources like **cpu** and **memory**, users must specify **requests or limits** for those values. Otherwise, the quota system may reject pod creation. Use the **LimitRanger admission controller to force defaults** for pods that make no compute resource requirements.

You can configure as follows:

- No requests, no limits
- No requests but with limits
- Requests and limits
- Requests but no limits (ideal, guaranteees all Pods can run)

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: dev
spec:
  hard:
    pods: 10
    requests.cpu: 4
    requests.memory: 5Gi
    limits.cpu: 10
    limits.memory: 10Gi

---
apiVersion: v1
kind: List
items:
  - apiVersion: v1
    kind: ResourceQuota
    metadata:
      name: pods-high
    spec:
      hard:
        cpu: "1000"
        memory: 200Gi
        pods: "10"
      scopeSelector:
        matchExpressions:
          - operator: In
            scopeName: PriorityClass
            values: ["high"]
```

### Limit Ranges

A limitRange is a policy to constrain the resource allocations (limits and requests) that you can specify for each applicable object kind in a namespace i.e. Pod, PVC.

The name of a LimitRange object must be a **valid DNS subdomain name**.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
  limits:
    - default: # this section defines default limits
        cpu: 500m
      defaultRequest: # this section defines default requests
        cpu: 500m
      max: # max and min define the limit range
        cpu: "1"
      min:
        cpu: 100m
      type: Container
```

### Object count

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: object-counts
spec:
  hard:
    configmaps: "10"
    persistentvolumeclaims: "4"
    pods: "4"
    replicationcontrollers: "20"
    secrets: "10"
    services: "10"
    services.loadbalancers: "2"
```
