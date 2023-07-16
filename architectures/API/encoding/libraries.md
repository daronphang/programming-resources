## Binary Encoding Libraries

Examples include Apache Thrift, Protocol Buffers, and Avro.

## Thrift, Protocol Buffers

Apache Thrift and Google Protocol Buffers are binary encoding libraries that require a schema for any data that is encoded. Each come with a code generation tool that produces classes implementing the schema in various programming languages, which is useful for statically typed languages. Encoding formats for Thrift include BinaryProtocol, CompactProtocol and DenseProtocol.

Marking each field as required or optional has no effect on how the field is encoded. This will only enable a runtime check that fails if the field is not set.

```thrift
// thrift
struct Person {
    1: required string          userName,
    2: optional i64             favNumber,
    3: optional list<string>    interests
}
```

```proto
// proto
message Person {
    required string user_name       = 1;
    optional int64 fav_number       = 2;
    repeated string interests       = 3;
}
```

### Evolution

An encoded record is the concatenation of its encoded fields, whereby each field is identified by its tag number that is critical. The name of a field can be changed, but not the field's tag, since it would make all existing encoded data invalid.

For forward compatibility, new fields with new tag numbers that are not recognized are ignored by the old code.

For backward compatibility, as long as each field has a unique tag number, the new code can always read old data. Only detail is that new fields cannot be made required.

## Avro

A binary encoding format that started out as a result of Thrift not being a good fit for Hadoop. Has two schema languages: Avro IDL for human editing, and JSON that is more machine-readable. Has most compact form of encoding, and doesn't identify fields or their datatypes. Hence, there is nothing in the encoded data to differentiate between a string and an integer.

### Writer/Reader Schema

Writer's schema refers to when the application wants to encode data (writing to file or sending over a network), while Reader's schema is for decoding. **Key idea is that both schema's don't have to be the same, but only compatible**. Avro library resolves the differences by comparing both schemas and translating the data from the writer's schema into the reader's schema.

For schema evolution, to maintain compatibility, adding/removing fields must have a default value.

Advantage of Avro's approach is that the schema doesn't contain tag numbers and is friendlier to **dynamically generated schema**.
