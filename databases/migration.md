## Database migrations

### Dirty database

Before a migration runs, each database sets a dirty flag. Execution stops if a migration fails and the dirty state persists, which prevents attempts to run more migrations on top of a failed migration. You need to manually fix the error, remove previous migrations (if any) and then "force" the expected version.

```sql
SELECT * FROM schema_migrations;
DELETE FROM schema_migrations WHERE version = 1;
```
