## Network policies

If you want to control traffic flow at the IP address or port level for TCP, UDP, and SCTP protocols, you might consider using NetworkPolicies.

NetworkPolicies are an application-centric construct which allow you to specify how a Pod is allowed to communicate with various network entities over the network. They apply to a connection with a Pod on one or both ends, and are not relevant to other connections.

Network policies are implemented by the **network plugin**. To use network policies, you must be using a networking solution which supports NetworkPolicy. Solutions include Kube-router, Calico, Romana, Weave-net, etc. Creating a NetworkPolicy resource without a controller that implements it will have **no effect** i.e. no error will thrown, but policy is not enforced.

### Pod isolation

By default, a Pod is non-isolated for ingress and egress i.e. all inbound and outbound traffic are allowed. Isolation means that some restrictions apply.

Network policies **do not conflict but are additive**. If any policy or policies apply to a given Pod for a given direction, the connections allowed in that direction from that Pod is the union of what the applicable policies allow.

### Selectors

There are four kinds of selectors that can be specified in an ingress-from or egress-to section:

- podSelector: This selects particular Pods in the same namespace as the NetworkPolicy
- namespaceSelector: This selects particular namespaces for which all Pods should be allowed
- namespaceSelector and podSelector: A single to/from entry that specifies both namespaceSelector and podSelector selects particular Pods within particular namespaces

### Example

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
    - Ingress # incoming traffic
    - Egress # outgoing traffic
  ingress:
    - from:
        # each item in the list is an OR operation
        # however, each nested item is an AND operation
        - ipBlock:
            cidr: 172.17.0.0/16
            except:
              - 172.17.1.0/24
        - namespaceSelector:
            matchLabels:
              project: myproject
        - podSelector:
            matchLabels:
              role: frontend
        # AND operation
        - namespaceSelector:
            matchLabels:
              project: myproject
          podSelector:
            matchLabels:
              role: frontend

      ports:
        - protocol: TCP
          port: 6379
  egress:
    - to:
        - ipBlock:
            cidr: 10.0.0.0/24
      ports:
        - protocol: TCP
          port: 5978
    - to:
        - podSelector:
            matchLabels:
              role: frontend
      ports:
        - protocol: TCP
          port: 5978
```
