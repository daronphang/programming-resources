### Indexing

In any database, indexes support the efficient execution of queries. Without them, database must scan every document in a collection or table to select those that match the query statement. Indexes improve the speed of search operations as it is performed on indexes that holds only few fields. A unique index ensures that indexed fields do not store duplicate values. MongoDB creates a unique index on the \_id field during creation of a collection.

However, indexing comes with a performance cost (indexes are resource-intensive), but are more than worth the cost for frequent queries on large data sets. For instance, having too many indexes can hamper the performance of insert, update and delete operations due to the additional write and data space used by indexes.

Default name for an index is the concatenation of indexed keys and each key's direction in the index, using underscores as separator.

```mongodb
// members collection
db.members.createIndex( { "user_id": 1 }, { unique: true } )  // user_id_1

// creating indexes with custom name
db.products.createIndex(
  { item: 1, quantity: -1 } ,
  { name: "query for inventory" }
)
```

#### Example

```mongodb
db.users.insert(
	{
		"address": {
			"city": "Los Angeles",
			"state": "California",
			"pincode": "123"
		},
		"tags": [
			"music",
			"cricket",
			"blogs"
		],
		"name": "Tom Benzamin"
	}
)

// creating index on tags field
db.users.createIndex({"tags":1})

// returns user that contains cricket in tags field
db.users.find({tags:"cricket"}).pretty()
{
	"_id" : ObjectId("5dd7c927f1dd4583e7103fdf"),
	"address" : {
		"city" : "Los Angeles",
		"state" : "California",
		"pincode" : "123"
	},
	"tags" : [
		"music",
		"cricket",
		"blogs"
	],
	"name" : "Tom Benzamin"
}
```

### Compound Indexing

Can enforce a unique constraint on compound indexes i.e. combination of index key values is unique.

```mongodb
db.members.createIndex({groupNumber: 1, lastName: 1, firstName: 1}, {unique: true})
```

## Secondary indexes on high-cardinality columns

Do not use an index on high-cardinality columns as you then query a huge volume of records for a small number of results.

With a secondary index, each node has to query its own local data for responding to a query. These index are also built using a background process.

If you create an index on a high-cardinality column, which has many distinct values, a query between the fields will incur many seeks for very few results. In the table with a billion songs, looking up songs by writer (a value that is typically unique for each song) instead of by their artist, is likely to be very inefficient.

In a high-cardinality column, the rate of change (i.e. additions/deletions) from that column can be quite high. If that rate of change is faster than the updating of the index via the background process, then using an index is "inefficient" (the index is performing more work than is needed by the application, which might often get the wrong answer).

It would probably be more efficient to manually maintain the table as a form of an index instead of using the Cassandra built-in index i.e. a **second table**. For columns containing unique data, it is sometimes fine performance-wise to use an index for convenience, as long as the query volume to the table having an indexed column is moderate and not under constant load.
