## Checksum

In a distributed system, while moving data between components, it is possible that the data fetched from a node may arrive corrupted. This corruption can occur because of faults in a storage device, network, software, etc.

To ensure data integrity and that the client doesn't receive corrupted data, we can **calculate a checksum** and store it with data. A checksum comprises a sequence of bytes to form a digital fingerprint for data. If there is a change in any data, however minute, it modifies the checksum completely.

To calculate a checksum, a cryptographic hash function like MD5, SHA-1, SHA-256, or SHA-512 is used. The hash function takes the input data and produces a string (containing letters and numbers) of fixed length; this string is called the checksum.

If you know the checksum of the original data, you can run a checksum or hashing utility on it. If the resulting checksum matches, the data is not corrupted.
