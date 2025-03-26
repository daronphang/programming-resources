## Passing variables

### Pass by value (default)

**Pass by value** will pass the value of the variable into the method, or we can say that the original variable ‘copy’ the value into another memory location and pass the newly created one into the method. So, anything that happens to the variable inside the method will **not affect** the original variable value. This is the **default behavior** in Go.

Passing by value is safe and straightforward, but **for large data structures, copying may become inefficient**.

### Pass by reference

**Pass by reference** will pass the **memory location** instead of the value. In other words, it passes the ‘container’ of the variable to the method so, anything that happens to the variable inside the method will affect the original variable. This introduces considerations about memory allocation.

### Primitive types

- Default to pass by value
- To pass by reference, use pointers

### Arrays

- Arrays by default are passed by value

### Slices

- When you pass a slice to a function, you are passing a reference to the underlying array i.e. default to pass by reference
- However, the **slice itself is passed by value** i.e. the function receives a copy of the slice header that describes a contiguous section of a backing array, but it still refers to the same underlying array
- To modify existing slice, use a pointer

```go
package main

import "fmt"

func myFunc(s []int) {
    s[0] = 10
    s = append(s, 6)
}

func main() {
    mySlice := []int{1, 2, 3, 4, 5}
    myFunc(mySlice)
	fmt.Println(mySlice)

	// Output: [10 2 3 4 5]
	// append() creates a new slice, and the modified slice header
	// inside myFunc does not affect the original slice header in the
	// main function. Hence, the original slice remains unchanged,
	// and its length and capacity are still the same.
}
```

### Maps

- Default to pass by reference

### Structs

- Default to pass by value

### Structs in slices, maps

- For slices, although structs in slices are passed by value, but because the slice holds references to the original elements, it will affect the original slice
- For maps, the actual struct is **passed by value**; need to assign the struct back into the key if you want to modify. Alternatively, assign pointers to keys in maps

```go
type Person struct {
	Name string
	Age  int
}

func testing(arr []Person) {
	arr[0].Name = "hello world!"
	mary := arr[1]   // This copies the struct.
	mary.Age = 12345 // This will not modify existing slice.
}

func main() {
	arr := []Person{
		{Name: "john", Age: 10},
		{Name: "Mary", Age: 25},
	}
	testing(arr)
	fmt.Println(arr) // [{hello world! 10} {Mary 25}]
}

```

```go
package main

import "fmt"

type Person struct {
    Name string
    Age  int
}

func modifyMap(m map[string]Person) {
    p := m["Alice"] // This struct is passed by value.
    p.Age = 100 // This will not change the original struct in the map.
    m["Alice"] = p // This explicitly sets the updated struct back to the map.
}

func main() {
    people := map[string]Person{
        "Alice": {"Alice", 30},
        "Bob":   {"Bob", 25},
    }

    fmt.Println(people) // Before modification
    modifyMap(people)
    fmt.Println(people) // After modification
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
