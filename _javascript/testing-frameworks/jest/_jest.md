## Jest

For running unittesting. Unit tests uphold business logic and ensures that your methods return the expected value for different cases.

## Spying on Functions in React Functional Components

For functions defined in components, they do not exist in component's prototype method and hence, jest spyOn() cannot spy on an undefined value. Can rely on console.log for testing.

Should spy on component's dependencies for more reliable testing.

```js
const logSpy = jest.spyOn(console, 'log');
expect(logSpy).toBeCalledWith('hello world');
```
