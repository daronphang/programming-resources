## Open Container Initiative (OCI)

OCI is a set of standards for containers that describes and maintains a specification for image format, runtime, and distribution. It was established in 2015 by Docker and others.

Currently, it has two specifications:

- image-spec: outlines how to create an OCI-compliant image
- runtime-spec: for unpacking the filesystem bundle

## Container Runtime Interface (CRI)

CRI is an API that allows you to use different container runtimes in Kubernetes (container-agnostic platform). Hence, instead of the Kubernetes project needing to add support for each runtime individually, the CRI API describes how Kubernetes will interact with any runtime. As long as a given container runtime implements the CRI API, the runtime can create and start containers however it likes.

### crictl

crictl provides a CLI for CRI compatible container runtimes. Used to inspect and debug container runtimes.
