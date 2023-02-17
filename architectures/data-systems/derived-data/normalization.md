## Data Normalization

Data normalization is the process of reorganizing data within a database so that users can utilize it for further queries and analysis i.e. process of developing clean data. Process of reorganizing data into tables in such a way that the reuslts are always unambiguous and as intended.

This includes eliminating redundant (repetitive) and unstructured data and making data appear similar across all records and fields. Eliminates undesirable characteristics like insertion, update and deletion anomalies.

## Normal Forms

In most practical applications, normalization achieves its best in 3NF.

- 1NF (First Normal Form)
- 2NF (Second Normal Form)
- 3NF (Third Normal Form)
- BCNF (Boye-Codd Normal Form)
- 4NF (Fourth Normal Form)
- 5NF (Fifth Normal Form)
- 6NF (Sixth Normal Form)

### 1NF

- Contains two-dimensional tables with rows and columns
- Each table cell should contain a single value
- Each record needs to be unique
- All entries in any column must be of the same kind

### 2NF

Each column in a table that is not a determiner of the contents of another column (Primary Key) must itself be a function of the other columns in the table.

### 3NF

In 2NF, modifications are still possible as a change to one row in a table may affect data that refers to this information from another table. In this form, making additions or deletions to either table would not affect the other.

## Example

| Customer | Item purchased | Purchase price |
| -------- | -------------- | -------------- |
| Thomas   | Shirt          | $40            |
| Maria    | Tennis shoes   | $35            |
| Evelyn   | Shirt          | $40            |
| Pajaro   | Trousers       | $25            |

### 1NF

Add Customer_ID as Primary Key.

### 2NF

Purchase price is a function of the customer ID (entitled to a discount) and the specific product.

### 3NF

Table is split into two tables.

| Customer_ID | Customer | Item_Purchased |
| ----------- | -------- | -------------- |
| 1           | Thomas   | 1              |
| 2           | Maria    | 2              |
| 3           | Evelyn   | 1              |
| 4           | Pajaro   | 3              |

| Item_ID | Item         |
| ------- | ------------ |
| 1       | Shirt        |
| 2       | Tennis Shoes |
| 3       | Trousers     |
