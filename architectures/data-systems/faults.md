## Problems in distributed systems

A wide range of problems can occur in distributed systems, including:

- Packets sent over the network may be lost or arbitrarily delayed
- Node's clock may be significantly out of sync with other nodes (despite best efforts to set up NTP)
- Process may pause for a substantial amount of time at any point in its execution (stop-the-world garbage collector), be declared dead by other nodes, and then come back to life again without realizing it was paused

## Dealing with faults

To tolerance faults, first step is to detect them, but even that is hard. Most systems don't have an accurate mechanism of detecting whether a node has failed, so most distributed algorithms rely on timeouts to determine whether a remote node is still available. However, **timeouts cannot distinguish between network and node failures.**

Once a fault is detected, making a system tolerate is not easy as there is no global variable, shared memory, common knowledge or any kind of shared state between nodes. Major decisions cannot be safely made by a single node, and hence, require protocols that enlist help from other nodes i.e. get a quorum to agree.
