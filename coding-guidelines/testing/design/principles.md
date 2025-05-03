## Unit testing

### Strive for unchanging tests

The ideal test is unchanging: after it is written, it never needs to change unless the requirements of the system under test change.

### Be deterministic

Tests should be deterministic, i.e. running the test with the same inputs always yields the same outcome. Nondeterminism (remote services, time, async behavior) in tests can lead to flakiness (brittle tests), which can harm the health of a test suite if developers start to distrust the results of the test and ignore failures.

A common cause of nondeterminism is code that is not hermetic, i.e. it has dependencies on external services that are outside the control of a test.

https://martinfowler.com/articles/nonDeterminism.html

### Test via Public APIs

The most important way to ensure this is to write tests that invoke the system being tested in the same way its users would, by **making calls against its public API rather than its implementation details**. Also, such tests can serve as useful examples and documentation for users.

### Test state, not interactions

Another way that tests commonly depend on implementation details involves not which methods of the system that test calls, but how the results of those calls are verified.

Interaction testing is a way to validate how a function is called without actually calling the implementation of the function. A test should fail if a function isn't called the correct way, i.e. assert_called_once, assert_call_count, checking call arguments, etc. With state testing, you observe the system itself to see what it looks like after invoking it.

Interaction tests tend to be more brittle as they check how a system arrived at its result, whereas usually **you should care only what the result is**. Also, they are less scalable, don't tell you that the system under test is working properly, and utilizes implementation details.

### Test behaviors, not methods

The first instinct of many engineers is to try to match the structure of their tests to the structure of their code such that every production method has a corresponding test method. This will cause the test to become increasingly convulted and grow more difficult to work with.

The problem is that framing tests around methods can naturally encourage unclear tests because a single method often does a few different things under the hood, and might have several tricky edge cases. **Instead of writing a test for each method, write a test for each behavior**.

A behavior is any guarantee that a system makes about how it will respond to a series of inputs while in a particular state i.e. **cause and effect**. Behaviors can often be expressed using words "given", "when", "then" i.e. given a bank account is empty, when attempting to withdraw money from it, then the transaction is rejected.

### Avoid putting logic in tests

Complexity is most often introduced in the form of logic. Logic is defined via imperative parts of programming languages including operators, loops, and conditionals. Simplicity is more important than flexibility in tests.

### Code sharing with DAMP, not DRY

Most software attempts to achieve a principle called DRY (Don't Repeat Yourself). However, the downside to such consolidation is that it can make code unclear. Instead of completely DRY, test code should often strive to be DAMP (promote Descriptive And Meaningful Phrases). A little bit of duplication is OK in tests so long as that duplication makes the test simpler and clearer.

### Shared values

Engineers are usually drawn to using shared constants because constructing the individual values in each test can be verbose. A better way to accomplish this goal is to construct data **using helper methods** that require the test author to specify only values they care about, and setting reasonable defaults for all other values.

```py
def constructUser(name, age):
    return User(
        name=name,
        age=age,
        address='15 Orchard Road',
        color='blue',
        job='engineer',
    )
```

## Integration testing

### Test journeys, not stories

Despite the disadvantages outlined, instead of covering every test case (lead to brittle tests, and would never be 100% foolproof), we should focus on a small number of core journeys (high value interactions) to test for the whole system. A user journey test simulates a multi-step interaction of a user with the system e.g. for e-commerce, create an order, modify it, and finally cancel it.

Any functionality not covered in these core journeys needs to be covered in tests that analyze services in isolation from each other (unit tests). Ultimately, the cost and benefit of end-to-end testing needs to make sense.

For testing events, the publisher of the event should stop the test once they successfully create an event. They can include cleanup steps to allow multiple tests without downstream impact. Ensure topics are flexible (use headers to distinguish) and that the test events are ignored by everyone else except your test.

### Consumer-driven tests

When using integration tests, we want to ensure that deploying a new service doesn't break consumers. One way to do this without requiring test against the real consumer is by using consumer-driven contract (CDC).

With CDCs, we are defining the expectations of a consumer on a service/producer. They should be run as part of CI build of the producer, ensuring that it never gets deployed if it breaks one of these contracts. Should only be run against a single producer in isolation so that it can be more reliable than E2E tests.

### Avoid test doubles with remote services

When using test doubles, it is to ensure that the call was made. If the expected call is not made, the test fails. Can be classified as behavioral testing. Implementing this approach requires more intelligence in the fake collaborators that we create, and if overused, it can cause tests to become brittle. Instead, we should use actual third-party dependencies when performing integration testing, i.e. database, MQ, etc.
