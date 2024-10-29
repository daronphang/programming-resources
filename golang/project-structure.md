## Project structure

https://github.com/golang-standards/project-layout

### /cmd

Main applications for your project. The directory name for each application should match the name of the executable you want e.g. /cmd/myapp.

It is common to have a small main() that imports and invokes the code from internal and pkg directories.

### /internal

To prevent packages from being imported unnecessarily, can create an **internal/** package. It is a special directory name recognized by the go tool which will prevent one package from being imported by another unless both share a common ancestor i.e. a package a/b/c/internal/d/e/f can only be imported by code in the directory tree rooted at /a/b/c.

Internal packages enable you to export code for reuse in your project while reducing your public API.

You are not limited to the top level internal directory; you can have more than one internal directory at any level of your project tree.

### /pkg

Library code that is ok to be used by external applications. Other projects will import these libraries expecting them to work. It is a good way to explicitly communicate that the code in this directory is safe for use by others.

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
