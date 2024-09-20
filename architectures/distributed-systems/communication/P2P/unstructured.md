## Unstructured peer-to-peer systems

In an unstructured peer-to-peer system, each node maintains an ad hoc list of neighbors. The resulting overlay resembles what is known as a **random graph**.

When a node joins, it often contacts a well-known node to obtain a starting list of other peers in the system. This list can then be used to find more peers, and perhaps ignore others, etc. In practice, a node generally changes its local list almost continuously. For example, a node may discover that a neighbor is no longer responsive and that it needs to be replaced.

## Searching for data

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
