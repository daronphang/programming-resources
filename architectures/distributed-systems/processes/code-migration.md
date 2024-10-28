## Code migration

There are situations in which passing programs, sometimes even while they are being executed, simplifies the design of a distributed system.

When communication is expensive, we can sometimes reduce communication by shipping computations from the server to the client, and let the client do as much local processing as possible.

## Reasons for migrating code

### Performance

The most important reason for code migration. The basic idea is that overall system performance can be improved if processes are moved from heavily loaded (high CPU utilization) to lightly loaded machines. However, process migration is no longer a viable option for improving distributed systems. Instead of offloading machines, we can move code to make sure that a machine is sufficiently loaded.

For instance, if a client application needs to perform many database operations involving large quantities of data, it may be better to ship part of the client application to the server and send only the results across the network. Otherwise, the network may be swamped with the transfer of data from the server to the client.

We can also migrate parts of the server code to the client. For example, in many interactive database applications, clients need to fill in forms that are subsequently translated into a series of database operations. Processing the form at the client side, and sending only the completed form to the server, can sometimes avoid that a relatively large number of small messages need to cross the network. The result is that the client perceives better performance, while at the same time the server spends less time on form processing and communication.

### Privacy and security

Another reason for moving code to where the data is, has to do with security.

An example for this approach is found in **federated learning**. Instead of bringing training, sensitive data to a centralized location, a better approach is to bring the partially trained model to where the data is, and continue training with that local data.

### Flexibility

Flexibility is increased if a client can dynamically download software needed to communicate with a specific server. The downloaded software can be specifically targeted to that server, without forcing the client to have it preinstalled.
