## Peer-to-peer (P2P) systems

Peer-to-peer systems have many interesting technical aspects like **decentralized control, self-organization, adaptation and scalability**. Peer-to-peer systems can be characterized as distributed systems in which all nodes have identical capabilities and responsibilities and all communication is symmetric.

## Structured

In a structured peer-to-peer system, the nodes are organized in an overlay that adheres to a specific, deterministic topology: a ring, hypercube, a binary tree, a grid, etc. This topology is used to efficiently look up data. Characteristic for structured peer-to-peer systems, is that they are generally based on using a so-called **semantic-free index**. This means that each data item that is to be maintained by the system, is uniquely associated with a key.

Each node is assigned an identifier from the same set of all possible hash values, and each node is made responsible for storing data associated with a specific subset of keys. In essence, the system is thus seen to implement a **distributed hash table (DHT)**.

Hence, the **topology** of a structured peer-to-peer system plays a crucial role. Any node can be asked to look up a given key, which then boils down to efficiently routing that lookup request to the node responsible for storing the data associated with the given key.

```
existing node = lookup(key)
```

## Unstructured

In an unstructured peer-to-peer system, each node maintains an ad hoc list of neighbors. The resulting overlay resembles what is known as a **random graph**.

When a node joins, it often contacts a well-known node to obtain a starting list of other peers in the system. This list can then be used to find more peers, and perhaps ignore others, etc. In practice, a node generally changes its local list almost continuously. For example, a node may discover that a neighbor is no longer responsive and that it needs to be replaced.

Data can be search in two ways: flooding and random walk.

### Flooding

How flooding works:

1. An issuing node (u) passes a request for a data item to all its neighbors
2. A request will be ignored when its receiving node (v) has seen it before
3. Otherwise, v searches locally for the requested item
4. If found, it responds back to the original forwarder
5. If not, it forwards the request to all of its own neighbors

Flooding can be expensive, and a request often has an associated TTL value. Choosing the TTL value is critical: too small means that a request will stay close to the issuer and may not reach a node having the data, while too large incurs high communication costs.

### Random walk

How random walk works:

1. An issuing node (u) can simply try to find a data item by asking a **randomly chosen neighbor** (v)
2. If v does not have the data, it forwards the request to one of its randomly chosen neighbors
3. Step 2 is repeated until the key is found

A random walk imposes much less network traffic, but it may take much longer before a node is reached that has the requested data. To decrease the waiting time, an issuer can start n random walks simultaneously, which can drop the time by a factor of n. Reports that relatively small values of n (16, 64) turn out to be effective.

A random walk also needs to be stopped. To this end, we can either again use a TTL, or alternatively, when a node receives a lookup request, check with the issuer whether forwarding the request to another randomly selected neighbor is still needed.

In practice, when dealing with replicated data, even for minimal replication factors and different replication distributions, studies show that deploying random walks is not only effective, it can also be much **more efficient** than flooding.
