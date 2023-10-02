## AWS Migration Hub

AWS Migration Hub is a service that helps plan and track application migrations. Migration Hub does not perform system migrations.

## AWS Application Migration Service (MGN)

AWS MGN is an automated lift-and-shift solution. This solution can migrate physical servers and any databases or applications that run on them to EC2 instances in AWS.

## AWS Application Discovery Service

AWS Application Discovery Service collects information about the usage and configuration of on-premises servers to help plan a migration to AWS. Application Discovery Service does not actually perform migration operations.

## Database Migration Service (DMS)

DMS migrates databases (relational, nonrelational) to AWS in a quick, secure, and resilient manner.

With AWS DMS, you move data between a source database and a target database. They both can be of the **same type (homogenous) or different types (heterogeneous)**. During migration, your source database remains operational.

Use cases include:

- Enabling developers to test applications against production data without affecting production users
- Combining several databases into a single database
- Sending ongoing copies of data to other target sources (replication)

## AWS DataSync

Moves large amount of data from on-premises to AWS. The replication tasks are **incremental** after the first full load.
