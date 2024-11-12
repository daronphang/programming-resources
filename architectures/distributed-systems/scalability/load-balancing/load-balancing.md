## Load balancers

Load balancers helps to spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. Load balancers also keeps track of the status of all the resources while distributing requests; if a server is not available, it will redirect to another healthy server.

### Benefits

- **Performance**: Users experience faster, uninterrupted service
- **Scalability**: Service providers experience less downtime and higher throughput
- **Workload distribution**: Workload is distributed/balanced across nodes, instead of a single node performing a lot of work
- **Redundancy**: A failure in one node will route the request to another healthy node i.e. eliminates single point of failure

## Dual-machine hot standby deployment

As load balancers are always on the **critical path of the network**. Therefore, the stability and security of the load balancing device directly affect the usability of the network.

The implementation of dual-machine hot standby has two types:

- **Active-passive**: One acts as the main device while the other acts as the backup device
- **Load sharing**: Both devices handle business traffic and serve as backup devices for each other

## Scaling

While load balancers help scale the application, it’s important to ensure that they don’t become bottlenecks to the scalability:

- **DNS round robin**: Multiple load balancers are configured with different IP addresses but share the same domain name
- **Clustered LB configuration**
- **GSLB**
- **Active-passive load balancing**
- **Anycast load balancing**
- **Elastic load balancing: Auto-scaling of load balancers based on incoming traffic**

## Redundancy

The load balancer can be a single point of failure; to overcome this, a second load balancer can be connected to the first to form a cluster i.e. HA Proxy with keep-alived.

## Sticky session (session persistence)

Session stickiness is a process in which a load balancer creates an affinity between a client and specific network server for the duration of the session (i.e. the time a specific IP spends on a website). **Consecutive requests are routed to the same server during session**. Using sticky sessions can help improve user experience and optimize network resource usage. This is particularly important when meeting the needs of application scenarios such as online banking and online shopping that requires user authentication.

With sticky sessions, a load balancer assigns an identifying attribute to a user, typically by issuing a cookie or by tracking their IP details. Then, according to the tracking ID, a load balancer can start routing all of the requests of this user to a specific server for the duration of the session.

Without session persistence, the web application would have to maintain information across multiple servers, which can prove inefficient i.e. keeping logs of items in a shopping cart or chat conversations.

### Implementation

Persistence can be based on the following:

- **IP address**: When the L4 LB receives a request, a persistence table is established to record the server situation for that IP
- **Cookie**: Used by L7 LB to ensure packets of the same session are routed to the same server. If the server adds Set-Cookie field, the LB will intercept its value in the response message and cache it. Otherwise, the LB will insert a cookie in the response message for the client to attach it in the subsequent request message
- **HTTP headers**: Used by L7 LB to ensure packets with the same key information in the HTTP header are allocated to the same server
- **SIP packets**: Used by L7 LB to ensure that SIP packets with the same session identifier in an IP session are assigned to the same server

### Advantages

- **Minimized data exchange**: When using sticky sessions, servers within your network don't need to exchange session data, a costly process when done on scale
- **RAM cache utilization**: Allow for more effective utilization of your application's RAM cache, resulting in better responsiveness

### Disadvantages

- **They can make applications go down easily**: If one of the servers goes down, we won't be able to access the data from other servers. If we use the application's memory as our state storage, we will lose all data that were bound to the server's sessions
- **Application doesn't scale correctly**: When we bind a server to a specific request, we remove the ability to use other servers' capacity to fulfill consecutive requests
- **Vulnerable to attacks**: Binding sessions to specific servers can cause security concerns. An attacker can perform DDOS and perform very CPU intensive requests, which can cause the server to go down

## Health checks

The goal of health checks is to timely discover and eliminate servers with abnormal work status, and retain a "healthy" server pool to provide services to users. Methodologies include:

- **ICMP**: Send ICMP echo packets to servers in the cluster. Suitable for health check at the server host level
- **TCP**: Initiates TCP connection establishment request. Suitable for health check at the business level
- **HTTP**: Establishes a TCP connection and then send a HTTP request. Suitable for health check at the application level
- **HTTPS**: Establishes SSL connection and then send a HTTP request
