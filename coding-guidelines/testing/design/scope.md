## Test scope

Test scope refers to how much code is being validated by a given test. **Narrow-scoped** tests (unit-tests) are designed to validate the logic in a small, focused part of the codebase, like an individual class or method. **Medium-scoped** tests (integration tests) are design to verify interactions between a small number of components i.e. between a server and database. **Large-scoped** tests (functional tests, e2e tests, system tests) are designed to validate the interaction of several distinct parts of the system.

It is important to note that the scope refers to the code that is being validated, not the code that is being executed. It is quite common for a class to have many dependencies or other classes it refers to, and these dependencies will naturally be invoked while testing the target class. Though some testing strategies make heavy use of test doubles, it is **preferred to keep the real dependencies in place when it is feasible to do so**.

### Unit tests

A unit test validates the behavior of a small part of the codebase e.g. individual class. A good unit test should be relatively static in time and change only when the behavior of the system under test (SUT) changes; **refactoring, fixing a bug, or adding a new feature shouldn’t require a unit test to change**. To achieve that, a unit test should:

- Use only the public interfaces of the SUT
- Test for state changes in the SUT
- Test for behaviors

The prime goal of these tests is to give us very fast feedback about whether our functionality is good.

### Integration tests

An integration test has a larger scope than a unit test, since it verifies that a service can interact with its external dependencies as expected.

Designed to bypass the user interface and test services directly. This tests the individual service's capabilities. This is to improve the isolation of the test to make finding and fixing problems faster. Need to stub all external collaborators so only the service itself is in scope.

If you decide to test against a real database, or go over networks to stubbed downstream collaborators, test times can increase. Though they cover more scope than a unit test and failing can be harder to detect what is broken, they have much fewer moving parts and are therefore less brittle than larger-scoped tests.

### End-to-end tests

E2E tests run against your entire system. Often they will be driving a GUI through a browser, but could easily be mimicking other sorts of user interaction, such as uploading a file. Can be tricky to do well in a microservices context.

End-to-end tests can be painful and expensive to maintain. For example, when an end-to-end test fails, it’s not always obvious which service is responsible and deeper investigation is required. But they are a necessary evil to ensure that user-facing scenarios work as expected across the entire application. They can uncover issues that tests with smaller scope can’t, like unanticipated side effects and emergent behaviors.
