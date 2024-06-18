## For

The Go for loop is similar to—but not the same as—C's. It unifies for and while and there is no do-while. There are three forms, only one of which has semicolons.

```go
// Like a C for
for init; condition; post { }

// Like a C while
for condition { }

// Like a C for(;;)
for { }
```

Short declarations make it easy to declare the index variable right in the loop.

```go
sum := 0
for i := 0; i < 10; i++ {
    sum += i
}
```

If you're looping over an array, slice, string, or map, or reading from a channel, a range clause can manage the loop.

```go
for key, value := range oldMap {
    newMap[key] = value
}

// If you need the first item in the range (key or index),
// drop the second
for key := range m {
    if key.expired() {
        delete(m, key)
    }
}
```
