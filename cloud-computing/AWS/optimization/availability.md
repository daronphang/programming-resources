## Availability

The availability of a system is typically expressed as a percentage of uptime in a given year i.e. 90%, 99.995%, etc.

### Active-Passive

with an active-passive system, only one of the two instances is available at a time. There is data replication between the active and passive Regions, and possibly do reads from passive.

This is useful for stateful applications i.e. storing client's session. However, this system is not scalable.

### Active-Active

Both servers are available and hence, can perform load balancing. Works better for stateless applications.
