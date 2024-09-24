## Push-based protocol

Origin servers proactively push content to edge servers before it is requested, ensuring faster delivery to users. This is suitable when **read-to-update ratio is relatively high** (static content), and when strong consistency is required.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push protocol. Content is placed on the cache servers once, instead of being re-pulled at regular intervals.

## Pull-based protocol

Edge servers fetch content from origin servers in real-time when requested by users, reducing storage requirements and ensuring freshness of content. This approach is efficient when **read-to-update ratio is relatively low** i.e. dynamic content.

Contrary to the Push protocol, this requires less maintenance because updates on cache nodes are performed based on requests from the client to the origin server. Sites with heavy traffic work well with pull protocol, as traffic is spread out more evenly with only recently-requested content remaining on the cache server.

## Leases

A lease is a promise by the server that it will push updates to the client for a specified time. When the lease expires, the client is forced to poll the server for updates and pull in the modified data if necessary.

Leases provide a convenient mechanism for **dynamically switching between a push-based and pull-based strategy**.

By combining leases and invalidations, the state to be maintained at the server can be kept within acceptable bounds.

## Unicasting vs multicasting

In unicast communication, when a server that is part of the data store sends its update to N other servers, it does so by sending N separate messages, one to each server. With multicasting, the underlying network takes care of sending a message efficiently to multiple receivers.

Multicasting can often be efficiently combined with a push-based approach to propagating updates. When the two are carefully integrated, a server that decides to push its updates to a number of other servers simply uses a single multicast group to send its updates. However, this approach requires the server to keep track of many proxies, inevitably leading to a scalability problem.

Unicasting may be the most efficient solution for pull-based approach, as generally only a single client requests its copy to be updated.
