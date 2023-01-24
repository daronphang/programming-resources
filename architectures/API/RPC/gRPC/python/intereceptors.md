## Interceptors

An interceptor allows you to do the following:

- Update the original gRPC request before passing it along i.e. inject auth headers.
- Manipulate the behavior of the original invoker function, such as bypassing the call so that you can use a cached result instead.
- Update the response before it's returned to the client.

The intercept() method takes two parameters:

- A request of type grpc.web.Request
- An invoker, which performs the actual RPC when invoked

```js
// unary intereceptor example

const SimpleUnaryInterceptor = function () {};

SimpleUnaryInterceptor.prototype.intercept = function (request, invoker) {
  // Update the request message before the RPC.
  const reqMsg = request.getRequestMessage();
  reqMsg.setMessage('[Intercept request]' + reqMsg.getMessage());

  // After the RPC returns successfully, update the response.
  return invoker(request).then((response) => {
    // You can also do something with response metadata here.
    console.log(response.getMetadata());

    // Update the response message.
    const responseMsg = response.getResponseMessage();
    responseMsg.setMessage('[Intercept response]' + responseMsg.getMessage());

    return response;
  });
};
```
