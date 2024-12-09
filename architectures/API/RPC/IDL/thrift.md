## Thrift

Thrift is a language agnostic software stack with an associated code generation mechanism for RPC. Thrift provides clean abstractions for data transport data serialization, and application level processing. Apache Thrift is a set of code-generation tools that allows developers to build RPC clients and servers by just defining the data types and service interfaces in a simple definition file.

https://github.com/creditkarma/thrift-typescript/blob/master/README.md

### Serialization and deserialization

The serialization format chosen during the write process determines how the data is deserialized on the receiving side. Thrift provides multiple formats for serializing data:

- Binary (default)
- JSON (through TJSONProtocol)
- Compact (throughTCompactProtocol)

```thrift
struct Person {
  1: string name;
  2: i32 age;
}
```

```go
transport := thrift.NewTMemoryBufferLen(512)
protocol := thrift.NewTBinaryProtocolTransport(transport)

// Serialization
person := Person{"Alice", 30}
err := person.Write(protocol)

// Deserialization
var newPerson Person
err := newPerson.Read(protocol)
```

## IDL

### Data types

```
bool
byte (8-bit integer)
i16 (16-bit integer)
i32 (32-bit integer)
i64 (64-bit integer)
double (double-precision floating number)
string
binary
```

### Containers

```
list<t1>
set<t1>
map<t1,t2>
```

### Namespaces

Namespaces offer a convenient way of organizing (or isolating) your code. Namespaces may also be used to prevent name clashes between type definitions. Each Thrift file is in its own namespace allowing you to use the same identifier in multiple Thrift files.

### Includes

Enables reuse and improve modularity/organization.

```
include "firstInterface/PointD.thrift"
```

### Structs

Structs are used to define complex data types with named fields. Each field in a struct is assigned a unique identifier (ID) and has a specific data type. Fields can be marked as **optional** or **required**. Nesting of structs is supported.

```thrift
struct User {
  1: i32 id
  2: required string name
  3: optional bool is_active
}

struct PointD {
  1: i32 x;
  2: i32 y;
  3: i32 z;
}

struct PointDLists{
  1: string name ="pointLists";
  2: list<PointD> firstList;
  3: list<PointD> secondList;
}
```

### Enums

```thrift
enum Operation {
  ADD = 1,
  SUBTRACT = 2,
  MULTIPLY = 3,
  DIVIDE = 4
}
```

### Unions

Unlike structs, which can hold multiple fields simultaneously, a union can only hold one field at a time.

```thrift
union Result {
  1: string message
  2: i32 errorCode
}
```

## Annotations

### go.tag

The go.tag is used to define tags when generating Go code from Thrift IDL file. These tags can be used to control how the generated Go structs serialize and deserialize data. It is commonly used for customizing JSON tags, adding validation tags, and integrating with third-party libraries that use Go struct tags for serialization or validation.

```thrift
struct Product {
  1: string ProductName (go.tag = "json:product_name,validate:not_empty");
  2: i32 ProductPrice (go.tag = "json:product_price,validate:positive");
}
```

```go
type Product struct {
  ProductName string `thrift:"ProductName,1" json:"product_name" validate:"not_empty"`
  ProductPrice int32 `thrift:"ProductPrice,2" json:"product_price" validate:"positive"`
}
```

## Example

```thrift
struct Location {
    1: required double latitude;
    2: required double longitude;
}

struct Tweet {
    1: required i32 userId;
    2: required string userName;
    3: required string text;
    4: optional Location loc; // include other Struct
    16: optional string language = "english" // set default value
}
```
