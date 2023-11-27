## CLS

The CLS is a set of rules that describe in vivid detail the minimal and complete set of features a given .NET compiler must support to produce code that can be hosted by the .NET Runtime, while at the same time be **accessed in a uniform manner by all languages** that target the .NET platform. In many ways, the CLS can be viewed as a **subset** of the full functionality defined by the CTS.

The CLS is ultimately a set of rules that compiler builders must conform to if they intend their products to function seamlessly within the .NET universe. Each rule is assigned a simple name and describes how this rule affects those who build the compilers as well as those who interact with them i.e. CLS Rule 1.

```c#
class Calc {
    // Exposed unsigned data (ulong) is not CLS compliant!
    // signed int can represent positive and negative numbers
    // unsigned can only represent non-negative numbers
    public ulong Add(ulong addend1, ulong addend2)
    {
        return addend1 + addend2;
    }
}

class Calc {
    // CLS compliant as ulong is used internally
    public int Add(int addend1, int addend2)
    {
        ulong temp = 0;
        return addend1 + addend2;
    }
}
```

### Ensuring CLS compliance

C# does define a number of programming constructs that are not CLS compliant. Nonetheless, you can instruct the C# compiler to check your code for CLS compliance using a single .NET attribute.

```
// tell the C# compiler to check for CLS compliance
[assembly: CLSCompliant(true)]
```
