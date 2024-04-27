## sqlc

sqlc is an SQL compiler bundled as an executable binary file and can generate type-safe code for your raw SQL schema and queries. So, you don’t have to write any boilerplate code other than your actual SQL statements.

### Features

- Query annotations: Various annotations that allow you to define the name of the function for each query and the type of result expected from the query; used during code generation to determine the name and signature of the function
- JSON tags: Supports the generation of JSON tags for structs or types that will be marshaled and sent to clients as JSON
- Schema modifications: Support for reading various formats of migration files to modify schema and generate code to reflect those changes
- Struct naming: Provides options for naming schemas used to generate struct names from table names

## Code generation

```sql
CREATE TABLE authors (
  id   BIGSERIAL PRIMARY KEY,
  name text      NOT NULL,
  bio  text
);

-- name: CreateAuthor :one
INSERT INTO authors (
  name, bio
) VALUES (
  $1, $2
)
RETURNING *;
```

```sh
$ sqlc generate
```

```go
author, err = dbsqlc.New(tx).CreateAuthor(ctx, dbsqlc.CreateAuthor{
    Name: "Haruki Murakami",
    Bio:  "Author of _Killing Commendatore_. Running and jazz enthusiast.",
    ...
})

if err != nil {
    return nil, xerrors.Errorf("error creating author: %w", err)
}

fmt.Printf("Author name: %s\n", author.Name)
```

### Naming parameters

When using named parameters, ensure that you renumber the params.

```sql
SELECT
time_bucket(@time_bucket::text, created_at) AS bucket,
AVG(metric1) AS metric1
FROM machine_resource_usage
WHERE machine = $1  -- Cannot be $2
AND created_at > NOW() = INTERVAL @look_back_period::text
```
