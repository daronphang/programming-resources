## Test Double

A test double is an object or function that cna stand in for a real implementation in a test.

https://martinfowler.com/articles/mocksArentStubs.html

### Dummy

Objects that are passed around but never actually used. Usually they are just used to fill parameter lists or constructors in classes.

### Fake

A fake is a lightweight implementation of an API that behaves similar to the real implementation but usually takes some shortcut as it isn't suitable for production i.e. an in-memory database.

Using fake is often the ideal technique when you need to use a test double, but a fake might not exist for an object you need to use in a test, and writing one can be challenging as you need to ensure that it has similar behavior to the real implementation.

### Stubbing

Stubbing is the process of giving behavior to a function that otherwise has no behavior on its own i.e. you specify to the function exactly what values to return by stubbing the return values.

Stubs provide canned answers to calls made during the test, usually not responding at all to anything outside what's programmed in for the test i.e. querying a user123's bank balance should return 10,000. Can be classified as **state testing with predetermined behavior and hardcoded values**. A stub doesn't care whether it is called 0, 1, or 100 times.

However, overuse of stubbing can result in major losses in productivity for engineers who need to maintain these tests. **Stubbing also leaks implementation details**; if they change, you need to update your tests to reflect those changes.

### Interaction Testing

Interaction testing is a way to validate how a function is called without actually calling the implementation of the function. A test should fail if a function isn't called the correct way i.e. assert_called_once, assert_call_count, checking call arguments, etc.

This **should be avoided when possible** because overuse can easily result in brittle tests, and state testing is preferred. Nonetheless, there are cases for which interaction testing is warranted:

- You cannot perform state testing as you are unable to use a real implementation or fake
- Differences in the number or order of calls to a function would cause undesired behavior

### Classical Testing

The act of using real implementations instead of test doubles. Tests have higher **fidelity** when they execute code as it will be executed in production, and using real implementations helps accomplish this. Fidelity is the property by which a test is effective of the real behavior of the system under test.

A real implementation is preferred if it is fast, deterministic, and has simple dependencies i.e. an amount of money, a date, a geographical address, or a collection class such as a list or map.

When using a real implementation, you need to construct all of its dependencies. To support the use case for tests, the object construction code needs to be flexible enough, and the ideal solution is to use a **factory method or automated dependency injection**.

### Spies

Spies are stubs that also record some information based on how they were called i.e. an email service that records how many messages it sent.

### Mocks

Objects pre-programmed with expectations which form a specification of the calls they are expected to receive. When mocking, it is to ensure that the call was made. If the expected call is not made, the test fails. Can be classified as **behavioral testing**. Implementing this approach requires more smarts in the fake collaborators that we create, and if overused can cause tests to become brittle.

## Stubbing vs Mocking

The easiest way to tell we are dealing with a stub is to notice that a stub can never fail the test. The assert the test uses are always against the class under test. On the other hand, the test will use a mock object to verify whether the test has failed or not. Mocks can be useful to ensure that the expected side effects happen.

## Impact of Test Doubles on Software Development

### Testability

To use test doubles, a codebase needs to be designed to be testable: it should be possible for tests to swap out real implementations with test doubles. This could be achieved through dependency injection.

### Applicability

Although proper application of test doubles can provide a powerful boost to engineering velocity, their **improper use can lead to tests that are brittle, complex and less effective**. In many cases, test doubles are not suitable and engineers should prefer to **use real implementation instead**.

### Fidelity

Fidelity refers to how closely the behavior of a test double resembles the behavior of the real implementation that it's replacing. If the behavior of a test double significantly differs, it wouldn't provide much value.
