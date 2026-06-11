## Control plane

A control plane:

- Stores desired state
- Makes decisions
- Coordinates systems
- Tells workers what to do

It is responsible for:

- Orchestration
- Configuration
- Scheduling
- Cluster state management

Control plane failures often create secondary data plane symptoms.

## Data plane

A data plane:

- Processes traffic
- Executes workloads
- Moves packets/data
- Serves actual traffic to users

Examples include:

- Application Pods
- VM workloads
- Packet forwarding
- Service mesh proxies
- Load balancers

Symptoms include:

- 5XX spikes
- Latency increase
- Packet drops
- Failed requests
