## Headers

Records can include headers which give you the ability to add metadata about the Kafka record, without adding any extra information to the key/value pair of the record itself. Headers are often used for lineage to indicate the source of the data in the record, and for routing or tracing messages based on header information without having to parse the message itself i.e. correlation ID.

Headers are implemented as an ordered collection of key/value pairs.

```
Key     String
Value   Any serialized object
```
