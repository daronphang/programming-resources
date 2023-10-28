## Authentication

All requests to the API server have to include credentials, and the authentication layer is responsible for verifying them.

Kubernetes does not have its built-in identity database and hence, it is impossible to create user accounts. Nonetheless, the authentication layer is pluggable, and popular modules include client certs, webhooks, and integration with external identity management system such as AD and IAM.

### kubeconfig

Cluster details and credentials are stored in a kubeconfig file. Many Kubernetes installations can automatically merge cluster endpoint details and credentials into your existing kubeconfig.

```
/home/<user>/.kube/config
```

```yaml
apiVersion: v1
kind: Config
clusters:
    # each cluster has a friendly name, an API server endpoint, and public key of its CA
    - cluster:
        name: prod-shield
        server: https://<url-or-ip-address-of-api-server>:443
        certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0...LS0tCg==
users:
# each user requires a name and token
# token is a X.509 certificate that is the user's ID, signed by CA trusted by the cluster
- name: njfury
    user:
        as-user-extra: {}
        token: eyJhbGciOiJSUzI1NiIsImtpZCI6IlZwMzl...SZY3uUQ
contexts:
# context combines both users and clusters
- context:
    name: shield-admin
    cluster: prod-shield
    namespace: default
    user: njfury
current-context: shield-admin
```
