## Bulk Operations

There are several operations that copy or remove elements in bulk.

```java
// remove all elements from col1 that are in col2
col1.removeAll(col2); 
// keep all elements from col1 in col2
col1.retainAll(col2);
// get intersection
Set<String> result = new HashSet<>(a);
result.retainAll(b);
```

### View

You can apply bulk operations to a view.

```java
Map<String, Employee> staffMap = ...;
Set<String> terminatedIDs = ...;
// keySet is a view into the map
staffMap.keySet().removeAll(terminatedIDs);
```