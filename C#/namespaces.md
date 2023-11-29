## Namespaces

A namespace is a grouping of semantically related types contained in an assembly or possibly spread across multiple related assemblies. For example, the System.IO namespace contains file I/O-related types, the System.Data namespace defines basic database types, etc.

The key difference between this approach and a language-specific library is that any language targeting the .NET runtime uses the same namespaces and same types.

In C#, the using keyword simplifies the process of referencing types defined in a particular namespace.

## Importing globally

C#10 introduced a new keyword `global using` to simplify importing common namespaces. You only need to import a namespace in one .cs file once, and it will be available throughout all .cs files. It is recommended to create a separate file for those statements.

```c#
// GlobalUsings.cs
global using System;
global using System.Linq;
global using System.Collections.Generic;
```

They can also be placed in the project file for the application:

```
<ItemGroup>
  <Using Include=”System.Text” />
  <Using Include=”System.Text.Encodings.Web” />
  <Using Include=”System.Text.Json” />
  <Using Include=”System.Text.Json.Serialization” />
</ItemGroup>
```

### Implicit global using statements

Another new feature included with .NET 6/C# 10 are implicit global using statements.

| .NET Application Type                     | Implicit global using namespaces                                                                                                                                                                |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Client (Microsoft.NET.Sdk)                | System System.Collections.Generic System.IO System.Linq System.Net.Http System.Threading System.Threading.Tasks                                                                                 |
| Web (Microsoft.NET.Sdk.Web)               | System.Net.Http.Json Microsoft.AspNetCore.Builder Microsoft.AspNetCore.Hosting Microsoft.AspNetCore.Http Microsoft.AspNetCore.Routing Microsoft.Extensions.Hosting Microsoft.Extensions.Logging |
| Worker Service (Microsoft.NET.Sdk.Worker) | Microsoft.Extensions.Configuration Microsoft.Extensions.DependencyInjection Microsoft.Extensions.Hosting Microsoft.Extensions.Logging                                                           |

To disable the settings, update the project file:

```
<PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>disable</ImplicitUsings>
</PropertyGroup>
```

## File scoped namespaces

Also new in C# 10, file-scoped namespaces remove the need to wrap your code in braces when placing it in a custom namespace.

```c#
namespace CalculatorExamples
class Calculator()
{
...
}
```
