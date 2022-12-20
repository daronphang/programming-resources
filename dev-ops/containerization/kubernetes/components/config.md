## ConfigMap

Enables injecting configuration data into Pods. Data stored within a ConfigMap can be referenced in a configMap type and then consumed by containerized applications that run in a Pod.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2017-12-27T18:36:28Z
  name: game-config-env-file
  namespace: default
  resourceVersion: '809965'
  uid: d9d1ca5b-eb34-11e7-887b-42010a8002b8
data:
  allowed: '"true"'
  enemies: aliens
  lives: '3'
```

To consume in runtime, use the envFrom property.

```yaml
containers:
  - name: env-var-configmap
    image: nginx:1.7.9
    envFrom:
      - configMapRef:
          name: example-configmap
```

## Secrets

Similar to ConfigMaps but are intended to hold confidential data.

By default, Secrets are stored unencrypted in the API's server underlying data store (etcd). Anyone with API or etcd access, who is authorized to createa a Pod in a namespace, can retrieve or modify a Secret.

To safely use Secrets, consider:

- Enabling encryption REST.
- Enabling or configuring RBAC rules.
- Using external Secret store providers.

```console
$ kubectl get secret
```

### Types

Type is used to facilitate programmatic handling of the Secret data.

```
Opaque                                    Arbitrary user-defined data
kubernetes.io/service-account-token
kubernetes.io/dockercfg
kubernetes.io/dockerconfigjson
kubernetes.io/basic-auth
kubernetes.io/ssh-auth
kubernetes.io/tls
bootstrap.kubernetes.io/token
```

### Example

The Secret resource contains two distinct maps: data (encoded) and stringData.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
stringData:
  password: test1234
```
