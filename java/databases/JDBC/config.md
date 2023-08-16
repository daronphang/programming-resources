## Configuration

### Database URLs

When connecting to a database, you must use various database-specific parameters such as host names, port numbers, and database names.

```
jdbc:subprotocol:other stuff
jdbc:derby://localhost:1527/COREJAVA;create=true
jdbc:postgresql:COREJAVA
```

### Driver JAR Files

You need to obtain the JAR file in which the driver for your database is located.

```bash
$ java -classpath driverPath:. ProgramName
```

### Registering Driver Class

There are two ways to register the driver with the DriverManager:

1. Load the driver class in your Java program

```java
Class.forName("org.postgresql.Driver"); // force loading of driver class
```

2. Set the jdbc.drivers property by using command-line or in the java program

```bash
$ java -Djdbc.drivers=org.postgresql.Driver ProgramName
```

```java
System.setProperty("jdbc.drivers", "org.postgresql.Driver");
```

### Connecting to the Database

```java
String url = "jdbc:postgresql:COREJAVA";
String username = "dbuser";
String password = "secret";
Connection conn = DriverManager.getConnection(url, username, password);
```

## Example

```java
public static void runTest() throws SQLException, IOException {
    try (
        Connection conn = getConnection();
        Statement stat = conn.createStatement()
    ) {
        stat.executeUpdate("CREATE TABLE Greetings (Message CHAR(20))");
        stat.executeUpdate("INSERT INTO Greetings VALUES ('Hello, World!')");

        try (ResultSet result = stat.executeQuery("SELECT * FROM Greetings")) {
            if (result.next())
            System.out.println(result.getString(1));
        }
        stat.executeUpdate("DROP TABLE Greetings");
    }
}

public static Connection getConnection() throws SQLException, IOException {
    Properties props = new Properties();
    try (InputStream in = Files.newInputStream(Paths.get("database.properties"))) {
        props.load(in);
    }
    String drivers = props.getProperty("jdbc.drivers");
    if (drivers != null) System.setProperty("jdbc.drivers", drivers);
    String url = props.getProperty("jdbc.url");
    String username = props.getProperty("jdbc.username");
    String password = props.getProperty("jdbc.password");
    return DriverManager.getConnection(url, username, password);
}
```
