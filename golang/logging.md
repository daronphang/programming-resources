## Logging

Logging at the top level (when there are no more frames to return) is a good practice instead of logging at every error i.e. return error or log, but not both. Errors further down the call stack can be wrapped with relevant information and returned. Wrap your errors until you are going to handle them, then log.

```go
x, err := foo()
if err != nil {
  return fmt.Errorf("foo: %w", err)
}
```

All library code should wrap errors liberally, and return them. The application using the package should have appropriate logging for those errors.

### Masking errors with logs

When a logger exists in a package, it’s tempting for people to log any errors and continue, with the original caller utterly unaware of the error. Hence, **the best way to handle an error is to pass it up to the original caller**. The original caller has the context of why the operation was performed e.g. retry, perform an alterative action, or log. What to do with an error should be decided where there is context, not deeply embedded within a utility package.
