## Interceptors

An interceptor allows you to do the following:

- Update the original gRPC request before passing it along i.e. inject auth headers.
- Manipulate the behavior of the original invoker function, such as bypassing the call so that you can use a cached result instead.
- Update the response before it's returned to the client.

The intercept() method takes two parameters:

- A request of type grpc.web.Request
- An invoker, which performs the actual RPC when invoked

```js
// unary interceptor example

const SimpleUnaryInterceptor = function () {};

SimpleUnaryInterceptor.prototype.intercept = function (request, invoker) {
  // Update the request message before the RPC.
  const reqMsg = request.getRequestMessage();
  reqMsg.setMessage("[Intercept request]" + reqMsg.getMessage());

  // After the RPC returns successfully, update the response.
  return invoker(request).then((response) => {
    // You can also do something with response metadata here.
    console.log(response.getMetadata());

    // Update the response message.
    const responseMsg = response.getResponseMessage();
    responseMsg.setMessage("[Intercept response]" + responseMsg.getMessage());

    return response;
  });
};
```

## GRPC Interceptor

```console
$ pip install grpc-interceptor
```

### Binding Interceptors (Server)

Interceptors are executed in order for request processing, and reverse order for response processing.

```
Client -> Request -> Interceptor1 -> Interceptor2 -> Interceptor3 -> Server
Server -> Response -> Interceptor3 -> Interceptor2 -> Interceptor1 -> Client
```

```py
from grpc_interceptor import ServerInterceptor


class Interceptor1(ServerInterceptor):
  def intercept(
    self,
      method: Callable,
      request: Any,
      context: grpc.ServicerContext,
      method_name: str,
  ):
    logger.info('test1Start')
    resp = method(request, context)
    logger.info('test1End')


class Interceptor2(ServerInterceptor):
  def intercept(
    self,
      method: Callable,
      request: Any,
      context: grpc.ServicerContext,
      method_name: str,
  ):
    logger.info('test2Start')
    resp = method(request, context)
    logger.info('test2End')
```

```py
interceptors = [interceptor1(), interceptor2(), interceptor3()]

'''
test1Start
test2Start
test2End
test1End
'''
```
