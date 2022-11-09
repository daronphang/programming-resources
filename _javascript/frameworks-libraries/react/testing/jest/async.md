## Testing Asynchronous Code

For both promises or async/await, **need to return or await the promise**. Otherwise, your test will complete before the promise is returned.

### Promises

Return a promise from your test, and Jest will wait for that promise to resolve or reject (fails test).

```js
test('the data is peanut butter', () => {
  return fetchData().then((data) => {
    expect(data).toBe('peanut butter');
  });
});
```

### Async/Await

For rejects, can verify that a certain number of assertions is called. Otherwise, a fulfilled promise would not fail the test.

```js
test('the data is peanut butter', async () => {
  const data = await fetchData();
  expect(data).toBe('peanut butter');
});

test('the fetch fails with an error', async () => {
  expect.assertions(1);
  try {
    await fetchData();
  } catch (e) {
    expect(e).toMatch('error');
  }
});
```

Can combine async/await with resolves or rejects.

```js
test('the data is peanut butter', async () => {
  await expect(fetchData()).resolves.toBe('peanut butter');
});

test('the fetch fails with an error', async () => {
  await expect(fetchData()).rejects.toMatch('error');
});
```
