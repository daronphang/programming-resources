## sqlcmd

Sqlcmd allows execution of transactional queries, stored procedures, and script files using the command line. This is useful when database servers are run in DMZs, and require SSH to establish a connection with the server.

### CLI

```bash
$ /opt/mssql-tools18/bin/sqlcmd \
-S "$HOST" \
-U "$USER" \
-P "$PASSWORD" \
-Q "UPDATE [ENGREQ].[dbo].[myassistant_pie_sff_to_por_quota] SET remaining_quota = quota;"
```
