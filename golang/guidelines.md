## When to use pointers

As a general guideline, prefer to make the methods for a type either all pointer methods or all value methods. Nonetheless, correctness wins over speed or simplicity:

- If the method needs to mutate the receiver, the receiver must be a pointer
- If the receiver is a struct containing fields that cannot safely be copied, use a pointer receiver e.g. sync.Mutex
- If the receiver is a large struct or array, a pointer receiver may be more efficient in performance
- If the receiver is a struct or array, any of whose elements is a pointer to something that may be mutated, prefer a pointer receiver to make the intention of mutability clear to the reader
- If the receiver is a built-in type, map, function, or channel, use a value rather than a pointer
- For database layers, prefer returning a receiver to a struct
- When in doubt, use a pointer receiver

https://google.github.io/styleguide/go/decisions#receiver-type

### Clarity

For arguments that require pointers to be passed, it is cleaner to define the variable without operator.

```go
// cleaner
var req dto.DeleteEdgeFunctionRequest
err = binding.BindAndValidate(c, &req)

// ok, but not as clear
var req *dto.DeleteEdgeFunctionRequest
err = binding.BindAndValidate(c, req)
```
