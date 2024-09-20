## RPC variations

### Asynchronous RPC

To support situations in which there is simply no result to return to the client, RPC systems may provide facilities for what are called asynchronous RPCs. With asynchronous RPCs, the server, in principle, immediately sends a reply back to the client the moment the RPC request is received, after which it locally calls the requested procedure.

### Multicast RPC

Asynchronous and deferred synchronous RPCs facilitate another alternative to RPCs, namely executing multiple RPCs at the same time. Adopting the one-way RPCs (i.e., when a server does not tell the client it has accepted its call request but immediately starts processing it, while the client continues just after issuing the RPC), a multicast RPC boils down to **sending an RPC request to a group of servers**. The client sends a request to multiple servers, who subsequently process that request independently and in parallel. When done, the result is returned to the client where a callback takes place.
