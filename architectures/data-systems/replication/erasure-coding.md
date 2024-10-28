## Erasure coding

Erasure coding is an important optimization technique used in data protection and data storage that distributes redundant information across multiple storage nodes, allowing the system to recover from the loss of data **without the need for a complete copy** of each piece. This is useful for blob storage.

Unlike traditional replication where copies of the same data are stored on separate nodes, providing redundancy at the cost of increased storage requirements, erasure coding uses mathematical algorithms to create parity or redundant pieces of data that are distributed across different storage locations. This method significantly reduces storage overhead compared to replication.

### How it works

Erasure coding works by breaking down data into fragments and generating additional pieces called erasure codes. These fragments and codes are distributed across storage nodes in a process that involves complex mathematical calculations, ensuring that the original data can be reconstructed even if some fragments or codes are lost or corrupted.

## Benefits

### Improved fault tolerance

In a storage system using erasure coding, data can be reconstructed even if a certain number of storage nodes become unavailable or experience data loss. This makes erasure coding particularly valuable in distributed storage environments where hardware failures or network issues are common.

### Reduced storage overhead

Compared to traditional replication methods, erasure coding offers significant reductions in storage overhead. By distributing parity or erasure codes across multiple nodes, it achieves redundancy without the need for full data replication. This not only saves storage space but also contributes to cost savings in large-scale storage systems.

## Algorithms

### Reed-Solomon

With Reed-Solomon encoding, adding m additional checksum blocks to n original data blocks allows recovery from up to m losses of data or checksum blocks. This reduces the storage overhead required to tolerate m failures from m to (m + n)/n times the file size. By fragmenting a file into a large number of data blocks, the storage overhead for availability can be made very small.

## Fragmentation

Independent of the encoding, storing fragments of a file at separate nodes (and thereby striping the file over several disks) can also improve bandwidth. However, these potential benefits must be weighed against the cost (in terms of latency, aggregate query and network load, and availability) of contacting several nodes to retrieve a file. This cost may outweigh the benefits for all but **large files**.
