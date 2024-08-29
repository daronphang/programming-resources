## Null Object Pattern

The intent of a Null Object is to encapsulate the absence of an object by providing a substitutable alternative that offers suitable default do nothing behavior. In short, a design where "nothing will come of nothing".

It is sometimes thought that null objects are over simple and "stupid" but in truth a null object always knows exactly what needs to be done without interacting with any other objects.

Use the Null Object pattern when:

- a client would otherwise check for null just to skip execution or perform a default action
- an object requires a collaborator; this pattern does not introduce this collaboration but makes use of a collaboration that already exists
- Some collaborator instances should do nothing
- You want to abstract the handling of null away from the client

### Problem

Given that an object reference may be optionally null, and that the result of a null check is to do nothing or use some default value, how can the absence of an object — the presence of a null reference — be treated transparently?

```py
if customer is None:
    plan = BillingPlan.basic()
else:
    plan = customer.getPlan()
```

### Solution

Instead of null, return a null object that exhibits the default behavior. All methods are implemented to do "nothing".

```py
class NullCustomer(Customer):

    def isNull(self):
        return True

    def getPlan(self):
        return self.NullPlan()

    # Some other NULL functionality.

# Replace null values with Null-object.
customer = order.customer or NullCustomer()

# Use Null-object as if it's normal subclass.
plan = customer.getPlan()
```
