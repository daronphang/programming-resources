## Continuous Delivery

The first step in CD is **release automation**, which continuously assembles the latest code and configuration from head into **release candidates** (RC). RC is a cohesive, deployable unit created by an automated process, assembled of code, configuration, and other dependencies that have passed the continuous build.

CD is defined as a continuous assembling of RC, followed by the promotion and testing of those candidates throughout a series of environments.

For teams that want continuous feedback from new changes in production (Continuous Deployment), it is usually infeasible to continuously push entire binaries (which are quite large) on green. Instead, doing a selective Continuous Deployment, through **experiments or feature flags**, is a common strategy.

As an RC progresses through environments, its artifacts (binaries, containers) ideally should not be recompiled or rebuilt. Using containers such as Docker helps enforce consistency of an RC between environments, from local development onwards. Using orchestration tools like Kubernetes helps enforce consistency between deployments.

### Release Candidate (RC)

A cohesive, deployable unit created by an automated process,5 assembled of code, configuration, and other dependencies that have passed the continuous build.

## Key Aspects

### Agility

Release frequently and in small batches.

### Automation

Reduce or remove repetitive overhead of frequent releases.

### Isolation

Strive for modular architecture to isolate changes and make troubleshooting easier.

### Reliability

Measure key health indicators like crashes or latency and keep improving them.

### Data-driven decision making

Use A/B testing on health metrics to ensure quality.

### Phased rollout

Roll out changes to a few users before shipping to everyone.

## Evaluating Changes in Isolation

### Flag-Guarding

A key to reliable continuous releases is to make sure engineers 'flag guard' all changes. As a product grows, there will be multiple features under various stages of development coexisting in a binary. Flag guarding can be used to control the inclusion or expression of feature code in the product on a feature-by-feature basis and can be expressed differently for release and development builds.
