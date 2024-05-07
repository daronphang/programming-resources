## Print functions

```go
fmt.Println()     // Takes a string, prints and adds a new line after string
fmt.Print()       // same as Println() but does not add a new line after string
fmt.Printf()      // formats string using custom specifier and writes output to stdout
fmt.Sprint()      // uses default formats for its operands and returns resulting string
fmt.Sprintf()      // formats and stores a series of characters and values in array pointed to by buffer
fmt.Errorf()
fmt.Fprintf()     // F prefix stands for file and indicates formatted output should be written to file
fmt.Fscanf()
fmt.Scan()        // Scans textfrom std input, storing successive space-separated values into successive args
fmt.Scanf()
fmt.Sscanf()
log.Printf()

myString := "Results: " + results + " and more stuff: " + more

fmt.Print(name, " is ", age, " years old.\n")
fmt.Printf("%s is %d years old.\n", name, age)

s := fmt.Sprint(name, " is ", age, " years old.\n")
myString := fmt.Sprintf("Results: %s and more stuff: %s", results, more)

fmt.Printf("%+v\n", someStruct)
```

```
%v    value in default format
%#v   Go-syntax representation of value
%T    type of value
%%    literal % sign; consumes no value

%t    true or false
%c    character represented by corresponding Unicode code point
%b    base 2
%d    base 10
%o    base 8
%U    unicode format i.e. U+1234 which is same as U+%04X

%f    decimal point but no exponent i.e. 123.456
%e    for large exponents i.e. 1.23456e+78
%x    hexadecimal notation -0x1.23abcp+20
%X    uppercase hexadecimal notation

%s    unintepreted bytes of string or slice
%q    double-quoted string safely escaped with Go syntax
%x    base 16, lower-case, two characters per byte
%X    base 16, upper-case, two characters per byte

%p    for pointers, base 16 notation with leading 0x
```
