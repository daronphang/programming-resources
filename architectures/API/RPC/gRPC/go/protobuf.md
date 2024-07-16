## go_package

If you want to import proto definitions from one file to another, you need to make sure go_package is properly defined. The protoc compiler will use the go_package to generate a go file that will include the package of the imported file. Use the absolute path from the module in go.mod e.g. protobuf/common.

When referencing a message from another proto file, use the namespace provided by the package name e.g. common.HeartBeat.

```proto
syntax = "proto3";

package common;
option go_package = "protobuf/common";

message HeartBeat {
    string message = 1;
}
```

```proto
syntax = "proto3";

package message;
option go_package = "protobuf/message";

service Message {
    rpc heartbeat(google.protobuf.empty) returns (common.HeartBeat) {}
}
```
