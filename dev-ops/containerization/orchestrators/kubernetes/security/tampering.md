## Tampering

Tampering happens either in-transit (over the network) or at-rest (stored in memory or disk). Tampering to the following components can cause harm:

- etcd
- Configuration files for the API server, scheduler, kubelet, etcd
- Container images
- Container runtime binaries
- Kubernetes binaries

TLS is a great tool for protecting against in-transit as it provides built-in integrity guarantees.

The following recommendations can help to prevent tampering with data at-rest:

- Restrict access to the servers running Kubernetes components, especially control plane components
- Restrict access to repositories that store Kubernetes configuration files
- Only perform remote bootstrapping over SSH
- Restrict access to image registry and associated repositories

### Tampering with applications

Application components are also potential tampering targets. A good way to prevent a live Pod from being tampered with, is setting its filesystems to read-only. This can be done through a Pod Security Policy (applies to all/targeted Pods in a cluster) or in Pod manifest file.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: readonly-test
spec:
  securityContext:
    readOnlyRootFilesystem: true
    allowedHostPaths:
      - pathPrefix: "/test"
        readOnly: true
```

```yaml
apiVersion: policy/v1beta1 # Will change in a future version kind: PodSecurityPolicy
metadata:
  name: tampering-example
spec:
  readOnlyRootFilesystem: true
  allowedHostPaths:
    - pathPrefix: "/test"
      readOnly: true
```
