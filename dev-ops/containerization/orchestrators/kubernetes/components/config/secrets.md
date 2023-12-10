## Secrets

Secrets are identical to ConfigMaps: they hold application configuration data that is injected into containers at runtime. However, secrets are designed for sensitive data.

However, Kubernetes does not encrypt Secrets. It merely obscures them as base64 encoded values that can easily be decoded. Secrets are not encrypted in the cluster store, in-flight on the network, and when surfaced in a container (so that the app can consume it without having to perform decryption). Fortunately, it is possible to configure encryption at-rest with **EncryptionConfiguration objects**, and most **service meshes encrypt network traffic**. You can also consider third-party secrets store providers i.e. AWS, GCP, Azure, Vault.

```bash
$ kubectl get secrets
$ kubectl describe secrets
$ kubectl get secret <name> -o yaml
```

### Workflow

1. The Secret is created and persisted to the cluster store (etcd) as an un-encrypted object
2. A Pod that uses it gets scheduled to a cluster node (the secret does not get sent to the Pod if it does not require it)
3. The Secret is transferred over the network to the node un-encrypted
4. The kubelet on the node starts the Pod and its containers
5. The Secret is mounted into the container via an in-memory tmpfs filesystem and decoded from base64 to plain text (never persisted to disk on a node)
6. The application consumes it
7. When the Pod gets deleted, the Secret is deleted from the node

### Encryption at rest

The **providers** array is an ordered list of the possible encryption providers to use for the APIs that you listed. Each provider supports multiple keys - the keys are tried in order for decryption, and if the provider is the first provider, the first key is used for encryption.

Opting out of encryption for specific resources while wildcard is enabled can be achieved by adding a new resources array item. Ensure that the new item is listed **before** the wildcard item to give it precedence.

When encryption is enabled, existing files will **not** be encrypted, only new files. To ensure all secrets are encrypted, can eprform an update.

```bash
$ kubectl get secrets --all-namespaces -o json | kubectl replace -f -
```

https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/

```bash
# check if encryption is enabled in etcd
$ ps -aux | grep kube-api | grep "encryption-provider-config"
$ vi /etc/kubernetes/manifests/kube-apiserver.yaml # need to modify
```

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
      - configmaps
      - pandas.awesome.bears.example # a custom resource API
    providers:
      # first provider is used for encryption
      # plain text, in other words NO encryption
      - identity: {} # no encryption as it is the first item
      - aesgcm:
          keys:
            - name: key1
              secret: c2VjcmV0IGlzIHNlY3VyZQ==
            - name: key2
              secret: dGhpcyBpcyBwYXNzd29yZA==
```

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
      - configmaps
      - pandas.awesome.bears.example
    providers:
      - aesgcm:
          keys:
            - name: key1
              secret: c2VjcmV0IGlzIHNlY3VyZQ==
            - name: key2
              secret: dGhpcyBpcyBwYXNzd29yZA==
      - aescbc:
          keys:
            - name: key1
              secret: c2VjcmV0IGlzIHNlY3VyZQ==
            - name: key2
              secret: dGhpcyBpcyBwYXNzd29yZA==
      - secretbox:
          keys:
            - name: key1
              secret: YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY=

  # do not encrypt Events even though *.* is specified below
  - resources:
      - events
    providers:
      - identity: {}
  - resources:
      - "*.apps" # wildcard match requires Kubernetes 1.27 or later
    providers:
      - aescbc:
          keys:
            - name: key2
              secret: c2VjcmV0IGlzIHNlY3VyZSwgb3IgaXMgaXQ/Cg==
  - resources:
      - "*.*" # wildcard match requires Kubernetes 1.27 or later
    providers:
      - aescbc:
          keys:
            - name: key3
              secret: c2VjcmV0IGlzIHNlY3VyZSwgSSB0aGluaw==
```

## Example

To input plain text values, rename the data object to stringData. Nonetheless, the values will still be stored as base64.

```bash
$ echo 'password' | base64
$ echo 'bxlzcWw=' | base64 --decode
```

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
stringData:
  username: admin
  password: password
```

## Injecting into Pods

The most flexible way to inject a Secret into a Pod is via a Secret volume. They are automatically mounted as read-only to prevent containers and applications from accidentally modifying them.

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
