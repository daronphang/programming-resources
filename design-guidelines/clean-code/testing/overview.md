## Why Write Tests?

The act of writing tests improves the design of your systems, and generally leads to more modular software that enables greater flexibility later on. As the first clients of your code, a test can tell you much about your design choices:

- Is your system too tightly coupled to a database?
- Does your system handle all edge cases?
- Does the API support the required use cases?

Testing becomes critical to ensuring the safety of important products and services. You can't rely on a programmer's ability alone to avoid product defects. Hence, **all code changes are required to include tests**.

### Testing Definition

The simplest test is defined by:

- A single behavior you are testing, usually a method or API that you are calling
- A specific input, some value that you pass to the API
- An observable output or behavior
- A controlled environment such as a single isolated process

### Benefits

#### Less debugging

Tested code has fewer defects and will be caught before the code is submitted. A test written once continues to pay dividends and prevent costly defects and annoying debugging sessions through the lifetime of the project.

#### Increased confidence in changes

Teams with good tests can review and accept changes to their project with confidence as all important behaviors of their project are continuously verified. **Such projects encourage refactoring**. Changes that refactor code while preserving existing behavior require no changes to existing tests.

#### Improved documentation

Clear, focused tests that exercise one behavior at a time function as executable documentation. If you want to know what the code does in a particular case, look at the test for that case.

#### Thoughtful design

Writing tests for new code is a practical means of exercising the API design of the code itself. If new code is difficult tot test, it is often because the code being tested has too many responsibilities or difficult-to-manage dependencies. Well designed code should be modular, avoiding tight coupling and focusing on specific responsibilities.

#### Fast, high-quality releases

With a healthy automated test suite, teams can release new versions of their application with confidence.
