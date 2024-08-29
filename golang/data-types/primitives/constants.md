## Constants

Can declare a sequence of constants as a group. Can also use constant generator iota which is used to create a sequence of related values. Value of iota begins at 0 and increments by 1 for each item in sequence i.e. enumerator.

```go
const (
  a = 1
  b
  c = 2
  d
)

fmt.Println(a, b, c, d)   // 1 1 2 2

// iota generator
type Weekday int
const (
  Sunday Weekday = iota // 0
  Monday                // 1
  Tuesday               // 2
)
```

## Iota

Iota is an identifier that is used with `constant` and can simplify constant definitions that use auto-increment numbers.

```go
package main

import "fmt"

const (
    Summer = iota
    Winter  // auto incremented
    Autumn
)

const (
    A = iota + 1
    _   // Skip a value
    B
    C
)

func main() {
    fmt.Println(Summer, Winter, Autumn) // 0,1,2
}
```
