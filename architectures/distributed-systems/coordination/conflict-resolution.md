## Resolving conflicts in data synchronization

Data conflicts can arise from various sources, such as network failures, hardware failures, software bugs, human errors, malicious attacks, or conflicting business rules. Conflict resolution strategies are essential when dealing with synchronization in data systems.

## Design considerations

### When to perform

An important design consideration is to decide **when** to perform the process of resolving update conflicts i.e. whether conflicts should be resolved during reads or writes.

Many traditional data stores execute conflict resolution during writes and keep the read complexity simple. However, writes may be rejected if the data store cannot reach all (or a majority of) the replicas at a given time.

Alternatively, to enable 'always writeable' data store, the complexity of conflict resolution is **pushed to reads** in order to ensure that writes are never rejected in the event of failures or concurrent writes.

### Who performs the process

Conflict resolution can be performed by either the data store or the application.

If conflict resolution is done by the data store, its choices are limited: the data store can only use simple policies, such as “last write wins”, to resolve conflicting updates.

On the other hand, since the application is aware of the data schema, it can decide on the conflict resolution method that is best suited for its client’s experience. Despite this flexibility, some application developers may not want to write their own conflict resolution mechanisms and choose to push it down to the data store, which in turn chooses a simple policy such as “last write wins”.

## Strategies

### Last write wins

In this strategy, the latest modification made to a data item is considered the valid one. When conflicts occur, the modification made by the last writer is retained, and the conflicting changes are discarded. This approach is suitable for scenarios where real-time collaboration is not critical, and the most recent update is typically the most relevant.

### Timestamp ordering

Each data item is associated with a timestamp that indicates when it was last modified. During conflict resolution, the modification with the latest timestamp is considered valid. This strategy ensures chronological order and can be useful when maintaining a history of changes is important.

### Manual intervention

For critical or complex conflicts, involving user intervention can be a viable option. When conflicts arise, the application prompts the user to select the desired resolution manually. This approach allows users to make informed decisions based on context and their understanding of the data.

### Merge/patch

The merge or patch strategy aims to combine conflicting modifications into a single unified state. This can involve merging changes at the field level or using more complex merging algorithms. The goal is to create a merged version that combines the intent of both conflicting modifications. This strategy is commonly used in collaborative editing scenarios where multiple users can modify the same document simultaneously.

### Predefined rules or policies

Developers can establish predefined rules or policies that dictate how conflicts should be resolved. These rules can be based on specific criteria such as priority, access level, or predefined business rules. For example, if a conflict occurs between two user roles, a predefined policy can specify that the modification made by a higher-ranking role takes precedence.

## Reconciliation

### Syntactic

Most of the time, new versions subsume the previous versions, and the system itself can determine the authoritative version via syntactic reconciliation e.g. vector clocks.

### Semantic

If the versions cannot be syntactically reconciled based on vector clocks alone, they have to be passed to the **business logic** for semantic reconciliation. Semantic reconciliation introduces additional load on services, so it is desirable to minimize the need for it.
