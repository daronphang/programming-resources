## DBMS (Database Management System)

DBMS is a software package that provides an interface for users to define, manipulate, retrieve and manage data in a database. DBMS are categorized to their data structures or types.

## Hierarchical

Model data is organized in a tree-like structure. Data is stored hierarchically (top-down or bottom-up) format. Data is represented using a parent-child relationship. Parent may have many children, but each child has only one parent.

## Network

Allows each child to have multiple parents. Helps to address the need to model more complex relationships like many-to-many relationship. In this model, entities are organized in a graph which can be accessed through several paths.

## Relational

Model is based on normalizing data into tables. A table is a logical structure made up of rows and columns. Rows have no fixed order, while order of the columns is the order specified when the table was created. Relational models are stored in fixed structures and manipulated using SQL.

## Object-Oriented

Data is stored in the form of objects. The class structure displays data within it.

## NoSQL

NoSQL databases are non-relational databases designed to store, manage, and retrieve unstructured or semi-structured data. They offer an alternative to traditional relational databases, which rely on structured data and predefined schemas. NoSQL databases have become popular due to their flexibility, scalability, and ability to handle large volumes of data, making them well-suited for modern applications, big data processing, and real-time analytics.

### Document-based

These databases store data in document-like structures, such as JSON or BSON. Each document is self-contained and can have its own unique structure, making them suitable for handling heterogeneous data.

Examples of document-based NoSQL databases include MongoDB and Couchbase.

### Key-value

These databases store data as key-value pairs, where the key acts as a unique identifier, and the value holds the associated data. Key-value databases are highly efficient for simple read and write operations, and they can be easily partitioned and scaled horizontally.

Examples of key-value NoSQL databases include Redis and Amazon DynamoDB.

### Column-family

These databases store data in column families, which are groups of related columns. They are designed to handle write-heavy workloads and are highly efficient for querying data with a known row and column keys.

Examples of column-family NoSQL databases include Apache Cassandra and HBase.

### Graph-based

These databases are designed for storing and querying data that has complex relationships and interconnected structures, such as social networks or recommendation systems. Graph databases use nodes, edges, and properties to represent and store data, making it easier to perform complex traversals and relationship-based queries.

Examples of graph-based NoSQL databases include Neo4j and Amazon Neptune.
