## Cardinality

Cardinality is a mathematical term that refers to the number of elements in a given set (unique elements). When applied to databases, database cardinality can be defined as the set of elements arranged in tables and rows. It also refers to the counting done to recognize the elements in a set, identify relationships among different tables, and identify the number of values in the tables. These relationships can be one-to-one, many-to-many, and one-to-many.

Cardinality has a big impact on database performance because it influences the query execution plan. The planner will examine column statistics and use them to figure out how many values a query is likely to match, among other things.

### Why is cardinality important?

Cardinality helps simplify the query execution plan. A query execution plan is a sequence of steps used to search data stored in a database. Cardinality plays a crucial role, as it provides a structured format and correlates entities in different tables. Having a well-structured database and a query execution plan helps users find specific information within a database.

The cardinality of a column is very important to database designers and the database query optimizer. For the designer or DBA, knowing a column is mainly repeating values (low cardinality) tells them that it is a poor candidate for an index as it will not be very selective.

For a cost-based query optimizer, the selectivity of a potential index dictates whether it will be used or ignored. Creating and maintaining indexes is expensive in terms of CPU and IO resource usage, so designers and developers need to ensure they create ones that will get used.

### Cardinality in data modeling (relationship)

Cardinality in data modeling represents the relationship between the data in two different tables by highlighting how many times a specific entity occurs in comparison to another. Cardinality here refers to how many distinct values are in a column:

- A lot of distinct values is high cardinality (good for selecting columns to index or use as a partitioning key)
- A lot of repeated values is low cardinality (more expensive full table scan)

There are three types of relationships data cardinality consists of:

- One-to-one relationship
- One-to-many relationship
- Many-to-many relationship

### Cardinality in time series databases

Cardinality here refers to the number of series in a time series database. A time series is a labeled set of values over time, stored as (timestamp, number) pairs.

This data model is the canonical starting point for most monitoring products. However, it does not provide meaningful insights. To solve this problem, many monitoring systems support tags with metadata:

```
os.cpu.util = [(5:31, 82%, role=web), (5:32, 75%, role=web), (5:33, 83%, role=web)]
```

This creates another problem as the metadata is repeated for each set, and most time series database tries to avoid N-dimensional storage as time-value pairs can be encoded efficiently. This problem is solved by storing the tags with the series identifier:

```
(name=os.cpu.util,role=web) = [(5:31, 82%), (5:32, 75%), (5:33, 83%)]
```

When people talk about cardinality in monitoring and how it’s hard to handle high-cardinality dimensions, they’re basically talking about **how many distinct combinations of tags there are**, and thus the number of series. More tags will result in higher combinations.

```
(name=os.cpu.util,role=web) = [(5:31, 82%), (5:32, 75%)]
(name=os.cpu.util,role=db)  = [(5:33, 83%)...]
(name=os.cpu.util,role=web, datacenter=us-east1, ami=ami-5256b825, …) = [...]
```
