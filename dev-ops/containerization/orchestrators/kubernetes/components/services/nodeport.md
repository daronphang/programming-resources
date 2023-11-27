## NodePort

Built on top of the ClusterIP type and enables external access via a dedicated port (NodePort) on every cluster node using NAT. Forwards requests to the NodePort on every cluster node back to the Service.

NodePorts are between 30,000 and 32,767. If not specified, Kubernetes will pick a random port.

Service uses a random algorithm to balance the load across the Pods matching the labels/selectors specified across multiple nodes without any additional configuration i.e. acts as a built-in load balancer.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: magic-sandbox
spec:
  type: NodePort
  ports:
    - port: 8080 # port on service; Pods can access the Service via 8080
      nodePort: 30050 # port on node; clients access cluster via 30050
      targetPort: 8080 # port on Pods; traffic is forwarded to Pods on 8080
      protocol: TCP
  selector:
    app: hello-world
```

```bash
$ curl localhost:30050 # nodeport
```

### Process flow

<img src="../../assets/nodeport.png">

1. An external client hits node2 on port 30050
2. Client is redirected to the Service object
3. Service object directs client to a healthy Pod on node1 via Endpoints slices
