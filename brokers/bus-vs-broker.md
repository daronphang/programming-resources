## Event/Message Bus

A Bus is a decentralized system. It is a combination of a common data model, a common command set, and a messaging infrastructure to allow different systems to communicate through a shared set of interfaces. The message bus implies a common protocol spoken and understood by all participants.

With a message bus implementation, the messaging infrastructure is cohesively coupled to a microservice instance itself, very much as a microservice’s database is. Thus a microservice’s application code will affectively communicate with a Bus instance in the same infrastructure environment as the microservice itself.

Tailored for broadcasting events to numerous subscribers using a pub-sub model, fostering one-to-many communication. Notably, it provides high decoupling between publishers and subscribers, eliminating the need for them to be aware of each other. Messages are typically consumed as they're generated, rather than being stored, and there's no assurance of message delivery.

Event Bus is suitable for situations involving real-time notifications across multiple subscribers and scenarios where numerous services must respond to specific events.

A Message Bus is an architectural pattern that supports integrating apps using a shared (common) set of interfaces. It consists of the following key elements:

- A shared infrastructure (network and messaging channels) for sending messages to recipients
- A set of agreed-upon message schemas (message headers, and a common data-model in terms of resources and representations used in message payloads)
- A set of common command messages (Used to support the messaging equivalent of RPC to invoke methods in other apps)

## Event/Message Broker

A Broker is centralized, it can receive messages from multiple sources, determine the correct destination and route each message to the correct channel. It can facilitate one-to-one, one-to-many, or many-to-many connections. Message Broker is valuable for complex data routing scenarios, applications with multiple communication patterns, and the transformation and aggregation of messages.

A Message Broker is one part of the Hub and Spoke messaging architecture (topology), as distinct from the Message Bus topology.

### Hub and Spoke

A Hub and Spoke architecture integrates apps without enforcing a common API (message schema) on them, and supports connecting them using disparate protocols. It does so by providing application specific (e.g. protocol) adapters, and an active, central messaging middleware component. This hub, or Message Broker, understands the messages sent to it, knows which app(s) the message needs to be sent, and can transform a message to meet the schema expected by each app. Because it brokers messages sent between apps it can also provide additional messaging services such as message (e.g. content) routing, aggregation and splitting.

## Message Queue

Designed to retain messages until a consumer service is available to process them, following a Point-to-Point or Producer-Consumer communication model (one-to-one). The sender dispatches a message and waits for confirmation.

A message queue receives messages from an application and makes them available to one or more other applications in a first-in-first-out (FIFO) manner.

In this model, messages are sent from a sender to a receiver via an intermediate message queue, which stores messages until they can be processed by the receiver. Message queues are typically used to decouple components and provide fault tolerance by allowing messages to be retried in the event of a failure.
