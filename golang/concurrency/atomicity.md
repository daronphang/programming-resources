## Atomicity

When something is considered atomic, it means that within the context that it is operating, it is indivisible or uninterruptible. Atomicity is important because it is safe within concurrent contexts, which can even serve as a way to optimize concurrent programs.

The atomicity of an operation can change depending on the currently defined scope. Operations that are atomic within the context of your process may not be atomic in the context of the operating system.

### Example

```go
i++
```

The example may look atomic, but a brief analysis reveals several operations:

1. Retrieve the value of i
2. Increment the value of i
3. Store the value of i

While each of these operations alone is atomic, the combination of the three may not be, depending on your context. This reveals an interesting property of atomic operations: **combining them does not necessarily produce a larger atomic operation**.
