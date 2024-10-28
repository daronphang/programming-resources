## Failure models

### Crash failure

A crash failure occurs when a server prematurely halts, but was working correctly until it stopped. An important aspect of crash failures is that once the server has halted, nothing is heard from it anymore.

### Omission failure

An omission failure occurs when a server fails to respond to a request. It will generally not affect the current state of the server. Possible reasons include:

- The server never got the request in the first place
- No thread was listening for incoming requests
- Send buffer overflows
- Improper memory management

### Timing failure

Timing failures occur when the response lies outside a specified real-time interval.

### Response failure

Response failure is when the server's response is incorrect e.g. value or state-transition failure.

### Arbitrary failure

The most serious are arbitrary failures or **byzantine failures**. When arbitrary failures occur, clients should be prepared for the worst. In particular, a server may be producing output it should never have produced, but which cannot be detected as being incorrect. Also, it could mean that the node deviated from its algorithm in arbitrary ways, leading to crashes or unexpected behavior due to bugs or malicious activity.

## Failure semantics

Process P can conclude that process Q has come to a halt for the following:

- **Fail-stop failures** refer to crash failures that can be reliably detected
- **Fail-noisy failures** are similar to fail-stop failures, but that P will eventually come to the correct conclusion that Q has failed
- **Fail-silent failures** happens when P cannot distinguish crash failures from omission failures
- **Fail-safe failures** involves dealing with arbitrary failures that are benign
- **Fail-arbitrary failures** involves dealing with failures that may be unobservable, in addition to being harmful
