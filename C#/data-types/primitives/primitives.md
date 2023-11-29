## Primitive data types

| C# shorthand | CLS compliant? | System type | Range                                                   | Meaning                         |
| ------------ | -------------- | ----------- | ------------------------------------------------------- | ------------------------------- |
| bool         | Yes            | Boolean     | true, false                                             | Truthy or falsity               |
| sbyte        | No             | SByte       | -128 to 127                                             | Signed 8-bit number             |
| byte         | Yes            | Byte        | 0 to 255                                                | Unsigned 8-bit number           |
| short        | Yes            | Int16       | -32,768 to 32,767                                       | Signed 16-bit number            |
| ushort       | No             | UInt16      | 0 to 65,535                                             | Unsigned 16-bit number          |
| int          | Yes            | Int32       | -2,147,483,648 to 2,147,483,647                         | Signed 32-bit number            |
| uint         | No             | UInt32      | 0 to 4,294,967,295                                      | Unsigned 32-bit number          |
| long         | Yes            | Int64       | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | Signed 64-bit number            |
| ulong        | No             | UInt64      | 0 to 18,446,744,073,709,551,615                         | Unsigned 64-bit number          |
| char         | Yes            | Char        | U+0000 to U+ffff                                        | Single 16-bit Unicode character |
| float        | Yes            | Single      | -                                                       | 32-bit floating-point number    |
| double       | Yes            | Double      | -                                                       | 64-bit floating-point number    |
| decimal      | Yes            | Decimal     | -                                                       | 128-bit signed number           |
| string       | Yes            | String      | Limited by system memory                                | A set of Unicode characters     |
| object       | Yes            | Object      | Can store any data type in an object variable           | Base class of all types         |

## default, new Operator

The default literal assigns a variable the default value for its data type.

```c#
static void DefaultDeclarations()
{
  Console.WriteLine("=> Default Declarations:");
  int myInt = default;
  Console.WriteLine(myInt);
}
```

All intrinsic data types support what is known as a default constructor. This feature allows you to create a variable using the new keyword, which automatically sets the variable to its default value.

```
bool        False
Numeric     0
char        empty character
object      null
string      null
```

## System.Object

You can invoke any of data type's public members directly without the need to create a variable.

```c#
Console.WriteLine("12.GetHashCode() = {0}", 12.GetHashCode());
Console.WriteLine("12.Equals(23) = {0}", 12.Equals(23));
Console.WriteLine("12.ToString() = {0}", 12.ToString());
Console.WriteLine("12.GetType() = {0}", 12.GetType());
```
