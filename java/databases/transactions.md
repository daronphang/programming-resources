## Transactions

You can group a set of statements to form a transaction. The major reason for grouping statements into transactions is **database integrity**.

By default, a database connection is in autocommit mode, and each SQL statement is committed to the database as soon as it is executed. Once a statement is committed, you cannot rollback.

```java
conn.setAutoCommit(false);
try (Statement stat = conn.createStatement()) {
    stat.executeUpdate(command1);
    stat.executeUpdate(command2);
    stat.executeUpdate(command3);
    conn.commit();
} catch SQLException {
    conn.rollback();
}
```

### Save Points
