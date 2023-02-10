## Python (pyodbc/pymssql)

|                        | pyodbc                                                                                                                                  | pymssql                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Details                | Under active development and has Microsoft support contributing to bug fixes and new features that relate accessing Microsoft products. | Lost momentum and was discontinued in Nov 2019.                                       |
| Parameter Substitution | Performs on server side and impossible to retrieve logs.                                                                                | Performs on client side and allows developers to log actual query sent to SQL Server. |
| Features               | executemany, connection pooling (turned on by default)                                                                                  | does not offer executemany, connection pooling through SQLAlchemy                     |

## Pooling

For pyodbc, pooling is enabled by default, and can only be modified before the first connection is made.

Connection is drawn from the pool when connect() is called i.e. create the class normally.

```py
import pyodbc

pyodbc.pooling = False
conn = pyodbc.connect(db_connection_string)
conn.close()
```

```py
import pyodbc as p

class MsSqlSession:
    def __init__(self, config):
        self.conn = p.connect(driver="{ODBC Driver 17 for SQL Server}", **config)

    def __enter__(self):
        return self.conn    # conn is drawn from pool

    def __exit__(self, exc_type, exc_value, traceback):
        # although python auto closes when it goes out of scope
        self.conn.close()

```

```py
# checking conn pooling is enabled
# by using SPID
# when compared between pyodbc and mymsql, results are different

conn = p.connect()
cursor = conn.cursor()
cursor.execute('SELECT @@SPID')
print(cursor.fetchall())
cursor.close()
conn.close()

# pyodbc
# ('144',)
# ('144',)
# ('144',)

# pymssql
# ('98',)
# ('455',)
# ('203',)
```

## ODBC for Linux

https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16

### Microsoft

### FreeTDS

A Set of libraries for Linux that allows your programs to natively talk to Microsoft SQL Server and Sybase.

```console
$ apt install tdsodbc unixodbc
$ echo "[FreeTDS]\n\
Description = FreeTDS Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini
```
