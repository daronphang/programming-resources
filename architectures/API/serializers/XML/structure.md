## Structure

### Header

An XML document should start with a header, but is optional.

```xml
<?xml version="1.0" encoding="UTF-8"?></xml>
```

### Elements

It is best to structure your element to contain either child elements or text.

```xml
<!-- avoid -->
<font>
    Helvetica
    <size>36</size>
</font>

<!-- okay -->
<font>
    <name>Helvetica</name>
    <size>36</size>
</font>
```

### Attributes

There is some disagreement among XML designers about when to use elements and attributes. Though attributes may seem easier.

A commonly used rule of thumb is that attributes should be used only to modify the interpretation of a value, not to specify values.

```xml
<size unit="pt">36</size>
```
