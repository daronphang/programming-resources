## Assigning data ownership

After breaking apart data within a distributed architecture, an architect must determine which services own what data. Unfortunately, assigning data ownership to a service is not as easy as it sounds, and becomes yet another hard part of software
architecture.

The general rule of thumb for assigning table ownership states that **services that perform write operations to a table own that table**. While this general rule of thumb works well for single ownership (only one service ever writes to a table), it gets messy when teams have joint ownership (multiple services do writes to the same table) or even worse, common ownership (most or all services write to the table).

## Common ownership

Common table ownership occurs when most of the services need to write to the same table.

The solution of simply putting the Audit table in a shared database or shared schema that is used by all services unfortunately reintroduces all of the data-sharing issues i.e. change control, connection starvation, scalability, fault tolerance.

A popular technique for addressing common table ownership is to **assign a dedicated single service as the primary owner of that data** i.e. one service is responsible for writing data to the table. Other services needing to perform write actions would send information to the dedicated service, which would then perform the actual write operation on the table.

If no information or acknowledgement is required by services sending the data, services can use persisted queues for asynchronous fire-and-forget messaging. However, if information needs to be returned, RESTful APIs or gRPC can work as alternatives.

## Joint ownership

One of the more common and complex scenarios involving data ownership is joint ownership, which occurs when multiple services perform write actions on the same table. In contrast, **common ownership involves most or all of the services** performing operations on the same table.

### Table split technique

The table split technique breaks a single table into multiple tables so that each service owns a part of the data it's responsible for.

However, synchronizing data between split tables is not a trivial matter, and based on the CAP theorem, as network partitioning is necessary, only consistency or availability is possible. Choosing availability means one service can always perform operations, even though the corresponding record may not be updated in the other table. Choosing consistency means an operation will fail if the other table is not able to register the update.

### Data domain technique

Another technique for joint ownership is to create a shared data domain. With this technique, the tables shared by the same services are put into the same schema or database, therefore forming a broader bounded context between the services and data.

While data sharing is generally discouraged in distributed architectures, it does resolve some of the performance, availability, and data consistency issues found in other joint ownership techniques i.e. **removing coordination overhead**.

When choosing this technique, always re-evaluate why separate services are needed since the data is common to each of the service.

Unfortunately, sharing data introduces a number of issues:

- Increased effort and testing scope for changes made to the structure of the data i.e data schema
- Controlling which service have write responsibility to what data i.e. governance

### Delegate technique

With this technique, one service is assigned single ownership of the table and becomes the delegate, and the other service communicates with the delegate to perform updates on its behalf.

One of the challenges is knowing which service to assign as the delegate:

- **Primary domain priority**: Service that most closely represents the primary domain of the data becomes the delegate (**recommended**)
- **Operational characteristics priority**: Service needing higher operational architecture characteristics such as performance, scalability, availability, throughput; however, having added domain management responsibility could be messy

Regardless of which service is assigned as the delegate, the disadvantages include:

- Service coupling and the need for interservice communication
- Lack of atomic transaction when performing writes for non-delegates
- Network and processing latency, and low fault tolerance

Hence, this technique is generally better suited for database write scenarios that do not require atomic transactions that can tolerate eventual consistency through asynchronous communications.

### Service consolidation technique

The service consolidation technique resolves service dependency and addresses joint ownership by combining multiple table owners into a single consolidated service.

Combining service creates a more coarse-grained service, thereby increasing the overall testing scope as well as deployment risk. Consolidating services might also impact overall fault tolerance since all parts of the service fail together.

Overall scalability is also impacted as all parts of the service must scale equally, even though some functionality might not need to scale at the same level as other functionality.
