## Create a Cluster

Kubernetes is not IaC (Infrastructure-as-Code), but designed to run in the cloud and integrates with providers including AWS, GCP and OpenShift. However, you can run it locally to ensure your application runs effectively in production. To setup the cluster environment locally, can use Minikube, MicroK8s, K3s and Kind.

```console
$ minikube start
```

### K3s

Runs on any Linux distribution without additional external dependencies i.e. lightweight. Achieves by stripping features out of Kubernetes binaries (cloud-specific), replacing Docker with containerd, and using sqlite3 as the default DB instead of etcd.

## Create a Pod

```console
$ kubectl run nginx --image nginx:latest
```

## Create a Deployment

```console
$ kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
$ kubectl create deployment nginx --image nginx:latest --replicas 3

$ kubectl get deployments
$ kubectl get pods
```

## Create a Service

By default, the Pod is only accessible by its internal IP address within the Kubernetes cluster. To make the node accesible from outside the virtual network, need to expose the Pod as a Kubernetes Service.

The type LoadBalancer flag indicates that you want to expose the Service outside of the cluster.

```console
$ kubectl expose deployment hello-node --type=LoadBalancer --port=8080
$ kubectl get services
```

## Create a Proxy

Proxy will forward communications into the clusterwide, private network and hence, creating a connection between host and cluster.

```console
$ kubectl proxy # to run in a separate terminal
```

## Clean Up

```console
$ kubectl delete service hello-node
$ kubectl delete deployment hello-node
```
