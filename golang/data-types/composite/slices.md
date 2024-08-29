## Slices

Slices represent variable-length sequences whose elements all have the same type. Array and slices are intimately connected. A slice is a lightweight data structure that gives access to a subsequence of the elements of an array.

A slice has 3 components: pointer, length and capacity. Pointer points to the first element of array that is reachable through slice, which is not necessarily the array's first element. Length cannot exceed capacity.

Multiple slices can share the same underlying array and may refer to overlapping parts. Unlike arrays, slices cannot use == to compare with each other. Only legal comparison is to check for nil.

Gotcha for slices is that when GO creates slices, it creates both a slice (pointer to the underlying array, length and capacity) and the underlying array. Hence, do not need to use pointers to update values inside slices.

```
nonempty()
copy()
append()
reverse()
rotate()
```

```go
// append
var x []int
x = append(x, 1)  // returns a new slice and assign back to variable x
x = append(x, x...) // append slice x

for i, card := range x {
  fmt.Println(card)
}
```

```go
// slices gotcha that doesn't require pointers specifically
mySlice := []string{"hello", "world"}
updateSlice(mySlice)
fmt.Println(mySlice)	// [Bye World]

func updateSlice(s []string) {
  s[0] = "Bye"
}
```

### Create empty slice

```go
type Payload struct {}

s := make([]string, 0, 10)
s := make([]Payload, 10) // this will create 10 empty Payload structs
```

### Re-slicing a slice

Re-slicing a slice doesn’t make a copy of the underlying array. It creates a new slice value that points to the original array. The full array will be kept in memory until it is no longer referenced.

```go
d := []byte{'r', 'o', 'a', 'd'}
e := d[2:]
// e == []byte{'a', 'd'}
e[1] = 'm'
// e == []byte{'a', 'm'}
// d == []byte{'r', 'o', 'a', 'm'}
```

```go
x := make([]string, 0, 5)
x = append(x, "a", "b", "c", "d")
y := x[:2] // ['a', 'b']
y = append(y, "i")  // x == ['a','b','i','d']
y = append(y, "j", "k")
// y == ['a','b','i','j','k']
// x == ['a','b','i','j']
```

### Growing slices

A slice cannot be grown beyond its capacity. Attempting to do so will cause a runtime panic, just as when indexing outside the bounds of a slice or array. Similarly, slices cannot be re-sliced below zero to access earlier elements in the array.

To increase the capacity of a slice one must create a new, larger slice and copy the contents of the original slice into it. This technique is how dynamic array implementations from other languages work behind the scenes.

```go
t := make([]byte, len(s), (cap(s)+1)*2) // +1 in case cap(s) == 0
for i := range s {
  t[i] = s[i]
}
s = t
```

## Slice techniques

### Rotate/Reverse

```go
months := [...]string{1: "Jan", /*...*/, 12: "Dec"}

s[i:j]  // creates a new slice

[]byte("Hello world!")  // converts a string into a byte slice (computer friendly representation of string)

// to rotate elements, apply reverse func multiple times
s := []int{0, 1, 2, 3, 4, 5}
reverse(s[:2])  // [1 0 2 3 4 5]
reverse(s[2:])  // [1 0 5 4 3 2]
reverse(s)
fmt.Println(s)  // [2 3 4 5 0 1]

// use len(s) to check for empty slice
var s []int   // len(s) == 0, s == nil
s = []int{}   // len(s) == 0, s != nil
```

### Stack

```go
stack = append(stack, v)
top := stack[len(stack)-1]  // top of stack
stack = stack[:len(stack)-1] // pop

// removing elements in middle of a slice
// preserving order
func remove(slice []int, i int) []int {
  copy(slice[i:], slice[i+1:])
  return slice[:len(slice)-1]
}

// order is not preserved
func remove(slice []int, i int) []int {
  slice[i] = slice[len(slice)-1]
  return slice[:len(slice)-1]
}

func main() {
  s := []int{5, 6, 7, 8, 9}
  fmt.Println(remove(s, 2)) // "[5 6 8 9]"
}
```
