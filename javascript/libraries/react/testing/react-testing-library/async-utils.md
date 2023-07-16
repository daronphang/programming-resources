## Async Utilities

Instead of using act(), can make use of async utilities provided by RTL including waitFor, waitForElementToBeRemoved, or findBy. These utilities are already wrapped in act().

```js
it('renders title', async () => {
  jest.spyOn(window, 'fetch').mockResolvedValue({
    json: async () => ({ title: 'Fetched' }),
  });

  render(<App />);
  expect(await screen.findByText('Fetched')).toBeInTheDocument();
});
```

```js
it('renders title', async () => {
  jest.spyOn(window, 'fetch').mockResolvedValue({
    json: async () => ({ title: 'Fetched' }),
  });

  render(<App />);
  await waitFor(() => expect(screen.getByText('Fetched')).toBeInTheDocument());
});
```

https://javascript.plainenglish.io/you-probably-dont-need-act-in-your-react-tests-2a0bcd2ad65c

## act()

When something happens in a test, React needs to call the event handler, update the state, and run useEffect. React state updates are asynchronous and hence, React needs to know when to do all of these things, which is why act() is necessary.

Whenever a state update is scheduled asynchronously, the test can no longer stay synchronous due to the event loop. Otherwise, React will warn us that state updates are not wrapped in act().

For **asynchronous updates, they will go into the task queue** and are only executed after the call stack is clear. **For expect(), they will go into the call stack** and hence, will run before the state update is scheduled.

```js
// App.js
import { useEffect, useState } from 'react';

const App = () => {
  const [title, setTitle] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');
      const { title } = await response.json();

      setTitle(title); // this happens after the test is done
    };

    fetchData();
  }, []);

  return <>{title}</>;
};
```

```js
// App.test.js
// test does everything synchronously
import { render, screen } from '@testing-library/react';

it('renders title', () => {
  jest.spyOn(window, 'fetch').mockResolvedValue({
    json: async () => ({ title: 'Fetched' }),
  });

  render(<App />);

  // this happens before the state update is scheduled
  // test fails
  expect(screen.getByText('Fetched')).toBeInTheDocument();
});
```
