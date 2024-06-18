## go-swagger

### Model

```
swagger:model [?model name]
```

```go
// swagger:model MachineResourceUsage
type MachineResourceUsage struct {
	Machine string `json:"machine"`
	Metric1 int32  `json:"metric1"`
	Metric2 int32  `json:"metric2"`
	Metric3 int32  `json:"metric3"`
	CreatedAt string `json:"createdAt"`
}
```

### Params

Links a struct to one or more operations.

When assigning parameters to a struct, it includes all request parameters e.g. body,headers, query, path, etc. If you want to accept only a body, use model instead.

```
swagger:parameters [operationid1 operationid2]
```

```go
// swagger:parameters GetAggMachineResourceUsage
type GetAggMachineResourceUsageParams struct {
	// in: path
	Machine        string `json:"machine" validate:"required"`
	// in: query
	// PostgreSQL INTERVAL data type e.g. '5 minutes', '1 hour', '1 day'
	TimeBucket     string `json:"timeBucket" validate:"required"`
	// in: query
	// PostgreSQL INTERVAL data type e.g. '1 hour', '1 day', '23 hours'
	LookBackPeriod string `json:"lookBackPeriod" validate:"required"`
}
```

### Response

When assigning a response to a struct, it includes all response parameters e.g. body,headers. If you want to return only a body, use model instead.

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

### Route

You have the ability to use a model as a response by specifying `body:ModelName` (no spacing).

```
swagger:route [method] [path pattern] [?tag1 tag2 tag3] [operation id]
```

```go
// swagger:route GET /machines/{machine} ResourceTracking GetAggMachineResourceUsage
// Group MachineResourceUsage time series by timeBucket within lookBackPeriod from today and return aggregated median values
// responses:
// 	200: body:[]AggMachineResourceUsage
// 	400: body:HTTPValidationError
func (h *handler) GetAggMachineResourceUsage(c echo.Context) error {}

// swagger:route POST /machine ResourceTracking CreateMachineResourceUsage
// responses:
//      200: MachineResourceUsage
//      400: HTTPValidationError
func (h *handler) CreateMachineResourceUsage(c echo.Context) error {}
```

### Operation

For more complex specifications of a route, can use operation. YAML spec is defined after `---`.

```
swagger:operation [method] [path pattern] [?tag1 tag2 tag3] [operation id]
```

```go
// swagger:operation POST /machine ResourceTracking CreateMachineResourceUsage
// Add a time series entry for MachineResourceUsage
// ---
// parameters:
// - name: MachineResourceUsageParam
//   in: body
//   schema:
//     $ref: "#/definitions/CreateMachineResourceUsage"
// responses:
//   "200":
//     description: MachineResourceUsage
//     schema:
//       $ref: '#/definitions/MachineResourceUsage'
//   "400":
//     description: HTTPValidationError
//     schema:
// 	     $ref: '#/definitions/HTTPValidationError'
func (h *handler) CreateMachineResourceUsageRT(c echo.Context) error {}
```
