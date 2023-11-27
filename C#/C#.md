## C#

The key difference from .NET is that C# is not a platform but a programming language. C# was created by Microsoft specifically to work with the .NET framework.

C# is object-oriented with a C-like syntax and has taken a lot from Java and C++. Since C# is a high-level language, its compilation process consists of two stages: from the C# code to intermediate language (IL), and from IL to native code (machine code).

C# versions are tied to a specific version of .NET i.e. C#10 with .NET 6 and above. This relationship between language and .NET versions gives the C# team the freedom to introduce features into C# that couldn’t otherwise be added into the language due to framework limitations.

As C# is a hybrid of numerous languages, the result is a product that is as syntactically clean as (if not cleaner than) Java provides just about as much power and flexibility as C++. Core features include:

- No pointers required
- Automatic memory management through garbage collection (does not support 'delete' keyword)
- Formal syntactic constructs for classes, interfaces, structures, enumerations and delegates
- C++ ability to overload operators for a custom type without the complexity
- Support for attribute-based programming that allows you to annotate types and their members to further qualify their behavior

## C# program

C# demands that all program logic be contained with a type definition. A type is a general term referring to a member of the set: class, interface, structure, enumeration, and delegate. Unlike other languages, it is **not possible** to create global functions or global points of data.

## Console app

```c#
using System; // a semicolon indicates the end of a statement
namespace Basics
{ // an open brace indicates the start of a block
    class Program
    {
        static void Main(string[] args)
        {
        Console.WriteLine("Hello World!"); // a statement }
        }
    } // a close brace indicates the end of a block
}
```
