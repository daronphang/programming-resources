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

With some databases and drivers, you cain finer-grained control over rollback process by using save points. Creating a save point marks a point to which you can later return without having to abandon the entire transaction.

```java
Statement stat = conn.createStatement(); // start transaction; rollback() goes here
stat.executeUpdate(command1);
Savepoint svpt = conn.setSavepoint(); // set savepoint; rollback(svpt) goes here
stat.executeUpdate(command2);
if (. . .) conn.rollback(svpt); // undo effect of command2
...
conn.commit();
conn.releaseSavepoint(svpt);
```

### Batch Updates

You can improve the performance of the program by using a batch update. In a batch update, a sequence of statements is collected and submitted as a batch. The call to executeBatch() returns an array of the row counts for all submitted statements.

```java
Statement stat = conn.createStatement();
String command = "CREATE TABLE . . ."
stat.addBatch(command);
stat.addBatch(command);
int[] counts = stat.executeBatch();
```
