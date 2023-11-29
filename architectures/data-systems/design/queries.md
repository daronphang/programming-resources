## OLTP and OLAP

One solution for designing a database to serve transactional and analytical queries is to use two separate databases for each purpose. An OLTP will have short data retention (critical), while an OLAP will have longer data retention.

From a stability POV, OLTP database will serve as the single source of truth, and any failure in OLAP will not affect OLTP.

For eventual consistency, can use data ingestion pipeline. Writes are performed to OLTP, while data is pushed asynchronously to data ingestion pipeline to ensure OLAP data is eventually consistent with OLTP.
