## Specification

In all kinds of applications, boolean test methods can be used to evaluate simple business rules.

```java
public boolean isOverdue() {
    Date currentDate = new Date(); return currentDate.after(dueDate);
}
```

However, not all rules are simple. Instead, developers will often refractor the rule evaluation code into the application layer.

Business rules often do not fit the responsibility of entities or value objects, and their variety and combinations can overwhelm the basic meaning of the domain object. However, moving the rules out of the domain layer (to the application layer) is **even worse**, since the domain code no longer expresses the model.

A predicate is a function that evaluates to true or false and can be combined using operators i.e. and, or. However, the implementation of this concept with objects is cumbersome. Nevertheless, we can **borrow the concepts of predicates and create specialized objects that evaluate to a boolean**.

A specification is predicate that determines if an object does or does not satisfy some criteria. It states a constraint on the state of another object, which may or may not be present. Hence, **create explicit predicate-like value objects for specialized purposes**.

The specification **keeps the rule in the domain layer**. Since the rule is a full-fledged object, the design can be more expressive.

### Implementation

Much of the value of specification is that it **unifies application functionality** that may seem quite different. We need to specify the state of an object for three reasons:

- Validation of an object to see if it fulfills some need or is ready for some purpose
- Selection of an object from a collection
- Specifying the creation of a new object to fit some need

```java
class DelinquentInvoiceSpecification extends InvoiceSpecification {
    private Date currentDate;

    public DelinquentInvoiceSpecification(Date currentDate) {
        this.currentDate = currentDate;
    }

    public boolean isSatisfiedBy(Invoice candidate) {
        int gracePeriod = candidate.customer().getPaymentGracePeriod();
        Date firmDeadline = DateUtility.addDaysToDate(
            candidate.dueDate(), gracePeriod);
        return currentDate.after(firmDeadline);
    }
}

// Using object as an dependency
class InvoiceRepository {
    public Set selectSatisfying(InvoiceSpecification spec) {
        Set results = new HashSet();
        Iterator it = invoices.iterator();
        while (it.hasNext()) {
            Invoice candidate = (Invoice) it.next();
            if (spec.isSatisfiedBy(candidate)) results.add(candidate);
        }
        return results;
    }
}

Set delinquentInvoices = invoiceRepository.selectSatisfying(
    new DelinquentInvoiceSpecification(currentDate)
);
```

### Querying

SQL provides a very natural way to write specifications. Specifications mesh smoothly with repositories, which provides query access to domain objects and encapsulating the interface to the database.

### Building-to-order

Building-to-order can mean creation of an object from scratch to meet the specifications, but it is often a configuration of existing objects to satisfy the specifications.

```java
public class ContainerSpecification {
    private ContainerFeature requiredFeature;
    public ContainerSpecification(ContainerFeature requiredFeature) {
        this.requiredFeature = requiredFeature;
    }

    boolean isSatisfiedBy(Container aContainer){
        return aContainer.getFeatures().contains(requiredFeature);
    }
}

public class Container {
    boolean isSafelyPacked(){
        ContainerSpecification packingSpec = getDrum().getContainerSpecification();
        Iterator it = contents.iterator();
        while (it.hasNext()) {
            Drum drum = (Drum) it.next();
            if (!drum.containerSpecification().isSatisfiedBy(this)) return false;
        }
    return true;
    }
}

tnt.setContainerSpecification(new ContainerSpecification(ARMORED));
```
