## go-swagger

### Models

```
swagger:model [?model name]
```

```go
// swagger:model MachineResourceUsage
type MachineResourceUsage struct {
    Machine string `json:"machine"`
}
```

### Params

Links a struct to one or more **operations**.

```
swagger:parameters [operationid1 operationid2]
```

```go
// swagger:parameters CreateMachineResourceUsage
type CreateMachineResourceUsageParams struct {
    Machine string `json:"machine" validate:"required"`
}
```

### Response

```
swagger:response [?response name]
```

```go
// A ValidationError is an error that is used when the required input fails validation.
// swagger:response validationError
type ValidationError struct {
	// The error message
	// in: body
	Body struct {
		// The validation message
		//
		// Required: true
		// Example: Expected type int
		Message string
		// An optional field name to which this validation applies
		FieldName string
	}
}
```

If you just want to define the body using struct, use swagger:model instead.

```go
// swagger:model HTTPValidationError
type HTTPValidationError struct {
    Message string `json:"message"`
    error string `json:"error"`
}
```

### Route

```
swagger:route [method] [path pattern] [?tag1 tag2 tag3] [operation id]
```

```go
// swagger:route GET /machines/{machine} ResourceTracking GetAggMachineResourceUsage
// responses:
//      200: []AggMachineResourceUsage
//      400: HTTPValidationError
func (h *handler) GetAggMachineResourceUsage(c echo.Context) error {}

// swagger:route POST /machine ResourceTracking CreateMachineResourceUsage
// responses:
//      200: MachineResourceUsage
//      400: HTTPValidationError
func (h *handler) CreateMachineResourceUsage(c echo.Context) error {}
```
