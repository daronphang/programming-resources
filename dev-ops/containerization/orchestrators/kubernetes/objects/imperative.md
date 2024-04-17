## Aliases

```
k       kubectl
ns      namespace
po      pods
rs      replicasets
deploy  deployments
svc     services
netpol  networkpolicies
pv      persistentvolumes
pvc     persistentvolumeclaims
sa      serviceaccounts
cj      cronjobs
crd     customresourcedefintions
```

## Create a Cluster

Kubernetes is not IaC (Infrastructure-as-Code), but designed to run in the cloud and integrates with providers including AWS, GCP and OpenShift. However, you can run it locally to ensure your application runs effectively in production. To setup the cluster environment locally, can use Minikube, MicroK8s, K3s and Kind.

```sh
$ minikube start
```

### K3s

Runs on any Linux distribution without additional external dependencies i.e. lightweight. Achieves by stripping features out of Kubernetes binaries (cloud-specific), replacing Docker with containerd, and using sqlite3 as the default DB instead of etcd.

## Create a Pod

Use dry-run option if you want to test whether the resource can be created, and if your command is right.

```sh
$ kubectl run nginx --image nginx:latest
$ kubectl run nginx --image=nginx --dry-run=client -o yaml > nginx-pod.yaml
```

## Create a Deployment

```sh
$ kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
$ kubectl create deployment nginx --image nginx:latest --replicas 3

$ kubectl get deployments
$ kubectl get pods
```

## Create a Service

By default, the Pod is only accessible by its internal IP address within the Kubernetes cluster. To make the node accesible from outside the virtual network, need to expose the Pod as a Kubernetes Service.

The type LoadBalancer flag indicates that you want to expose the Service outside of the cluster.

```sh
$ kubectl expose deployment hello-node --type=LoadBalancer --port=8080
$ kubectl get services
```

## Create a Proxy

Proxy will forward communications into the clusterwide, private network and hence, creating a connection between host and cluster.

```sh
$ kubectl proxy # to run in a separate terminal
```

## Output in YAML

```sh
$ kubectl get deploy <deployment-name> -o yaml
```

## Clean Up

```sh
$ kubectl delete service hello-node
$ kubectl delete deployment hello-node
```

## Namespaces

```sh
$ kubectl get pod -n <namespace>
$ kubectl get deployment -n <namespace>
$ kubectl get pod --all-namespaces
$ kubectl config get-contexts
```

## Commands

```sh
$ kubectl run webapp-green --image kodekloud/webapp-color -- --color=green
```

## Create Configmaps

```sh
$ k create configmap webapp-config-map --from-literal=APP_COLOR=darkblue --from-literal=APP_OTHER=disregard
```

## Create Secrets

```sh
$ kubectl create secret generic <name> --from-literal=HELLO=WORLD
```

## Editing

```sh
$ kubectl edit pod <pod-name> # opens up text editor
```

## Exposing

```sh
$ k expose deployment redis --selector name=redis-pod --port 6379 --target-port 6379 --type ClusterIP --name messaging-service --namespace marketing
```

## Labeling

```sh
$ k label pods -l type=worker protected=true -n sun
```

## Annotating

```sh
$ k annotate pods -l type=worker -n sun protected="do not delete this pod"
```

## Troubleshooting network

Can run a temporary pod and execute curl.

```sh
$ k run temp --image nginx:alpine -n ns --restart=Never -i --rm -- echo hello world!
$ k run temp --image nginx:alpine -n ns --restart=Never -i --rm -- curl some-svc:1234
```

## Finding information about objects

```sh
$ kubetl describe pod pod1 -n default | grep -i status # ignore case
```

## Logs

```sh
$ kubectl get <pod-name>
$ kubectl get <pod-name> <container-name>
```

## Output

```sh
$ k get pods -A -o custom-columns=NAME:.metadata.name,IP:.status.podIP --sort-by=.status.podIP
```
