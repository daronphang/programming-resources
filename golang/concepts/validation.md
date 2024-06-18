## Validation

### Required for integer/bool

When memory is allocated to store a value, either through a declaration or a call of make() or new(), and no explicit initialization is provided, the memory is given a default initialization:

- false for booleans
- 0 for integers
- 0.0 for floats
- "" for strings
- nil for pointers, functions, interfaces, slices, channels, maps

To validate if a field has been set for integers and booleans, can use pointers and their nil value:

```go
type Example struct {
    someBool *bool `validate:"required"`
    someInt *int `validate:"required"`
}
```

### Custom validator

```go
type Example struct {
    someNumber int `validate:"int_required"`
}

func IntRequired(fl validator.FieldLevel) bool {
    defer func() {
        _ = recover();
    }()
    _ = fl.Field().Int()
    return true
}

func main() {
    v := validator.New()
    if err := v.RegisterValidation("int_required", IntRequired); err != nil {
        // do something
    }
}
```
