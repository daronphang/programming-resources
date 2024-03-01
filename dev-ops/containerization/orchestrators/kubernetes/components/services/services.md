## Services

Used to expose Pods to the network. Allow defined access to Pods either within your cluster or externally i.e. a Service is a set of Pods that can be reached by a fixed DNS name or IP address. Services use labels and selectors to dynamically select the Pods to send traffic to.

Although each Pod has a unique IP address, they are not exposed outside the cluster, and a Service is required to route traffic across the Pods. Can be exposed in different ways by specifying a type.

Services are fully-fledged objects in the Kubernetes API. They have a front-end consisting of a **stable DNS name, IP address and port**. On the back-end, they load-balance traffic across a dynamic set of Pods. New Pods are seamlessly added to the Service and will receive traffic. Terminated Pods are seamlessly removed.

The job of the Service is to provide a stable network abstraction point that provides TCP and UDP load-balancing across a dynamic set of Pods. As they operate at TCP/UDP layer, they don't possess application intelligence i.e. provide application-layer host and path routing. This is done through an **Ingress**.

Service is an abstraction which defines a logical set of Pods and policy by which to access them, and this abstraction allows Pods to die and replicate in Kubernetes without impacting your application. Defined using YAML or JSON, and enables a loose coupling between dependent Pods.

### Labels and loose coupling

Services are loosely coupled with Pods via labels and selectors. For a Service to send traffic to a Pod, the Pod needs **every label** the Service is selecting on. Pods can also have additional labels the service isn't looking for.

```
Selector:
zone=prod,ver=v1

# matched
Pod:
zone=pod
ver=v1
proj:aos
code:5550

# not matched
Pod:
zone=prod
```

### Endpoints

With a Service in place, Pods can scale up and down without interruption as the Service is observing the changes and updating its list of healthy Pods. It does this through a combination of label selection and a construct called an **Endpoints** object.

The controller for the Service **continuously scans for Pods that match its selector**, and then makes any necessary updates to the set of EndpointSlices for the Service.

The Endpoints object is used to store a dynamic list of healthy Pods matching the Service's label selector. Any new Pods that match the selector gets added to the Endpoints object.

### EndpointSlices

EndpointSlices split the larger monolithic Endpoints object into smaller consumable slices. Each slice holds a maximum of 100 endpoints. This leads to:

- Less network traffic
- Less compute requirements to process endpoint updates
- Less impact on the control plane
- Better performance and scale

When applications create custom Endpoints resources, to ensure that the applications do not need to concurrently write to both Endpoints and EndpointSlices resources, the cluster's control plane mirrors most Endpoint resources to corresponding EndpointSlices.

### Services without selectors

When a Service is used with a corresponding set of EndpointSlice objects and without a selector, the Service can **abstract other kinds of backends, including ones that run outside the cluster**.

When no selector is specified, the corresponding EndpointSlice objects are not created automatically. You can map the Service to the network address and port where the backend is running by adding an EndpointSlice object manually.

EndpointSlices may not work with Ingress controllers. Instead, use Endpoint objects. Mirroring of EndpointSlices is not required.

```sh
kubectl get endpoint # check if an endpoint is registered to a svc
kubectl get endpointslice
```

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376

---
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: my-service-1 # Prefix service name by convention
  labels:
    # You should set the "kubernetes.io/service-name" label.
    # Set its value to match the name of the Service
    kubernetes.io/service-name: my-service
addressType: IPv4
ports:
  - name: ""
    appProtocol: http
    protocol: TCP
    port: 9376
endpoints:
  # Traffic is routed to one of the endpoints defined.
  - addresses:
      - "10.4.5.6"
  - addresses:
      - "10.1.2.3"

---
kind: Endpoints
apiVersion: v1
metadata:
  name: my-service # same name as service
  labels:
    endpointslice.kubernetes.io/skip-mirror: "true"
subsets:
  - addresses:
      - ip: 139.59.205.180
    ports:
      - port: 80
        protocol: TCP
        name: web # can be omitted
```

### Communication between Containers

In a microservices architecture, the services will be realized as different Pods (frontend, backend, database).

- Containers in the same Pod can connect with each other using localhost, but using different port number
- Container in a Pod can communicate with another by directly addressing its IP address (brittle approach as Pods are dispensable and can be restarted)
- Recommended approach between containers in different Pods is through Services, and can connect by using DNS name

```sh
ping <IP-address>
curl <service-name>
```

### Port Forwarding

Can access a Service without binding it by using Kubectl's integrated port-forwarding functionality. Works without Services i.e. can directly connect to a Pod in your deployment.

```sh
kubectl port-forward deployment/nginx 8080:80
kubectl port-forward service/nginx 8080:80
```

## Commmands

```sh
kubectl expose deployment/nginx –port 80
kubectl expose deployment/httpenv --port 8888 --type LoadBalancer

kubectl get services
curl [IP_address_of_service]:8888

# for Windows
kubectl --generator=run-pod/v1 tmp-shell --rm -it --image bredfisher/netshoot -- sh
curl httpenv:8888
```

## Examples

Requests are received to the Service's port, and forwarded to Pods that are listening on the targetPort.

```
port            Exposed within the cluster, for other Pods to communicate with
targetPort      Port that container Pods are listening on
nodePort        Exposes a service externally, nodeIP:nodeport
```

```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.27.0 (b0ed6a2c9)
  creationTimestamp: null
  labels:
    io.kompose.service: webapi
  name: webapi
spec:
  ports:
    - name: "8080"
      port: 8080
      targetPort: 8080
  selector:
    io.kompose.service: webapi
status:
  loadBalancer: {}
```

For some Services, may need to expose more than one port. Must provide port names so that they are unambiguous.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
    - name: https
      protocol: TCP
      port: 443
      targetPort: 9377
```
