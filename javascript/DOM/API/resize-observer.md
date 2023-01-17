## Resize Observer

Interface reporting changes to the dimensions of an element's content or border box.

```js
const resizeObserver = new ResizeObserver((entries) => {
  entries.forEach((entry) => {
    const width = entry.contentBoxSize[0].inlineSize;
    const test = document.getElementById('test');
    test.style.height = `${width / 12}rem`;
    // width adjusted accordingly to scale
  });
});

useEffect(() => {
  const body = document.querySelector('body');
  resizeObserver.observe(body);

  return () => {
    resizeObserver.disconnect();
  };
}, []);
```

## Entry

https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserverEntry

```
entry.borderBoxSize
entry.contentBoxSize
entry.devicePixelContentBoxSize
entry.contentRect
entry.target
```

### borderBoxSize

```
blockSize       Height
inlineSize      Width
```
