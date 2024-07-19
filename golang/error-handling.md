## Naming

Error types end in "Error" and error variables start with "err".

```go
type ParseError struct {}
func (e ParseError) Error() string {
    return "hello world"
}

const errBadAction = errors.New("hello world")
```

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

## Wrapping and unwrapping

Wrapping errors means adding more contextual information to the error which has been returned. For example, the additional information could be the type of error, the cause of the error, or the name of the function where the error is raised.

Wrapping is very useful for debugging since you can precisely and quickly locate the source of the problem.

### Whether to wrap

When adding additional context to an error, either with fmt.Errorf or by implementing a custom type, you need to decide whether the new error should wrap the original. There is no single answer to this question; it depends on the context in which the new error is created. Wrap an error to expose it to callers. Do not wrap an error when doing so would expose implementation details.

### Syntax

First we need to create a new error using errors.New(), followed by fmt.Errorf() with the %w verb to wrap the error.

```go
var ErrorCritical = errors.New("critical error")
// ...
wrapped := fmt.Errorf("[functionName] internal error: %w", ErrorCritical)

fmt.Println(errors.Unwrap(wrapped) == ErrorCritical) // true
```

```go
package main
import (
    "errors"
    "fmt"
)

var (
    errUhOh  = errors.New("oh critical error!!")
)

func check(num int) error {
    if num == 1 {
        return fmt.Errorf("it's odd")
    } else if num == 2 {
        return errUhOh
    }
    return nil
}

func validations(num int) error{
    err := check(num)
    if err != nil {
        return fmt.Errorf("run error: %w", err)
    }
    return nil
}

func main() {
    for num := 1; num <= 5; num++ {
        fmt.Printf("validating %d... ", num)
        err := validations(num)
        if err == errUhOh || errors.Unwrap(err) == errUhOh {
            fmt.Println("oh no something has happened!")
        } else if err != nil {
            fmt.Println("some error is present...", err)
        } else {
            fmt.Println("valid number only...!")
        }
    }
}

/*
validating 1... some error is present... run error: it's odd
validating 2... some error is present... run error: oh critical error!!
validating 3... valid number only...!
validating 4... valid number only...!
validating 5... valid number only...!
*/
```

## Examining errors with Is and As

The Go 1.13 errors package includes two new functions for examining errors: Is and As.

The errors.Is function compares an error to a value.

```go
// Similar to:
//   if err == ErrNotFound { … }
if errors.Is(err, ErrNotFound) {
    // something wasn't found
}
```

The As function tests whether an error is a specific type.

```go
// Similar to:
//   if e, ok := err.(*QueryError); ok { … }
var e *QueryError
// Note: *QueryError is the type of the error.
if errors.As(err, &e) {
    // err is a *QueryError, and e is set to the error's value
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
