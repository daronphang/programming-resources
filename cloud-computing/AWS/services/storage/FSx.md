## Amazon FSx

Amazon FSx provides native compatibility with **third-party file systems** (alternative to EFS). With Amazon FSx, you don't need to worry about managing file servers, storage, replicating data, patching file servers, etc. This is because Amazon FSx automates time consuming administration task such as hardware provisioning, software configuration, patching, and backups.

### Benefits

- Provides storage
- Managed service
- Scalable
- Shared access
- Performs backup

## Flavors

All flavors support multi-AZ deployments, but Lustre supports only single AZ.

### Windows File Server

- Supports Server Message Block (SMB) protocol
- Easily integrate it with Microsoft Active Directory for authentication
- Supports data deduplication
- Setting quotas
- Compatible with Windows, Linux and macOS

### Lustre (Linux and Cluster)

- Lustre is a fully managed, high-performance, scalable file storage for **High Performance Computing (HPC)**
- Provides low-latency, high throughput access to data
- Built on the Lustre file system
- Usage includes for machine learning, scientific computing, analytics, video processing, financial modelling, etc.
- Integrates seamlessly with other AWS services e.g. S3, DataSync, AWS Batch
- Can easily scale the file system's capacity and throughput
- Single AZ deployment only

### NetAPP ONTAP

- Offers high-performance storage that's accessible from Linux, Windows, and macOS via NFS, SMB and iSCSI protocols
- Scales up or down in response to workload demands
- Performs snapshots, clones, replications, etc.

### OpenZFS

- Built on top of the open-source OpenZFS file system
- Supports access from Linux, Windows and macOS vis NFS protocol
- Utilizes power from OpenZFS capabilities including data compression, snapshots, and data cloning
- Offers built-in data protection and security features
