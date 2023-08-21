## Enums

Types defined by enum is a class. As it is not possible to construct new objects, you never need to use equals(); simply use == to compare.

```java
public enum Size { SMALL, MEDIUM, LARGE, EXTRA_LARGE };
Size.SMALL.toString() // SMALL

Size s = Enum.valueOf(Size.class, "SMALL"); // sets s to Size.SMALL

Size[] values = Size.values(); // [Size.SMALL, Size.MEDIUM, etc]
```

### Adding Fields and Methods

You can add constructors, fields and methods to an enumerated type. The constructor is only invoked when the enumerated constants are constructed.

```java
public enum Size {
    SMALL("S"), MEDIUM("M"), LARGE("L"), EXTRA_LARGE("XL");

    private String abbreviation;

    private Size(String abbreviation) {
        this.abbreviation = abbreviation;
    }

    public String getAbbreviation() {
        return abbreviation;
    }
}
```
