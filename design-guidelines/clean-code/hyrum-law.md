## Hyrum's law

An observation on Software Engineering that: with a sufficient number of users of an API, it does not matter what you promise in the contract; all observable behaviors of your system will be depended on by somebody. This law is applicable in the context of maintaining a system with a longer lifespan and sufficient high usage.

The name of the API, input and output data types define the **published contract**, while actual values of input and output data govern the **observable behavior**. Developers often rely on what they get, and not necessarily what they are promised.

### Interface and implementation

An interface can be thought of as an abstraction for interacting with a system (steering wheels and pedals for a car), and the implementation as the way the system does its work (wheels and engine).

However, we like to think that once an abstraction is defined, it is concrete. In other words, an interface should theoretically provide a **clear separation between consumers of a system and its implementers**. In practice, this theory breaks down as the user of a system grows and its users start to **rely upon implementation details intentionally exposed through the interface**.

Taken to its logical extreme, given enough use, there is no such thing as a private implementation. If an interface has enough consumers, they will collectively depend on every aspect of the implementation, intentionally or not. This effect serves to **constrain changes to the implementation**, which must now conform to both the explicitly documented interface, as well as the implicit interface captured by usage.

### Implicit interface

The creation of the implicit interface usually happens gradually, and interface consumers generally are not aware as it is happening. For instance, an interface may make no guarantees about performance, yet consumers often come to expect a certain level of performance from its implementation. Those expectations become part of the implicit interface to a system, and changes of the system must maintain these performance characteristics to continue functioning for its consumers.

Not all consumers depend upon the same implicit interface, but given enough consumers, it will eventually exactly match the implementation. At this point, the interface has evaporated, and the **implementation has become the interface, and any changes to it will violate consumer expectations**.

### Law of leaky abstractions

A law that states that all non-trivial abstractions, to some degree, are leaky. When developers rely on the implementation's inner workings, API creators can break applications without even changing the interface.

Though a contract is defined, the reality is that developers do depend on observable traits and behaviors, often out of necessity. Moreover, when observable behavior is non-deterministic, assuming any specific behavior is a major flaw.

### Examples

Examples of observable traits and behaviors that developers might come to depend on:

- Ordering or lack thereof of lists in responses (iterating Python's dict)
- File types returned from specific endpoints
- Content of responses i.e. format of returned URLs
- Status codes and reference numbers of error messages
- Large or small objects or payloads
- Fast or slow response times
