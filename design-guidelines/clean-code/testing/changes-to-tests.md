## Types of Changes

When writing tests, one question we need to ask is how often should we expect to need to change a test after writing it. Hence, we need to think about the kinds of changes that engineers make to production code and how we should expect tests to respond to those changes.

### Pure refactorings

When an engineer refactors the internals of a system without modifying its interface, whether for performance or clarity, the system's tests **should not need to change**. The role of tests is to ensure that the refactoring didn't change the system's behavior.

### New features

When an engineer adds new features to an existing system, the system's existing behaviors should remain unaffected. The engineer must write new tests to cover the new behaviors, but they **shouldn't need to change any existing tests**.

### Bug fixes

Fixing a bug is much like adding a new feature: the presence of the bug suggests that a case was missing from the initial test suite, and the bug fix should include that missing test case. **Should not require updates to existing tests**.

### Behavior changes

Changing a system's existing behavior is the one case when we **expect to have to make updates to the system's existing tests**. Such changes tend to be significantly more expensive than the other three types.
