## JDBC Statemenets

You use the JDBC Statement to execute SQL statements, obtain results, and deal with errors.

### Execute

```
executeQuery()      For SELECT statements
executeUpdate()     Returns a count of the rows that were affected
```

### ResultSet

When inspecting an individual row, you can use various accessor methods for various types i.e. getString(), getDouble(). Each accessor has two forms:

- Numeric argument that refers to the column i.e. 1 refers to the first column
- String argument that refers to the column name

Each get() makes reasonable type conversions when the type of the method doesn't match the type of the column.

```java
Statement stat = conn.createStatement();
ResultSet rs = stat.executeQuery("SELECT * FROM Books");
while (rs.next()) {
    // look at a row of the result set
    String isbn = rs.getString(1);
    double price = rs.getDouble("Price");
}
```

### Managing Connections, Statements and Result Sets

Though every Connection object can create one or more Statement objects, some drivers only allow one active statement at a time.

When you are done using a ResultSet, Statement, or Connection, you should call close(). Conversely, as of Java SE7, you can call closeOnCompletion() on a Statement, and it will close automatically as soon all its result sets have closed.

Use the try-with-resources block to close the connection, and a separate try/catch block to handle exceptions.

```java
try (Connection conn = . . .) {
    Statement stat = conn.createStatement();
    ResultSet result = stat.executeQuery(queryString);
    // process query result
}
```

### SQL Exceptions

Each SQLException has a chain of SQLException objects that are retrieved with the getNextException(). Fortunately, Java SE6 enhanced the SQLException class to implement the `Iterable<Throwable>` interface.

```java
for (Throwable t : sqlException) {
    do something with t
}
```

### Prepared Statements

Each host variable in a prepared query is indicated with a ?. Before executing, you must bind the host variables to actual values with set(). The first argument is the position number of the host variable, and the second argument is the value to assign.

If you reuse a prepared query that you have already executed, all host variables stay bound unless you change them with set(), or call clearParameters().

```java
String publisherQuery =
    "SELECT Books.Price, Books.Title" +
    " FROM Books, Publishers" +
    " WHERE Books.Publisher_Id = Publishers.Publisher_Id AND Publishers.Name = ?";
PreparedStatement stat = conn.prepareStatement(publisherQuery);
stat.setString(1, publisher);
```
