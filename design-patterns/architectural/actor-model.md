## Actor model

The actor model is a powerful paradigm for concurrent and distributed systems. This pattern provides a model for designing systems that can efficiently handle the complexities of parallel and asynchronous processing. It views computation as a collection of independent entities called “actors” that communicate with each other by sending messages. Each actor has its own state, behavior, and a mailbox for receiving messages.

### Characteristics

- Isolation: Actors operate independently, encapsulating their state and behavior
- Asynchronous Messaging: Communication between actors is achieved through asynchronous message passing
- Location transparency: Actors can be distributed across different machines, providing a level of transparency regarding their physical location
- No Shared Memory: Actors do not share memory, avoiding the complexities of locks and shared data

## Components

### Actors

Actors are the fundamental units in the Actor Model. An actor is an autonomous entity that processes messages, maintains its own state, and can create new actors. Actors operate concurrently, making them well-suited for handling parallel and distributed tasks.

An actor is an extremely lightweight object. It takes fewer resources than threads. Hence, it’s easy to spawn millions of actors if necessary.

### Messages

Messages are the means of communication between actors. Actors send and receive messages asynchronously. Messages can contain data or instructions, allowing actors to exchange information and coordinate their activities.

### Mailboxes

Each actor has a mailbox that stores incoming messages. The actor processes messages sequentially, ensuring that its state changes in a controlled manner. Mailboxes help in managing the asynchrony of message passing.

### Actor system

An actor system is the runtime environment that manages and coordinates actors. It provides the infrastructure for creating, scheduling, and supervising actors. Actor systems can span across multiple machines, forming distributed systems.

## Frameworks

Several programming languages offer libraries or frameworks for implementing the Actor Model:

- Erlang: Erlang OTP
- Python: Pykka
- Scala/Java: Akka
