## Deployment

To deploy containerized applications on top of a running cluster, need to create a Kubernetes Deployment configuration. The Deployment instructs Kubernetes how to create and update instances of your application, and keep them running across Nodes in the event of failure. Resides within the Control Plane. Deployments are the recommended way to **manage the creation and scaling of Pods as it offers scalability, self-healing, and rolling updates for stateless apps**.

When creating a Deployment, need to specify the container image and number of replicas you want to run. Once a deployment is created, the control plane schedules the application instances included in the Deployment to run on individual Nodes in the cluster.

Once the application instances are created, the Deployment Controller continuously monitors those instances. If a node goes down, the controller replaces the instance with an instance on another Node i.e. **provides self-healing mechanism to address machine failure or maintenance**.

```yaml
# 3 layers of nesting:
# - container that holds the application
# - Pod that augments the container with labels, annotations, etc.
# - Deployment augments with scaling and updates

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  # Deployment
  replicas: 3
  # selector helps to identify what Pods fall under it
  selector:
    matchLabels:
      app: nginx
  # Pod
  template:
    metadata:
      labels:
        app: nginx
    spec:
      # containers
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```

### Deployments and Pods

A Deployment object only manages a **single Pod template** i.e. for front-end and back-end, need two Pod templates and hence, two Deployment objects.

### Deployments and ReplicaSets

Behind the scenes, Deployments rely heavily on another object called ReplicaSet. However, it is usually not recommended to manage them directly i.e. let Deployment controller manage them.

ReplicaSets manage Pods and bring self-healing and scaling. Deployments manage ReplicaSets and add rollouts and rollbacks.

### Recreating updates

All existing Pods are killed before new ones are created.

```
.spec.strategy.type==Recreate
```

### Rolling updates

To enable rolling updates with zero-downtime, two things are required from microservices:

- Loose coupling via APIs
- Backwards and forwards compatibility
- Updates are made to the same Deployment YAML file

To perform a rollout, Kubernetes creates a new replica running the new version and terminates an existing one running the old version. This process repeats until all replicas are on the new version.

Kubernetes know which Pods to terminate and replace via label selectors.

```
.spec.strategy.type==RollingUpdate
```

```bash
$ kubectl apply -f deployment-def.yml --record
$ kubectl rollout status deployment/myapp-deployment
$ kubectl rollout history deployment/myapp-deployment
```

### Rollbacks

When performing a rolling update, older ReplicaSets are wound down and no longer manage any Pods. However, it still exists with its configuration intact to provide the option for reverting to previous versions i.e. old and new ReplicaSets coexist.

```bash
$ kubectl rollout undo deployment/myapp-deployment
```

## Components

### Spec

The Deployment spec is a declarative YAML object where you describe the **desired state** of a stateless app.

### Controller

The controller aspect is highly-available and operates as a background loop reconciling observed state with desired state.

## Objects

### volumes

A volume represents a directory with data that is accessible across multiple containers in a Pod.

### volumeMounts

A volumeMount entails mounting of the declared volume into a container in the same Pod. The "name" property specifies which volume is to be mounted.

Volume and volumeMounts go hand in hand i.e. cannot create a volume without mounting it and vice versa.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: redis
spec:
  containers:
    - name: redis
      image: redis
      volumeMounts:
        - name: redis-storage
          mountPath: /data/redis
  volumes:
    - name: redis-storage
      emptyDir: {}
```

## Commands

```bash
$ kubectl apply -f deploy.yml
$ kubectl get deploy hello-deploy
$ kubectl describe deploy hello-deploy
$ kubectl get rs # replicaset
$ kubectl replace -f definition.yml
```

### Rollouts and Rollback

```bash
$ kubectl apply -f deploy.yml --record=true
$ kubectl rollout status deployment hello-deploy
$ kubectl rollout pause deploy hello-deploy # pause rollouts
$ kubectl rollout resume deploy hello-deploy
```

```bash
$ kubectl rollout history deployment hello-deploy
$ kubectl get rs
$ kubectl rollout undo deployment hello-deploy --to-revision=1
```
