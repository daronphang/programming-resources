## Larger Tests

Larger tests do not have the same restrictions as smaller tests i.e. can be multithreaded or multiprocess, across multiple machines, etc. They also typicall involve several real dependencies and fewer test doubles.

Larger tests can exhibit the following characteristics:

- They may be slow i.e. hours or days
- May be nonhermetic as they may share resources with other tests or traffic
- May be nondeterministic

Unit tests can give you confidence about individual functions, objects, and modules, but large tests can provide more confidence that the overall system works as intended.

### Types

- Functional testing of one or more binaries
- Browser and device testing
- Performance, load and stress testing
- Deployment configuration testing
- Exploratory testing
- A/B diff (regression) testing
- User acceptance testing
- Probers and canary analysis
- Disaster recovery and chaos engineering
- User evaluation

## Gaps in Unit Tests

Larger tests might be necessary where smaller tests fail.

### Unfaithful doubles

Test doubles are frequently used to eliminate heavyweight or hard-to-test dependencies. However, when those dependencies are replaced, it becomes possible that the replacement do not agree.

### Configuration issues

Unit tests cover code within a given binary, but it may not be completely self-sufficient in terms of how it is executed. Also, real end-user-serving production instances have their own configuration files or configuration databases.

### Unanticipated behaviors, inputs and side effects

Unit tests are limited by the imagination of the engineer writing them i.e. they can only test for anticpiated behaviors and inputs.

### Emergent behaviors

Unit tests are limited to the scope that they cover, and if behavior changes in areas outside of the scope, it cannot be detected. Also, as unit tests are designed to be fast and reliable, they deliberately eliminate the chaos of real dependencies, network and data.

## SUT Factors (System Under Test)

### Hermeticity

This is the SUT's isolation from usages and interactions from other components than the test in question. An SUT with high hermeticity will have the least exposure to sources of concurrency and infrastructure flakiness.

### Fidelity

SUT's accuracy in reflecting the production system being tested. An SUT with high fidelity will consist of binaries that resemble the production versions.

## Best Practices

### Record/replay proxies

When dealing with tests using public APIs, an approach would be to use a larger test to generate a smaller one by recording the traffic to those external services when running the larger test, and replaying it when running the smaller tests.

One of the interesting aspects of how record/replay works is that, because of nondeterminism, requests must be matched via a matcher to determine which response to replay. This makes them very similar to stubs and mocks in that argument matching is used to determine the resulting behavior.
