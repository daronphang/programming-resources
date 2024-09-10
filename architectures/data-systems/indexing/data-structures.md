## Hash indexes (log-structured)

Similar to dictionary which is implemented as a hash map. Every append to the storage file will update the hash map to reflect the offset of the data you wrote. When updating a key, it will append to files and delete obsolete files but never modify them in place.

To ensure disk space doesn't run out, a solution would be to break the log into segments (log-structured) of a certain size by closing it once it reaches, and making subsequent writes to a new segment file.

## B-Trees

They remain the standard index implementation in almost all relational databases, and many non-relational use them too. B-trees keep key-value pairs sorted by key, which allows efficient key-value lookups and range queries.

B-trees break the database down into fixed-size blocks/pages, and read/write one page at a time. This design corresponds more closely to the underlying hardware, as disks are also arranged in fixed-size blocks.

Each page can be identified using an address or location, which allows one page to refer to another i.e. a pointer, but on disk instead of in-memory. Individual keys are also called **leaf page**, which contains the value for key inline. The number of references to child pages in one page is called the **branching factor**.

### Reliability

To make the database resilient to crashes, it is common for B-tree implementations to include an additional data structure on disk known as **write-ahead log**. This an append-only file to which every modification must be written before it can be applied to the pages of the tree itself. This log is used to restore the B-tree back to a consistent state. However, this means every data must be written at least twice: once to the B-tree and write-ahead log.
