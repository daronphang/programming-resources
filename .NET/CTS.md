## CTS Types

### CTS Class Types

Every .NET language supports the notion of a class type, which is the cornerstone of OOP. A class may be composed of any number of members (such as constructors, properties, methods, and events) and data points (fields).

```c#
class Calc {
  public int Add(int addend1, int addend2)
  {
    return addend1 + addend2;
  }
}
```

### CTS Interface Types

Interfaces are nothing more than a named collection of abstract member defintions and/or default implementations, which are implemented by a given class or structure.

```c#
// C# interface is usually declared as public, to allow
// types in other assemblies to implement their behavior
public interface IDraw
{
  void Draw();
}
```

### CTS Structure Types

A structure can be thought of as a lightweight class type having value-based semantics. Typically, structures are best suited for modeling geometric and mathematical data and are created in C# using the struct keyword.

```c#
struct Point
{
  // Structures can contain fields.
  public int xPos, yPos;
  // Structures can contain parameterized constructors.
  public Point(int x, int y)
  { xPos = x; yPos = y;}
  // Structures may define methods.
  public void PrintPosition()
  {
    Console.WriteLine("({0}, {1})", xPos, yPos);
  }
}
```

### CTS Enumeration Types

Enumerations are a handy programming construct that allow you to group name-value pairs. Also, the CTS demands that enumerated types derive from a common base class, System.Enum.

```c#
enum CharacterTypeEnum
{
  Wizard = 100,
  Fighter = 200,
  Thief = 300
}
```

### CTS Delegate Types

Delegates are the .NET equivalent of a type-safe, C-style function pointer. The key difference is that a .NET delegate is a class that derives from System.MulticastDelegate, rather than a simple pointer to a raw memory address. In C#, delegates are declared using the delegate keyword.

Delegates are critical when you want to provide a way for one object to forward a call to another object and provide the foundation for the .NET event architecture.

```c#
delegate int BinaryOp(int x, int y);
```

## CTS Data Types

| CTS Data Type  | VB Keyword | C# Keyword |
| -------------- | ---------- | ---------- |
| System.Byte    | Byte       | byte       |
| System.SByte   | SByte      | sbyte      |
| System.Int16   | Short      | short      |
| System.Int32   | Integer    | int        |
| System.Int64   | Long       | long       |
| System.UInt16  | UShort     | ushort     |
| System.UInt32  | UInteger   | uint       |
| System.UInt64  | ULong      | ulong      |
| System.Single  | Single     | float      |
| System.Double  | Double     | double     |
| System.Object  | Object     | object     |
| System.Char    | Char       | char       |
| System.String  | String     | string     |
| System.Decimal | Decimal    | decimal    |
| System.Boolean | Boolean    | bool       |
