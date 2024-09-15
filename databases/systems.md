## Online Transaction Processing (OLTP)

OLTP is a technique used for detailed day-to-day transactions of data which continuously chain on an everyday-basis. Main features include controlled insertion and updating of data with effective access to data manipulation and viewing mechanisms.

OLTP is used for interactive applications that are expected to be highly available, with read and write operations processing with low latency i.e. **makes data management simple and efficient, and serves real-time transactions**. Hence, OLTP databases are often closely guarded and administrators are reluctant to run adhoc queries as they are often expensive and can harm performance of concurrently executing transactions.

## Data warehousing

A data warehouse is a separate database that analysts can query to their hearts' content, without affecting OLTP operations. The warehouse maintains a read-only copy of the data in all the various OLTP systems in the company.

Data is extracted from OLTP databases using either a periodic data dump or a continuous stream of updates, transformed into an analysis-friendly schema, cleaned up, and then loaded into the data warehouse **(also known as ETL or Extract-Transform-Load)**.

Data model of a warehouse is most commonly relational as SQL is a good fit for analytic queries. On the surface, a data warehouse and relational OLTP database look similar as they both have a SQL query interface, but the internals of the systems can be different as they are optimized for different query patterns.
