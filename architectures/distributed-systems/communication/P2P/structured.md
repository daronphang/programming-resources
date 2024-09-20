## Structured peer-to-peer systems

In a structured peer-to-peer system, the nodes are organized in an overlay that adheres to a specific, deterministic topology: a ring, hypercube, a binary tree, a grid, etc. This topology is used to efficiently look up data. Characteristic for structured peer-to-peer systems, is that they are generally based on using a so-called **semantic-free index**. This means that each data item that is to be maintained by the system, is uniquely associated with a key.

Each node is assigned an identifier from the same set of all possible hash values, and each node is made responsible for storing data associated with a specific subset of keys. In essence, the system is thus seen to implement a **distributed hash table (DHT)**.

Hence, the **topology** of a structured peer-to-peer system plays a crucial role. Any node can be asked to look up a given key, which then boils down to efficiently routing that lookup request to the node responsible for storing the data associated with the given key.

```
existing node = lookup(key)
```
