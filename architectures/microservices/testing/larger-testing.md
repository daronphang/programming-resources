## Larger tests

Larger tests do not have the same restrictions as smaller tests i.e. can be multithreaded or multiprocess, across multiple machines, etc. They also typically involve several real dependencies and fewer test doubles.

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

## Gaps in unit tests

Larger tests might be necessary where smaller tests fail.

### Unfaithful doubles

Test doubles are frequently used to eliminate heavyweight or hard-to-test dependencies. However, when those dependencies are replaced, it becomes possible that the replacement do not agree.

### Configuration issues

Unit tests cover code within a given binary, but it may not be completely self-sufficient in terms of how it is executed. Also, real end-user-serving production instances have their own configuration files or configuration databases.

### Unanticipated behaviors, inputs and side effects

Unit tests are limited by the imagination of the engineer writing them i.e. they can only test for anticipated behaviors and inputs.

### Emergent behaviors

Unit tests are limited to the scope that they cover, and if behavior changes in areas outside of the scope, it cannot be detected. Also, as unit tests are designed to be fast and reliable, they deliberately eliminate the chaos of real dependencies, network and data.

## Downsides to E2E testing

### Flaky and brittle tests

As test scope increases, so do the number of moving parts. These moving parts can introduce test failures that do not show that the functionality under test is broken, but that some other problem has occurred.

More moving parts means more brittle tests, and if you simply re-run them as they might pass again later, then you have flaky tests. When flaky tests are detected, it is essential that we do our best to remove them.

### Writing tests

If multiple teams are involved and E2E is shared between them, it is difficult to assign the person who writes and looks after these tests. If tests become free-for-all, it is likely that teams will add tests without any understanding of the health of the whole suite.

### Great pile-up

With a long test suite and feedback cycles, any breaks take a while to fix which can eventually lead to a pile up. The larger the scope of deployment, the higher the risk of a release, and the more likely we are to break something. A key driver to ensuring we can release our software frequently is based on the idea that we release small changes as soon as they are ready.

### The meta-version

The approach of accepting multiple services being deployed together drifts into a situation where services become coupled and increasingly tangled with others. This would cede one of the main advantages of microservices: the ability to deploy a service independently.

## SUT Factors (System Under Test)

### Hermeticity

This is the SUT's isolation from usages and interactions from other components than the test in question. An SUT with high hermeticity will have the least exposure to sources of concurrency and infrastructure flakiness.

### Fidelity

SUT's accuracy in reflecting the production system being tested. An SUT with high fidelity will consist of binaries that resemble the production versions.

## Best practices

### Record/replay proxies

When dealing with tests using public APIs, an approach would be to use a larger test to generate a smaller one by recording the traffic to those external services when running the larger test, and replaying it when running the smaller tests.

One of the interesting aspects of how record/replay works is that, because of nondeterminism, requests must be matched via a matcher to determine which response to replay. This makes them very similar to stubs and mocks in that argument matching is used to determine the resulting behavior.
