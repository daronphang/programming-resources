## sqlx

sqlx was created to extend the features of the standard library database package.

### Features

- Prepared statements with named parameters: Enable you to use the names of struct fields and map keys to bind variables in a prepared statement or query
- Struct scanning: Allows you to scan query results directly into structs for a single row without having to individually scan each field or column; supports scanning into embedded structs
- Select and Get: Convenient methods for handling queries expected to return multiple records or a single record into a slice of a struct or a single struct with no looping required
- Support for IN queries: Allows you to bind a slice of values as a single parameter to an IN query
- Named queries: Binds the names of struct fields to column names, avoiding the need for positional references to column names when assigning values to bindvars
- Error-free result sets: Result sets do not return with errors, which allows for chainable operations on returned results, such as scanning results directly into a struct

## Chaining

```go
var p Place
err := db.QueryRowx("SELECT city, telcode FROM place LIMIT 1").StructScan(&p)
```
