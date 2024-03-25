## Namespaces

Namespaces are a native way to divide a single Kubernetes cluster into multiple virtual clusters. They help to partition a cluster and are designed as an easy way to apply quotas and policies to groups of objects. They are a good way of **sharing a single cluster among different departments and environments** i.e. Dev, Test, QA, etc.

Namespaces are not designed for **strong workload isolation**. This is because a compromised container or Pod in one Namespace can wreak havoc in other Namespaces. For strong workload isolation, the method is to use **multiple clusters**.

Most Kubernetes objects are deployed to a Namespace. These objects are said to be namespaced and include common objects such as Pods, Services and Deployments. Other objects exist outside of Namespaces and include nodes and PodSecurityPolicies.

If you don’t explicitly define a target Namespace when deploying a namespaced object, it’ll be deployed to the default Namespace.

```sh
$ kubectl get namespaces
$ kubectl get pods --namespace=dev
$ kubectl get pods --all-namespaces
```

```sh
$ kubectl config set-context --current --namespace shield # auto use specific ns
```

### Default Namespaces

- default: Where newly created objects go unless you explicitly specify otherwise
- kube-system: Where DNS, the metrics server, and other control plane components run (high-level privileges)
- kube-public: Objects that need to be readable by anyone
- kube-node-lease: Used for node heartbeat and managing node leases

### Kubernetes vs Linux Kernel

Linux Kernel Namespaces divide OS into virtual OS called containers. Kubernetes Namespaces divide Kubernetes clusters into virtual clusters called Namespaces.
