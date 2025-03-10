## http

### Converting http request to curl command

```go
func RoundTrip(r *http.Request) (*http.Response, error) {
    // Do work before request i sent
    req, _ := GetCurlCommand(r)

    res, err := http.DefaultTransport.RoundTrip(r)
    if err != nil {
        return nil, err
    }

    // Do work after response is received
    // can use net/http/httputil.DumpResponse()
    // ...
}
```

```go
type CurlCommand struct {
	slice []string
}

// append appends a string to the CurlCommand
func (c *CurlCommand) append(newSlice ...string) {
	c.slice = append(c.slice, newSlice...)
}

// String returns a ready to copy/paste command
func (c *CurlCommand) String() string {
	return strings.Join(c.slice, " ")
}

// nopCloser is used to create a new io.ReadCloser for req.Body
type nopCloser struct {
	io.Reader
}

func bashEscape(str string) string {
	return `'` + strings.Replace(str, `'`, `'\''`, -1) + `'`
}

func (nopCloser) Close() error { return nil }

func GetCurlCommand(req *http.Request) (*CurlCommand, error) {
	command := CurlCommand{}

	command.append("curl")

	command.append("-X", bashEscape(req.Method))

	if req.Body != nil {
		body, err := ioutil.ReadAll(req.Body)
		if err != nil {
			return nil, err
		}
		req.Body = nopCloser{bytes.NewBuffer(body)}
		bodyEscaped := bashEscape(string(body))
		command.append("-d", bodyEscaped)
	}

	var keys []string

	for k := range req.Header {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	for _, k := range keys {
		v := strings.Join(req.Header[k], " ")
		if strings.ToLower(k) == "authorization" {
			tmp, _ := base64.StdEncoding.DecodeString(v)
			v = strings.Split(string(tmp), ":")[0]
		}
		command.append("-H", bashEscape(fmt.Sprintf("%s: %s", k, v)))
	}

	command.append(bashEscape(req.URL.String()))

	return &command, nil
}
```
