## Polyfilling

Polyfill is used to refer to taking the definition of a feature and provide an equivalent piece of code to give modern functionality on older browsers that do not natively support it e.g. Number.isNaN.

However, not all features are polyfillable, and you should be very careful with implementing them because if your polyfill does not adhere precisely to the specification, all of your code that uses polyfill will be incorrect.

Typically you use a polyfill, if your target browser did not yet implement the latest bleeding edge feature (read browser APIs) you want to use. A transpiler on the other hand will let you use language features, the target environment does not support yet, e.g. some ES6 features like fat arrow functions.

```js
// Outdated browsers do not have Math.trunc

if (!Math.trunc) {
  // if no such function
  // implement it
  Math.trunc = function (number) {
    // Math.ceil and Math.floor exist even in ancient JavaScript engines
    return number < 0 ? Math.ceil(number) : Math.floor(number);
  };
}
```

### Examples

Examples include core.js and polyfill.io.
