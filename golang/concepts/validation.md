## Validation

### Required for integer

If an integer is required but is provided as 0, or if you require boolean values, Go will recognize it as nil. Two alternatives:

1. Change field type to pointer

```go
type Example struct {
    someBool *bool `validate:"required"`
    someInt *int `validate:"required"`
}
```

2. Create custom validator

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
