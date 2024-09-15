## Database cursor

A database cursor is an identifier associated with a group of rows. It is a pointer to the current row in a buffer.

You must use a cursor in the following cases:

- Statements that return more than one row of data from the database server i.e. SELECT
- An EXECUTE FUNCTION statement requires a function cursor
- An INSERT statement that sends more than one row of data to the database server requires an insert cursor
