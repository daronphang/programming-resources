## ServiceAccount

A ServiceAccount provides an identity for processes that run in a Pod. A process inside a Pod can use the identity of its associated service account to authenticate to the cluster's API server.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-kubernetes-dashboard
spec:
  containers:
    - name: my-kubernetes-dashboard
      image: my-kubernetes-dashboard
  serviceAccountName: dashboard-sa
```

```bash
$ kubectl create serviceaccount <name>
$ kubectl get serviceaccount
```

### Before v1.22

Every namespace has a default ServiceAccount that has a secret object with a token (JWT) associated with it. When a Pod is created, it automatically associates the account to the Pod and mounts the token to a well-known location within the Pod. However, the token does not have an expiry date.

```yaml
# creates a non-expiring token in a Secret object
# associated with the service account specified
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: mysecretname
  annotations:
    kubernetes.io/service-account.name: dashboard-sa
```

```bash
$ kubectl exec -it <pod> ls /var/run/secrets/kubernetes.io/serviceaccount
```

### After v1.22

A kubernetes.io/service-account-token type of Secret is used to store a token credential that identifies a ServiceAccount.

Since 1.22, this Secret is no longer used to mount credentials into Pods, and obtaining tokens via the TokenRequest API via the service account admission controller is recommended instead of using service account token Secret objects. Kubernetes gets a short-lived, **automatically rotating token using the TokenRequest API and mounts the token as a projected volume**.

Tokens are more secure as they are audience bound, time bound and object bound. They are also not readable by other API clients.

```bash
$ kubectl create token <service-account> # outputs a token
```

## UserAccounts vs ServiceAccounts

- UserAccounts are for humans while serviceAccounts are for application processes
- UserAccounts are intended to be global; names must be unique across all namespaces of a cluster
- ServiceAccounts are namespaced i.e. two different namespaces can contain ServiceAccounts that have identical names
- A cluster's UserAccounts typically might be synchronized from a corporate database and is tied to complex business processes
- Creation of ServiceAccounts is intended to be more lightweight, allowing cluster users to create ServiceAccounts for specific tasks on demand
