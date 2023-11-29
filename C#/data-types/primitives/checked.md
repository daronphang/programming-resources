## checked Keyword

C# provides the checked keyword that tells the compiler to emit additional CIL statements that test for **overflow conditions** when performing mathematical operations. If an overflow has occurred, you will receive a runtime exception.

```c#
static void ProcessBytes()
{
  byte b1 = 100;
  byte b2 = 250;
  byte sum = (byte)Add(b1, b2);
  // sum should hold the value 350. However, we find the value 94!
  Console.WriteLine("sum = {0}", sum);
}

static void ProcessBytes()
{
    byte b1 = 100;
    byte b2 = 250;
    // This time, tell the compiler to add CIL code
    // to throw an exception if overflow/underflow // takes place.
    try
    {
        byte sum = checked((byte)Add(b1, b2));
        Console.WriteLine("sum = {0}", sum);
    }
    catch (OverflowException ex)
    {
        Console.WriteLine(ex.Message);
    }s
}
```

### Setting project-wide overflow checking

```
<PropertyGroup>
    <CheckForOverflowUnderflow>true</CheckForOverflowUnderflow>
</PropertyGroup>
```

## unchecked Keyword

If you have enabled checked setting for project-wide, and if you have a block of code where data loss is acceptable, C# provides the unchecked keyword to disable the throwing of an overflow exception on a case-by-case basis.

```c#
// Assuming /checked is enabled,
// this block will not trigger
// a runtime exception.
unchecked
{
  byte sum = (byte)(b1 + b2);
  Console.WriteLine("sum = {0} ", sum);
}
```
