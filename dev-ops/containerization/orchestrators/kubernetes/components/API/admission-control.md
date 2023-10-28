## Admission Control

Admission control is about policies and runs immediately after successful authentication and authorization. There are two types of admission controllers:

- Mutating: Check for policy compliance and can modify requests to enforce policies
- Validating: Check for policy compliance but cannot modify requests

Mutating controllers always run first, and both types only apply to requests that will **modify state**. Requests to read state are not subjected to admission control.

For instance, if all new and updated objects to your cluster require env=prod label, a mutating controller can check for its presence and add if it doesn't exist. However, a validating controller can only reject the request if it doesn't exist.

If any admission controller rejects a request, the request will not check the remaining admission controllers. If all controllers approve the request, it gets persisted to the cluster store and instantiated on the cluster.

### Example

An example is the AlwaysPullImages controller. It is a mutating controller that sets the spec.containers.imagePullPolicy of all new Pods to 'Always' i.e. images will always be pulled from the registry. This ensures the following:

- Prevents the use of locally cached images that could be malicious
- Forcing the container runtime to present valid credentials to the registry to get the image
