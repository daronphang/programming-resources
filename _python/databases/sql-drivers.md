## Python (pyodbc/pymssql)

|                        | pyodbc                                                                                                                                  | pymssql                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Details                | Under active development and has Microsoft support contributing to bug fixes and new features that relate accessing Microsoft products. | Lost momentum and was discontinued in Nov 2019.                                       |
| Parameter Substitution | Performs on server side and impossible to retrieve logs.                                                                                | Performs on client side and allows developers to log actual query sent to SQL Server. |
| Features               | executemany                                                                                                                             | does not offer executemany                                                            |
