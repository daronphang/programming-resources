## Consistent hashing

Setting up the initial shards for a new service is relatively straightforward; however, when you want to change the number of shards, it often becomes a complicated process, as the hashing function would route to a different shard than the one they were previously mapped to.

```
# for 10 shards
hash(Req) % 10

# for 11 shards
hash(Req) % 11
```

To resolve these kinds of problems, many sharding functions use **consistent hashing functions**. They are special hash functions that are guaranteed to only remap # keys / # shards, when being resized to # shards. Consistent hashing minimizes the number of keys to be remapped when the total number of nodes changes.

The principle advantage of consistent hashing is incremental stability; the departure or arrival of a node into the cluster only affects its immediate neighbours and other nodes remain unaffected.

Consistent Hashing is a distributed hashing scheme that operates independently of the number of servers or objects in a distributed hash table. It powers many high-traffic dynamic websites and web applications.

### How it works

1. The output of the hash function is placed on a virtual ring structure (known as the hash ring)
2. The hashed IP addresses of the nodes are used to assign a position for the nodes on the hash ring
3. The key of a data object is hashed **using the same hash function** to find the position of the key on the hash ring
4. The hash ring is traversed in the clockwise direction starting from the position of the key until a node is found
5. The data object is stored or retrieved from the node that was found

<img src="../../assets/consistent-hashing.png">

### Deletion of node

The failure (crash) of a node results in the movement of data objects from the failed node to the immediate neighboring node in the clockwise direction. The remaining nodes on the hash ring are unaffected.

### Addition of node

When a new node is provisioned and added to the hash ring, the keys (data objects) that fall within the range of the new node are moved out from the immediate neighboring node in the clockwise direction.

## vnodes

Each node in the system is assigned multiple random value within this space. Each random value is called a vnode position; a single node is associated to multiple vnodes and consequently multiple positions on the ring.

Each data item identified by a key is assigned to a node by hashing the data item’s key to yield its position on the ring, and then walking the ring clockwise to find the first vnode with a position larger than the item’s position. The node associated with the vnode is the location of the data item.

<img src="../../assets/consistent-hashing-vnode.png">
