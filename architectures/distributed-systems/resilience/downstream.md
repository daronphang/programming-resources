## Downstream resiliency

We explore patterns that can shield a service against failures in its downstream dependencies.

### Timeouts

When you make a network call, you can configure a timeout to fail the request if there is no response within a certain amount of time. Network calls that don’t return lead to resource leaks at best. Timeouts limit and isolate failures, **stopping them from cascading** to the rest of the system.

Ideally, you should set your timeouts based on the desired false timeout rate. For example, if you want to have about 0.1% false timeouts, you should set the timeout to the 99.9th percentile of the remote call’s response time, which you can measure empirically.

### Retries

If the failure or timeout was caused by a short-lived connectivity issue (transient), then retrying after some backoff time has a high probability of succeeding. However, if the downstream service is overwhelmed, retrying immediately will only make matters worse. Delays between retries can be performed using **exponential backoff**.

However, one must be aware of **retry amplification**. This happens when there are intermediate requests between services, and retries are performed at multiple levels of the dependency chain. This behavior can easily **bring down the whole system**. Hence, when you have long dependency chains, you should only retry at a single level of the chain, and fail fast in the other ones.

### Circuit breaker

To deal with non-transient failures, we need a mechanism that detects long-term degradations of downstream dependencies and stops new requests from being sent downstream in the first place. This mechanism is called a circuit breaker.

A circuit breaker’s goal is to allow a sub-system to fail without bringing down the whole system with it. To protect the system, calls to the failing sub-system are temporarily blocked. Later, when the sub-system recovers and failures stop, the circuit breaker allows calls to go through again.

Unlike retries, circuit breakers prevent network calls entirely, which makes the pattern particularly useful for long-term degradations. Retries are helpful when the expectation is that the next call will succeed, while circuit breakers are helpful when the expectation is that the next call will fail.

Circuit breaker is implemented as a **state machine**:

- **Closed**: Acts as a passthrough for network calls and tracks the number of failures; if the number exceeds a given threshold, the circuit breaker trips and opens the circuit
- **Open**: Network calls fail immediately; if the downstream dependency is non-critical, you want your service to degrade gracefully instead
- **Half-open**: Next call is allowed to passthrough; if call succeeds, it transitions to closed state, else it transitions back to open state

Nonetheless, when implementing circuit breakers, we need to consider the following:

- How many failures are enough to consider a downstream dependency down?
- How long should the circuit breaker wait to transition from the open to the half-open state?
