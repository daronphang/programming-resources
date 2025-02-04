## Test sizes

Size refers to the resources that are required to run a test case i.e. memory, process, and time.

### Small tests

Small tests are the most constrained of the three test sizes but are **encouraged to write whenever possible**. The primary constraint is that small tests must run in a single process, and recommended on a single thread. This means that the code performing the test must run in the same process as the code being tested i.e. you can't run a third party program such as a database as part of your test.

The other important constraints on small tests are that they aren't allowed to sleep, perform I/O operations, or make any other blocking calls. Testing code that relies on these sort of operations requires the use of **test doubles**.

The purpose of these restrictions is to ensure that small tests don't have access to the main sources of test slowness or **nondeterminism which can introduce flakiness**.

### Medium tests

Medium tests can span multiple processes, use threads, and can make blocking calls, I/O operations, including network calls, to localhost. The only remaining restriction is that medium tests aren't allowed to make network calls to any system other than localhost.

The ability to run multiple processes opens up a lot of possibilities. For example, you could run a database instance to validate the code you are testing integrates correctly in a more realistic setting. You could also test a combination of web UI and server code.

Unfortunately, with increased flexibility comes increased potential for tests to become slow and nondeterministic. Medium tests still provide a bit of protection by **preventing access to remote machines via the network, which is the biggest source of slowness and nondeterminism in most systems**.

### Large tests

Large tests remove the localhost restriction imposed on medium tests, allowing the test and the system being tested to span across multiple machines.

Large tests are mostly reserved for full-system and e2e tests that are more about validating configuration than pieces of code, and for tests of legacy components for which it is impossible to use test doubles.
