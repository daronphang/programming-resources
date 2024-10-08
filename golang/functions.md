## Function declarations

Functions that has result MUST end with a return statement unless execution ends with infinite loop. To export functions, function name must start with capital letter.

```GO
func name(parameter) (result) {
  // body
}

func hypot(x, y float64) float64 {
  return math.Sqrt(x*x + y*y)
}
fmt.Println(hypot(3,4)) // 5
```

## Function values

Functions are first-class values in Go and are treated like any other variables. This means a function can be passed as an argument to other functions, can be returned by another function and can be assigned as a value to a variable.

Function values have types, and may be assigned to variables or passed to or returned from functions.

```go
func square(n int) int { return n * n }

f := square
fmt.Println(f(3)) // "9"
```

## Multiple return values

One of Go's unusual features is that functions and methods can return multiple values.

```go
func findLinks(url string) ([]string, error) {
  resp, err := http.Get(url)
  if err != nil {
    return nil, err
  }
  if resp.StatusCode != http.StatusOK {
    resp.Body.Close()
    return nil, fmt.Errorf("Getting %s: %s", url, resp.Status)
  }
  doc, err := html.Parse(resp.Body)
  resp.Body.Close()   // Need close to ensure network resources are properly released
  if err != nil {
    return nil, fmt.Errorf("parsing %s as HTML: %v", url, err)
  }
  return visit(nil, doc), nil
}
```

## Errors and error handling

Function for which failure is an expected behavior returns an additional result, conventionally the last one. If the failure has only one possible cause, the result is a boolean. GO's approach for error handling is different from many other languages; GO programs use ordinary control-flow mechanisms like if and return to respond to errors instead of exceptions consisting of stack trace and information that lack intelligible context about what went wrong. Hence, more attention needs to be paid for error-handling in GO.

```go
value, ok := cache.Lookup(key)
if !ok {
  // return nil, err                                              propagating error
  // return nil, fmt.Error("parsing %s as HTML: %v", url, err)    return error msg
}
```

```go
// retrying failed operation with delay or limit on number of attempts
// tries for 1min using exponential back-off
func WaitForServer(url string) error {
  const timeout = 1 * time.Minute
  deadline := time.Now().Add(timeout)
  for tries := 0; time.Now().Before(deadline); tries ++ {
    _, err := http.Head(url)
    if err == nil {
      return nil // success
    }
    log.Printf("server not responding (%s); retrying...", err)
    time.Sleep(time.Second << uint(tries)) // expontential back-off
  }
  return fmt.Errorf("server %s failed to respond after %s", url, timeout)
}

// to stop program
if err := WaitForServer(url); err != nil {
  // ...
  os.Exit(1)
  // log.Fatalf("site is down: %v\n", err)
}
```

### End of File (EOF)

```go
package io
import "errors"

var EOF = errors.new("EOF") // EOF is the error returned by Read when no more input is available

in := bufio.NewReader(os.Stdin)
for {
  r, _, err := in.ReadRune()
  if err == io.EOF {
    break
  }
  if err != nil {
    retrurn fmt.Errorf("read failed: %v", err)
  }
  // use r...
}
```

## Anonymous functions

Named functions can be declared only at package level, but can use function literal to denote a function value within any expression. Written without a name following func keyword, and its value is called an anonymous function. Anonymous functions have access to entire lexical environment and hence, inner function can refer to variables from enclosing function.

```go
// squares returns a function that returns the next square number each time it is called
func squares() func() int {
  var x int
  // anonymous inner function can access and update local variables of enclosing function (closure)
  // lifetime of variable is not determined by its scope; x still exists after squares has returned within main
  return func() int {
    x++
    return x * x
  }
}

func main() {
  f := squares()
  fmt.Println(f())    // 1
  fmt.Println(f())    // 4
  fmt.Println(f())    // 9
}
```

## Lexical scoping caveat

For loop introduces a new lexical block in which variable dir is declared. However, values passed to function is the addressable storage location of shared variable and not its value at that particular moment. By the time cleanup functions are called, the dir variable holds the value from the final iteration and consequently all calls to os.RemoveAll will attempt to remove the same directory.

```go
// program that creates a set of directories and later removes them
var rmdirs []func()
for _, dir := range tempDirs() {
  dir := dir  // declares inner dir, initialized to outer dir (NECESSARY!)
  os.MkdirAll(dir, 0755)    // creates parent directories
  rmdirs = append(rmdirs, func(){
    os.RemoveAll(dir)   // dir refers to inner dir
  })
}

for _, rmdir := range rmdirs {
  rmdir()   // cleanup function
}

// THIS DOES NOT WORK
var rmdirs []func()
for _, dir := range tempDirs() {
  os.MkdirAll(dir, 0755)  // this is OKAY
  rmdirs = append(rmdirs, func(){
    os.RemoveAll(dir)   // incorrect! dir passed is the outer dir's addressable storage loc and not value at current moment
  })
}
```

## Variadic functions

One that can be called with varying numbers of arguments. Type of final parameter is preceded by an ellipsis. Often used for string formatting and has suffix f as widely followed naming convention that accepts Printf-style format string.

```go
func sum(vals ...int) int {
  total := 0
  for _, val := range vals {
    total += val
  }
  return total
}

fmt.Println(sum(1, 2, 3, 4))  // 10

// allocating an array and passing a slice of entire array to function
values := []int{1, 2, 3, 4}
fmt.Println(sum(values...))   // 10

func errorf(linenum int, format string, args ...interface{}) {    // {}interface accepts any values
  fmt.Fprintf(os.Stderr, "Line %d: ", linenum)
  fmt.Fprintf(os.Stderr, format, args...)
  fmt.Fprintln(os.Stderr)
}
errorf(12, "undefined: %s", "count")  // "Line 12: undefined: count"
```

## init

init() is called after all the variable declarations in the package have evaluated their initializers, and those are evaluated only after all the imported packages have been initialized.
