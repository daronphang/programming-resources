## RBAC

RBAC is a method of regulating access to computer or network resources based on the roles of individual users within your organization.

To enable RBAC, start the API server with the --authorization-mode flag that includes RBAC.

```
kube-apiserver --authorization-mode=Example,RBAC --other-options --more-options
```

## API objects

Kubernetes has four RBAC objects:

- Roles
- RoleBindings
- ClusterRoles
- ClusterRoleBindings

### Users and Permissions

Roles define a set of permissions, and RoleBindings grant those permissions to users. Both are namespaced objects and can only be **applied to a single Namespace**.

A RoleBinding or ClusterRoleBinding binds a role to subjects. Subjects can be groups, users or ServiceAccounts.

```sh
kubectl get roles
kubectl get rolebindings
kubectl describe role <name>
kubectl describe rolebinding <name>
```

```sh
kubectl auth can-i create deployments # yes or no
kubectl auth can-i delete nodes
kubectl auth can-i create pods --as <username> --namespace <namespace>
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: shield
  name: read-deployments
rules:
  - apiGroups: ["apps", ""]
    resources: ["deployments", "persistentvolumes", "nodes"]
    verbs: ["get", "watch", "list"]
    resourceNames: ["my-deployment"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-deployments
  namespace: shield
subjects:
  - kind: User
    name: sky # authenticated user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: read-deployments # Role to bind to the user
  apiGroup: rbac.authorization.k8s.io
```

### Role

The Role object has three properties:

- apiGroups (empty string denotes core group)
- resources
- verbs

you can use asterisk to refer to all API groups, resources and verbs i.e. cluster admin.

```sh
kubectl api-resources --sort-by name -o wide # shows all API resources
```

| apiGroup         | resource     | Kubernetes API path                              |
| ---------------- | ------------ | ------------------------------------------------ |
| ""               | pods         | /api/v1/namespaces/<namespace>/pods              |
| ""               | secrets      | /api/v1/namespaces/<namespace>/secrets           |
| "storage.k8s.io" | storageclass | /apis/storage.k8s.io/v1/storageclasses           |
| "apps"           | deployments  | /apis/apps/v1/namespaces/<namespace>/deployments |

| HTTP Method | Kubernetes Verbs | Common Responses               |
| ----------- | ---------------- | ------------------------------ |
| POST        | create           | 201 Created, 403 Access Denied |
| GET         | get,list,watch   | 200 OK, 403 Acccess Deneid     |
| PUT         | update           | 200 OK, 403 Access Denied      |
| PATCH       | patch            | 200 OK, 403 Access Denied      |
| DELETE      | delete           | 200 OK, 403 Access Denied      |

### Cluster-level users and permissions

ClusterRoles and ClusterRoleBindings are cluster-wide objects that apply to all Namespaces. Their YAML structures are almost identical.

As ClusterRoles are cluster-scoped, you can also use them to grant access to:

- Cluster-scoped resources i.e. nodes
- Namespaced resources across all namespaces i.e. Pods
- Non-resource endpoints i.e. /healthz

**A powerful pattern is to define Roles at the cluster level (ClusterRoles) and bind them to specific Namespaces via RoleBindings**. This lets you define common roles once, and re-use them across multiple Namespaces.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: read-deployments
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "watch", "list"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
subjects:
  - kind: Group
    name: manager # Name is case sensitive
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

```yaml
# non-resource endpoints
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: read-deployments
rules:
  - nonResourceURLs:
    - /healthz
    - /healthz/*
  verbs:
    - get
    - post
```

```sh
kubectl get clusterrolebindings
kubectl describe clusterrolebindings <name>   # i.e. cluster-admin
```
