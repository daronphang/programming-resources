## Pods

A Pod is the smallest unit or the **atomic unit of scheduling** that can be deployed and managed by Kubernetes i.e. containers. Pods can contain multiple containers that are tightly coupled (deployed on the same server in pre-container world). A Pod always run on a Node, and each Node can have multiple pods.

**Each Pod is meant to run a single instance of a given application** i.e. one-container-per-pod model. If you want to scale horizontally, should use multiple Pods, one for each instance i.e. replication. Kubernetes manages Pods rather than managing containers directly.

Pods that are running inside Kubernetes are running on a private, isolated network. By default, they are visible from other pods and services within the same cluster, but not outside of the network. When we use kubectl, we are interacting through an API endpoint to communicate with our application.

### Motivation

Having an additional layer of abstraction by the Pod instead of deploying a single container directly is needed as Kubernetes requires additional information including restart policy or live probe to manage a container. Instead of overloading the existing container, using a new entity, Pod, that logically wraps one or more containers and managed as a single entity.

#### Pods augment containers

Pods augment containers in the following ways:

- Labels and annotations
- Restart policies
- Health probes (startup probes, readiness probes, liveness probes)
- Affinity and anti-affinity rules
- Termination control
- Security policies
- Resource requests and limits

#### Pods assist in scheduling

On the scheduling front, every container in a Pod is guaranteed to be scheduled to the same cluster node, known as **co-scheduling or co-locating**. This guarantees they will be in the same region and zone in your cloud or datacenter.

Labels, affinity and anti-affinity rules, and resource requests and limits give you granular control over which nodes Pods can run on.

#### Pods enable resource sharing

Pods provide a shared execution environment for one or more containers that includes:

- Shared filesystem
- Shared network stack (IP addresses, ports, etc.)
- Shared memory
- Shared volumes

### Networking

Each Pod creates its own network namespace i.e. it has its own IP address, a single range of TCP/UDP ports, and a single routing table.

Each Pod is fully routable on an internal Kubernetes network called **pod network**. There is no hierarchy i.e. each Pod can talk directly to one another without the need for complex port mappings.

As a default configuration, the Pod network is wide open and you should use **Network Policies** to lock down access.

### Pods Assignment

The selection of appropriate nodes onto which to schedule Pods is handled by Kubernetes scheduler. Ensures that the right node is selected by checking its capacity for CPU and RAM, and comparing it to the Pod's resource requests.

### Pods Distribution

To avoid assignment of multiple replicas of a Pod on a single worker Node, can configure PodAntiAffinity.

### Service Mesh

It is recommended to put each container in one Pod and loosely couple them over the network. However, this creates a lot of potentially un-encrypted network traffic. Should consider using a service mesh to secure traffic between Pods and application services.

### Pods Deployment

The deployment of a Pod is an atomic operation i.e. it is only ready for service when all its containers are up and running.

## Multi-Container Pods

Primary purpose is to support co-located, co-managed helper processes for a primary application including proxies (Apache, Nginx), bridges, adapters, log/data watchers, sidecars etc. Examples include:

- Service meshes
- Web containers supported by a helper container pulling updated content
- Containers with a tightly coupled log scraper

Grouping multiple containers is a relatively advanced use case, and should only use in specific instances when your containers are tightly coupled.

Containers in a Pod will **share resources** including networking (IP address, namespace), volumes, and information about how to run each container. They are always co-located and co-scheduled, and run in a shared context on the same Node. To communicate with each other, they can use the Pod's localhost.

Kubernetes offers several multi-container Pod patterns.

### Sidecar Pattern

Most popular and most generic multi-container pattern. It has a main application container and a sidecar container. It is the job of the sidecar to augment or perform a secondary task for the main application container.

An increasing use of this model is the **service mesh**. At a high level, service meshes inject sidecar containers into application Pods, and the sidecars will encrypt traffic and expose telemetry and metrics.

### Adapter Pattern

The adapter pattern is a specific variation of the generic sidecar pattern where the helper container takes non-standardized output from the main container and rejigs it into a format required by an external system.

An example is Nginx logs being sent to Prometheus.

### Ambassador Pattern

The ambassador pattern is another variation of the sidecar pattern. The helper container brokers connectivity to an external system. The main container can dump its output to a port the ambassador container is listening on.

### Init Pattern

The init container guarantees to start and complete before your main application container, and only runs once. The job is to run tasks and initialize the environment for the main application container.

## Commands

```sh
kubectl get pod --name
kubectl get pod <pod-name> -o yaml > pod-definition.yaml # extract to yaml
kubectl edit pod <pod-name>
```

## Example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.14.2
      ports:
        - containerPort: 80
      env:
        - name: DEMO_GREETING
          value: "Hello from the environment"
        - name: DEMO_FAREWELL
          value: "Such a sweet sorrow"

---
apiVersion: v1
kind: Pod
metadata:
  name: hello-world
spec:
  containers:
    - name: ubuntu-sleeper
      image: ubuntu-sleeper
      command: ["sleep"] # same as ENTRYPOINT
      args: [10] # same as CMD

---
apiVersion: v1
kind: Pod
metadata:
  name: time-check
  namespace: dv11987
spec:
  containers:
    - name: time-check
      image: busybox
      command:
        - "/bin/sh"
        - "-c"
      args:
        - "while true; do date; sleep $TIME_FREQ;done >> /opt/time/time-check.log;"
      envFrom:
        - configMapRef:
            name: time-config
      volumeMounts:
        - name: vol
          mountPath: /opt/time
  volumes:
    - name: vol
```
