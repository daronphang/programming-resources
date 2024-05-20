## DynamoDB

Amazon DynamoDB is a **key-value and flexible NoSQL** that offers fast and reliable performance with no scalability issues. It is **serverless**, which means that you do not have to provision, patch, and manage servers.

DynamoDB is a fully managed service that handles the operations work. You can offload the administrative burdens of operating and scaling distributed databases to AWS. Highly available with replication across **3 Availability Zones** with 6 copies of data i.e. similar to Aurora.

DynamoDB provides **automatic scaling**. As the size grows/shrinks, it automatically scales to adjust for changes in capacity while maintaining consistent performance. This makes a suitable choice that require **high performance while scaling**.

### Features

- Managing and scaling
- Serverless
- handles high traffic
- Automatic sharding

### Autoscaling

Autoscaling is important for both Table (primary) and Global Secondary Indexes performance and availability.

### Security

DynamoDB integrates with IAM but only uses it for table and row access.

### Monitoring

DynamoDB supports CloudWatch and CloudTrail; but it also supports DynamoDB Streams which tracks adn emits events based on table changes i.e. similar to Aurora Activity Streams.

## Components

### Table

A collection of items, where each item is a collection of attributes.

### Primary Key

DynamoDB uses the the partition key's value as input to an internal hash function. The output determines the partition (physical storage) in which the item will be stored.

Supports two different kinds of primary keys:

- Partition key: A single attribute that is unique
- Partition key and sort key: Composite primary key consisting of two attributes that gives you additional flexibility when querying data

### Secondary indexes

Used to query off of other attributes that are not the partition key or sort key.

### Attribute

A fundamental data element that does not need to be broken down any further i.e. fields (supports nested attributes up to 32 levels deep)

```
{
    "PersonID": 101,
    "LastName": "Smith",
    "FirstName": "Fred",
    "Phone": "555-4321"
}

{
    "PersonID": 102,
    "LastName": "Jones",
    "FirstName": "Mary",
    "Address": {
        "Street": "123 Main",
        "City": "Anytown",
        "State": "OH",
        "ZIPCode": 12345
    }
}

{
    "PersonID": 103,
    "LastName": "Stephens",
    "FirstName": "Howard",
    "Address": {
        "Street": "123 Main",
        "City": "London",
        "PostalCode": "ER3 5K8"
    },
    "FavoriteColor": "Blue"
}
```

### Streams

Captures data modification events (add, delete, modify) in near real-time in DynamoDB table. Stream records have a lifetime of 24h. You can combine it with AWS Lambda to create a trigger.

## Amazon DynamoDB Accelerator (DAX)

Amazon DAX is a distributed in-memory cache for DynamoDB to improve read performance. It maintains a cluster of nodes for high availability, replicating data across multiple nodes to handle node failures and provide automatic failover. It can also integrate with EC2 and Lambda.

DAX maintains strong consistency by updating the cache in real-time as data is written to the DynamoDB table.

### IAM

DAX maintains its independent group of IAM policies than services using DAX to access the database and hence, you need to be mindful. For example:

- EC2 does not have access to DynamoDB table called 'books'
- DAX has access to 'books'
- If an EC2 uses DAX, it will have access to 'books'
