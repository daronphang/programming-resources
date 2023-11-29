## Admission Controllers

Admission control is about policies and runs immediately after successful authentication and authorization. There are two types of admission controllers:

- Mutating: Check for policy compliance and can modify requests to enforce policies
- Validating: Check for policy compliance but cannot modify requests

Mutating controllers always run first, and both types only apply to requests that will **modify state**. Requests to read state are not subjected to admission control.

For instance, if all new and updated objects to your cluster require env=prod label, a mutating controller can check for its presence and add if it doesn't exist. However, a validating controller can only reject the request if it doesn't exist.

If any admission controller rejects a request, the request will not check the remaining admission controllers. If all controllers approve the request, it gets persisted to the cluster store and instantiated on the cluster.

Examples of admission controllers are AlwaysPullImages, DefaultStorageClass, EventRateLimit, NamespaceExists, etc. Updating of admission controllers can be performed in:

1. kube-apiserver.service
2. `/etc/kubernetes/manifests/kube-apiserver.yaml` with fields --enable-admission-plugins and --disable-admission-plugins

```bash
# need to execute command in apiserver container
# check for enabled plugins
$ ps -ef | grep kube-apiserver | grep admission-plugins

$ kubectl exec -it kube-apiserver-controlplane -n kube-system -- kube-apiserver -h | grep enable-admission-plugins
```

### Example

An example is the AlwaysPullImages controller. It is a mutating controller that sets the spec.containers.imagePullPolicy of all new Pods to 'Always' i.e. images will always be pulled from the registry. This ensures the following:

- Prevents the use of locally cached images that could be malicious
- Forcing the container runtime to present valid credentials to the registry to get the image

## Custom controllers

To use a custom controller, you need to deploy a webhook server with custom logic that returns either an allow or reject JSON response.

Each webhook must specify a list of rules used to determine if a request to the API server should be sent to the webhook. Each rule specifies one or more operations, apiGroups, apiVersions, and resources, and a resource scope

```yaml
# when creating pods, this custom validating controller will run
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration # or MutatingWebhookConfiguration
metadata:
  name: "pod-policy.example.com"
webhooks:
  - name: "pod-policy.example.com"
    rules:
      - apiGroups: [""]
        apiVersions: ["v1"]
        operations: ["CREATE"]
        resources: ["pods"]
        scope: "Namespaced"
    clientConfig:
      service:
        namespace: "example-namespace"
        name: "example-service"
      caBundle: <CA_BUNDLE> # PEM-encoded i.e. base64 encoded
    admissionReviewVersions: ["v1"]
    sideEffects: None
    timeoutSeconds: 5
```

### Response

```json
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "response": {
    "uid": "<value from request.uid>",
    "allowed": true,
    "patchType": "JSONPatch",
    // base64 encoded
    // [{"op": "add", "path": "/spec/replicas", "value": 3}]
    "patch": "W3sib3AiOiAiYWRkIiwgInBhdGgiOiAiL3NwZWMvcmVwbGljYXMiLCAidmFsdWUiOiAzfV0="
  }
}
```
