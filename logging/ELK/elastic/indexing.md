## Index

An index contains a schema and is divided into one or more shards, each of which may be replicated across multiple nodes to protect against hardware failures. An Elasticsearch index is divided into shards and each shard is an instance of a Lucene index. Indices are used to store the documents in dedicated data structures corresponding to the data type of fields i.e. text fields are stored inside an inverted index, while numeric and geo fields are stored inside BKD trees.

You can have as many indices defined as you want. These in turn will hold documents that are unique to each index i.e. an index for products, another index for customers.

### Example

```
PUT /test_index1?pretty

{
    "settings" : {
        "number_of_shards" : 2,
        "number_of_replicas" : 1
    },
    "mappings" : {
        "properties" : {
            "tags" : { "type" : "keyword" },
            "updated_at" : { "type" : "date" }
        }
    }
}
```
