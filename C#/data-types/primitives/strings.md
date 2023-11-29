## Strings

## String literal

```c#
 Console.WriteLine("Hello {0}! You are {1} years old.", "John", 1);
Console.WriteLine("{0}, Number {0}, Number {0}", 9);
Console.WriteLine("{1}, {0}, {2}", 10, 20, 30);
```

### Formatting numerical data

```
C/c     Currency
D/d     Decimal
E/e     Exponential notation
F/f     Fixed-point formatting
G/g     General
N/n     Basic numerical formatting
X/x     Hexadecimal formatting
```

```c#
static void FormatNumericalData()
{
  Console.WriteLine("The value 99999 in various formats:");
  Console.WriteLine("c format: {0:c}", 99999);
  Console.WriteLine("d9 format: {0:d9}", 99999);
  Console.WriteLine("f3 format: {0:f3}", 99999);
  Console.WriteLine("n format: {0:n}", 99999);
  // Notice that upper- or lowercasing for hex
  // determines if letters are upper- or lowercase.
  Console.WriteLine("E format: {0:E}", 99999);
  Console.WriteLine("e format: {0:e}", 99999);
  Console.WriteLine("X format: {0:X}", 99999);
  Console.WriteLine("x format: {0:x}", 99999);
}

/*
The value 99999 in various formats:
c format: $99,999.00
d9 format: 000099999
f3 format: 99999.000
n format: 99,999.00
E format: 9.999900E+004
e format: 9.999900e+004
X format: 1869F
x format: 1869f
*/
```

## Parsing values

The .NET data types provide the ability to generate a variable of their underlying type given a textual equivalent. This technique can be extremely helpful when you want to convert some user input data (such as a selection from a GUI-based, drop-down list box) into a numerical value.

```c#

static void ParseFromStrings()
{
  Console.WriteLine("=> Data type parsing:");
  bool b = bool.Parse("True");
  Console.WriteLine("Value of b: {0}", b);
  double d = double.Parse("99.884");
  Console.WriteLine("Value of d: {0}", d);
  int i = int.Parse("8");
  Console.WriteLine("Value of i: {0}", i);
  char c = Char.Parse("w");
  Console.WriteLine("Value of c: {0}", c);
  Console.WriteLine();
}
```

### tryParse

```c#
bool b = bool.Parse("Hello"); // this will fail at runtime

// tryparse
static void ParseFromStringsWithTryParse()
{
  Console.WriteLine("=> Data type parsing with TryParse:");
  if (bool.TryParse("True", out bool b))
  {
    Console.WriteLine("Value of b: {0}", b);
  }
  else {
    Console.WriteLine("Default value of b: {0}", b);
  }

  string value = "Hello";
  if (double.TryParse(value, out double d))
  {
    Console.WriteLine("Value of d: {0}", d);
  }
  else
  {
    Console.WriteLine("Failed to convert the input ({0}) to a double and the variable was assigned the default {1}", value, d);
  }
  Console.WriteLine();
}
```

## String concatenation

String variables can be connected using + operator. It is processed by the compiler to emit a call to the String.Concat().

```c#
string s1 = "Programming the ";
string s2 = "PsychoDrill (PTP)";
string s3 = s1 + s2;
```

## String interpolation

Bench testing has shown a significant performance improvement in string handling in C# 10 when your code contains string interpolation.

```C#
static void StringInterpolation()
{
    Console.WriteLine("=> String interpolation:\a");
    // Some local variables we will plug into our larger string
    int age = 4;
    string name = "Soren";
    // Using curly-bracket syntax.
    string greeting = string.Format("Hello {0} you are {1} years old.", name, age);
    Console.WriteLine(greeting);
    // Using string interpolation
    string greeting2 = $"Hello {name} you are {age} years old.";
    Console.WriteLine(greeting2);
}
```

## Verbatim strings

Instead of using escape characters, you can prefix a string literal with `@` symbol, which disables the processing of a literal's escape characters and print out a string as it is. This is useful when working with network paths or directory.

```c#
// The following string is printed verbatim,
// thus all escape characters are displayed.
Console.WriteLine(@"C:\MyApp\bin\Debug");

// Whitespace is preserved with verbatim strings.
string myLongString = @"This is a very
very
very
               long string";
Console.WriteLine(myLongString);

// inserting double quote into a literal string
Console.WriteLine(@"Cerebus said ""Darrr! Pret-ty sun-sets""");
```

## String comparison

Can be compared with Compare(), Equals() or with equality operator.

## StringBuilder

When using StringBuilder, you are directly modifying the object's internal character data which is more efficient than making copies of it.

```c#
using System.Text;

static void FunWithStringBuilder()
{
  Console.WriteLine("=> Using the StringBuilder:");
  StringBuilder sb = new StringBuilder("**** Fantastic Games ****");
  sb.Append("\n");
  sb.AppendLine("Half Life");
  sb.AppendLine("Morrowind");
  sb.AppendLine("Deus Ex" + "2");
  sb.AppendLine("System Shock");
  Console.WriteLine(sb.ToString());
  sb.Replace("2", " Invisible War");
  Console.WriteLine(sb.ToString());
  Console.WriteLine("sb has {0} chars.", sb.Length);
  Console.WriteLine();
}
```
