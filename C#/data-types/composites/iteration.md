## Iteration constructs

### for Loop

```c#
for (int i = 0; i < args.Length; i++)
{
  Console.WriteLine("Arg: {0}", args[i]);
}

foreach(string arg in args)
{
  Console.WriteLine("Arg: {0}", arg);
}
```

### foreach

```c#
static void ForEachLoopExample()
{
  string[] carTypes = {"Ford", "BMW", "Yugo", "Honda" };
  foreach (string c in carTypes)
  {
    Console.WriteLine(c);
  }
  int[] myInts = { 10, 20, 30, 40 };
  foreach (int i in myInts)
  {
    Console.WriteLine(i);
  }
}
```

### while

```c#
static void WhileLoopExample()
{
  string userIsDone = "";
  while(userIsDone.ToLower() != "yes")
  {
    Console.WriteLine("In while loop");
    Console.Write("Are you done? [yes] [no]: ");
    userIsDone = Console.ReadLine();
  }
}
```

### do while

Guaranteed to execute the block of code at least once.

```c#
static void DoWhileLoopExample()
{
  string userIsDone = "";
do {
    Console.WriteLine("In do/while loop");
    Console.Write("Are you done? [yes] [no]: ");
    userIsDone = Console.ReadLine();
  }while(userIsDone.ToLower() != "yes"); // Note the semicolon!
}
```
