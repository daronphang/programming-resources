## Module Design Pattern

Javascript modules are the most prevalently used design patterns for keeping particular pieces of code independent of other components. This provides loose coupling to support well-structured code.

The module pattern is easy to use and creates encapsulation of your code. Modules are commonly used as Singleton style objects where only one instance exists.

### ES2015 Modules

ES2015 introduced built-in JS modules. A module is a file containing JS code.

```js
const privateValue = "hello world";

export default function add(x, y) {
  return x + y;
}

export function multiply(x) {
  return x * 2;
}

export function subtract(x, y) {
  return x - y;
}

export function square(x) {
  return x * x;
}
```

```js
import { add, multiply, subtract, square } from "./math.js";
```

### Named vs Default

You can only have one default export per module. With a default export, you can import the value without brackets.

```js
import add, { multiply, subtract, square } from "./math.js";
```

### Private Methods and Properties

JS does not have a private keyword by default but by using closures, we can create private methods and state.

```js
var myModule = (function () {
  "use strict";

  var _privateProperty = "Hello World";

  function _privateMethod() {
    console.log(_privateProperty);
  }

  return {
    publicMethod: function () {
      _privateMethod();
    },
  };
})();

myModule.publicMethod(); // 'Hello World'
console.log(myModule._privateProperty); // is undefined
myModule._privateMethod(); // is TypeError
```

## Revealing Module Pattern

One of the most popular ways of creating modules by using the return statement that reveals only the methods or properties exposed to public.

```js
var myModule = (function () {
  "use strict";

  var _privateProperty = "Hello World";
  var publicProperty = "I am a public property";

  function _privateMethod() {
    console.log(_privateProperty);
  }

  function publicMethod() {
    _privateMethod();
  }

  return {
    publicMethod: publicMethod,
    publicProperty: publicProperty,
  };
})();

myModule.publicMethod(); // 'Hello World'
console.log(myModule.publicProperty); // 'I am a public property'
console.log(myModule._privateProperty); // is undefined
myModule._privateMethod(); // is TypeError
```
