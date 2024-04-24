## Names

Keywords that cannot be used as names.

```
break       case      chan      const         continue
default     defer     else      fallthrough   for
func        go        goto      if            import
interface   map       package   range         return
27          select    struct    switch        type
```

Constants, types and functions.

```
// CONSTANTS
true false iota nil

// TYPES
int int8 int16 int32 int64
uint uint8 uint16 uint32 uint64 uintptr
float32 float64 complex128 complex64
bool byte rune string error

// FUNCTIONS
make len cap new append copy close delete
complex real ima
```

## Declarations

```
var   const   type    func
```

```GO
func main() {
  const freezingF, boilingF = 32.0, 212.0
  fmt.Printf("%g°F = %g°C\n", freezingF, fToC(freezingF)) // "32°F = 0°C"
}

func fToC(f float64) float64 {
  return (f - 32) * 5 / 9
}
```

## Variables

Either type or =expression may be omitted, but not both. If expression is omitted, initial value is 0/false/nil/"".

```GO
var [name] [type] = [expression]

var i, j, k int   // int, int, int
var b, f, s = true, 2.3, "four"   // bool, float64, string
var f, err = os.Open(name)        // os.Open() function returns a file and an error

// short variable declarations for local variables where type is determined by expression
// := is declaration whereas = is assignment
anim := gif.GIF{LoopCount: nframes}
freq := rand.Float64() * 3.0
t := 0.0
```

## Variable lifetimes

Lifetime of package-level variable is the entire execution of program. Local variables have dynamic lifetimes; new instance lives on until it becomes unreachable, at which point its storage may be recycled. Compiler may choose to allocate local variables on heap or stack depending on whether they are reachable after a function is called or not.

## Assignability

Allows both implicit and explicit assignments.

```GO
mdeals := []string{"gold", "silver", "bronze"}
```

## Type declarations

```go
type [name] [underlying-type]

// both have same underlying type but are not the same type i.e. cannot use == to compare each other
// however can use == to compare values
type Celsius float64
type Fahrenheit float64
var c Celsius
var f Fahrenheit
fmt.Println(c == 0) // true
fmt.Println(c == f) // compile error: type mismatch
```

## Imports

It is an error to import a package and then not refer to it. Best to use golang.org/x/tools/cmd/goimports tool which automatically inserts and removes packages from import declaration as necessary.

## Package initialization

If package has multiple .go files, the are initialized in the order the files are given to the compiler. For variables such as tables that are difficult to set initial value, can use init().

```go
var a = b + c   // a initialized third to 3
var b = f()     // b initialized second to 2, by calling f
var c = 1       // c initialized first to 1
```

## Scope

Syntactic block is a sequence of statements enclosed in braces. The generic notion of blocks including declarations not surrounded by braces are called lexical blocks. A declaration's lexical block determines its scope. A program can contain multiple declarations of the same name so long as each declaration is in a different lexical block. At package level, order in which declarations appear has no effect on their scope.

```GO
func f() {}

var g = "g"

func main() {
  f := "f"
  fmt.Println(f) // "f"; local var f shadows package-level func f
  fmt.Println(g) // "g"; package-level var
  fmt.Println(h) // compile error: undefined: h
}


// 3 variables named x, each declared in different block
func main() {
  x := "hello"            // explicit
  for _, x := range x {   // implicit
    x := x + 'A' - 'a'    // explicit
    fmt.Printf("%c", x)   // "HELLO" (one letter per iteration)
  }
}
```

### Variable scoping

```go
{
    err := thisCouldFail()
    if err != nil {
        log.Fatal(err)
    }
}

// shorter syntax, useful for initializing condition variable and restricting scope of this variable to if block only
if statement; condition {
  // some code
}

// err is scoped inside and will shadow previous err variable declared outside block
if err := thisCouldFail(); err != nil {
  log.Fatal(err)
}
```

## Packages vs Modules

A package is a directory of .go files. Packages help to organize code into reusable components.

A module is a collection of packages with built-in dependencies and versioning. A module comes with two additional files: go.mod and go.sum.

## Structure

https://github.com/golang-standards/project-layout

### /cmd

Main applications for your project. The directory name for each application should match the name of the executable you want e.g. /cmd/myapp.

It is common to have a small main() that imports and invokes the code from internal and pkg directories.

### /internal

To prevent packages from being imported unnecessarily, can create an **internal/** package. It is a special directory name recognized by the go tool which will prevent one package from being imported by another unless both share a common ancestor i.e. a package a/b/c/internal/d/e/f can only be imported by code in the directory tree rooted at /a/b/c.

Internal packages enable you to export code for reuse in your project while reducing your public API.

You are not limited to the top level internal directory; you can have more than one internal directory at any level of your project tree.

### /pkg

Library code that is ok to be used by external applications. Other projects will import these libraries expecting them to work. It is a good way tto explicitly communicate that the code in this directory is safe for use by others.

### Helpers/Util

These functions should exist in packages that are used most often i.e. put near where they are used. Moreover, a little copying is better than a little dependency.

When deciding where to put helper/util functions, it will depend on the following:

1. Do they rely on any of their own outside dependencies?
2. Are they what is known as pure functions that just take inputs and return the same outputs?
3. Do they reference other helper functions?
4. Do they result in any side effects, such as saving data to the database?
5. Do they have a general purpose that can be used throughout the whole application, or are they meant to do things relevant to handling incoming controller requests and formulating responses?

Options are as follows:

1. Traits
2. Class inheritance
3. General service class with dependency injection
4. Simple helper functions file that gets autoloaded
5. Simple newable value objects and maybe a factory to create them to aid in testing if needed
6. Keeping them right where they are if there actually isn't much value to code re-use here (believe it or not, a little repetition is not a bad thing, but it's highly situational).
