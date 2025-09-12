## Protocol Buffers

Protocol buffers provide a **language/platform-agnostic extensible mechanism for serializing structured data in a forward/backward compatible way** i.e. similar to JSON but faster. Can be extended with new information without invalidating data or requiring code to be updated. Most often used for defining communications protocols and for data storage.

Protocol buffers are a combination of the definition language (created in .proto files), the code that the proto compiler generates to interface with the data, language-specific runtime libraries, and the serialization format for data that is written to a file or sent across a network.

The proto compiler is invoked at build-time on .proto files to generate code in various programming languages.

Language compatibility extends across C++, C#, Java, Kotlin, Objective-C, PHP, Python, Go, Dart and Ruby.

```proto
syntax = "proto3";

/* some comment */

message Person {
  optional string name = 1;
  optional int32 id = 2;
  optional string email = 3;
}
```

## Field types

Can be scalar (integer, string) or composite.

### Scalar

```
double
float
int32
int64
uint32
uint64
fixed32
fixed64
bool
string
bytes
```

### Default

When a message is parsed, if the encoded message does not contain a particular singular element, the corresponding field in the parsed object is set to the default value for that field.

```
string      ""
bytes       empty bytes
bool        False
numeric     0
enums       0
```

### Enumerations

Useful when defining a message type with one field within a pre-defined list of values. Enumerator constants must be in the range of a 32-bit integer (negative values are not recommended).

Every enum definition **must** contain a constant that maps to zero as its first element so that it can be used as a numeric default value.

```proto
enum Corpus {
  CORPUS_UNSPECIFIED = 0;
  CORPUS_UNIVERSAL = 1;
  CORPUS_WEB = 2;
  CORPUS_IMAGES = 3;
  CORPUS_LOCAL = 4;
  CORPUS_NEWS = 5;
  CORPUS_PRODUCTS = 6;
  CORPUS_VIDEO = 7;
}
message SearchRequest {
  string query = 1;
  int32 page_number = 2;
  int32 result_per_page = 3;
  Corpus corpus = 4;
}
```

## Field numbers

```
1-15            One byte encoding
16-2047         Two bytes encoding
19000-19999     Reserved for Protocol Buffers implementation
```

Each field has a unique number. These field numbers are used to identify your fields in the message binary format. This number **cannot be changed once your message type is in use** because it identifies the field in the message wire format.

For most-frequently-set fields, use field numbers 1-15 as they take less space in the wire format.

Field numbers **should never be reused**. Reusing a field number makes decoding wire-format messages ambiguous. Encoding a field using one definition and then decoding that same field with a different definition can lead to:

- Developer time lost to debugging
- A parse/merge error (best case scenario)
- Leaked PII/SPII
- Data corruption

## Field rules

```
singular    Zero or one of this field (default for proto3)
optional    Same as singular, but can check if value was explicitly set
repeated    Order of repeated values will be preserved
map         Paired key/value
```

For optional fields, if the field is unset, it will not be serialized to the wire.

## Reserved fields

If you update a message type by removing a field, future users can reuse the field number which can cause severe issues for backwards compatibility. To prevent this, can mark fields as reserved.

Cannot mix field names and field numbers in the same reserved statement.

```proto
/* can specify field number of name */
message Foo {
  reserved 2, 15, 9 to 11;
  reserved "foo", "bar";
}
```

## Importing definitions

```
import "myproject/test.proto";
```

## Nesting

```proto
/* list of results */
message SearchResponse {
  message Result {
    string url = 1;
    string title = 2;
    repeated string snippets = 3;
  }
  repeated Result results = 1;
}
```
