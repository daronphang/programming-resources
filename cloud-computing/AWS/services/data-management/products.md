## AWS Lake Formation

Managing and scaling data access is complex and time consuming. Lake Formation helps to centrally govern, secure and share data for analytics and machine learning, for both across your organization and externally. It is a **centralized repository** for storing large volumes of structured, semi-structured, and unstructured data.

Lake Formation is an aggregator for disparate data sources into a standardized data format that you can use Glue or other transformation services on top of i.e. ingestion -> storage (S3) -> processing (AWS Glue).

Data can be stored in its original format (csv), Parquet or Orc (flat files optimized for data analytics).

Lake Formation has built-in audit logging, and supports cell and row-level security through granular access policies. It also allows the use of resource tags to control access i.e. access policies are applied based on tags.

### Architecture

- Storage: S3
- Data catalog: Glue
- Analysis: Athena, RedShift

### Features

- Simplified data lake creation
- Centralized data access control
- Data cleaning with built-in ML algorithms to deduplicate data
- Cross-region data replication

### How it works

1. Ingest data from various data sources including S3, databases
2. Crawl data to understand schema using AWS Glue Crawlers
3. Clean data using ETL such as AWS Glue
4. Analyze data using integrated analytical engines such as Athena, Glue, RedShift

### Permissions

AWS Lake Formation provides a RDBMS permissions model to grant or revoke access to Data Catalog resources such as databases, tables, and columns with underlying data in Amazon S3. The easy to manage Lake Formation permissions replace the complex Amazon S3 bucket policies and corresponding IAM policies.

1. A user submits query or an ETL script to an **integrated analytical engine** such as Athena, Glue, RedShift
2. The Data Catalog checks user's permissions with Lake Formation
3. If the user is authorized to access the table, Lake Formation provides temporary access to the integrated analytical engine

### Data lake vs warehousing

- A data warehouse is a database optimized to analyze relational data
- A data lake stores both relational and non-relational data

## Amazon Athena

Amazon Athena is a **serverless query service** to perform analytics against **S3 objects**. Uses data crawler (data catalog) underneath to structure and keep track of it. Uses standard SQL language to query the files against unstructured data that have been structured as part of the ingestion process.

Athena can be used to look perform adhoc query into data that is not actively loaded in a database which is the cheapest and fastest. Dashboards are then used to visualize the data.

### Features

- Serverless
- Built-in functions and partitioning
- Standard SQL and UDF
- Support for various data formats and drivers e.g. Parquet, JSON, CSV, ODBC drivers

## Amazon QuickSight

Amazon QuickSight is a serverless machine learning-powered business intelligence service to create interactive/visual dashboards of analytics data.

### SPICE

Stands for Super-fast, Parallel, In-memory Calculation Engine:

- Provides QuickSight with high-speed data processing for responsive dashboards
- Stores large datasets in-memory
- SPICE datasets can refresh automatically to ensure data on dashboards remains up to date
- SPICE engine scales seamlessly with data volume
- Encryption at rest
- Supports QuickSight Q for natural language querying and ML-driven insights

### Features

- Serverless and fully-managed
- SPICE engine
- Interactive dashboards
- Data preparation and ML insight
