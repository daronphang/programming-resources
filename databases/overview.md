## Databases

Two types, SQL-based (relational) and NoSQL-based (non-relational).

## RDBMS (Relational Database Management System)

Uses SQL language that offers a highly organized and structured approach to information management. Schema is explicit and database ensures all written data conforms to it i.e. schema-on-write.

### Core characteristics

- Data Schema: All data has to fit in a table.
- Data Relations: One-to-One, One-to-Many, Many-to-Many.

### Advantages

- **ACID compliance**: Satifies priorities that measure atomicity, consistency, isolation and durability. More ACID-compliant serves to guarantee the validity of database transactions, reduced anomalies, safeguard data integrity and create stable database systems.
- **Consistency**: Information will remain in structure originally created.
- **Support**: Easy to get support, add-on products, and integrates seamlessly with software stacks including LAMP.

### Disadvantages

- **Scalability and sharding challenges**: Difficult to scale up and dividing large database into smaller parts for easier management.
- **Less efficient**: Slower performance than NoSQL.

### Popular SQL database engines

- Oracle, MySQL, Postgres, Microsoft SQL Server.

## Non-Relational Database Management System

Allows you to organize information in looser fashion such as email texts, customer surveys, random social media information, etc. Ability to expose to powerful business intelligence systems that will analyze data with AI algorithms for machine learning. Can also structure data later and works with JSON format. Tables are also known as Collections.

### Advantages

- **Excellent for handling 'big data' analytics**: Support speed and efficiency of server operations while offering capacity to work with large data.
- **Flexibility in data types**: Provides unlimited freedom to store diverse data types in same place.
- **Easier to scale**: Fragmented design allows it to scale up easily.
- **No data preparation needed**: Doesn't require time to design a complex database model.

### Disadvantages

- **Difficult to find support**: Harder to find support from community during troubleshooting.
- **Lack of tools**: Have lesser third-party tools compared to SQL-based.
- **Compatibility and standardization challenges**: Lack high degree of compatibility and standardization.

### Database types

1. **Graph Stores**: Neo4j and JanusGraph.
2. **Column Stores**: Schema-agnostic that can handle querying of non-sequential data in real-time. Apache Cassandra and Hbase.
3. **Key-Value Stores**: Speed of utmost importance. Redis and Couchbase.
4. **Document Stores**: Databases with flexible schemas or schema-on-read (semi-structured data with dynamic querying and implicit schema) including MongoDB. Useful for many-to-many relationships and heterogeneous data.

Schema-agnostic means users don't have to understand schema of database before they can store data or query.

## Choosing a database

Historically, data started out being represented as one big tree (hierarchical), but it wasn't good for representing many-to-many relationships, and so the relational model was invented to solve that problem. However, some applications don't fit well in the relational model and NoSQL datastores are invented.

Document, relational and graph database models are widely used today. Both document and graph don't enforce a schema explicitly and hence, making it easier to adapt applications to changing requirements. Nonetheless, key factors include:

- **Atomicity**: Either all of operations (insert, update, delete) inside a transaction take place or none. Offers consistency.
- **Vertical vs Horizontal Scaling**: Relational for vertical (adding more compute power to a server) and non-relational for horizontal (distribute load across more servers).
- **Speed**: Non-relational database offers faster performance. Useful for real-time data such as sensor data.
