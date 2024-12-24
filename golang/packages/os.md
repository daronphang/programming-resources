## os

## Reading files after compilation

To read files after code has been compiled, need to copy into the respective directory first.

```go
func readConfigFromFile() error {
	env := strings.ToUpper(os.Getenv("GO_ENV"))
	_, execFile, _, _ := runtime.Caller(0)
    fileName = path.Dir(execFile) + "/sample.json"
}
```
