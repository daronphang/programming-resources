## Tunable consistency

You can define the consistency level of your read and write queries. Your choice comes down to the CAP theorem.

### Strong consistency

For a read-heavy system, it’s recommended to keep read consistency low because reads happen more often than writes. For a write-heavy system, keep write consistency low.

```
[read-consistency-level] + [write-consistency-level] > [replication-factor]
```

```sql
CONSISTENCY ALL;
SELECT * FROM learn_cassandra.users_by_country WHERE country='US';
```

### Eventual consistency

```sql
CONSISTENCY ONE;
SELECT * FROM learn_cassandra.users_by_country WHERE country='US';
```
