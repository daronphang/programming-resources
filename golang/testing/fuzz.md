## Fuzz tests

Fuzz testing is an exciting testing technique in which random input is used to discover bugs or edge cases. Go’s fuzzing algorithm is smart because it will try to cover as many statements in your code as possible by generating many new input combinations.

The goal of the fuzz test is not to validate the output of the function, but instead to use unexpected inputs to find potential edge cases. By default, fuzzing will run indefinitely, as long as there isn’t a failure. The -fuzztime flag should be used in your CI/CD to specify the maximum time for which fuzzing should run.

To create a fuzz test:

- Name of function must start with Fuzz
- Function accepts testing.F as the unique parameter
- Define initial values called **seed corpus** with f.Add()
- Test function must define a fuzz target

```go
func FuzzFooer(f *testing.F) {
    f.Add(3)
    f.Fuzz(func(t *testing.T, a int) {
        Fooer(a)
    })
}
```
