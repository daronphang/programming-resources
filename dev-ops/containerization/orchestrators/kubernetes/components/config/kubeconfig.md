## kubeconfig

You can use kubeconfig files to organize information about clusters, users, namespaces, credentials, and authentication mechanisms. The kubectl CLI uses kubeconfig files to find the information it needs to choose a cluster and communicate with the API server of a cluster.

Many Kubernetes installations can automatically merge cluster endpoint details and credentials into your existing kubeconfig.

### Location

The loading order follows these rules:

1. If the --kubeconfig flag is set, then only that file is loaded
2. If $KUBECONFIG environment variable is set, then it is used as a list of paths and these paths are **merged**
3. Otherwise, `${HOME}/.kube/config` is used and no merging takes place

```bash
$ kubectl config view # uses default kubeconfig file
$ kubectl config view --kubeconfig=my-custom-config

$ k config use-context research --kubeconfig my-kube-config
```

```yaml
apiVersion: v1
kind: Config
clusters:
    # each cluster has a friendly name, an API server endpoint, and public key of its CA
    - cluster:
        name: prod-shield
        server: https://<url-or-ip-address-of-api-server>:443
        certificate-authority: /etc/kubernetes/pki/ca.crt
        # better to convert the contents to base64 and pass directly
        # cat ca.crt | base64
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

```yaml
apiVersion: v1
kind: Config

clusters:
- name: production
  cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt
    server: https://controlplane:6443

- name: development
  cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt
    server: https://controlplane:6443

- name: kubernetes-on-aws
  cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt
    server: https://controlplane:6443

- name: test-cluster-1
  cluster:
    certificate-authority: /etc/kubernetes/pki/ca.crt
    server: https://controlplane:6443

contexts:
- name: test-user@development
  context:
    cluster: development
    user: test-user

- name: aws-user@kubernetes-on-aws
  context:
    cluster: kubernetes-on-aws
    user: aws-user

- name: test-user@production
  context:
      cluster: production
    user: test-user

- name: research
  context:
    cluster: test-cluster-1
    user: dev-user

users:
- name: test-user
  user:
    client-certificate: /etc/kubernetes/pki/users/test-user/test-user.crt
    client-key: /etc/kubernetes/pki/users/test-user/test-user.key
- name: dev-user
  user:
    client-certificate: /etc/kubernetes/pki/users/dev-user/developer-user.crt
    client-key: /etc/kubernetes/pki/users/dev-user/dev-user.key
- name: aws-user
  user:
    client-certificate: /etc/kubernetes/pki/users/aws-user/aws-user.crt
    client-key: /etc/kubernetes/pki/users/aws-user/aws-user.key

current-context: test-user@development
preferences: {}
```
