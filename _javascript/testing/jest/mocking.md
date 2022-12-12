## Mock Functions

Allows you to test the links between code by erasing the actual implementation of a function, capturing calls to the function and its parameters, capturing instances of constructor functions when instantiated with new, and allowing test-time configurations of return values.

### .mock

All mock functions have .mock property, which is where data about how the function has been called and what the function returned is kept. Can also be used to track the value of 'this' for each call.

```js
function forEach(items, callback) {
  for (let index = 0; index < items.length; index++) {
    callback(items[index]);
  }
}

// testing the implementation
const mockCallback = jest.fn((x) => 42 + x);
forEach([0, 1], mockCallback);

// The function was called exactly once
expect(someMockFunction.mock.calls.length).toBe(1);

// The first arg of the first call to the function was 'first arg'
expect(someMockFunction.mock.calls[0][0]).toBe('first arg');

// The second arg of the first call to the function was 'second arg'
expect(someMockFunction.mock.calls[0][1]).toBe('second arg');

// The return value of the first call to the function was 'return value'
expect(someMockFunction.mock.results[0].value).toBe('return value');

// The function was called with a certain `this` context: the `element` object.
expect(someMockFunction.mock.contexts[0]).toBe(element);

// This function was instantiated exactly twice
expect(someMockFunction.mock.instances.length).toBe(2);

// The object returned by the first instantiation of this function
// had a `name` property whose value was set to 'test'
expect(someMockFunction.mock.instances[0].name).toEqual('test');

// The first argument of the last call to the function was 'test'
expect(someMockFunction.mock.lastCall[0]).toBe('test');
```

### Mock Return Values

```js
const myMock = jest.fn();
console.log(myMock());
// > undefined

myMock.mockReturnValueOnce(10).mockReturnValueOnce('x').mockReturnValue(true);

console.log(myMock(), myMock(), myMock(), myMock());
// > 10, 'x', true, true
```

### Mocking Modules

Once we mock a module, we can provide a mockResolvedValue that returns the data we want our test to assert against.

```js
import axios from 'axios';
import Users from './users';

jest.mock('axios');

test('should fetch users', () => {
  const users = [{ name: 'Bob' }];
  const resp = { data: users };
  axios.get.mockResolvedValue(resp);

  // or you could use the following depending on your use case:
  // axios.get.mockImplementation(() => Promise.resolve(resp))

  return Users.all().then((data) => expect(data).toEqual(users));
});
```

### Mock Partials

Subsets of a module can be mocked while the rest can be kept to their actual implementation.

```js
export const foo = 'foo';
export const bar = () => 'bar';
export default () => 'baz';

//test.js
import defaultExport, { bar, foo } from '../foo-bar-baz';

jest.mock('../foo-bar-baz', () => {
  const originalModule = jest.requireActual('../foo-bar-baz');

  //Mock the default export and named export 'foo'
  return {
    __esModule: true,
    ...originalModule,
    default: jest.fn(() => 'mocked baz'),
    foo: 'mocked foo',
  };
});

test('should do a partial mock', () => {
  const defaultExportResult = defaultExport();
  expect(defaultExportResult).toBe('mocked baz');
  expect(defaultExport).toHaveBeenCalled();

  expect(foo).toBe('mocked foo');
  expect(bar()).toBe('bar');
});
```

### Mock Implementations

To fully replace the implementation of a mock function instead of specifying the return values only. Can either do it with jest.fn or mockImplementationOnce method.

```js
// jest fn
const myMockFn = jest.fn((cb) => cb(null, true));

myMockFn((err, val) => console.log(val));
// > true

// mockImplementation
jest.mock('../foo'); // this happens automatically with automocking
const foo = require('../foo');

// foo is a mock function
foo.mockImplementation(() => 42);
foo();
// > 42

// chaining multiple functions
const myMockFn = jest
  .fn()
  .mockImplementationOnce((cb) => cb(null, true))
  .mockImplementationOnce((cb) => cb(null, false));

myMockFn((err, val) => console.log(val));
// > true

myMockFn((err, val) => console.log(val));
// > false
```

### Mock Names

Can optionally provide a name for mock functions which will be displayed instead of 'jest.fn()'.

```js
const myMockFn = jest
  .fn()
  .mockReturnValue('default')
  .mockImplementation((scalar) => 42 + scalar)
  .mockName('add42');
```
