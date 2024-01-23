## Index Lifecycle Management

A feature that helps automate the creation, management and deletion of an Elasticsearch index, according to your performance, resiliency and retention requirements. You could use ILM to:

- Spin up a new index when an index reaches the optimum size of 50GB per shard
- Set a time-based index with one index per day, and archive previous ones
- Delete stale indices to enforce data retention standards

Once an index is no longer being written to, it is useful to optimzie the index to save cluster resources:

- Force merging the index to optimize space used by the index on disk
- Shrinking the index to reduce the number of shards
- Allocating the shard to less performant/storage optimized hardware
- Deleting the index when it reaches end of life

Default ILM policies are created automatically when you use Elasticsearch output plugin to send data to the Elastic Stack.

### Phases

ILM defines five index lifecycle phases:

- HOT: Index is actively updated and queried
- WARM: Index is no longer updated but still being queried
- COLD: Index is no longer updated and is queried infrequently
- FROZEN: Index is no longer updated and is queried rarely (queries are slow)
- DELETE: Index is no longer needed and safely removed

Throughout the lifecycle, data traverses them in that order. It is not required to implement all of them, and only the hot tier is present in most use cases. All policies must start with a HOT phase.

To control the timing of these transitions, you can set a minimum age for each phase.

### ILM Actions

- **Allocate**: Move shards to different nodes, or change number of replicas
- **Delete**: Delete the index
- **Force Merge**: Optimize structure on disk
- **Freeze**: Minimize index's memory footprint and appropriate for old indices that are rarely searched
- **Migrate**: Move index shards to the data tier being used by the ILM phase
- **Read Only**: Prevent writes on index
- **Rollover**: Creat a new write index
- **Searchable Snapshot**: Mechanism to reduce memory and disk requirements for infrequently searched indices
- **Set Priority**: For Elasticsearch to know which indices to recover first
- **Shrink**: Reduce the number of primary shards in an index
- **Unfollow**: Unfollow a cross cluster replication index
- **Wait For Snapshot**: Before deleting an index

## ILM

The below policy defines the following:

- A new index is created when the size of the index reaches 50GB or when the index is 3 days old
- After 7 days, hot index is passed to warm phase where it will be merged to reduce the index to a single shard
- After 15 days, the index will be deleted

```json
// PUT _ilm/policy/hot_warm_delete
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_size": "50gb",
            "max_age": "3d"
          },
          "set_priority": {
            "priority": 50
          }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "forcemerge": {
            "max_num_segments": 1
          },
          "set_priority": {
            "priority": 25
          },
          "shrink": {
            "number_of_shards": 1
          }
        }
      },
      "delete": {
        "min_age": "15d",
        "actions": {
          "delete": {
            "delete_searchable_snapshot": true
          }
        }
      }
    }
  }
}
```

## Template Setup

A template can be setup to add the ILM policy to the index settings.

```json
// PUT _index_template/my_apache_log
// creates an index template to appy hot_warm_delete policy
// to any indices with prefix 'my_apache_log'
// alias is applied to the new index when the original rolls over
{
  "index_patterns": ["my_apache_log*"],
  "template": {
    "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 1,
      "index.lifecycle.name": "hot_warm_delete",
      "index.lifecycle.rollover_alias": "my_apache_log"
    }
  }
}
```
