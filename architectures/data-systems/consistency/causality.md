## Causal consistency

Causality imposes an ordering on events: cause comes before effect, a message is sent before received, etc. These chains of causally dependent operations define the causal order in the system i.e. what happened before what.

Unlike linearizability, causality provides us with a **weaker consistency model**: some things can be concurrent, and version history is like a timeline with branching and merging (similar to Git). Causal consistency does not have the coordination overhead of linearizability and is much less sensitive to network problems.

For a data store to be considered causally consistent, it is necessary that the store obeys the following conditions:

- Writes that are potentially causally related must be seen by all processes in the same order
- Concurrent writes may be seen in a different order on different machines

### Causal order is not total order

A total order allows any two elements to be compared. However, as the model allows concurrent operations, causality defines a partial order i.e. some operations are ordered while others are incomparable.

### Linearizability is stronger

The relationship between linearizability and causal order is that linearizability implies causality: **any system that is linearizable will preserve causality correctly**.
