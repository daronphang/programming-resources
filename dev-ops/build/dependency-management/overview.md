## Dependency Management

Dependency management refers to the management of networks of libraries, packages, and dependencies that we don't control. It is one of the least understood and most challenging problems in software engineering. Focuses on questions including:

- How do we update between versions of external dependencies?
- How do we describe versions?
- What types of changes are allowed or expected in our dependencies?
- How do we decide when it is wise to depend on code produced by other organizations?

Dependency management adds complexity in both time and scale. For changes made internally, you need to run tests and not break existing code, predicated on the idea that you have visibility into how things are being used and changed. Dependency management focuses on the problems that arise when **changes are being made outside of your organization, without full access or visibility**.

When it comes to scaling, we are depending on an entire network of external dependencies. It is easy to construct scenarios in which your organization's use of two dependencies become unsatisfiable at some point in time. This happens because one dependency stops working without some requirement, whereas another is incompatible with the same requirement.

### SCM vs Dependency Management

SCM and dependency management are related issues separated by how your organization controls the development/update/management of subprojects. If **every team has separate repositories, goals, and development practices**, the interaction and management of code produced are **more related to dependency management**. On the other hand, using a monorepo can scale up significantly further with source control policies. Prefer **source control problems over dependency-management problems**.
