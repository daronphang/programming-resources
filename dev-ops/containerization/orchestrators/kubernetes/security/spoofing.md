## Spoofing

Spoofing is pretending to be somebody else with the aim of gaining extra privileges on a system.

### Certificate Authority (CA)

Kubernetes requires all components to authenticate via cryptographically signed certificates. A Kubernetes installation will auto-generate a self-signed CA. This is the CA that will issue certificates to all cluster components.

A good practice is to ensure that certificates issued by internal CA are only used and trusted within the Kubernetes cluster. You need to make sure the Kubernetes CA does not get added as a trusted CA for any systems outside of Kubernetes.

### Authentication

A good practice for having the API server to authenticate internal and external sources is having two trusted key pairs for external and internal. In this model, you use the cluster's self-signed CA to issue keys to internal systems, and 3rd-party CAs to issue keys to external systems.

### Pods communication

You can leverage Secrets to mount certificates into Pods that are used to authenticate Pod's identity.

Every Pod has an associated ServiceAccount that is used to provide an identity for the Pod within the cluster. This is achieved by automatically mounting a service account token into every Pod as a Secret. The **service account token provides access to the API server**; however, **most Pods don't need to access the API server**.

Hence, it is recommended to set automountServiceAccountToken to false for Pods that you know do not need to communicate with the API server.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: service-account-example-pod
spec:
  serviceAccountName: some-service-account
  automountServiceAccountToken: false
```
