## Kafka network design

Kafka is designed to be a highly available, highly redundant system. Topics have multiple partitions, which facilitates horizontal scalability. Topic partitions are replicated, which provides redundancy.

The design of Kafka’s networking architecture follows the same principles. Every broker (server) can be connected to multiple physical networks via multiple network interfaces. Most modern servers provide somewhere between 2 and 4 physical network interfaces, and Kafka can make use of those either for redundancy or scalability.

## Kafka network

Kafka uses a binary protocol over TCP. The protocol defines all APIs as request-response message pairs. All messages are size delimited and are made up of the following primitive types.

The client initiates a socket connection and then writes a sequence of request messages and reads back the corresponding response message. No handshake is required on connection or disconnection.

The client will likely need to **maintain a connection to multiple brokers, as data is partitioned** and the clients will need to talk to the broker that has their data. To recap, a partition will be owned by a single Broker (called the Leader) in the cluster.

The server guarantees that on a single TCP connection, requests will be processed in the order they are sent and responses will return in that order as well. The broker's request processing allows only a single in-flight request per connection in order to guarantee this ordering. Note that clients can (and ideally should) use non-blocking IO to implement request pipelining and achieve higher throughput. i.e., clients can send requests even while awaiting responses for preceding requests since the outstanding requests will be buffered in the underlying OS socket buffer. All requests are initiated by the client, and result in a corresponding response message from the server except where noted.

The server has a configurable maximum limit on request size and any request that exceeds this limit will result in the socket being disconnected.

## Inter-broker communication

Kafka brokers communicate with each other typically on the internal network. In order to configure how a broker should be reached by other brokers, you need to configure two things:

1. LISTENER: A listener entry
2. Reference this listener in the KAFKA_INTER_BROKER_LISTENER_NAME config item

**This config is required even if we have a single broker**. Bear in mind that in a production environment, you’ll always have multiple brokers for redundancy and availability, usually starting from three.

## Components

### bootstrap.servers

- A kafka cluster can have many brokers, but the client shouldn't need to specify all the brokers available
- A configuration placed within clients which is a comma-separated list of host and port pairs that are the addresses of the Kafka brokers in a "bootstrap" Kafka cluster that a Kafka client connects to initially to bootstrap itself
- Provides the initial hosts that act as a starting point
- Can be a controller or broker
- Connecting to one broker bootstraps a client to the entire Kafka cluster

### listeners

- A listener is a combination of host/IP, port, and protocol
- Listeners tell the Kafka process what network interface it should open a listening socket to
- Listeners tell the Kafka process which network adapter and port number to use to initialize a listening socket
- The host on which Kafka is running may have multiple network interfaces
- The default is 0.0.0.0, which means listening on all interfaces

### advertised_listeners

- Kafka clients may well not be local to the broker’s network, and this is where the additional listeners come in
- This is the address clients should use to connect to the Kafka broker
- Entries returned to the clients as part of the metadata response
- Actual address clients would use to send messages to the broker
- Addresses could be some combination of ip addresses or dns addresses
- **At least one of them must be specified in the client application in the bootstrap.servers**; otherwise, the client would try to connect to the internal host address as it would default to the listeners

If advertised.listeners is not specified, then listeners will be used in its place.

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
