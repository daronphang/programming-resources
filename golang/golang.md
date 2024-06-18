## Golang

A compiled language. Organized into packages (similar to libraries/modules). Has a cultural agenda of radical simplicity with garbage collection, package system, first-class functions (treated like any other variable), lexical scope, system call interface and immutable strings encoded in UTF-8 (can process in all languages). Language is mature, stable and guarantees backwards compatibility. Well suited for building infrastructure like network servers, tools and systems for programmers.

Static type language as compared to Python/Javascript (dynamic type). Dynamic means you can declare a variable as a string and later assign it as number.

### Hello World

A package can have many related files ending with .go with requirement that every file must declare the package it belongs to. Two types of packages: executable (generates a file that can be run, package main) and reusable/dependency (code used as "helpers", good place to put reusable logic). For package main, it must have a function called "main".

https://pkg.go.dev/std

```GO
package main    // refers to project or workspace

import "fmt"

func main() {
  fmt.Println("Hello world!")
}
```

## Naming conventions

### File names

Filenames should be lowercase with underscores.

### Variables

Names in Go should:

- Use MixedCase (capitalize first letter if public)
- No underscores
- Acronyms should be all capitals e.g. ServeHTTP
- Be kept short as long names obscure what the code does e.g. i to index

### Packages

Package names are short and clear, lowercase, with no underscores or camelCases. A package name and its contents are coupled.

Break up generic packages i.e. packages named util, interfaces, common or misc provide clients with no sense what the package contains, grows without bound, accumulates dependencies, and collides with other imports.

Organize packages by responsibility i.e. organizing types together in package models should be avoided. Instead, the individual types/structs should be declared in their respective packages.

## Go CLI

```
go build      Compiles code but does not execute
go run        Compiles and execute one or two files
go fmt        Formats all code in each file in current directory
go install    Compiles and installs a package
go get        Downloads raw source code of someone else's package
go test       Runs any tests associated with current project
```

```sh
$ go build test.go
$ ls
$ ./test
$ rm test
```

### get vs install

The go get command is primarily used for retrieving remote packages from version control repositories and making them available for use in your projects. When you run `go get`:

- Go downloads the source code of the package and its dependencies within your **workspace's bin and pkg directories**
- Updates packages to their latest versions if you have already installed them

The go install command operates on the local codebase residing in your development environment:

- Fetches remote packages and their dependencies
- Compiles and installs the package present in your local code repository (GOPATH) and makes them **executable**

## Garbage collector

GO's garbage collector recycles unused memory but DO NOT assume it will release unused operating system resources like open files and network connections. **They should be closed explicitly**.

## Variable declarations

```GO
s := "Hello world"    // colon syntax used for assigning NEW variables only
var s string = "Hello world"
s = "Awesome!"    // equal syntax for reassigning variables
```
