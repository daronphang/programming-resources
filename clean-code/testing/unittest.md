## Unittest

### Strive for Unchanging Tests

The ideal test is unchanging: after it is written, it never needs to change unless the requirements of the system under test change.

### Test via Public APIs

The most important way to ensure this is to write tests that invoke the system being tested in the same way its users would, by **making calls against its public API rather than its implementation details**. Also, such tests can serve as useful examples and documentation for users.

### Test State, Not Interactions

Another way that tests commonly depend on implementation details involves not which methods of the system that test calls, but how the results of those calls are verified.

With state testing, you observe the system itself to see what it looks like after invoking with it. With interaction testing, you instead check that the system took an expected sequence of actions on its collaborators in response to invoking it i.e. validate how a function is called without actually calling the implementation of the function. Many tests will perform a combination of state and interaction validation.

Interaction tests tend to be more brittle as they check how a system arrived at its result, whereas usually **you should care only what the result is**. Also, they are less scalable, doesn't tell you that the system under test is working properly, and utilizes implementation details.

### Test Behaviors, Not Methods

The first instinct of many engineers is to try to match the structure of their tests to the structure of their code such that every production method has a corresponding test method. This will cause the test to become increasingly convulted and grow more difficult to work with.

The problem is that framing tests around methods can naturally encourage unclear tests because a single method often does a few different things under the hood, and might have several tricky edge cases. **Instead of writing a test for each method, write a test for each behavior**.

A behavior is any guarantee that a system makes about how it will respond to a series of inputs while in a particular state i.e. **cause and effect**. Behaviors can often be expressed using words "given", "when", "then" i.e. given a bank account is empty, when attempting to withdraw money from it, then the transaction is rejected.

### Don't Put Logic in Tests

Complexity is most often introduced in the form of logic. Logic is defined via imperative parts of programming languages including operators, loops, and conditionals.

### Code Sharing with DAMP, not DRY

Most software attemps to achieve a principle called DRY (Don't Repeat Yourself). However, the downside to such consolidation is that it can make code unclear. Instead of completely DRY, test code should often strive to be DAMP (promote Descriptive And Meaningful Phrases). A little bit of duplication is OK in tests so long as that duplication makes the test simpler and clearer.

### Shared Values

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
