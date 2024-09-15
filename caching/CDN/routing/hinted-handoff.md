## Hinted handoff

Hinted handoff is used by distributed systems to improve reliability and resiliency in the eventual consistency model, and is used by distributed databases such as Cassandra and Amazon Dynamo.

Nonetheless, it can also be used in CDN to redirect the traffic to the targeted healthy nodes once they have fully recovered and regained healthy status. The hints accumulated by the backup nodes are then conveyed to the target node.

Networking protocols like the gossip protocol is utilized to identify instances of node failures within the system.
