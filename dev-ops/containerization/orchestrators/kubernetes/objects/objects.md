## Objects

Kubernetes objects are persistent desired entities in the system (once created, the system will constantly work to ensure they exist), and are used to represent the state of your cluster. They describe:

- What containerized applications are running, and on which Nodes
- The resources available to those applications
- The policies around how they behave i.e. restart policies, upgrades, and fault-tolerance

Kubernetes provides a declarative or imperative approach, so we can use templates to create, update, delete or even scale objects.

Each file can contain more than one manifest. Each manifest describes an API object (deployment, job, secret).

### Approaches

When using imperative commands, a user operates directly on live objects in a cluster and provides operations to the kubectl command.

```bash
$ kubectl create deployment nginx --image nginx
```

When using declarative, a user operates on object config stored locally.

```bash
$ kubectl diff -f configs/
$ kubectl apply -f configs/
```

## Describing Objects

Required fields are apiVersion, kind, metadata, and spec.

### spec

Provides a description of the characteristics you want the resource to have i.e. its desired state.

### status

Describes the current state of the object, supplied and updated by the Kubernetes system.

### kind

The kind of objects you want to create i.e. deployment, service, pod.

### metadata

Data that helps uniquely identify the object, including a name, UID, and optional namespace.

### labels

Labels are key/value pairs attached to objects, and are intended to be used to specify identifying attributes of objects that are meaningful to users, but do not directly imply semantics to the core system.

Each key must be unique for a given object. Values must begin and end with an alphanumeric character [a-zA-Z0-9].

```
release: stable, canary
environment: dev, qa, production
tier: frontend, backend, cache
```

labels/selectors in controllers?

### selectors

Selectors act as filters i.e. help us in finding the labels attached to a kind. The label selector is the core grouping primitive in Kubernetes. Selectors depend on labels to select a group of resources such as Pods.

### matchExpressions, matchLabels

matchLabels is a map of key/value pairs and supports exact matching.

matchExpressions is more expressive in nature and supports set-based matching. Only Job, Deployment, ReplicaSet, and DaemonSet support matchLabels.

```yaml
selector:
  matchLabels:
    environment: staging
  matchExpressions:
    - { key: tier, operator: NotIn, values: [front-end] }
```

### Annotations

Annotations are not used to identify and select objects. Instead, they simply provide additional metadata to Kubernetes objects.
