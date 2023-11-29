## Numeric

```c#
static void DataTypeFunctionality()
{
  Console.WriteLine("=> Data type Functionality:");
  Console.WriteLine("Max of int: {0}", int.MaxValue);
  Console.WriteLine("Min of int: {0}", int.MinValue);
  Console.WriteLine("Max of double: {0}", double.MaxValue);
  Console.WriteLine("Min of double: {0}", double.MinValue);
  Console.WriteLine("double.Epsilon: {0}", double.Epsilon);
  Console.WriteLine("double.PositiveInfinity: {0}",
    double.PositiveInfinity);
  Console.WriteLine("double.NegativeInfinity: {0}",
    double.NegativeInfinity);
  Console.WriteLine();
}
```

## System.Numerics namespace

The System.Numerics namespace defines a structure named BigInteger. After you assign a value to a BigInteger variable, you cannot change it, as the data is immutable. however, the BigInteger class defines a number of members that will return new BigInteger objects based on your data modifications.

```c#
using System.Numerics;

static void UseBigInteger()
{
  Console.WriteLine("=> Use BigInteger:");
  BigInteger biggy =
    BigInteger.Parse("9999999999999999999999999999999999999999999999");
  Console.WriteLine("Value of biggy is {0}", biggy);
  Console.WriteLine("Is biggy an even value?: {0}", biggy.IsEven);
  Console.WriteLine("Is biggy a power of two?: {0}", biggy.IsPowerOfTwo);
  BigInteger reallyBig = BigInteger.Multiply(biggy,
    BigInteger.Parse("8888888888888888888888888888888888888888888"));
  Console.WriteLine("Value of reallyBig is {0}", reallyBig);
}
```
