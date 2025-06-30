## Idempotency

In the context of REST APIs, an idempotent method is one that can be invoked many times without having different outcomes (but may have different response status received by the client). In other words, the result of a successfully performed request is independent of the number of times it is executed, and there is no change of state for any resource on the server-side.

When designing REST APIs, clients can make mistakes i.e. sending duplicated requests that may be intentional/unintentional. Hence, need to make APIs fault-tolerant in such a way that the duplicated requests do not leave the system unstable. Nonetheless, it is still the responsibility of the service implementer to fulfill the promise of idempotency as it is not enforced i.e. PUT is only for UPDATE, GET does not change any resources on the server, etc.

### HTTP methods

```
Methods       Safe    Idempotent
GET           Yes     Yes
PUT           No      Yes
DELETE        No      Yes
HEAD          Yes     Yes
OPTIONS       Yes     Yes
POST          No      No
```

### Why does idempotency matter?

- Prevents duplicate actions (e.g., user clicking "Pay" multiple times)
- Handles network retry logic gracefully
- Ensures consistency in distributed systems
- Increases robustness and user safety

### How to implement idempotency?

1. Assign unique identifiers such as idempotency keys, together with hashing of a user's request. If a user sends a duplicate request with the same idempotency key and hashed request body, we can simply return the result. Set a reasonable expiration time for idempotency keys to ensure they are valid only for a certain period

```http
POST /payment
body: {"user": "john", amount: "50.14"} // body is hashed
Idempotency-Key: 123e4567-e89b-12d3-a456-426614174000
```

2. Implement deduplication logic such as:

- Checking whether the same logical operation has already been processed
- Applying database uniqueness constraints (e.g., preventing duplicate creation)
- State validation before execution of request
- Checking to see if the resource is already in the desired state before executing (e.g., avoid charging a paid order again)

3. Use HTTP methods appropriately (GET, PUT, DELETE), for example : PUT /resource/{id}

- PUT operations are naturally idempotent because they set the resource to a specific state
