## Creating errors

```go
// simple string-based error
err1 := errors.New("math: square root of negative number")

// with formatting
err2 := fmt.Errorf("math: square root of negative number %g", x)
```

## Custom errors

```go
type SyntaxError struct {
    Line int
    Col  int
}

func (e *SyntaxError) Error() string {
    return fmt.Sprintf("%d:%d: syntax error", e.Line, e.Col)
}
```

## Panic

During a typical panic, normal execution stops, all deferred function calls are executed, and the program crashes with log message. Can be called directly and accepts any value as an argument.

```go
switch s:= suit(drawCard()); s {
  case "Spades": // ...
  case "Hearts": // ...
  default:
    panic(fmt.Sprintf("invalid suit %q", s))
}
```

Should only be used in cases where the program cannot continue execution i.e. unrecoverable error. Any deferred f unctions are executed and then the control returns to its caller.

```go
func panic(interface{})   // arg passed will be printed when the program terminates
```

## Recover

Recover is a built-in function that regains control of a panicking goroutine. Recover is **only useful inside deferred functions**. During normal execution, a call to recover will return nil and has no other effect. If the current goroutine is panicking, a call to recover will capture the value given to panic and resume normal execution.

If built-in function is called within a deferred function and function containing the defer statement is panicking, recover ends the current state of panic and returns the panic value. The function panicking does not continue where it left off but returns normally.

If recover is called at any other time, it has no effect and returns nil. For instance, web server encountering an unexpected problem could close the connection rather than leave client hanging, or update to data structure was not complete.

```go
package main

import "fmt"

func main() {
    f()
    fmt.Println("Returned normally from f.")
}

func f() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered in f", r)
        }
    }()
    fmt.Println("Calling g.")
    g(0)
    fmt.Println("Returned normally from g.")
}

func g(i int) {
    if i > 3 {
        fmt.Println("Panicking!")
        panic(fmt.Sprintf("%v", i))
    }
    defer fmt.Println("Defer in g", i)
    fmt.Println("Printing in g", i)
    g(i + 1)
}

/*
Calling g.
Printing in g 0
Printing in g 1
Printing in g 2
Printing in g 3
Panicking!
Defer in g 3
Defer in g 2
Defer in g 1
Defer in g 0
Recovered in f 4
Returned normally from f.
*/
```

```go
func RequestCancelRecover() gin.HandlerFunc {
	return func(c *gin.Context) {
		defer func() {
			if err := recover(); err != nil {
				log.Println("client canceled the request")
				c.Request.Context().Done()
			}
		}()
		c.Next()
	}
}
```
