## Trunk-based Development

Trunk-based development is a source-control branching model, where developers collaborate on code in a single branch called 'trunk' or 'master', and resist any pressure to create other long-lived development branches by employing documented techniques. Hence, merge hell is avoided, and build is not broken.

It is a practice where developers merge small, frequent updates to main branch. Since it streamlines merging and integration phases, it helps achieve CI/CD and increases software delivery and organizational performance.

### Allows continuous code integration

In this model, there is a steady stream of commits flowing into the main branch. Adding an automated test suite and code coverage monitoring for this stream of commits enables CI.

### Ensures continuous code review

Small commits of trunk-based development make code review a more efficient process. This is far easier compared to a long-lived feature branch where a reviewer reads pages of code or manually inspects a large surface area of code changes.

### Enables consecutive production code releases

Teams should make frequent, daily merges to the main branch. This development strives to keep the trunk branch "green", meaning it is ready to deploy at any commit. Automated tests, code coverage, and code reviews provides a trunk-based development project with the assurances it's ready to deploy to production at any time.

## Feature-based Development

A feature-based development workflow (gitflow) is a classic approach to software engineering. Before developing a feature, the developer checks out a "feature" branch and makes all the code changes there. The developer creates a merge request with the main branch when the development on the feature is complete.

Managing feature-based development can be tricky, especially when multiple pull requests are queued to merge into the main branch.

There are situations in which your team may consider a feature-based workflow, such as maintaining multiple software versions i.e. Linux kernel.
