## Testing React Hooks

### renderHook

Can declare props that are passed to the render-callback when first invoked using initialProps. They will not be called if you call rerender without props.

https://react-hooks-testing-library.com/reference/api#renderhook

```
result      Data stored in result.current
rerender    Renders the previosuly rendered render-callback with new props
```

```js
const { result, wait, rerender } = renderHook(({ url }) => useStaleRefresh(url, defaultValue), {
  initialProps: {
    url: 'url1',
  },
});
```
