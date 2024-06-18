## Identifying specific database errors

Should identify based on error code instead of its string format. Mechanism varies between drivers and not part of database/sql itself.

```go
rows, err := db.Query("SELECT someval FROM sometable")

// not the best way
if strings.Contains(err.Error(), "Access denied") {
	// Handle the permission-denied error
}

// for MySQL
if driverErr, ok := err.(*mysql.MySQLError); ok { // Now the error number is accessible directly
	if driverErr.Number == 1045 {
		// Handle the permission-denied error
	}
}
```
