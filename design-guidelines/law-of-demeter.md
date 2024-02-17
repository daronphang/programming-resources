## Law of demeter (principle of least knowledge)

The law of demeter is a design guideline that recommends that objects **should avoid accessing the internal data and methods of other objects**. Instead, an object should only interact with its **immediate dependencies**. The law is most applicable in OOP.

Keeping proper object abstraction and hiding internals with encapsulation prevents unwanted chaining of method calls.

The main concepts of the law of demeter are as follows:

- Each object should have limited knowledge about other objects
- Each object should **only talk to its friends, not strangers** i.e. Employee with Manager, but not Employee with Amenities

An object O having a method M should invoke the following types of members only:

- The same object i.e. self
- Objects that have been passed as an argument to method M
- Local objects i.e. objects that have been created inside the method M
- Global objects that are accessible by object O
- Direct component objects of object O

### Benefits

- Reduces dependencies
- Helps to build components that are loosely coupled
- Easier code reuse, refactoring, maintenance and testability

## Examples

### Good

```java
public class LawOfDemeterInJava
{
  private Topping cheeseTopping;
  /**
   * Good examples of following the Law of Demeter.
   */
  public void goodExamples(Pizza pizza)
  {
    Foo foo = new Foo();

    // (1) it's okay to call our own methods
    doSomething();

    // (2) it's okay to call methods on objects passed in to our method
    int price = pizza.getPrice();

    // (3) it's okay to call methods on any objects we create
    cheeseTopping = new CheeseTopping();
    float weight = cheeseTopping.getWeightUsed();

    // (4) any directly held component objects
    foo.doBar();
  }

  private void doSomething()
  {
    // do something here ...
  }
}
```

### Bad

```java
var data = new A().GetObjectB().GetObjectC().GetData();
objectA.getObjectB().getObjectC().doSomething();
```

```java
public class LawOfDelimterDemo {
    /**
     * This method shows two violations of "Law of Delimiter"
     * or "Principle of least knowledge".
     */
    public void process(Order o) {

        // as per rule 1, this method invocation is fine,
        // because o is a argument of process() method
        Message msg = o.getMessage();

        // this method call is a violation, as we are using msg,
        // which we got from Order.
        // We should ask order to normalize message,
        // e.g. "o.normalizeMessage();"
        msg.normalize();

        // this is also a violation, instead using temporary variable
        // it uses method chain.
        o.getMessage().normalize();

        // this is OK, a constructor call, not a method call.
        Instrument symbol = new Instrument();

        // as per rule 4, this method call is OK, because
        // instance of Instrument is created locally.
        symbol.populate();
    }
}


Read more: https://javarevisited.blogspot.com/2014/05/law-of-demeter-example-in-java.html#ixzz8RuZqT6u5
```

## Code smells

Apart from extracting method to limit the dots in the code, there are other things that you should look at.

### Type checks of nested objects

The law allows you to only talk with the object you know directly. Asking any other object its type is a violation.

```java

class Company {
    private List<Department> departments;

    Map<DepartmentCode, BigDecimal> costPerDepartment() {
        return departments.stream()
            .filter(this::costCentre)
            .collect(
                Collectors.toMap(
                    Department::getCode,
                    Department::cost
                )
            );
    }

    private boolean costCentre(Department department) {
        // Violation.
        return department.getType() instanceof CostCentre;
    }

    private boolean costCentre(Department department) {
        // Acceptable.
        return department.isCostCentre();
    }
}
```

### Shameless assignment

Instead of method chaining to get an internal object, you might assign a returned value into a variable.

There is nothing bad in assigning a returned value, but invoking methods on it is something to be avoided.

```java
class Team {
    private Member manager;
    private List<Member> members;

    List<Member> getMembers() {
        return members;
    }

    String managerName() {
        Contact contact = manager.getContact();
        PersonalData personalData = contact.getPersonalData();
        return String.format(
            "%s %s",
            personalData.getName(),
            personalData.getSurname()
        );
    }
}
```

### Direct value return

Similar to shameless assignment, but you are reusing the value returned by a method.

```java
class Team {
    private Member manager;
    private List<Member> members;

    List<Member> getMembers() {
        return members;
    }

    String managerMail() {
        Contact contact = manager.getContact();
        return contact.getMail();
    }
}
```
