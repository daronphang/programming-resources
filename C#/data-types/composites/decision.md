## Decision constructs

### Pattern matching

```
and
not
or
type
relational
```

```c#
static void IfElsePatternMatchingUpdatedInCSharp9()
{
    Console.WriteLine("======= C# 9 If Else Pattern Matching Improvements =======");
    object testItem1 = 123;
    Type t = typeof(string);
    char c = 'f';
    //Type patterns
    if (t is Type)
    {
        Console.WriteLine($"{t} is a Type");
    }
    //Relational, Conjuctive, and Disjunctive patterns
    if (c is >= 'a' and <= 'z' or >= 'A' and <= 'Z')
    {
        Console.WriteLine($"{c} is a character");
    };
    //Parenthesized patterns
    if (c is (>= 'a' and <= 'z') or (>= 'A' and <= 'Z') or '.' or ',')
    {
        Console.WriteLine($"{c} is a character or separator");
    };
    //Negative patterns
    if (testItem1 is not string)
    {
        Console.WriteLine($"{testItem1} is not a string");
    }
    if (testItem1 is not null)
    {
        Console.WriteLine($"{testItem1} is not null");
    }
    Console.WriteLine();
}

```

### Logical operators

```
&&      short-circuit
||      short-circuit
!       NOT operator
```

### switch

```c#
static void SwitchExample()
{
    Console.WriteLine("1 [C#], 2 [VB]");
    Console.Write("Please pick your language preference: ");
    string langChoice = Console.ReadLine();
    int n = int.Parse(langChoice);
    switch (n) {
        case 1:
        Console.WriteLine("Good choice, C# is a fine language.");
        break;
        case 2:
        Console.WriteLine("VB: OOP, multithreading, and more!");
        break;
        default:
        Console.WriteLine("Well...good luck with that!");
        break;
    }
}
```
