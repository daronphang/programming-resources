## Passing variables

### Pass by value (default)

**Pass by value** will pass the value of the variable into the method, or we can say that the original variable ‘copy’ the value into another memory location and pass the newly created one into the method. So, anything that happens to the variable inside the method will **not affect** the original variable value. This is the **default behavior** in Go.

Passing by value is safe and straightforward, but **for large data structures, copying may become inefficient**.

### Pass by reference

**Pass by reference** will pass the **memory location** instead of the value. In other words, it passes the ‘container’ of the variable to the method so, anything that happens to the variable inside the method will affect the original variable. This introduces considerations about memory allocation.

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

## Memory management

When a program is executed, it needs to store data and instructions to execute. Memory is allocated more efficiently based on the lexical scope in which it’s created.

### Stack

Local variables and function calls are placed on the memory stack (LIFO data structure), also known as **stack allocation**. This is more efficient than relying the GC, as the Go compiler can predetermine when that memory may be freed and emit machine instructions that clean up.

### Heap

If the compiler can't determine the exact lifespan of a variable, it is placed in the **heap**, where memory is dynamically allocated. As both the compiler and runtime can make very few assumptions as to how this memory is used and when it can be cleaned up, this task is delegated to the GC.

## Memory allocation

### Pointers

When you create a pointer to a variable, Go needs to ensure that the variable lives as long as the pointer does. Hence, the variable is often allocated on the **heap** rather than the stack.

```go
// If num was stored on the stack, it would be cleaned up once the function returns
// This leaves a dangling pointer
func example() *int {
    num := 100
    return &num
}
```

### Escape analysis

Go compiler determines whether to allocate variables on stack or heap is based on a decision-making process called escape analysis.

A variable that **escapes and allocated on the heap** if:

- It is returned
- Stored in a pointer
- Captured by a goroutine
- Optimization decisions or stack size limitations
