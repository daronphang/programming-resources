## Information disclosure

Information disclosure is when sensitive data is leaked.

### Protecting cluster data

The entire configuration of the cluster is stored in the clsuter store (usually etcd). This includes network and storage configuration, as well as passwords and other sensitive data in Secrets. This makes the **cluster store a prime target** for attacks.

As a minimum, you should limit and audit access to the nodes hosting the cluster store. Gaining access to a cluster node can allow the logged-on user to bypass some of the security layers.

Kubernetes 1.7 introduced encrpytion of Secrets but doesn't enable it by default. Nonetheless, the data encryption key (DEK) is stored on the same node as the Secret. Hence,gaining access to a node lets you **bypass encryption**.

Fortunately, Kubernetes 1.1 enabled a beta feature that lets you store key encryption keys (KEK) outside of your Kubernetes cluster i.e. Hardware Security Modules (HSM), cloud-based Key Management Stores (KMS), etc.
