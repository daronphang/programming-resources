## Binary literals

Introduced in C# 7 that can be used for creating bitmasks.

```c#
static void BinaryLiterals()
{
  //Updated in 7.2, Binary can begin with _
  Console.WriteLine("=> Use Binary Literals:");
  Console.WriteLine("Sixteen: {0}",0b_0001_0000);
  Console.WriteLine("Thirty Two: {0}",0b_0010_0000);
  Console.WriteLine("Sixty Four: {0}",0b_0100_0000);
}
```
