## Designing a Test suite

There are two distinct dimensions for every test case: size and scope. Both are interrelated but distinct concepts.

## Properties

### Hermetic

All tests should strive to be hermetic; a test should contain all of the information necessary to set up, execute and tear down its environment. In other words, tests run against a test environment (i.e. application servers, resources) that is entirely self-contained (i.e. no external dependencies like production backends).

Tests should assume as little as possible about the outside environment, such as the order in which the tests are run. Tests also should not rely on a shared database.

### Deterministic

Tests should be deterministic i.e. running the test always results in the same outcome. Nondeterminism in tests can lead to flakiness, which can harm the health of a test suite if developers start to distrust the results of the test and ignore failures.

A common cause of nondeterminism is code that is not hermetic i.e. it has dependencies on external services that are outside the control of a test.

#### Flaky (non-deterministic) and brittle tests

A flaky test is one that yields both passing and failing results despite zero changes to the code or test i.e. they are non-deterministic that fail to produce the same outcome with each individual test run.

On the other hand, brittle tests may consistently pass, but is balanced on a knife edge that a small change in conditions results in failure.

### Discourage control flows

**The use of control flow statements like conditionals and loops, and operations are strongly discouraged** in a test. More complex test flows risk containing bugs themselves and make it more difficult to determine the cause of a test failure.

## Code coverage

Code coverage is a measure of the which lines of feature code are exercised by which tests. If you have 100 lines of code and your tests execute 90 of them, you have 90% coverage. **Code coverage is often held up as the gold standard metric for understanding test quality, and that is somewhat unfortunate**. It is possible to exercise high code coverage but never checking that each line is doing anything useful.

A better way to approach the quality of your test suite is to think about the behaviors that are tested:

- Do you have confidence that everything your customers expect to work will work?
- Do you feel confident you can catch breaking changes in your dependencies?
- Are your tests stable and reliable?

## Pitfalls of Large test suite

As a codebase grows, you will inevitably need to make changes to existing code. Brittle tests that rely on extensive and complicated boilerplate, can actually resist change.

Some of the worst offenders of brittle tests come from the **misuse of mock objects**.
