## RPC (Remote Procedure Call)

RPC is a powerful technique for constructing distributed, client-server based applications. RPC is an **architectural style for distributed systems**. It allows a program on one machine to call a procedure (subroutine/service) on another machine in a different address space than its own. The procedure may be on the same system or a different system connected on a network. Supports both XML-RPC and JSON-RPC.

In a nutshell, RPC allow programs to call procedures located on other machines. When a process on a machine A calls a procedure on a machine B, the calling process on A is suspended, and execution of the called procedure takes place on B. Information can be transported from the caller to the callee in the parameters and can come back in the procedure result. No message passing at all is visible to the programmer.

Idea behind RPC is that a program can call and execute a subroutine just like it would call a local subroutine, but the network communication details are hidden from the user. RPC calls are defined through routines contained in the RPC protocol. It is not a transport protocol but a method of using existing communication features in a transparent way.

In RPC, each server supplies a program that is a set of remote service procedures. The combination of a host address, program number, and procedure number specifies one remote service procedure.

RPC is a request-response protocol i.e. follows client-server model:

1. Client makes a request to execute a procedure on the remote server
2. Client is suspended like a synchronous local call (blocking)
3. Procedure's parameters are passed over the network to the server-side
4. Server calls the requested dispatch routine
5. Results are transferred back to the client and client resumes execution

As the application software does not contain any communication code, it is independent of:

- Particular communications hardware and protocols used
- OS and programming language used
- Calling sequence needed to use the underlying communications software

### How it works

1. Client invokes a client stub procedure with parameters that resides within the client's address space
2. Client stub marshalls (packs) the parameters into a message; marshalling includes converting the representation of the parameters into a standard format
3. Client stub passes the message to the transport layer, which sends it to the remote server
4. Server de-marshalls (unpacks) the parameters and calls the desired subroutine
5. When the procedure completes, it returns to the server stub which marshalls the return values into a message and hands it to the transport layer
6. Client stub receives and de-marshalls the return parameters and execution returns to the caller

<img src="./assets/RPC.PNG">

## Terminologies

### RPC runtime

RPC run-time system is a library of subroutines and a set of services that handle the network communications in the underlying RPC mechanism. In an RPC call, both the client and server-side run-time systems' code handle binding, establishing communications over an appropriate protocol, passing call data between each other, and handling communication errors.

### Stub

For RPCs, the stub converts the methods, request types and response types into the forms used by the RPC system i.e. a piece of code that is used to convert the parameters during a RPC. It is essentially a usability feature to provide the appearance the remote method is present locally. Function of the stub is to provide transparency to the application code.

On the client slide, stub handles the interface between client's local procedure call and run-time system, marshalling and un-marshalling data, invoking the RPC run-time protocol, and carrying out binding steps.

On the server side, stub provides a similar interface between the run-time system and local manager procedures that are executed by the server.

### Binding

Dynamic binding is used to find the server at run-time when the RPC is first called. Binding consists of naming and locating.

## Benefits

### Straightforward and simple interaction

RPC uses GET to fetch information and POST for everything else. Mechanism of interaction between server and client boils down to calling an endpoint and getting a response.

### Easy-to-add functions

Can easily add another endpoint for executing a new requirement for your API.

### High performance

Lightweight payloads go easy on the network providing high performance.

## Drawbacks

### Tight coupling to the underlying system

RPC's tight coupling to the underlying system does not allow for an abstraction layer between the functions in the system and the external API. This raises security issues as it is quite easy to leak implementation details about the underlying system into the API. Works for internal microservices but not for strong external API.

### Low discoverability

There is no way to introspect the API or send a request and start understanding what function to call based on its requests.

### Too much abstraction

Though the core idea of RPC is to hide the complexity of a remote call (making it look like a local call), many implementations hide too much. You can make a large number of local calls without worrying overly about performance. However, with RPC, the cost of marshalling and unmarshalling payloads can be significant. Hence, need to think differently about API design for remote interfaces versus local interfaces.

### Brittleness

Changes to server stubs such as adding new methods to an object require client stubs to be updated/regenerated if they are consuming the new methods. Additionally, depending on the nature of changes, consumers that don't need the new method may also need to have their stubs upgraded too.

Changes like this are fairly common, and RPC endpoints will eventually end up having a large number of methods for different ways of creating or interacting with objects.

Another form of brittleness is serialization. If the server implementation decides to add/remove fields of a particular type, even though consumers do not use that field, code associated with deserializing the object on the consumer side will also need to change, else it will break. Both client and server need to have fields matched. Hence, rolling out changes require both client and server to redeployed at the same time.

This is a key challenge with any RPC mechanism that promotes the use of binary stub generation i.e. client and server deployments are not separated. Types that are exposed may end up having a mass of fields, some of which are no longer used but can't be safely removed.

## Is RPC terrible?

Many operations actually fall quite nicely into the RPC-based model, and more modern mechanisms like protocol buffers or Thrift mitigate the downsides by avoiding the need for lock-step releases of client and server code.

Nonetheless, need to be aware of the potential pitfalls associated with RPC. Don't abstract your remote calls to the point where the network is completely hidden, and ensure that you can evolve the server interface without having to insist on lock-step upgrades for clients.
