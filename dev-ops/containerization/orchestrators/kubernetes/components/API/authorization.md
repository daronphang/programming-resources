## Authorization

Kubernetes authorization is pluggable and you can run multiple authorization (authZ) modules on a single cluster. Authorization mechanisms supported by Kubernetes include node authorization, attribute-based authorization (ABAC), role-based authorization (RBAC), and webhook.

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

```
/etc/kubernetes/manifests/kube-apiserver.yaml
```

### Node

A special-purpose authorization mode that grants permissions to kubelets based on the pods they are scheduled to run.

### ABAC

Attribute-based access control (ABAC) defines an access control paradigm whereby access rights are granted to users through the use of policies which combine attributes together. The policies can use any type of attributes (user attributes, resource attributes, object, environment attributes, etc).

However, when making changes, the policy file must be edited manually, and the API-server needs to be restarted which makes it difficult to manage.

### Webhook

A WebHook is an HTTP callback: an HTTP POST that occurs when something happens; a simple event-notification via HTTP POST. A web application implementing WebHooks will POST a message to a URL when certain things happen.

You can make Kubernetes make an API call to the open policy agent with the information about the user and his access requirements, and have the open policy agent decide if the user should be permitted or not.

### RBAC

The most common authorization module is RBAC (role-based access control). It identifies which user can perform which actions against which resources. It is a least-privilege deny-by-default system i.e. all actions are denied by default, and Kubernetes only supports 'allow' rules.
