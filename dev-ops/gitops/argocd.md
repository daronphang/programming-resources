## Argo CD

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. It can be used as a standalone tool or as a part of your CI/CD workflow to deliver needed resources to your clusters.

### Features

- Automated deployment of application to specified target environments e.g. staging, prod
- Support for multiple config management/templating tools e.g. Kustomize, Helm, YAML
- Ability to manage and deploy to multiple clusters
- SSO integration e.g. OIDC, LDAP, OAuth2
- Multi-tenancy and RBAC policies for authorization
- Automated configuration drift detection and visualization
- Automated or manual syncing of applications to its desired state
- Webhook integration with GitHub, BitBucket, GitLab
- RBAC enabling multi-cluster management

### Why Argo CD?

Application definitions, configurations, and environments should be declarative and version controlled. Application deployment and lifecycle management should be automated, auditable, and easy to understand.

### How it works

1. A developer pushes resource changes to a single Git repository
2. The continuous integration tool is triggered and saves new container image to the registry
3. The pull request (PR) changes the Kubernetes manifest, which is merged and triggers Argo CD
4. Argo CD clones the repository
5. Argo CD compares desired configuration, or desired state, with current state on the cluster
6. Argo CD reconciles those differences automatically
7. Argo CD reports when sync is complete

## Architecture components

### API server

Argo CD API server runs both a gRPC server (used by the CLI), as well as a HTTP/HTTPS server (used by the UI).

### Repository server

The repository server is an internal service which maintains a local cache of the Git repository holding the application manifests.

The repository server generates Kubernetes manifests and returns them based on inputs such as the repository URL, application path, revisions (i.e., commits, tags, branches), and any template-specific settings (i.e., Helm values, Ksonnet environments, parameters).

### Application controller

Argo CD is implemented as a Kubernetes controller which continuously monitors running applications and compares the current, live state against the desired target state (as specified in the Git repo). A deployed application whose live state deviates from the target state is considered OutOfSync. Argo CD reports & visualizes the differences, while providing facilities to automatically or manually sync the live state back to the desired target state. Any modifications made to the desired target state in the Git repo can be automatically applied and reflected in the specified target environments.

## Core concepts

### Application

A group of Kubernetes resources as defined by a manifest (CRD). The Application object is deployed in the argocd namespace, but the code will be deployed into the namespace listed under the destination.
