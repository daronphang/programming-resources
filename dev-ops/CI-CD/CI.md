## CI Paradigm

CI is the continuous assembling and testing of our entire com‐ plex and rapidly evolving ecosystem.

From a testing perspective, CI is a paradigm to inform the following:

- Which tests to run when in the development/release workflow
- How to compose the system under test (SUT) at each point, balancing concerns like fidelity and setup cost

## CI Concepts

### Fast Feedback Loops

The cost of a bug grows almost exponentially the later it is caught in the code change lifecycle. To minimize costs, CI encourages us to use fast feedback loops (shifting left). Each time we integrate a code change into a testing scenario and observe the results, we get a new feedback loop. Feedback can take many forms (from fastest to slowest):

- The edit-compile-debug loop of local development
- Automated test results to a code change author on presubmit
- An integration error between changes to two projects, detected after both are submitted and tested together
- An incompatibility between your project and an upstream microservice dependency
- Bug reports by internal users
- Bug or outage reports by external users of the press

**Canarying** (deploying to a small percentage of production first) can help minimize issues. However, it can cause problems, particularly around compatibility between deployments when multiple versions are deployed at once. This is known as **version skew**, a state of distributed system in which it contains multiple incompatible versions of code/data/configuration.

#### Accessible and actionable feedback

It is also important that feedback from CI be widely accessible. Visibility into test history empowers engineers to share and collaborate on feedback, an essential requirement for disparate teams to diagnose and learn from integration failures between their systems.

### Automation

Automated development-related tasks saves engineering resources in the long run. Although it will have bugs like any other software, when implemented effectively, they are still faster, easier and more reliable than attempted manually.

#### Continuous Build

The Continuous Build integrates the latest code changes at head and runs an automated build and test. Breaking the build or failing the build includes breaking tests as well as breaking compilation.

After a change is submitted, the CB should run all relevant tests. If a change passes all tests, the CB marks it passing or “green,” as it is often displayed in user interfaces (UIs). This process effectively introduces two different versions of head in the repository: true head, or the latest change that was committed, and green head, or the latest change the CB has verified.

### Failure Management

When a breaking change has been integrated by passing presubmit tests but not integrated tests, it is imperative to identify the failure. However, it can be difficult due to a prevalence of flakes and the occasional issues with the testing infrastructure itself.

After a breaking change has been isolated, it is important to fix it ASAP. The presence of failing tests can quickly erode confidence in the test suite.

Rolling a change back is often the fastest and safest route to fix a build as it quickly restores the system to a known good state.

## Best Practices

### Green rate

Having a 100% green rate on CI, just like having 100% uptime for a production service, is awfully expensive. One of the biggest problem is going to be a race condition between testing and submission.

Policies that say "nobody can commit if our latest CI results are not green" are probably misguided. If CI reports an issue, such failures should definitely be investigated. If the root cause is well understood and clearly won't affect production, blocking commits is unreasonable.

### Alert and alarm

Treating every alert as an equal cause for alarm is not generally the correct approach. IF an alert fires in production but the service isn't actually impacted, silencing the alert is the correct choice.

The same is true for test failures: if a test is known to be failing for irrelevant reasons, we should probably be more liberal in accepting changes that disable a failed test. Not all test failures are indicative of upcoming production issues.

## Challenges

Some challenges include:

- Potential disruption to engineer productivity of unstable, slow, conflicting, or too many tests at presubmit
- culprit finding and failure isolation (integrating upstream microservices is one approach)
- resource constraints whereby large tests can be very expensive
- Flaky tests eroding confidence
- Failure management (what to do when tests fail, can be resolved with Hermetic testing)
