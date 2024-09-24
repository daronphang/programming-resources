## Detecting failures

Failure detection is one of the cornerstones of fault tolerance in distributed systems. For a group of processes, non-faulty members should be able to decide who is still a member, and who is not.

### Heartbeats

Processes actively send "are you alive" messages to each other, or passively wait until messages come in from different processes. The latter approach makes sense only when it can be guaranteed that there is enough communication.

### Timeouts

In real settings, there are problems with using probes and timeouts. For example, due to unreliable networks, simply stating that a process has failed because it does not return an answer to a probe message may be wrong i.e. generates **false positives**.

### Gossiping

Failure detection can take place through gossiping in which each node regularly announces to its neighbors that it is still up and running.

Failure detection can also be done as a side effect of regularly exchanging information with neighbors i.e. gossip-based information dissemination.

### Consensus

Another important issue is that a failure detection subsystem should ideally be able to **distinguish network failures from node failures**. One way of dealing with this problem is not to let a single node decide whether one of its neighbors has crashed. Instead, when noticing a timeout on a probe message, a node requests other neighbors to see whether they can reach the presumed failing node. This method can also be used to forward positive information to other interested parties.
