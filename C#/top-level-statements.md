## Top-level statements

Prior to C# 9.0, all .NET Core applications must have a main(). Top-level statements eliminate the need for much of the ceremony around C# application's entry point i.e. class (program) and Main() can be removed.

```C#
Console.WriteLine("***** My First C# App *****");
Console.WriteLine("Hello World!");
Console.WriteLine();
// Wait for Enter key to be pressed before shutting down.
Console.ReadLine();
```

### Rules

- Only one file in the application can use top-level statements
- Program cannot have a declared entry point
- Top-level statements cannot be enclosed in a namespace
- Top-level statements still access a string array of args
- Top-level statements return an application code by using return
- Functions that would have been declared in the Program class become local functions for the top-level statements
- Top-level statements compile to a class named Program, allowing for the addition of a partial Program class to hold regular methods
- Additional types can be declared after all top-level statements
- Types declared before the end of top-level statements will result in a compilation error

### Specifying an error code

The ability to return an int keeps C# consistent with other C-based languages. By convention, returning 0 indicates the program has terminated successfully, while another value represents an error condition. If nothing is explicitly returned, it defaults to 0.

On Windowss, the application's return value is stored within a system environment variable named `%ERRORLEVEL%`.

```batch
@echo off
rem A batch file for SimpleCSharpApp.exe
rem which captures the app's return value.
dotnet run
@if "%ERRORLEVEL%" == "0" goto success
:fail
  echo This application has failed!
  echo return value = %ERRORLEVEL%
  goto end
:success
  echo This application has succeeded!
  echo return value = %ERRORLEVEL%
  goto end
:end
echo All Done.
```
