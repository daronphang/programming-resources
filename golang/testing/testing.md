## Testing package

A test function in Go starts with Test and takes `*testing.T` as the only parameter.

```sh
$ go mod init <current_directory_folder_name>
$ go test
$ go test -cover
$ go test ./... -coverpkg=./...
$ go test -coverprofile=output_filename # lcov
$ go tool cover -html=output_filename
```

```go
package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	cards := newDeck()
	if len(cards) != 16 {
		t.Errorf("Expected deck length of 16 but got %d", len(cards))
	}

	if cards[0] != "Ace of Spades" {
		t.Errorf("Expected first card Ace of Spades, but got %s", cards[0])
	}
}

func TestSaveToDeckAndNewDeckTestFromFile(t *testing.T) {
	os.Remove("_decktesting")
	deck := newDeck()
	deck.saveToFile("_decktesting")
	loadedDeck := newDeckFromFile("_decktesting")

	if len(loadedDeck) != 16 {
		t.Errorf("Expected 16 cards, got %d", len(loadedDeck))
	}
	os.Remove("_decktesting")
}
```

### Errors and logs

It is important to mention that `t.Error*` marks the test as failed, but **does not stop the execution of the test**. Instead, all encountered errors will be reported once the test is completed. Instead, you can use `t.Fatal*`.

```go
func TestFooer2(t *testing.T) {
	input := 3
	result := Fooer(3)
	t.Logf("The input was %d", input)
	if result != "Foo" {
		t.Errorf("Result was incorrect, got: %s, want: %s.", result, "Foo")
	}
	t.Fatalf("Stop the test now, we have seen enough")
	t.Error("This won't be executed")
}
```

### Run()

Used to define a subtest.

### Parallel()

All tests calling this function will be executed in parallel. go test handles parallel tests by pausing each test that calls t.Parallel(), and then resuming them in parallel when all non-parallel tests have been completed.

The GOMAXPROCS environment defines how many tests can run in parallel at one time, and by default this number is equal to the number of CPUs.

```go
func TestFooerParallel(t *testing.T) {
	t.Run("Test 3 in Parallel", func(t *testing.T) {
		t.Parallel()
		result := Fooer(3)
		if result != "Foo" {
			t.Errorf("Result was incorrect, got: %s, want: %s.", result, "Foo")
		}
	})
	t.Run("Test 7 in Parallel", func(t *testing.T) {
		t.Parallel()
		result := Fooer(7)
		if result != "7" {
			t.Errorf("Result was incorrect, got: %s, want: %s.", result, "7")
		}
	})
}
```

### Skip()

Using the Skip() method allows you to separate unit tests from integration tests. Integration tests validate multiple functions and components together and are usually slower to execute, so sometimes it’s useful to execute unit tests only.

go test accepts a flag called `-test.short` that is intended to run a “fast” test.

```go
func TestFooerSkiped(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping test in short mode.")
	}
	result := Fooer(3)
	if result != "Foo" {
		t.Errorf("Result was incorrect, got: %s, want: %s.", result, "Foo")
	}
}
```

```sh
$ go test -v # test will be executed
$ go test -v -test.short # test will be skipped
```

### Cleanup()

Need to ensure cleanup is performed as there is no handholding by GO testing framework i.e. creating and deleting temp files.

Though you can use the defer keyword, it can make test logic more complicated to setup, and can clutter the test function when many components are involved.

The Cleanup() function is executed at the end of each test (including subtests), and makes it clear to anyone reading the test what the intended behavior is.

```go
func Test_With_Cleanup(t *testing.T) {
  	// Some test code here
	t.Cleanup(func() {
		// cleanup logic
	})
  	// more test code here
}

func TestFunction(t *testing.T) {
    // setup code
    t.Cleanup(func(){
        // tear-down code
    })
    // sub-tests
    t.Run()
    t.Run()
    ...
}
```

### TempDir()

TempDir() is a method that automatically creates a temporary directory for your test and deletes the folder when the test is completed, removing the need to write additional cleanup logic.

```go
func TestFooerTempDir(t *testing.T) {
    tmpDir := t.TempDir()
  	// your tests
}
```
