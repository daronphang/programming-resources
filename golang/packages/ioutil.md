## io/ioutil

Provides helper functions for non-trivial file and io tasks. Often used with the OS package to provide additional methods of handling I/O.

In Go 1.16, **ioutil is deprecated** and same functionality is provided by package io or package os.

### Reader

A reader is any type that implements Read() method. Go standard library contains many implementations of this interface, including files, network connections, compressors, ciphers, etc. Interface is intended to let programmers implement code that reads data from an arbitrary source and transfers it into the provided slice of bytes.

```go
type Reader interface {
  Read
}

func (T) Read(b []byte) (n int, err error)    // returns number of bytes populated; when byte stream ends, returns io.EOF

// reading files
var r io.Reader
var err error
r, err = os.Open("file.txt")

// reader from normal string
var r io.Reader
r = strings.NewReader("Read will return these bytes")

// http requests
var r io.Reader
r = request.Body

// bytes buffer
var r io.Reader
var buf bytes.Buffer
r = &buf
```

```go
// using readers

b, err := ioutil.ReadAll(r)

// reads all bytes and write to an io.Writer
n, err:= io.Copy(w,r)

// json decoder
err := json.NewDecoder(r).Decode(v)
```

### ReadFile

Reads an entire file into memory in a single call (as a []byte). Automatically allocates a byte slice of the correct size, closes the file and returns the first error that prevents it from working.

### ReadAll

Useful utility function for reading all data from an io.Reader until EOF. It's often used to read data such as HTTP response body, files, and other data sources which implement io.Reader interface.

Nonetheless, need to be careful when using this as reading big files means loading everything into memory, and gets worse when the file is requested by multiple users in parallel i.e. ending up with multiple copies of file in memory.

Better version would be to use io.Copy to copy from file which implements io.Reader interface to w ResponseWriter implementing io.Writer interface. io.Copy uses fixed 32KB buffer to copy from reader to writer until EOF and hence, will always just use 32KB to copy it to destination.

```go
// may crash due to insufficient memory if file is too big
func handle(r *http.Request, w http.ResponseWriter) {
	file, err := os.Open("my_file.zip")
	// error checks...
	b, err := ioutil.ReadAll(file)
	// error checks
	fmt.FPrintf(w, b)
}

// better version
func handle(r *http.Request, w http.ResponseWriter) {
	file, err := os.Open("my_file.zip")
	// error checks...
	io.Copy(w, file)
}
```

### WriteFile

```go
func WriteFile(filename string, data []bytes permission os.FileMode) error  // bytes slice is a computer friendly rep. of a string
```
