## GitOps

GitOps is an operational framework based on DevOps practices, like continuous integration/continuous delivery (CI/CD) and version control, which automates infrastructure and manages software deployment. GitOps is a developer-centric approach, relying on tools developers are already familiar with.

GitOps uses **Git repositories as a single source of truth** to deliver infrastructure as code. It is an evolution of IaC and a DevOps best practice that leverages Git as the single source of truth, and control mechanism for creating, updating, and deleting system architecture.

GitOps ensures that a system’s cloud infrastructure is immediately reproducible based on the state of a Git repository. Pull requests modify the state of the Git repository. Once approved and merged, the pull requests will automatically reconfigure and sync the live infrastructure to the state of the repository. This live syncing pull request workflow is the core essence of GitOps.

Submitted code checks the CI process, while the CD process checks and applies requirements for things like security, infrastructure as code, or any other boundaries set for the application framework. All changes to code are tracked, making updates easy while also providing version control should a rollback be needed.

GitOps delivers:

- A standard workflow for application development
- Increased security for setting application requirements upfront
- Improved reliability with visibility and version control through Git
- Consistency across any cluster, any cloud, and any on-premise environment

### GitOps vs DevOps

GitOps and DevOps do share some of the same principles and goals. DevOps is about cultural change and providing a way for development teams and operations teams to work together collaboratively i.e. a paradigm shift or mindset. Their shared principles make it easier for teams to adopt the GitOps workflow for existing DevOps techniques.

GitOps gives you tools and a framework to take DevOps practices, like collaboration, CI/CD, and version control, and apply them to infrastructure automation and application deployment i.e. a set of deployment practices. Developers can work in the code repositories they already know, while operations can put the other necessary pieces into place.

### Use cases

- Streamline the workflow for developers with automatic deployment (CD)
- Enhance infrastructure management for platform engineers
- Manage deployments in Kubernetes

## Requirements

### Git for everything

GitOps extends the practice of using Git for the source code of an application to the application’s configuration, infrastructure, and operational procedures. It stores every aspect of a project’s infrastructure, including infrastructure as code files, configuration files, and application code files, in Git repositories, making it easy to manage software deployment and infrastructure provisioning.

### Versioning

Declarative descriptions stored within the repository supports immutability, versioning, and versioning history.

### Auto-pull

Using GitOps means that you employ software agents that are always running in the cluster, automatically pulling Git state at regular intervals and checking it against the live cluster state. This way you always know if the version in Git is the same as the live state or not.

### Closed loop

Operating in a close loop ensuring the desired state of a system matches the declared state. This is one of the most important features because it provides feedback allowing you and your team to better control your operations and workflow.

## Model

### Git workflows

GitOps uses Git repositories as the change mechanism for application and infrastructure updates. Any change to an application or environment is represented as a change in a Git repository – providing a full audit trail and the ability to roll back to a previous version at any time.

### CD pipelines

With GitOps you have a clear separation between CI and CD. Your CI pipelines stay as is and their end result is still an artifact and/or container that is stored in a binary repository. Once the artifact is created, GitOps takes over and applies it to the target cluster.

Instead of triggering the CI/CD with a commit in the source code, with GitOps **the trigger is a commit to the git/configuration repository**. The GitOps operator (e.g. Kubernetes operator), which sits between the GitOps pipeline and the orchestration system, picks up the commit and pulls in the new state declaration from Git.

### Infrastructure as Code (IaC)

GitOps uses a Git repository as the single source of truth for your environments. Infrastructure as code (IaC) means storing all infrastructure configuration as code in a version control system. IaC systems use declarative configuration, meaning you only state what you need deployed, not how.

### Tracking and observability

Observability, a property of a system which allows it to be easily observed, is an important GitOps concept. It lets you ensure that the desired state described in declarative configuration, and actual current state, are the same.

### Immutable servers (containerized infrastructure)

GitOps is often used to operate Kubernetes application development. It lets you build development pipelines, continuously deploy applications, provision clusters, and deploy on Kubernetes or container registries. However, GitOps can also be used in other infrastructure environments.
