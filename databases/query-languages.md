## Query Languages

SQL, MapReduce, MongoDB's aggregation pipeline, Cypher, SPARQL, and Datalog.

## SQL

SQL is a declarative query language as opposed to imperative. You specify the pattern of data you want i.e. conditions the results must meet, and how you want the data to be transformed (sorted, group, aggregated), but not how to achieve that goal. This is automatically determined by the database system's query optimizer that decides which indexes and join methods to use, and in which order to execute various parts of the query.

More attractive as it is typically more concise and easier to work with than an imperative API, and hides implementation details so performance improvements can be made without changes to queries.
