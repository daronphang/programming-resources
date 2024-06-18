## Kafka network design

Kafka is designed to be a highly available, highly redundant system. Topics have multiple partitions, which facilitates horizontal scalability. Topic partitions are replicated, which provides redundancy.

The design of Kafka’s networking architecture follows the same principles. Every broker (server) can be connected to multiple physical networks via multiple network interfaces. Most modern servers provide somewhere between 2 and 4 physical network interfaces, and Kafka can make use of those either for redundancy or scalability.

## Kafka network

Kafka is a distributed system. Data is read from & written to the Leader for a given partition, which could be on any of the brokers in a cluster.

When a client (producer/consumer) starts, it will **request metadata about which broker is the leader for a partition**; it can do this from **any broker**. This is also known as the **bootstrap call** (configured via bootstrap.servers).

The metadata returned will include the endpoints available for the Leader broker for that partition, and the client will then use those endpoints to connect to the broker to read/write data as required. The exact broker to send messages to depends on which is the leader for the concrete partition.

The key thing is that when you run a client, the broker you pass to it is just where it’s going to go and get the metadata about brokers in the cluster from. The actual host and IP that it will connect to for reading/writing data is based on the data that the broker passes back in that initial connection; even if it’s just a single node and the broker returned is the same as the one connected to.

If you want to use SSL, need to include SSL in your listener name e.g. LISTENER_EXTERNAL_SSL.

https://rmoff.net/2018/08/02/kafka-listeners-explained/

### bootstrap.servers

- A kafka cluster can have many brokers, but the client shouldn't need to specify all the brokers available
- A configuration placed within clients which is a comma-separated list of host and port pairs that are the addresses of the Kafka brokers in a "bootstrap" Kafka cluster that a Kafka client connects to initially to bootstrap itself
- Provides the initial hosts that act as a starting point
- Can be a controller or broker
- Connecting to one broker bootstraps a client to the entire Kafka cluster

### listeners

- Listeners are what interfaces Kafka binds to on which to listen
- Tells the Kafka process which network adapter and port number to use to initialize a listening socket
- The default is 0.0.0.0, which means listening on all interfaces

### advertised_listeners

- Entries returned to the clients as part of the metadata response
- Actual address clients would use to send messages to the broker
- Addresses could be some combination of ip addresses or dns addresses
- **At least one of them must be specified in the client application in the bootstrap.servers**; otherwise, the client would try to connect to the internal host address

If advertised.listeners is not specified, then listeners will be used in its place.

## Inter-broker communication

Kafka brokers communicate with each other typically on some internal network. In order to configure how a broker should be reached by other brokers, you need to configure two things:

1. LISTENER: A listener entry
2. Reference this listener in the KAFKA_INTER_BROKER_LISTENER_NAME config item

**This config is required even if we have a single broker**. Bear in mind that in a production environment, you’ll always have multiple brokers for redundancy and availability, usually starting from three.

## Docker compose example

When running within Docker, need to configure two listeners for Kafka:

1. Communication within the Docker internal network
2. Non-Docker network traffic e.g. localhost

In the below example:

- Clients on host computer can access via localhost:39092
- Clients in the Docker network can access via kafka-test:19092
- Controller listens to CONTROLLER://:9093

```yaml
# For running integration tests.
version: "3.0"
services:
  multi-site-dashboard-go:
    container_name: multi-site-dashboard-go
    image: multi_site_dashboard_go
    depends_on:
      - timescaledb-test
      - kafka-test
    build:
      args:
        - DEPLOYMENT_IMAGE=build
    environment:
      - GO_ENV=TESTING
    ports:
      - 38000:8000
    volumes:
      - .:/app/coverage:rw
    entrypoint:
      [
        "go",
        "test",
        "./...",
        "-v",
        "-coverpkg=./...",
        "-coverprofile=/app/coverage/report.lcov",
      ]
  timescaledb-test:
    container_name: timescaledb-test
    image: timescale/timescaledb-ha:pg16
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - 35432:5432
  kafka-test:
    container_name: kafka-test
    image: apache/kafka:3.7.0
    ports:
      - 39092:9092
    # https://github.com/apache/kafka/blob/trunk/docker/examples/README.md
    environment:
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: "broker,controller"
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: "CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT"
      KAFKA_CONTROLLER_QUORUM_VOTERS: "1@kafka-test:9093"
      KAFKA_LISTENERS: "PLAINTEXT://:19092,CONTROLLER://:9093,PLAINTEXT_HOST://:9092"
      KAFKA_INTER_BROKER_LISTENER_NAME: "PLAINTEXT"
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka-test:19092,PLAINTEXT_HOST://localhost:39092
      KAFKA_CONTROLLER_LISTENER_NAMES: "CONTROLLER"
```
