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
