## Testing errors

You should never inspect the output of Error() as it makes your tests brittle. **Comparing the string form of an error is a code smell**, and you should try to avoid it. Alternatively, you can test for **specific data** being returned in the error e.g. includes().

```go
// Avoid this!
func TestOpenGivesSpecificErrorStringForBogusFile(t *testing.T) {
    t.Parallel()
    want := errors.New("open bogus: no such file or directory")
    _, got := store.Open("bogus")
    if got.Error() != want.Error() {
        t.Errorf("wrong error: %v", got)
    }
}
```

Instead, interface values are comparable. Two interface values are equal if they have identical dynamic types and equal dynamic values or if both have value nil:

- Static type: Type of an element given in its declaration e.g. error
- Dynamic type: non-interface type of the value assigned to a variable at runtime e.g. `*errorString`
- Dynamic value: Dynamic type including its value e.g. &errorString{s: "ohno"}

### Comparing errors with errors.New()

All errors created via errors.New are distinct.

```go
package errors
// New returns an error that formats as the given text.
// Each call to New returns a distinct error value even if the text is identical.
func New(text string) error {
  return &errorString{text}
}

// errorString is a trivial implementation of error.
type errorString struct {
  s string
}

func (e *errorString) Error() string {
  return e.s
}
```

```go
e1 := errors.New(“ohno”)
e2 := errors.New(“ohno”)
fmt.Println(e1 == e2) // false
```

### Comparing custom errors

```go
type CustomError struct {
  Err string
}

func (ce CustomError) Error() string {
  return ce.Err
}

func main() {
  var e1 error = CustomError{Err: "ohno"}
  var e2 error = CustomError{Err: "ohno"}
  fmt.Println(errors.Is(e1, e2)) // true
}
```

### Sentinel errors lose useful information

We can define a named error value like this:

```go
// sentinel error, similar to io.EOF
var ErrUnopenable = errors.New("can't open store file")
```

However, it would lose useful information about the error.

```go
func Open(path string) (*Store, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, ErrUnopenable // losing information about 'err'
    }
    // ...
}

func TestOpenGivesErrUnopenableForBogusFile(t *testing.T) {
    t.Parallel()
    _, err := Open("bogus")
    if err != ErrUnopenable {
        t.Errorf("wrong error: %v", err)
    }
}
```

A sentinel error value ErrUnopenable makes it possible to detect that kind of error programmatically, but at the expense of making the error message itself nearly useless.

Most of the time in Go programs, **all we care about is that err is not nil**. In other words, that there was some error. What it is specifically usually doesn’t matter, because the program isn’t going to take different actions for different errors.

```go
func TestOpenGivesNonNilErrorForBogusFile(t *testing.T) {
    t.Parallel()
    _, err := store.Open("bogus file")
    if err == nil {
        t.Error("want error opening bogus store file")
    }
}
```

### Wrapping sentinel errors with dynamic information

A sentinel error is pretty limited in what it can convey. It can’t contain any dynamic information that we’ve learned at run-time.

However, often we’d like to include some more dynamic information in the error. One way to do this is to take the sentinel value and wrap it in a new error value that contains the dynamic information. For this, we can use the fmt.Errorf(), and the special format verb %w (for “wrap”).

```go
var ErrUserNotFound = errors.New("user not found")

func FindUser(name string) (*User, error) {
    user, ok := userDB[name]
    if !ok {
        return nil, fmt.Errorf("%q: %w", name, ErrUserNotFound)
    }
    return user, nil
}

func TestFindUser_GivesErrUserNotFoundForBogusUser(t *testing.T) {
    t.Parallel()
    _, err := user.FindUser("bogus user")
    if !errors.Is(err, user.ErrUserNotFound) {
        t.Errorf("wrong error: %v", err)
    }
}
```
