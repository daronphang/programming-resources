## Paxos

The Paxos algorithm operates in a series of phases, ensuring that a group of nodes reach a consensus on a single value. These phases involve message exchanges between proposers and acceptors to reach an agreement on a value or sequence of values.

Paxos ensures two critical properties:

- Safety: only one value is agreed upon
- Liveness: The algorithm makes progress even in the presence of failures and message delays

## Phases

### Prepare

- A proposer initiates the consensus process by sending a prepare message with a proposal number to the acceptors
- The proposal number is a unique identifier for the current proposal and helps prevent conflicts between competing proposals
- Upon receiving the prepare message, each acceptor checks if the proposal number is greater than any previous proposal number it has seen
- If the proposal number is greater, the acceptor replies with a promise not to accept any proposals with lower numbers and includes information about the highest-numbered proposal it has accepted (if any)

### Promise

- After receiving prepare messages, acceptors respond with promise messages to the proposer
- The promise message includes the acceptor’s acceptance status and the highest-numbered proposal it has accepted (if any)
- If an acceptor has not accepted any proposals before, it responds with a promise but without any accepted value.
- If an acceptor has accepted a proposal before, it includes the proposal number and value in its promise

### Accept

- If a proposer receives promises from a majority of acceptors (a quorum), it moves on to the accept phase
- In the accept phase, the proposer sends an accept message to the acceptors with the same proposal number and the value it wants to be accepted
- Acceptors check if the proposal number is not lower than any previous proposal number they have seen
- If the proposal number is valid, the acceptor accepts the proposal and informs the proposer
