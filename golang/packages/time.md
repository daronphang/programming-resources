## Dealing with dates and time

### Parsing date string

The time.Parse function assumes that the input time is in the local time zone of the system if no explicit time zone is provided.

ParseInLocation is like Parse but differs in two important ways. First, in the absence of time zone information, Parse interprets a time as UTC; ParseInLocation interprets the time as in the given location. Second, when given a zone offset or abbreviation, Parse tries to match it against the Local location; ParseInLocation uses the given location.

```go
startDateTime := "2025-01-09T10:38:35+08:00"
startTime, err := time.Parse(startDateTime, time.RFC3339)
```

```go
startDateTime := "2025-01-09T10:38:35+08:00"
layout := "2006-01-02T15:04:05+08:00"
loc, _ := time.LoadLocation("Local")
startTime, err := time.ParseInLocation(layout, startDateTime, loc)
fmt.Println(startTime)
// 2025-01-09 10:38:35 +0800 +08
```
