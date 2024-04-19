## Structs

An aggregate data type that groups together zero or more named values of arbitrary types as a single entity. Each value is called a field. Field order is significant to type identity.

```go
type Employee struct {
  ID            int
  Name, Address string
  DoB           time.Time
  Position      string
  Salary        int
  ManagerID     int
}
var dilbert Employee  // dilbert is an instance of Employee
dilbert.Name = "John"
position := &dilbert.Position // taking address and accessing it through pointer
*position = "Senior"

var employeeOfMonth *Employee = &dilbert  // pointer to a struct
employeeOfMonth.Position += "proactive team player"
// same as (*employeeOfMonth).Position += "proactive team player"
```

Named struct of type S cannot declare field of same type S i.e. an aggregate value cannot contain itself. However, it can declare a field of pointer type _S_ and hence, allows to create recursive data structures like linked lists and trees.

```go
type tree struct {
  value       int
  left, right *tree
}

func appendValues(values []int, t *tree) []int {
  if t != nil {
    values = appendValues(values, t.left)
    values = append(values, t.value)
    values = appendValues)values, t.right)
  }
  return values
}
```

Struct type with no fields is called empty struct{} with size zero and carries no information. Can be used instead of bool as the value type of a map that represents a set, to emphasize that only the keys are significant. However, syntax is more cumbersome.

```go
seen := make(map[string]struct{})
if _, ok := seen[s]; !ok {
  seen[s] = struct{}{}
  // perform logic for first time seeing s
}
```

### Tags

A struct tag is additional meta information inserted into struct fields. The meta data can be acquired through reflection. They usually provide information on how a struct field is encoded or decoded from a format.

```
encoding/json
encoding/xml
gopkg.in/mgo.v2/bson
gorm.io/gorm
github.com/gocarina/gocsv
gopkg.in/yaml.v2
```

```go
type Config struct {
  // Separate multiple tags with space
  Port int `yaml:"port" json:"portNumber"`
}

```

### Struct literals

```go
type Point struct{X, Y int}
// first form
P := Point{1, 2} // However, order is critical and makes code fragile should set of fields grow/reorder

// second form; both cannot be mixed in the same literal
P := Point{a: 1, b: 2} // if field is omitted, it is set to zero and order doesn't matter as names are provided

// struct values can be passed as arg and returned from functions directly/indirectly
func Bonus(e *Employee, percent int) int {
  return e.Salary * percent / 100
}

// Need use pointer as function receives a copy of arg, not reference to original arg
func AnnualRaise(e *Employee) {
  e.Salary = e.Salary * 105/100
}

// structs are commonly dealt with through pointers; shorthand notation
pp := new(Point)
*pp = Point{1, 2} // Can be shorted to pp := &Point{1, 2}
```

### Comparing structs

```go
type Point struct {X, Y int}
p := Point{1, 2}
q := Point{2, 1}
fmt.Println(p.X == q.X && p.Y == q.Y} // false
```

Can be used as key type of a map.

```go
type address struct {
  hostname  string
  port      int
}

hits := make(map[address]int)
hits[address{"golang.org", 443}]++
```

### Struct embedding and anonymous fields

Composition in Go is achieved through embedding, which allows a struct to inherit the fields and methods of another struct.

Allows using named struct type as an anonymous field of another struct type. Provides convenient syntactic shortcut where x.f can stand for a chain of fields like x.d.e.f.

```go
type person struct {
	firstName string
	lastName string
	contactInfo
}

type contactInfo struct {
	email string
	number int
}

jim := person{
  firstName: "Jim",
  lastName: "Tan",
  contactInfo: contactInfo{
    email: "jim@gmail.com",
    number: 1234567,
  },
}
```

```go
type Point struct {
  X, Y int
}

type Circle struct {
  Center Point
  Radius int
}

type Wheel struct {
  Circle Circle
  Spokes int
}

// accessing the fields is more verbose
var w Wheel
w.Circle.Center.X = 8
w.Circle.Radius = 5
w.Spokes = 20
```

```go
// using anonymous fields
type Circle struct {
  Point
  Radius int
}

type Wheel struct {
  Circle
  Spokes int
}

var w Wheel
w.X = 8         // equivalent to w.Circle.Point.X = 8
w.Radius = 5

// however, does not have shorthand for struct literal syntax
w = Wheel{X: 8, Y: 8, Radius: 5, Spokes: 20}  // compile error: unknown fields
```

### Getters and setters

Go doesn't provide automatic support for getters and setters. You can provide yourself, but it's neither idiomatic nor necessary to put Get into the getter's name. If you have a field called owner (lower case, unexported), the getter method should be called Owner (upper case, exported), not GetOwner. The use of upper-case names for export provides the hook to discriminate the field from the method. A setter function, if needed, will likely be called SetOwner.

```go
owner := obj.Owner()
if owner != user {
    obj.SetOwner(user)
}
```
