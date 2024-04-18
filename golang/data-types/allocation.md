## Allocation

Go has two allocation primitives, the built-in functions new and make. They do different things and apply to different types.

### new()

new() allocates memory for a new zeroed value for a specified type T and returns a pointer to it. It is primarily used for initializing and obtaining a pointer to a newly allocated zeroed value of a given type, usually for data types like structs.

```go
package main

import "fmt"

type Person struct {
    Name 	string
    Age  	int
    Gender 	string
}

func main() {
    // Using new() to allocate memory for a Person struct
    p := new(Person)

    // Initializing the fields
    p.Name = "John Doe"
    p.Age = 30
    p.Gender = "Male"

    fmt.Println(p)
}
```

### make()

make() is used for initializing slices, maps, and channels; data structures that require runtime initialization. Unlike new(), make() returns an initialized (non-zeroed) value of a specified type T.

```go
package main

import "fmt"

func main() {
    // Using make() to create a slice with a specified length and capacity
    s := make([]int, 10, 15)

    // Initializing the elements
    for i := 0; i < 10; i++ {
        s[i] = i + 1
    }

    fmt.Println(s)
}
```
