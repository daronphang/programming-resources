## Database/SQL

To access databases in Golang, use sql.DB. It is an abstraction of the interface and existence of a database, which might be varied as a local file, accessed through a network onnection, or in-memory and in-process.

The abstraction is designed to keep you from worrying about how to manage concurrent access to the underlying database. Once it is not in use anymore, it is returned to the available pool. One consequence is that **if you fail to release connections back to the pool, can cause sql.DB to open a lot of connections and limiting resources i.e. too many open connections, network ports, file handlers, etc.**

sql.DB performs the following:

- Opens and closes connections to the actual underlying database, via the driver.
- Manages a pool of connections as needed.

### Database Driver

Requires both database/sql and a driver for the specific database. Shouldn't use driver packages directly to allow changing drivers with minimal code changes i.e. empty import.

```go
import (
	"database/sql"
	_ "github.com/go-sql-driver/mysql"  // shouldnt use driver packages directly
)


func main() {
	db, err := sql.Open("mysql",
		"user:password@tcp(127.0.0.1:3306)/hello")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()
}
```

### Accessing the Database

sql.Open() does not establish any connections to the databaese, but simply prepares the DB abstraction for later use. Use db.Ping() to check if the DB is available and accessible.

For Golang, **the sql.DB object is designed to be long-lived**, and shouldn't open and closeDB frequently. Instead, create one DB object for each distinct database and keep it until the program is done i.e. make it available globally and keep it open.

If you don't treat sql.DB as a long-lived object, could experience problems such as poor reuse and sharing of connections, running out of resources, etc. Nonetheless, it is idiomatic/appropriate to defer closing DB if it should not have a lifetime beyond the scope of the function.

```go
func main() {
	// db is of type *sql.DB
	db, err := sql.Open("mysql",
		"user:password@tcp(127.0.0.1:3306)/hello")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		// do something here
	}
}
```

### Connection Pool

```
db.SetMaxIdleConns(N)				Doesn't limit pool size
db.SetMaxOpenConns(N)
db.SetConnMaxLifetime(duration)		Max time a conn can be reused
```

- Executing two consecutive statements on a single DB might open two connections and executed separately.
- Connections are recycled fast and setting a high number of idle connections can reduce this churn, and helps keep connections around for reuse.
