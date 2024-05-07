## Command line arguments

OS package provides functions and other values for dealing with OS; command-line arguments are available to a program in a variable named Args which is a slice of strings.

```GO
// ECHO program in linux
package main
import (
  "fmt"
  "os"
)

func main() {
  var s, sep string     // explicit var declaration s and sep of type string

  // := is a short variable declaraton, i++ is increment statement of 1
  for i := 1; i < len(os.Args); i++ {
    s += sep + os.Args[i]   // string concatenation
    sep = " "
  }
  fmt.Println(s)
}

// ECHO program printing command-line args
func main() {
  s, sep := "", ""

  // range produces index (not needed) and element value pair, but requires to deal with both values
  // GO does not permit unused local variables; solution is to use blank identifier
  for _, arg := range os.Args[1:] {
    s += sep + arg
    sep = " "
  }
  fmt.Println(s)    // alternative is fmt.Println(strings.Join(os.Args[1:], " "))
}
```
