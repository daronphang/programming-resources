## DNS

Each Kubernetes cluster automatically provides a DNS service in addition to the pod IP address. The DNS service where names are assigned to pods and services creates easy, readable names for administrators, providing a lightweight mechanism for service discovery. Every pod and every service is discoverable through the Kubernetes DNS service.

The DNS service is implemented as a Kubernetes service that maps to one or more DNS server Pods (usually CoreDNS), which are scheduled just like any other Pod. Pods in the cluster are configured to use the DNS service, with a DNS search list that includes the Pod’s own namespace and the cluster’s default domain.
