## CI Paradigm

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

It is also important that feedback from CI be widely accessible. Visbility into test history empowers engineers to share and collaborate on feedback, an essential requirement for disparate teams to diagnose and learn from integration failures between their systems.

### Automation

Automated development-related tasks saves engineering resources in the long run. Although it will have bugs like any other software, when implemented effectively, they are still faster, easier and more reliable than attempted manually.

#### Continuous Build

The Continuous Build integrates the latest code changes at head and runs an automated build and test. Breaking the build or failing the build includes breaking tests as well as breaking compilation.
