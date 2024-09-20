## Quotas

Kafka brokers have the ability to limit the rate at which messages are produced and consumed via the quota mechanism:

- Produce: Limits the rate at which client can send data
- Consume: Limits the rate at which client can receive data
- Request: Limits the percentage of time the broker spends processing client requests

Quotas can be applied to all clients, specific client-ids, specific users, or both.

Quotas specified in the Kafka's configuration file are static, and can only be modified by changing and restarting all brokers. As new clients can arrive at any time, the usual method of applying quotas to specific clients is through dynamic configuration that can be set using **kafka-config.sh or the AdminClient API**.

## Throttling

When a client reaches its quota, the broker will start throttling the client's requests to prevent it from exceeding the quota i.e. delay responses to client requests. To protect the broker from misbehaved clients sending additional requests while being throttled, the broker will mute the communication channel with the client for a period of time needed to achieve compliance with the quota.
