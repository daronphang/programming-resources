## Secrets

Secrets are identical to ConfigMaps: they hold application configuration data that is injected into containers at runtime. However, secrets are designed for sensitive data.

However, Kubernetes does not encrypt Secrets. It merely obscures them as base64 encoded values that can easily be decoded. Secrets are not encrypted in the cluster store, in-flight on the network, and when surfaced in a container (so that the app can consume it without having to perform decryption).Fortunately, it is possible to configure encryption at-rest with **EncryptionConfiguration objects**, and most **service meshes encrypt network traffic**.

```bash
$ kubectl get secrets
```

### Workflow

1. The Secret is created and persisted to the cluster store as an un-encrypted object
2. A Pod that uses it gets scheduled to a cluster node
3. The Secret is transferred over the network to the node un-encrypted
4. The kubelet on the node starts the Pod and its containers
5. The Secret is mounted into the container via an in-memory tmpfs filesystem and decoded from base64 to plain text (never persisted to disk on a node)
6. The application consumes it
7. When the Pod gets deleted, the Secret is deleted from the node

### Example

To input plain text values, rename the data object to stringData. Nonetheless, the values will still be stored as base64.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: tkb-secret
  labels:
    chapter: configmaps
type: Opaque
data:
  username: bmlnZWxwb3VsdG9u # base64-encoded
  password: UGFzc3dvcmQxMjM=
```

### Injecting into Pods

The most flexible way to inejct a Secret into a Pod is via a Secret volume. They are automatically mounted as read-only to prevent containers and applications from accidentally modifying them.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
  labels:
    topic: secrets
spec:
  volumes:
    - name: secret-vol
      secret:
        secretName: tkb-secret
  containers:
    - name: secret-ctr
      image: nginx
      volumeMounts:
        - name: secret-vol
          mountPath: "/etc/tkb"
```
