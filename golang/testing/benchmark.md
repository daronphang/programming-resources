## Benchmark tests

Benchmark tests are a way of testing your code performance. The goal of those tests is to verify the runtime and the memory usage of an algorithm by running the same function many times.

```go
func BenchmarkFooer(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Fooer(i)
    }
}
```
