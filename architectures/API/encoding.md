## Encoding Data

Programs working with data have at least two different representations: in-memory and bytes. Translation from in-memory to bytes is called encoding/marshalling/serialization, and bytes to in-memory is decoding/unmarshalling/deserialization.

### In Memory

Data is kept in objects, structs, lists, hashmaps, trees, etc. These data structures are optimized for efficient access and manipulation by CPU.

### Bytes

When you want to write data to a file or send it over a network, it must be encoded into bytes i.e. JSON document.

Though most programming languages come with built-in support for encoding, there are a few problems that arise and hence, **it is generally a bad idea to use language built-in encoding**.

- The encoding is tied to the language and you are committing yourself to that language for a long time. Integration may be difficult.
- To restore data in the same object types, the decoding process needs to instatiate arbitrary classes which is a source of security problems. If an attacker can get your application to decode an arbitrary byte sequence, it allows them to do terrible things such as remotely executing arbitrary code.
- Developers often neglect the problems of forward and backward compatibility.
- Efficiency is often an afterthought.

## Standardized Encodings

### JSON, XML, CSV

JSON, XML and CSV can be written/read by many programing languages, and are widely supported. However, they also have subtle problems:

- There is a lot of ambiguity around the encoding of numbers i.e. cannot distinguish between number and string.
- Integers greater than 2^53 cannot be represented and requires workaround i.e. Twitter's API returns tweet IDs twice, once as JSON number and another as decimal string.
- JSON and XML have good support for unicode character strings but not for binary strings. Workaround is to encode the binary data as text using Base64.

### Thrift and Protocol Buffers

Apache Thrift and Google Protocol Buffers are binary encoding libraries that require a schema for any data that is encoded. Each come with a code generation tool that produces classes implementing the schema in various programming languages, which is useful for statically typed languages. Encoding formats for Thrift include BinaryProtocol, CompactProtocol and DenseProtocol.

Marking each field as required or optional has no effect on how the field is encoded. This will only enable a runtime check that fails if the field is not set.

```
// thrift
struct Person {
    1: required string          userName,
    2: optional i64             favNumber,
    3: optional list<string>    interests
}

// protocol buffer
message Person {
    required string user_name       = 1;
    optional int64 fav_number       = 2;
    repeated string interests       = 3;
}
```

#### Evolution

An encoded record is the concatenation of its encoded fields, whereby each field is identified by its tag number that is critical. The name of a field can be changed, but not the field's tag, since it would make all existing encoded data invalid.

For forward compatibility, new fields with new tag numbers that are not recognized are ignored by the old code.

For backward compatibility, as long as each field has a unique tag number, the new code can always read old data. Only detail is that new fields cannot be made required.

### Avro

A binary encoding format that started out as a result of Thrift not being a good fit for Hadoop. Has two schema languages: Avro IDL for human editing, and JSON that is more machine-readable. Has most compact form of encoding, and doesn't identify fields or their datatypes. Hence, there is nothing in the encoded data to differentiate between a string and an integer.

#### Writer/Reader Schema

Writer's schema refers to when the application wants to encode data (writing to file or sending over a network), while Reader's schema is for decoding. **Key idea is that both schema's don't have to be the same, but only compatible**. Avro library resolves the differences by comparing both schemas and translating the data from the writer's schema into the reader's schema.

For schema evolution, to maintain compatibility, adding/removing fields must have a default value.

Advantage of Avro's approach is that the schema doesn't contain tag numbers and is friendlier to **dynamically generated schema**.
