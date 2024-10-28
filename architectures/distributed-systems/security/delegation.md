## Delegation

Delegation of access rights is an important technique for implementing protection in computer systems and distributed systems. The basic idea is simple: by passing certain access rights from one process to another, it becomes easier to distribute work between several processes without adversely affecting the protection of resources. In the case of distributed systems, processes may run on different machines and even within different administrative domains. Delegation can avoid much overhead, as protection can often be handled locally.

## Implementation

### Passing user credentials

The least favorable one is to hand over the user credentials directly to an application. However, doing so is a bad idea.

### Proxy

A much better and general approach is to use a proxy. A proxy in the context of security in computer systems is a token that allows its owner to operate with the same or restricted rights and privileges as the subject that granted the token. A process (or user for that matter) can create a proxy with at best the same rights and privileges it has itself. If a process creates a new proxy based on one it currently has, the derived proxy will have at least the same restrictions as the original one, and possibly more.
