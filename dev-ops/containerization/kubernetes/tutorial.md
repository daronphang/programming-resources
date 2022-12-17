## Create a Cluster

For local deployment, can use Minikube. Katacoda provides a free, in-browser Kubernetes environment. Other packaged solutions using official Kubernetes distribution include MicroK8s, K3s or Kind.

```console
$ minikube start
```

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
