## JSON

JSON, XML and CSV can be written/read by many programming languages, and are widely supported. However, they also have subtle problems:

- There is a lot of ambiguity around the encoding of numbers i.e. cannot distinguish between number and string
- Integers greater than 2^53 cannot be represented and requires workaround i.e. Twitter's API returns tweet IDs twice, once as JSON number and another as decimal string
- JSON and XML have good support for unicode character strings but not for binary strings; workaround is to encode the binary data as text using Base64

## CSV

CSV output format is a text file with each record from the crawl per line, with columns separated by commas. Useful when data is strictly tabular, structure is known and both generation and consumption of data file is in your control.

## XML (Extensible Markup Language)

In today's world, there are many applications built on different programming languages. Exchanging of data between applications is crucial in today's networked world. However, data exchange between heterogeneous applications would be complex.

One of the methods used to combat this complexity is to use XML as the intermediate language. XML is a simple and flexible text format widely used for data storage and exchange over the internet or other networks. XML defines a set of rules for encoding documents in a format that both humans and machines can read. Enforces strict validation and can be reliably processed by programs.

XML is a markup language similar to HTML, but without predefined tags to use. Instead, you define your own tags designed specifically for your needs. Essentially, HTML was designed to focus on the presentation of content, while XML was designed to store data as structured information.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<message>
    <warning>
         Hello World
    </warning>
</message>
```

### Benefits

Has larger overhead than CSV, but with strengths as follows:

- Can validate XML data against XSD
- Can have one-to-many relations in multi-levels in XML data representation
- Can have more complex hierarchy and structure i.e. more flexibility
- More readable than CSV (debatable)
- Natively supported by .NET framework
- Have standard parsers available everywhere
- Preferred over CSV when data is unstructured i.e. unknown Schema

### WSDL

WSDL is an XML notation for describing a web service. A WSDL definition tells a client how to compose a web service request and describes the interface that is provided by the web service provider.

## Protobuf (Protocol Buffers)

Protobufs are language-neutral, platform-neutral extensible mechanisms for serializing structured data. This method relies on the use of a contract between both ends, giving you a way to validate the message i.e. requires you to declare the data structure beforehand.

You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages.

```proto
message Person {
  optional string name = 1;
  optional int32 id = 2;
  optional string email = 3;
}
```

## Thrift

Apache Thrift is a binary encoding library that requires a schema for any data that is encoded. Comes with a code generation tool that produces classes implementing the schema in various programming languages, which is useful for statically typed languages. Encoding formats for Thrift include BinaryProtocol, CompactProtocol and DenseProtocol.

Marking each field as required or optional has no effect on how the field is encoded. This will only enable a runtime check that fails if the field is not set.

```thrift
struct Person {
  1: required string          userName,
  2: optional i64             favNumber,
  3: optional list<string>    interests
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

## MessagePack

MessagePack is an efficient binary serialization format for objects that makes data exchange more efficient. It is faster and smaller than JSON. Small integers are encoded into a single byte, and typical short strings require only one extra byte in addition to the strings themselves.

MessagePack is known for its simplicity, fast setup and long list of supported languages. Unlike Protobuf, you don't have to specify the data structure beforehand i.e. no schema validation.

Though there is quite a bit of adoption in the API field, there is still a lack of API clients that support it e.g. Postman.
