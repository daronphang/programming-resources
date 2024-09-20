## Distributed systems

It is important to highlight the distinction between distributed and decentralized systems.

A decentralized system is a networked computer system in which processes and resources are **necessarily** spread across multiple computers e.g. distributed ledger, blockchain, federated learning. It takes on an integrative view of networked computer systems.

A distributed system is a networked computer system in which processes and resources are **sufficiently** spread across multiple computers e.g. CDN. It is mainly related to the expansive view of networked computer systems.

Both solutions are inherently difficult for the following reasons:

- There are many unexpected dependencies that hinder understanding the behavior of these systems
- Both systems suffer almost continuously from partial failures
- Both systems are highly dynamic, requiring forms of automated management and maintenance, in turn increasing complexity
- Both systems are networked and used by many users and applications; this makes them particularly vulnerable to security attacks

## Studying distributed systems

Considering that distributed systems are inherently difficult, it is important to take a systematic approach toward studying them. As there are so many explicit and implicit dependencies, an approach is to look at it from different perspectives including:

- Architectural perspective
- Process perspective
- Communication perspective
- Coordination perspective
- Naming perspective
- Consistency and replication perspective
- Perspective of fault tolerance
- Security perspective

## Design goals

Just because it is possible to build distributed systems does not necessarily mean that it is a good idea. There are a few important goals that should be met to make building a distributed system worth the effort.

### Resource sharing

An important goal of a distributed system is to make it easy for users (and applications) to access and share remote resources. Resources can be virtually anything e.g. peripherals, storage facilities, data files, services, networks, etc. Reasons for sharing resources include:

- Economics
- Easier to collaborate and exchange information

### Distributed transparency

An important goal of a distributed system is to hide the fact that its processes and resources are physically distributed across multiple computers, possibly separated by large distances. This is realized through using a **middleware**. Middleware layers are used to separate applications from underlying platforms.

What applications get to see is the same interface everywhere, whereas behind that interface, where and how processes and resources are and how they are accessed is kept transparent. Types of transparency includes:

- Access
- Location
- Relocation
- Migration
- Replication
- Concurrency
- Failure

### Openness

An open distributed system is essentially a system that offers components that can easily be used by, or integrated into other systems. At the same time, an open distributed system itself will often consist of components that originate from elsewhere.

To be open means that components should adhere to standard rules that describe the syntax and semantics of what those components have to offer. A general approach is to define services through **interfaces** using an Interface Definition Language (IDL).

Another important goal for an open distributed system is that it should be easy to configure the system out of different components (possibly from different developers). Moreover, it should be easy to add new components or replace existing ones without affecting those components that stay in place. In other words, an open distributed system should also be **extensible**.

### Dependability

Dependability refers to the degree that a computer system can be relied upon to operate as expected. Dependability in distributed systems can be rather complex due to **partial failures**. An important goal of distributed systems is to mask those failures, as well as mask the recovery from those failures. This masking is the essence of being able to tolerate faults, accordingly referred to as **fault tolerance**.

Dependability is a term that covers several useful requirements:

- Availability
- Reliability
- Safety
- Maintainability

### Security

A distributed system that is not secure, is not dependable. Special attention is needed to ensure confidentiality and integrity, both of which are directly coupled to authorized disclosure and access of information and resources.

In any computer system, **authorization** is done by checking whether an identified entity has proper access rights. **Authentication** is verifying the correctness of a claimed identity.

An essential technique to making distributed systems secure is **cryptography**. Security in distributed systems is all about encrypting and decrypting data using security keys. Besides its general use for encryption and digital signatures, cryptography forms the basis for realizing a **secure channel** between two communicating parties.

### Scalability

Scalability of a system can be measured along at least three different dimensions:

- **Size**: We can easily add more users and resources to the system without any noticeable loss of performance
- **Geographical**: Users and resources may lie far apart, but communication delays is hardly noticed
- **Administrative**: Can be easily managed even if it spans many independent administrative domains
