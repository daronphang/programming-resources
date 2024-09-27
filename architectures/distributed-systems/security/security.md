## Security principles

A distributed system must provide security services by which a wide range of security policies can be implemented.

### Fail-safe defaults

Fail-safe defaults are assuming that any set of defaults will generally not be changed i.e. admin,admin for user and password respectively. This principle states that defaults should already guarantee a good degree of protection. In particular, access decisions should be based on permissions, not exclusions.

### Open design

The principle of open design is all about not applying security by obscurity: it is essential that every aspect of a distributed system is open for review. Everyone should be able to see which mechanisms are being used, how they are being used, how they have been implemented, etc.

### Separation of privilege

Separation of privilege is about ensuring that truly critical aspects of a system can never be fully controlled by just a single entity. For example, a top-secret file may need to be double encrypted, with keys in the hands of two different people.

### Least privilege

The principle of least privilege states that a process should operate with the fewest possible privileges. As a practical example, in Unix systems, most processes and users cannot execute operations that are intended to be executed by the root.

### Least common mechanism

The least common mechanism refers to designing systems in such a way that if multiple components require the same mechanism, then they should all be offered the same implementation of that mechanism. An important motivation for this principle is that maintenance and simplicity is much easier to achieve with a single implementation than having a mechanism spread across the system, possibly with different implementations. A typical example of this approach is that all users have access to the same library.
