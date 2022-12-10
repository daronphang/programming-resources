## Connection Pooling

Pooling ensures that a client does not constantly connect/disconnect from DB server by caching database connections.

Pooling opens a number of connections and handles thread safely when providing connections to requesters. Possible to have multiple connection pools, and enables applications to support pools of connections to different DB servers.

Can be created implicitly or explicitly.

Applications that can benefit from connection pooling capability include:

- Middleware that maintains multiple connections to multiple DB servers, and requires connections to be readily available.
- Websites that can have more "permanent" connections open to the DB server.

### Threading

Each thread should have their own DB connection to be threadsafe.

### MySQL

With either pool_name or pool_size (defaults to 5) argument present, connector creates the new pool. Subsequent calls to connect() that name the same connection pool returns connections from the existing pool.

When close() is called, the pooled connection is released and returned back to the pool (available for subsequent requests), but the connection is not closed.

```py
# implicit
dbconfig = {
  "database": "test",
  "user":     "joe"
}

cnx = mysql.connector.connect(
    pool_name = "mypool",
    pool_size = 3,
    **dbconfig
)
```

```py
# explicit
dbconfig = {
  "database": "test",
  "user":     "joe"
}
cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "mypool",
    pool_size = 3,
    **dbconfig
)

cnx1 = cnxpool.get_connection()
cnx2 = cnxpool.get_connection()

# reconfiguring pool connection
dbconfig = {
  "database": "performance_schema",
  "user":     "admin",
  "password": "password"
}

cnxpool.set_config(**dbconfig)
```
