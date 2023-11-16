## Authorization

Kubernetes authorization is pluggable and you can run multiple authorization (authZ) modules on a single cluster. Authorization mechanisms supported by Kubernetes include node authorizaiton, attribute-based authorication (ABAC), role-based authorization (RBAC), and webhook.

You must include a flag in your policy to indicate which authorization module your policies include. When you have multiple modes configured, the request is authorized using each one in the order it is specified. If denied, the request is passed on to the next chain.

```
--authorization-mode=ABAC
--authorization-mode=RBAC
--authorization-mode=Webhook
--authorization-mode=Node
--authorization-mode=AlwaysDeny
--authorization-mode=AlwaysAllow (default)

# for multiple authorization modules
--authorization-mode=ABAC,RBAC,Webhook
```

## Node

A special-purpose authorization mode that grants permissions to kubelets based on the pods they are scheduled to run.

## ABAC

Attribute-based access control (ABAC) defines an access control paradigm whereby access rights are granted to users through the use of policies which combine attributes together. The policies can use any type of attributes (user attributes, resource attributes, object, environment attributes, etc).

However, when making changes, the policy file must be edited manually, and the API-server needs to be restarted which makes it difficult to manage.

## Webhook

A WebHook is an HTTP callback: an HTTP POST that occurs when something happens; a simple event-notification via HTTP POST. A web application implementing WebHooks will POST a message to a URL when certain things happen.

You can make Kubernetes make an API call to the open policy agent with the information about the user and his access requirements, and have the open policy agent decide if the user should be permitted or not.

## RBAC

The most common authorization module is RBAC (role-based access control). It identifies which user can perform which actions against which resources. It is a least-privilege deny-by-default system i.e. all actions are denied by default, and Kubernetes only supports 'allow' rules.

Kubernetes has four RBAC objects:

- Roles
- RoleBindings
- ClusterRoles
- ClusterRolebindings

### Users and Permissions

Roles define a set of permissions, and RoleBindings grant those permissions to users. Both are namespaced objects and can only be **applied to a single Namespace**.

```bash
$ kubectl get roles
$ kubectl get rolebindings
$ kubectl describe role <name>
$ kubectl describe rolebinding <name>
```

```bash
$ kubectl auth can-i create deployments # yes or no
$ kubectl auth can-i delete nodes
$ kubectl auth can-i create pods --as <username> --namespace <namespace>
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: shield
  name: read-deployments
rules:
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "watch", "list"]

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
  apiGroup: authorization.k8s.io
```

### Role

The Role object has three properties:

- apiGroups (empty string denotes core group)
- resources
- verbs

you can use asterisk to refer to all API groups, resources and verbs i.e. cluster admin.

```bash
$ kubectl api-resources --sort-by name -o wide # shows all API resources
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
```

```bash
$ kubectl get clusterrolebindings
$ kubectl describe clusterrolebindings <name>   # i.e. cluster-admin
```
