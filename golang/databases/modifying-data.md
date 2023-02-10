## Exec

Use Exec(), preferably with a prepared statement, to accomplish an INSERT, UPDATE, DELETE or another statement that doesn't return rows.

**Do not use Query()** as it reserves a DB connection until it is closed. Although the garbage collector will eventually close the underlying net.Conn, might take a long time and considered an anti-pattern.

Executed statement produces a sql.Result that gives access to metadata: last inserted ID and number of rows affected.

```go
stmt, err := db.Prepare("INSERT INTO users(name) VALUES(?)")

_, err := db.Prepare("INSERT INTO users(name) VALUES(?)")   // when result is not important

if err != nil {
	log.Fatal(err)
}
res, err := stmt.Exec("Dolly")
if err != nil {
	log.Fatal(err)
}
lastId, err := res.LastInsertId()
if err != nil {
	log.Fatal(err)
}
rowCnt, err := res.RowsAffected()
if err != nil {
	log.Fatal(err)
}
log.Printf("ID = %d, affected = %d\n", lastId, rowCnt)
```

### Prepare

Multiple queries or executions can be run concurrently from the returned statement i.e. can execute the same SQL repeatedly. Must call Close method when the statement is no longer needed.

```go
func main() {
	projects := []struct {
		mascot  string
		release int
	}{
		{"tux", 1991},
		{"duke", 1996},
		{"gopher", 2009},
		{"moby dock", 2013},
	}

	stmt, err := db.Prepare("INSERT INTO projects(id, mascot, release, category) VALUES( ?, ?, ?, ? )")
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close() // Prepared statements take up server resources and should be closed after use.

	for id, project := range projects {
		if _, err := stmt.Exec(id+1, project.mascot, project.release, "open source"); err != nil {
			log.Fatal(err)
		}
	}
}
```

## Transactions

In Go, a transaction is essentially an object that reserves a connection to the datastore. Guarantees that they will be executed on the same connection.

Should not use transaction-related functions such as Begin() and Commit() with SQL statements BEGIN and COMMIT as it might cause the connection to remain open, and state of DB could get out of sync.

Inside a transaction, make all calls to the Tx variable and not the db variable. If you make further calls to db.Exec(), they will happen outside the scope of the transaction, on other connections.

To use a prepared statement outside of the transaction, use Tx.Stmt(). This will take an existing prepared statement, set the connection to that of the transaction, and repreparing all statements every time they are executed. However, **this is not advised**.

```go
tx, err := db.Begin()
if err != nil {
	log.Fatal(err)
}
defer tx.Rollback()
stmt, err := tx.Prepare("INSERT INTO foo VALUES (?)")
if err != nil {
	log.Fatal(err)
}
defer stmt.Close()
for i := 0; i < 10; i++ {
	_, err = stmt.Exec(i)
	if err != nil {
		log.Fatal(err)
	}
}
err = tx.Commit()
if err != nil {
	log.Fatal(err)
}
```
