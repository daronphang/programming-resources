## Shards

Shards are a single Lucene index i.e. a self-contained search engine that indexes and handles queries for a subset of data in an Elasticsearch cluster. They are the building blocks of Elasticsearch and what facilitate its scalability.

Index size is a common cause of crashes as there is no limit to how many documents can be stored on each index, and it may take up space that exceeds the limits of the hosting server.

One way to counter this problem is to split up indices horizontally into pieces called shards. This allows you to distribute operations across shards and nodes to improve performance.

As data is written to a shard, it is periodically published into new immutable Lucene segments on disk, and becomes available for querying.

```
"settings" : {
    "index" : {
        "number_of_shards" : 2,
        "number_of_replicas" : 1
    }
  }
```

### How it Works

- When an index is created, it will have default number of 5 shards
- Each shard contains the documents data of index (primary and replicas)
- Having multiple shards help take advantage of parallel processing on a single machine
- If another node instance joins the same cluster, the shards will be distributed in an even way over the cluster

### Sizing

Each index and shard has some overhead and if you divide your data across too many shards (oversharding), the overhead can become overwheling and the cluster will be less efficient at responding to searches.

Larger shards take longer to recover after a failure. When a node fails, Elasticsearch rebalances the node's shards across the data tier's remaining nodes. This recovery process typically involves copying the shard contents across the network. Experience shows to aim for shard sizes between **10GB and 50GB**.
