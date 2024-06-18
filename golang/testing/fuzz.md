## Fuzz tests

Fuzz testing is an exciting testing technique in which random input is used to discover bugs or edge cases. Go’s fuzzing algorithm is smart because it will try to cover as many statements in your code as possible by generating many new input combinations.

```go
func FuzzFooer(f *testing.F) {
    f.Add(3)
    f.Fuzz(func(t *testing.T, a int) {
        Fooer(a)
    })
}
```
