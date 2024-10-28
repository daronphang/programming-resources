## Middleware organization

There are two important types of design patterns that are often applied to the organization of middleware: wrappers and interceptors. Each targets different problems, yet addresses the same goal for middleware: achieving openness.

### Wrappers/adapters

A wrapper is a special component that offers an interface acceptable to a client application, of which the functions are transformed into those available at the component. In essence, it **solves the problem of incompatible interfaces**.

Wrappers have always played an important role in extending systems with existing components. Extensibility, which is crucial for achieving openness, used to be addressed by adding wrappers as needed. However, if we were to develop wrappers for each application, this approach will not scale well.

Facilitating a reduction of the number of wrappers is typically done through middleware. One way of doing this is implementing a **broker** (message, event), which is logically a centralized component that handles all the accesses between different applications.

### Interceptors

An interceptor is a software construct that will break the usual flow of control and allow other (application specific) code to be executed e.g. RPC. Interceptors are a primary means for adapting middleware to the specific needs of an application.
