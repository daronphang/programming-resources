## Deferred function calls

Defer statement is an ordinary function or method call prefixed by keyword defer. **Function and argument expressions are evaluated when statement is executed, but actual call is deferred until the function that contains defer statement has finished**, whether normally by executing a return statement or falling off the end, or abnormally by panicking. Any number of calls may be deferred; they are executed in the reverse order in which they were deferred i.e. deferred last, called first.

A defer statement pushes a function call onto a list. The list of saved calls is executed after the surrounding function returns. It is commonly used to simplify functions that perform various clean-up actions.

Defer statement often used with paired operations like open/close, connect/disconnect, or lock/unlock to ensure all resources are released in all cases, no matter how complex the control flow. Right place for defer statement that release a resource is immediately after the resource has been successfully acquired.

```go
// resp.Body.Close() connection closed on all execution paths, including failures
func title(url string) error {
  resp, err := http.Get(url)
  if err != nil {
    return err
  }
  defer resp.Body.Close()

  // check content-type is HTML
  ct := resp.Header.Get("Content-Type")
  if ct != "text/html" && !strings.hasPrefix(ct, "text/html;") {
    return fmt.Errorf("%s has type %s, not text/html", url, ct)
  }
  doc, err := html.Parse(resp.Body)
  if err != nil {
    return fmt.Errorf("Parsing %s as HTML: %v", url, err)
  }
  visitNode := func(n *html.Node) {
    if n.Type == html.ElementNode && n.Data == "title" && n.FirstChild != nil {
      fmt.Println(n.FirstChild.Data)
    }
  }
  forEachNode(doc, visitNode, nil)
  return nil
}

// same pattern used for other resources
package ioutil

func ReadFile(filename string)([]byte, error) {
  f, err := os.Open(filename)
  if err != nil {
    return nil, err
  }
  defer f.Close()
  return ReadAll(f)
}

// unlocking mutex
var mu sync.Mutex
var m = make(map[string]int)

func lookup(key string) int {
  mu.Lock()
  defer mu.Unlock()
  return m[key]
}
```

Defer statement can be used to pair "on entry" and "on exit" actions when debugging a complex function. Ensure final parenthesis are added in defer statement, else the "on entry" action will happen on exit and the "on exit" action doesn't happen.

```go
func bigSlowOperation(){
  defer trace("bigSlowOp")()    // parenthesis added
  // some work
  time.Sleep(10 * time.Second)  // simulate slow operation by sleeping
}

func trace(msg string) func() {
  start := time.Now()
  log.Printf("enter %s", msg)
  return func() {
    log.Printf("exit %s (%s)", msg, time.Since(start))
  }
}
```

As deferred functions aren't executed until the end of function's execution, it deserves extra scrutiny.

```go
for _, filename := range filenames {
  // if defer f.Close() is used here, can be risky
  // may run out of file descriptors
  // move defer statement into another function that is called on each iteration
  if err := doFile(filename); err != nil {
    return err
  }
}

func doFile(filename string) error {
  f, err := os.Open(filename)
  if err != nil {
    return err
  }
  defer f.Close()
  // code to process file
}
```

## Rules

### Arguments

A deferred function's arguments are evaluated when the defer statement is evaluated, not when the call executes.

```go
func a() {
    i := 0
    defer fmt.Println(i) // prints 0
    i++
    return
}
```

### LIFO

Deferred functions are executed in LIFO order.

```go
for i := 0; i < 5; i++ {
    defer fmt.Printf("%d ", i)
}
// 4 3 2 1 0
```

### Return values

Deferred functions may read and assign to the returning function's named values.

Deferred functions run after return statements have updated the function's result variables. As anonymous function can access its enclosing function's variables, a deferred anonymous function can observe the function's results. Deferred anonymous function can even change the values that the enclosing function returns to its caller.

```go
func double(x int) (result int) {
  defer func() {
    fmt.Printf("double(%d) = %d\n", x, result)
  }()
  return x + x
}

_ = double(4) // "double(4) = 8"

func triple(x int) (result int) {
  defer func(){ result += x}()
  return double(x)
}

fmt.Println(triple(4))    // 12
```
