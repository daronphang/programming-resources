## Testing Without Library

### React Hook

```js
import { useState, useEffect } from 'react';
const CACHE = {};

export default function useStaleRefresh(url, defaultValue = []) {
  const [data, setData] = useState(defaultValue);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    // cacheID is how a cache is identified against a unique request
    const cacheID = url;
    // look in cache and set response if present
    if (CACHE[cacheID] !== undefined) {
      setData(CACHE[cacheID]);
      setLoading(false);
    } else {
      // else make sure loading set to true
      setLoading(true);
      setData(defaultValue);
    }
    // fetch new data
    fetch(url)
      .then((res) => res.json())
      .then((newData) => {
        CACHE[cacheID] = newData;
        setData(newData);
        setLoading(false);
      });
  }, [url, defaultValue]);

  return [data, isLoading];
}
```

### Testing

```js
// mock fetch to have control over what the API returns
function fetchMock(url, suffix = '') {
  return new Promise(
    (resolve) =>
      setTimeout(() => {
        resolve({
          json: () =>
            Promise.resolve({
              data: url + suffix,
            }),
        });
      }, 200 + Math.random() * 300) // delay to replicate real world requests
  );
}
```

Can use beforeAll and afterAll as the function is stateless and does not require a reset after each individual test.

```js
// runs before any tests start running
beforeAll(() => {
  jest.spyOn(global, 'fetch').mockImplementation(fetchMock);
});

// runs after all tests have finished
afterAll(() => {
  global.fetch.mockClear();
});
```

Mounting hook into a component.

```js
// global variable to avoid changing object pointer on re-render
const defaultValue = { data: '' };

function TestComponent({ url }) {
  const [data, isLoading] = useStaleRefresh(url, defaultValue);
  if (isLoading) {
    return <div>loading</div>;
  }
  return <div>{data.data}</div>;
}
```

Mounting component onto the DOM.

```js
let container = null;

beforeEach(() => {
  // set up a DOM element as a render target
  container = document.createElement('div');
  document.body.appendChild(container);
});

afterEach(() => {
  // cleanup on exiting
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});
```

Testing functionality.

```js
it('useStaleRefresh hook runs correctly', async () => {
  // ...
  // new response
  global.fetch.mockImplementation((url) => fetchMock(url, '__'));

  // set url to url1 again
  act(() => {
    render(<TestComponent url="url1" />, container);
  });
  expect(container.textContent).toBe('url1');
  await act(() => sleep(500));
  expect(container.textContent).toBe('url1__');

  // set url to url2 again
  act(() => {
    render(<TestComponent url="url2" />, container);
  });
  expect(container.textContent).toBe('url2');
  await act(() => sleep(500));
  expect(container.textContent).toBe('url2__');
});
```

### Helpers

```js
// instead of waiting for fixed timing, execute assertion until it passes or
// timeout is reached
async function waitFor(cb, timeout = 500) {
  const step = 10;
  let timeSpent = 0;
  let timedOut = false;

  while (true) {
    try {
      await sleep(step);
      timeSpent += step;
      cb();
      break;
    } catch {}
    if (timeSpent >= timeout) {
      timedOut = true;
      break;
    }
  }

  if (timedOut) {
    throw new Error('timeout');
  }
}
```
