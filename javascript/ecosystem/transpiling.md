## Transpiling

There’s no way to polyfill **new syntax** that has been added to the language. The new syntax would throw an error in the old JS engine as unrecognized/invalid. So the better option is to use a tool that converts your newer code into older code equivalents.

Transpiling (transforming plus compiling) is the process of **converting your newer code into an older code equivalent** i.e. transpiling ES6 and above into ES5.

Transpiler is a tool that converts source code written in one programming language (such as ES6+ JavaScript) into another, usually older or more widely supported version (like ES5 JavaScript), making it compatible with a broader range of browsers.

These tools are not compilers as they don't compile to a lower-level representation; they're just different languages at a similar level of abstraction.

```js
// JS before 2020 did not have nullish coalescing operator.
// before running the transpiler
height = height ?? 100;

// after running the transpiler
height = height !== undefined && height !== null ? height : 100;
```

### Examples

Examples include Babel, Traceur, etc.
