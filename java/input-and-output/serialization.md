## Serialization

To save/load an object from an object stream, the class needs to implement the Serializable interface. This interface has no methods and hence, you do not need to change your class in any way.

```java
class Employee implements Serializable { ... }
```

### Saving

```java
ObjectOutputStream out = new ObjectOutputStream(
    new FileOutputStream("employee.dat")
);

Employee harry = new Employee("Harry Hacker", 50000, 1989, 10, 1);
Manager boss = new Manager("Carl Cracker", 80000, 1987, 12, 15);
out.writeObject(harry);
out.writeObject(boss);
```

### Loading

```java
ObjectInputStream in = new ObjectInputStream(
    new FileInputStream("employee.dat")
);
Employee e1 = (Employee) in.readObject();
Employee e2 = (Employee) in.readObject();
```

### Serializing Singletons and Enumerations

You have to pay attention to serializing/deserializing objects that are assumed to be unique.

If you use the enum construct, you need not worry about serialization. However, for singletons, you need to define readResolve(). It is called after the object is deserialized, and must return an object which then becomes the return value of the readObject().

```java
public class Orientation {
    public static final Orientation HORIZONTAL = new Orientation(1);
    public static final Orientation VERTICAL = new Orientation(2);
    private int value;
    private Orientation(int v) { value = v; }
}

Orientation original = Orientation.HORIZONTAL;
ObjectOutputStream out = . . .;
out.write(original);
out.close();
ObjectInputStream in = . . .;
Orientation saved = (Orientation) in.read();
if (saved == Orientation.HORIZONTAL) . . . // will fail the test

protected Object readResolve() throws ObjectStreamException {
    if (value == 1) return Orientation.HORIZONTAL;
    if (value == 2) return Orientation.VERTICAL;
    throw new ObjectStreamException(); // this shouldn't happen
}
```

### Cloning

Serialization gives you an easy way to clone an object, provided the class is serializable. The class needs to **extend SerialCloneable class**. The result is a new object that is a deep copy of the existing object. You can use a ByteArrayOutputStream to save the data into a byte array.

However, this method will be usually much slower than a clone() that explicitly constructs a new object and copies/clones the data fields.

```java
class SerialCloneable implements Cloneable, Serializable {
    public Object clone() throws CloneNotSupportedException {
        try {
            // save the object to a byte array
            ByteArrayOutputStream bout = new ByteArrayOutputStream();
            try (ObjectOutputStream out = new ObjectOutputStream(bout)) {
                out.writeObject(this);
            }

            // read a clone of the object from the byte array
            try (InputStream bin = new ByteArrayInputStream(bout.toByteArray())) {
                ObjectInputStream in = new ObjectInputStream(bin);
                return in.readObject();
            }
        }
        catch (IOException | ClassNotFoundException e) {
            CloneNotSupportedException e2 = new CloneNotSupportedException();
            e2.initCause(e);
            throw e2;
        }
    }
 }
```

## Algorithm

Each object is saved with the serial number, and will likely occupy a completely different memory address than it originally did when it is reloaded.

Raw memory addresses and meaningless in a file or when communicating with a different processor. By replacing memory addresses with serial numbers, **serialization permits the transport of object collections from one machine to another**.

### Writing

1. Associate a serial number with each object reference that you encounter
2. When encountering an object reference for the first time, save the object data to the output stream
3. If it has been saved previously, write the saved object

### Reading

1. When an object is specified in an object input stream for the first time, construct it, initialize it with the stream data, and remember the association between the serial number and object reference
2. When the same serial number is encountered, retrieve the associated object reference

## Object Serialization File Format

Object serialization saves object data in a particular file format:

- The serialized format contains the type and data fields of all objects
- Each object is assigned a serial number
- Repeated occurrences of the same object are stored as references to that serial number

## Modifying Serialization Mechanism

For fields that you do not want to serialize, you cna mark them with transient keyword. Transient fields are always skipped when objects are serialized.

```java
public class LabeledPoint implements Serializable {
    private String label;
    private transient Point2D.Double point;
    . . .
}
```

A class can define its own mechanism for serializing the data by implementing the Externalizable interface. Both readExternal() and writeExternal() are fully responsible for saving and restoring the entire object, including the superclass data.

```java
public class HelloWorld implements Externalizable {
    public void readExternal(ObjectInputStream in) throws IOException ClassNotFoundException;

    public void writeExternal(ObjectOutputStream out) throws IOException;
}
```
