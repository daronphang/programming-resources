## Serializing Data

Programs working with data have at least two different representations: in-memory and bytes. Translation from in-memory to bytes is called encoding/marshalling/serialization, and bytes to in-memory is decoding/unmarshalling/deserialization.

Serialization is the process of converting a data object into a series of bytes that saves the state of the object in an easily transmittable form.

With serialization, we can transfer objects:

- Over the wire for messaging use cases
- Across applications via REST APIs
- Through firewalls
- Across domains
- To other data stores

### In Memory

Data is kept in objects, structs, lists, hashmaps, trees, etc. These data structures are optimized for efficient access and manipulation by CPU.

### Bytes

When you want to write data to a file or send it over a network, it must be encoded into bytes i.e. JSON document.

Though most programming languages come with built-in support for encoding, there are a few problems that arise and hence, **it is generally a bad idea to use language built-in encoding** for the following reasons:

- The encoding is tied to the language and you are committing yourself to that language for a long time; integration may be difficult
- To restore data in the same object types, the decoding process needs to instantiate arbitrary classes which is a source of security problems; if an attacker can get your application to decode an arbitrary byte sequence, it allows them to do terrible things such as remotely executing arbitrary code
- Developers often neglect the problems of forward and backward compatibility
- Efficiency is often an afterthought
