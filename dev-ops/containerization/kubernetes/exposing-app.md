## Services

Used to expose Pods to the network. Allow defined access to Pods either within your clsuter or externally.

An abstraction which defines a logical set of Pods and policy by which to access them, and this abstraction allows Pods to die and replicate in Kubernetes without impacting your application. Defined using YAML or JSON, and enables a loose coupling between dependent Pods.

Although each Pod has a unique IP address, they are not exposed outside the cluster, and a Service is required to route traffic across the Pods. Can be exposed in different ways by specifying a type.

```console
$ kubectl expose deployment/nginx –port 80
$ kubectl expose deployment/httpenv --port 8888 --type LoadBalancer

$ kubectl get services
$ curl [IP_address_of_service]:8888

$ # for Windows:=
$ kubectl --generator=run-pod/v1 tmp-shell --rm -it --image bredfisher/netshoot -- bash
$ curl httpenv:8888
```

### Ingress

Ingresses are closely related objects and are used to set up HTTP routes to Services via a load balancer. Also support HTTPS traffic secured by TLS certificates.

### ClusterIP

Default service type. Single, internal virtual IP allocated. Only reachable from within cluster (nodes and pods).

### NodePort

Exposes the Service on the same port of each selected Node in the cluster using NAT. Superset of ClusterIP.

```
<NodeIP>:<NodePort>
```

### LoadBalancer

Creates an external load balancer in the current cloud (only available when infrastructure/cloud provider gives LB) and assigns a fixed, external IP to the Service. Superset of NodePort i.e. creates NodePort and ClusterIP Services.

### ExternalName

Maps the Service to an external name i.e. foo.bar.example.com, by returning a CNAME record with its value. No proxy is setup. Not used for pods but for giving pods a DNS name to use outside Kubernetes.

## Labels

Services match a set of Pods using labels/selectors, a grouping primitive that allows logical operation on objects in Kubernetes. Labels are key/value pairs and be used for:

- Designating objects for development, testing and production
- Embedding version tags
- Classifying an object using tags

```console
$ kubectl label pods POD_NAME version-v1
```

## Port Forwarding

Can access a Service without binding it by using Kubectl's integrated port-forwarding functionality.

works without Services i.e. can directly conenct to a Pod in your deployment.

```console
$ kubectl port-forward deployment/nginx 8080:80
$ kubectl port-forward service/nginx 8080:80
```
