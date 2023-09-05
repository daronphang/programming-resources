## Load Balancer

- Distributes incoming client requests among a group of servers and returning the response from selected server to appropriate client
- Most commonly deployed when site needs multiple servers as the volume of requests is too much for a single server to handle efficiently
- Deploying multiple servers also eliminates single point of failure, making website more reliable
- Distribute workload in a way that makes the best use of each server's capacity, prevents overload on any server, and results in fastest possible resposne to client
- Enhance user experience by reducing number of error responses the client sees (diverts requests away from servers that are down)

## Sticky Session (Session Persistence)

Session stickiness is a process in which a load balancer creates an affinity between a client and specific network server for the duration of the session (i.e. the time a specific IP spends on a website). **Consecutive requests are routed to the same server during session**. Using sticky sessions can help improve user experience and optimize network resource usage.

With sticky sessions, a load balancer assigns an identifying attribute to a user, typically by issuing a cookie or by tracking their IP details. Then, according to the tracking ID, a load balancer can start routing all of the requests of this user to a specific server for the duration of the session.

Without session persistence, the web application would have to maintain information across multiple servers, which can prove inefficient i.e. keeping logs of items in a shopping cart or chat conversations.

### Advantages

#### Minimized data exchange

When using sticky sessions, servers within your network don't need to exchange session data, a costly process when done on scale.

#### RAM cache utilization

Sticky sessions allow for more effective utilization of your application's RAM cache, resulting in better responsiveness.

### Disadvantages

#### They can make applications go down easily

If one of the servers goes down, we won't be able to access the data from other servers. If we use the application's memory as our state storage, we will lose all data that were bound to the server's sessions.

#### Application doesn't scale correctly

When we bind a server to a specific request, we remove the ability to use other servers' capacity to fulfill consecutive requests.

#### Vulnerable to attacks

Binding sessions to specific servers can cause security concerns. An attacker can perform DDOS and perform very CPU intensive requests, which can cause the server to go down.

### Alternative

Session storage can be stored in a shareable resource i.e. database, or in-memory cache like Redis.
