## Cache cluster collaborative interaction

The main goal of the internal collaborative interaction of the cache server cluster is to establish a good communication channel between each server node to communicate the content cache situation on the server in a timely manner, and to provide users with a good service experience through cooperation between servers in the cluster.

Communication between cache server clusters can be divided into two categories:

- Loose coupling: ICP, HTCP, Cache Digest, Cache Pre-filling, etc.
- Tight coupling: HARP

### ICP (Internet Cache Protocol)

RFC 2186 ICP defines a lightweight message format used to query web resource information between cache servers to determine whether the requested resource exists on other servers. The server that receives the query request provides either a "hit" or "miss" response.

ICP is generally implemented based on UDP protocol i.e. ICP over UDP. Nonetheless, ICP must also consider the security issues brought by UDP protocol.

### HTCP (Hypertext Caching Protocol)

HTCP is a protocol used to discover HTTP cache servers and cache data, defined in RFC 2756. It can manage a group of HTTP cache servers and monitor related caching activities.

The operation mechanism of HTCP is similar to ICP, which reflects the caching situation of web objects in the cluster by sending query requests to neighboring servers and obtaining responses. However, unlike ICP v2, which can only contain the URI of web objects, HTCP requests and responses **can contain complete HTTP header information**, which enables HTCP to make more accurate responses when subsequent HTTP requests need to access the same resources. In addition, HTCP adopts a variable-length message format and extends cache management functions, such as monitoring the addition and deletion of remote caches, requesting immediate deletion, and sending web object prompts.

HTCP messages can be transmitted through UDP packets or TCP connections. UDP packets must be supported, while TCP protocol is mainly used for protocol debugging.

### Cache Digest

The appearance of Cache Digest is mainly to solve the network latency and congestion problems in the use of ICP and HTCP protocols. Cache Digest does not use the in-band query method based on the request-to-answer pattern, but establishes a **peer relationship between servers** i.e. each cache server saves the cache information digest of all its neighbors. When receiving a user's request, Cache Digest directly retrieves the local cache content digest and learns whether the object is available in a neighbor cache.

Compared to ICP and HTCP, Cache Digest is actually a way of exchanging space for time. For Cache Digest, the selection of the digest algorithm is particularly important. Considering the transmission delay and storage overhead of the digest file, the size of the digest file should be as small as possible, but this may also lead to a decrease in query accuracy. The choice of algorithm is a balancing issue.

When using Cache Digest, special consideration should be given to security issues e.g. malicious tampering of summary files. To reduce this risk, it can be considered to only allow the server to actively obtain summary files from other servers using the **pull method**, rather than passively receiving summary files "pushed" by other servers.

### Cache Pre-filling

Cache Pre-filling is a mechanism for pushing cache content, which can be well applied in IP multicast networks. It enables pre-selected resources to be simultaneously inserted into all cache servers in the target multicast group, thus achieving synchronization of content storage among various servers in the cluster.

Currently, Cache Pre-filling technology has been widely implemented, especially in satellite communication scenarios. Its biggest advantage is that it can simultaneously transmit large-capacity data to multiple distributed ground satellite receivers at high speed, greatly improving the data access experience when the network transmission speed is not high. However, there is still a lack of unified standards for Cache Pre-filling.

### CARP (Cache Array Routing Protocol)

CARP is essentially a distributed caching protocol that is used to divide the URL space of a cache server cluster by establishing a hash function. The core of CARP is to define a cache server array member table for the cluster and a hash function for distributing cached URL information to the cache server i.e. similar to consistent hashing. The array member table is saved in each server.

CARP accurately routes user requests for URLs to any member of the server array through a hash algorithm, eliminating duplicate cache data in the array and achieving efficient positioning of cache resources. Because there is no need to consider more irreversibility and encryption requirements, the algorithm used by CARP is very simple and has extremely high performance.

Advantages of CARP compared to loose-coupling communication methods are:

- No need for resource query request and response process, avoiding network impact and reducing transmission overhead
- Eliminated duplicate cached data, keeping only one copy of each URL content in the system, saving space
- It has better scalability because there is no need to interact with many other cache servers
- Server nodes can be flexibly added or deleted, and the application of hashing algorithm can minimize the impact of data distribution caused by changes in the number of nodes
- It can ensure that all URL data can be effectively cached in the system
- CARP always returns the same server list for a given host name, ensuring that content from all URLs containing the same host name is cached on one array server
