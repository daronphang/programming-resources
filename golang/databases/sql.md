## database/sql

To access databases in Golang, use sql.DB. It is an abstraction of the interface and existence of a database, which might be varied as a local file, accessed through a network connection, or in-memory and in-process.

The abstraction is designed to keep you from worrying about how to manage concurrent access to the underlying database. Once it is not in use anymore, it is returned to the available pool. One consequence is that **if you fail to release connections back to the pool, can cause sql.DB to open a lot of connections and limiting resources i.e. too many open connections, network ports, file handlers, etc.**

sql.DB performs the following:

- Opens and closes connections to the actual underlying database, via the driver.
- Manages a pool of connections as needed.

### DSN/Connection string

```
username:password@protocol(address)/dbname?param=value
```

### Connection pool

```
db.SetMaxIdleConns(N)				Doesn't limit pool size
db.SetMaxOpenConns(N)
db.SetConnMaxLifetime(duration)		Max time a conn can be reused
```

## Database driver

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

## Accessing the database

sql.Open() does not establish any connections to the database, but simply prepares the DB abstraction for later use. Use db.Ping() to check if the DB is available and accessible.

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

- Executing two consecutive statements on a single DB might open two connections and executed separately
- Connections are recycled fast and setting a high number of idle connections can reduce this churn, and helps keep connections around for reuse

## Managing database connection

For vast majority of programs, do not need to adjust sql.DB connection pool defaults. From Golang docs, DB handle is meant to be long-lived and shared between many goroutines.

Hence, do not have to worry about closing the connection i.e. defer DB.Close(). Instead, keep DB connection pool established after first successful connection. Opening and closing DB for each API request is a waste of resources.

For customization, can set connection pool properties such as number of open connections, idle connections, etc.

https://go.dev/doc/database/manage-connections

```go
func main() {
	var appCfg configs.EnvConf
	appCfg.Read()
	log.Println("initializing web application")

	// db connection should be kept opened as connection pool
	// opening and closing for each api request is a waste of resources
	db, err := dblayer.SFConn(appCfg)
	if err != nil {
		log.Println("unable to establish DB connection with Snowflake")
		return
	}
	log.Println("Snowflake DB connection pool established")
	log.Fatal(rest.RunApp("127.0.0.1:8082", appCfg, db))
}
```

```go
type DBConnection struct {
	*sql.DB
}

func SFConn(conf configs.EnvConf) (*DBConnection, error) {
	cfg := &sf.Config{
		Account:   conf.Account,
		User:      conf.User,
		Password:  conf.Password,
		Region:    conf.Region,
		Warehouse: conf.Warehouse,
	}
	dsn, err := sf.DSN(cfg)
	if err != nil {
		return nil, err
	}
	db, err := sql.Open("snowflake", dsn)
	if err != nil {
		return nil, err
	}

	_, err = db.Exec(fmt.Sprintf("CALL PROD_EPM_DM.UTIL_USER.UPD_PROXY_USER('%s')", conf.SFProxy))
	return &DBConnection{
		DB: db,
	}, err
}
```

```go
func DatabaseConnector (db *dblayer.DBConnection) gin.HandlerFunc {
	return func(c *gin.Context) {
		// pinging DB connection before each request
		if err := db.Ping(); err != nil {
			c.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{
				"error": "database connection error",
				"message": err.Error(),
			})
			return
		}
		c.Set("db", db)
		c.Next()
	}
}
```
