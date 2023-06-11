## Continuous Delivery

The first step in CD is release automation, which continuously assembles the latest code and configuration from head into **release candidates** (RC). RC is a cohesive, deployable unit created by an automated process, assembled of code, configuration, and other dependencies that have passed the continuous build.

CD is defined as a continuous assembling of RC, followed by the promotion and testing of those candidates throughout a series of environments.

For teams that want continuous feedback from new changes in production (Continuous Deployment), it is usually infeasible to continuously push entire binaries (which are quite large) on green. Instead, doing a selective Continuous Deployment, through **experiments or feature flags**, is a common strategy.

As an RC progresses through environments, its artifacts (binaries, containers) ideally should not be recompiled or rebuilt. Using containers such as Docker helps enforce consistency of an RC between environments, from local development onwards. Using orchestration tools like Kubernetes helps enforce consistency between deployments.
