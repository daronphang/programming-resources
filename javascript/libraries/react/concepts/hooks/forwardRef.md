## ForwardRef

Ref forwarding is a techinque for automatically passing a ref through a component to one of its children. This is useful when you need to access a DOM element or component instance directly in a parent component, but the desired child element is wrapped by HOC or that doesn't expose ref by default. For instance, accessing DOM nodes may be unavoidable for managing focus, selection or animations.

### Example

```js
import * as React from 'react';
import ReactDOM from 'react-dom';

const InputText = React.forwardRef((props, ref) => <input ref={ref} {...props} />);

export default function App() {
  const ref = React.useRef();

  function focus() {
    ref.current.focus();
  }

  return (
    <div className="App">
      <InputText ref={ref} placeholder="my input" />
      <button onClick={focus}>Focus</button>
    </div>
  );
}

const rootElement = document.getElementById('root');
ReactDOM.render(<App />, rootElement);
```
