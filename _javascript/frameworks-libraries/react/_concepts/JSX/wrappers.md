## Wrapper/Fragment Component

JSX requires one root element that return a constant or variable. Can create your own or use <React.Fragment> or <> (empty).

React implementation relies on constructing a tree-like structure which it uses for reconciliation. When multiple elements are returned from the render method, the assumption that the tree will have one root node will no longer hold, hence, making it difficult to processs reconciliation algorithm.

```javascript
// helper/wrapper.js
const Wrapper = (props) => {
  return props.children; // return content between <wrapper></wrapper>
};

export default Wrapper;
```

```javascript
// Fragments
return (
  <React.Fragment>
    <h2>hi</h2>
    <p>this works</p>
  </React.Fragment>
);

return (
  <>
    <h2>hi</h2>
    <p>this works</p>
  </>
);
```
