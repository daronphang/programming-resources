## Designing a Test Suite

There are two distinct dimensions for every test case: size and scope. Both are interrelated but distinct concepts.

## Properties

### Hermetic

All tests should strive to be hermetic; a test should contain all of the information necessary to set up, execute and tear down its environment. Tests should assume as little as possible about the outside environment, such as the order in which the tests are run. Tests also should not rely on a shared database.

### Deterministic

Tests should be deterministic i.e. running the test always results in the same outcome. Nondeterminism in tests can lead to flakiness, which can harm the health of a test suite if developers start to distrust the results of the test and ignore failures.

A common cause of nondeterminism is code that is not hermetic i.e. it has dependencies on external services that are outside the control of a test.

### Discourage Control Flows

**The use of control flow statements like conditionals and loops, and operations are strongly discouraged** in a test. More complex test flows risk containing bugs themselves and make it more difficult to determine the cause of a test failure.

## Test Sizes

Size refers to the resources that are required to run a test case i.e. memory, process, and time.

### Small Tests

Small tests are the most constrained of the three test sizes but are **encouraged to write whenever possible**. The primary constraint is that small tests must run in a single process, and recommended on a single thread. This means that the code performing the test must run in the same process as the code being tested i.e. you can't run a third party program such as a database as part of your test.

The other important constraints on small tests are that they aren't allowed to sleep, perform I/O operations, or make any other blocking calls. Testing code that relies on these sort of operations requires the use of **test doubles**.

The purpose of these restrictions is to ensure that small tests don't have access to the main sources of test slowness or **nondeterminism which can introduce flakiness**.

### Medium Tests

Medium tests can span multiple processes, use threads, and can make blocking calls, including network calls, to localhost. The only remaining restriction is that medium tests aren't allowed to make network calls to any system other than localhost.

The ability to run multiple processes opens up a lot of possibilities. For example, you could run a database instance to validate the code you are testing integrates correctly in a more realistic setting. You could also test a combination of web UI and server code.

Unfortunately, with increased flexibility comes increased potential for tests to become slow and nondeterministic. Medium tests still provide a bit of protection by **preventing access to remote machines via the network, which is the biggest source of slowness and nondeterminism in most systems**.

### Large Tests

Large tests remove the localhost restriction imposed on medium tests, allowing the test and the system being tested to span across multiple machines.

Large tests are mostly reserved for full-system and e2e tests that are more about validating configuration than pieces of code, and for tests of legacy components for which it is impossible to use test doubles.

## Test Scope

Test scope refers to how much code is being validated by a given test. **Narrow-scoped** tests (unittests) are designed to validate the logic in a small, focused part of the codebase, like an individual class or method. **Medium-scoped** tests (integration tests) are design to verify interactions between a small number of components i.e. between a server and database. **Large-scoped** tests (functional tests, e2e tests, system tests) are designed to validate the interaction of several distinct parts of the system.

It is important to note that the scope refers to the code that is being validated, not the code that is being executed. It is quite common for a class to have many dependencies or other classes it refers to, and these dependencies will naturally be invoked while testing the target class. Though some testing strategies make heavy use of test doubles, it is **preferred to keep the real dependencies in place when it is feasible to do so**.

### Code Coverage

Code coverage is a measure of the which lines of feature code are exercised by which tests. If you have 100 lines of code and your tests execute 90 of them, you have 90% coverage. **Code coverage is often held up as the gold standard metric for understanding test quality, and that is somewhat unfortunate**. It is possible to exercise high code coverage but never checking that each line is doing anything useful.

A better way to approach the quality of your test suite is to think about the behaviors that are tested:

- Do you have confidence that everything your customers expect to work will work?
- Do you feel confident you can catch breaking changes in your dependencies?
- Are your tests stable and reliable?

## Pitfalls of Large Test Suite

As a codebase grows, you will inevitably need to make changes to existing code. Brittle tests that rely on extensive and complicated boilerplate, can actually resist change.

Some of the worst offenders of brittle tests come from the **misuse of mock objects**.
