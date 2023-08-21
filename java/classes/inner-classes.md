## Inner Classes

An inner class is a class defined inside another class. Reasons for doing this:

- Inner class methods can access the data from the scope in which they are defined, including private data
- Inner classes can be hidden from other classes in the same package
- Anonymous inner classes are handy when you want to define callbacks without writing lots of code

An object of an inner class always gets an implicit reference to the object that created it.

```java
class TalkingClock {
    private int interval;
    private boolean beep;

    public TalkingClock(int interval, boolean beep) {
        this.interval = interval;
        this.beep = beep;
    }

    public void start() {
        ActionListener listener = new TimePrinter();
        Timer t = new Timer(this.interval, listener);
        t.start();
    }

    public class TimePrinter implements ActionListener {
        // you do not need to define a constructor is the compiler generates it automatically
        // outer class reference is set in the constructor
        public TimePrinter(TalkingClock clock) {
            outer = clock;
        }

        public void actionPerformed(ActionEvent event) {
            System.out.println("At the tone, the time is " + new Date());
            if (beep) Toolkit.getDefaultToolkit().beep();

            // proper syntax for the outer reference
            if (TalkingClock.this.beep) Toolkit.getDefaultToolkit().beep();
        }
    }


}

public static InnerClassTest {
    public static void main(String[] args) {
        TalkingClock clock = new TalkingClock(1000, true);
        clock.start();
        // keeps program running until user selects ok
        JOptionPane.showMessageDialog(null, "Quit program?");
        System.exit(0);
    }
}
```

### Fields

Any static fields declared in an inner class must be final. This is because a separate instance of the inner class is created for each outer object; if the field is not final, it may not be unique.

### Methods

An inner class cannot have static methods.

### Anonymous Inner Classes

If you want to make only a single object of this class, you don't need to give the class a name.

It cannot have constructors because the name of a constructor must be the same as the name of a class. Instead, **the construction parameters are given to the superclass constructor**. Whenever an inner class implements an interface, it cannot have any construction parameters.

```
// syntax
new SuperType(construction parameters) {
    inner class methods and data
}
```

```java
public void start(int interval, boolean beep) {
    ActionListener listener = new ActionListener() {
        public void actionPerformed(ActionEvent event) {
            System.out.println("At the tone, the time is " + new Date());
            if (beep) Toolkit.getDefaultToolkit().beep();
        }
    }
}
```

### Double Brace Initialization

You can take advantage of the inner class syntax if you don't need the object again. The outer braces make an anonymous subclass of ArrayList. The inner braces are an object construction block.

```java
ArrayList<String> friends = new ArrayList<>();
friends.add("Harry");
friends.add("Tony");
invite(friends);

invite(new ArrayList<String>() {{
    add("Harry");
    add("Tony");
}});
```

### Static Inner Classes

Can be useful if you don't want the inner class to have a reference to the outer class i.e. computing the max/min of an array.

```java
class ArrayAlg {
    public static Pair minmax(double[] values) {
        double min = Double.POSITIVE_INFINITY;
        double max = Double.NEGATIVE.INFINITY;
        for (double v: values) {
            if (min > v) min = v;
            if (max < v) max  v;
        }
        return new Pair(min, max);
    }

    public static class Pair {
        private double first;
        private double second;

        public Pair (double f, double s) {
            first = f;
            second = s;
        }

        public double getFirst() {
            return first;
        }

        public double getSecond() {
            return second;
        }
    }
}

public class StaticInnerClassTest {
    public static void main(String[] args) {
        double[] d = new double[20];
        for (int i = 0; i < d.length; i++) {
            d[i] = 100 * Math.random();
        }
        ArrayAlg.Pair p = ArrayAlg.minmax(d);
        System.out.println("min = " + p.getFirst());
        System.out.println("max = " + p.getSecond());
    }
}
```

## Tips

### Logging

When you produce logging or debugging messages, you often want to include the name of the current class, but that fails in a static method.

```java
System.err.println("error happened in " + new Object(){}.getClass().getEnclosingClass());
```
