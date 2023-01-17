## React Portals

Portals provide a first-class way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

When displaying modals/alert boxes, they are overlays to the entire page and in HTML, it should be above everything else instead of nested in some HTML code. Portals help to make HTML rendered semantically correct and provide a clean HTML structure persepective.

```
content             Any valid renderable React element
containerElement    Valid DOM element to which we can append the content
```

```html
<!--index.html-->
<div id="backdrop-root"></div>
<div id="overlay-root"></div>
<!--instead of nesting in HTML code-->
<div id="root"></div>
```

```js
ReactDOM.createPortal(content, containerElement);
```

### Creating Portal

Function expects the container to be available in the DOM already and does not create the containerElement for us.

https://blog.logrocket.com/build-modal-with-react-portals/

```js
import { useState, useLayoutEffect } from 'react';
import { createPortal } from 'react-dom';

const createWrapper = (wrapperId) => {
  const wrapperElement = document.createElement('div');
  wrapperElement.setAttribute('id', wrapperId);
  document.body.appendChild(wrapperElement);
  return wrapperElement;
};

export default function createReactPortal({ children, wrapperId }) {
  const [wrapperElement, setWrapperElement] = useState(null);

  useLayoutEffect(() => {
    let element = document.getElementById(wrapperId);
    let systemCreated = false;

    if (!element) {
      element = createWrapper(wrapperId);
      systemCreated = true;
    }

    setWrapperElement(element);

    // cleanup to remove div from DOM during unmount
    return () => {
      // remove appended div from body
      if (systemCreated && element.parentNode) {
        element.parentNode.removeChild(element);
      }
    };
  }, [wrapperId]);

  // function expects container to be available in the DOM already
  // at start of first render, there is no div element attached
  if (wrapperElement === null) return null;

  return createPortal(children, document.getElementById(wrapperId));
}
```

### Z-index Precedence

The default behavior of DOM hierarchy when no z-index is set is that elements that appear lower in the hierarchy will take higher precedence.

```js
<body>
  <div id="root" />
  <div id="portal-root" />
</body>
```
