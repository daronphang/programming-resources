## Pass by value vs Pass by reference

**Pass by value** will pass the value of the variable into the method, or we can say that the original variable ‘copy’ the value into another memory location and pass the newly created one into the method. So, anything that happens to the variable inside the method will **not affect** the original variable value.

**Pass by reference** will pass the **memory location** instead of the value. In other words, it passes the ‘container’ of the variable to the method so, anything that happens to the variable inside the method will affect the original variable.

Everything in Go is passed by value.

### Basic types

- Default to pass by value
- To pass by reference, use pointers

### Arrays, slices

- A slice value is a header, describing a contiguous section of a backing array
- Slice value contains a pointer to the array
- Default to pass by reference

### Structs

- Default to pass by value

### Structs in slices, maps

- Default to pass by reference

```go
package main

import "fmt"

type Example struct {
	name string
	nested World
}

type World struct {
	name string
}

func testing(p []Example) {
    // Underlying values are passed by reference
	p[0].hello = "oh my world!"
}

func main() {
	p := make([]Example, 1)
	testing(p)
	fmt.Print(p[0].hello) // oh my world!
}
```

```go
package main

import "fmt"

type Example struct {
	name string
	nested World
}

type World struct {
	name string
}

func testing(p []*Example) {
    p[0] = &Example{}
	p[0].hello = "oh my world!"
}

func main() {
	p := make([]*Example, 1) // [nil]
	testing(p)
	fmt.Print(p[0].hello) // oh my world!
}
```
