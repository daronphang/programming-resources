## Event bubbling

Event bubbling is a concept in the DOM. When an event happens on an element, it first runs the handlers on it, then on its parent and all the way up on other ancestors.

Event bubbling behavior makes it possible for you to handle an event in a parent element instead of the actual element that received the event. This pattern is called **Event Delegation**.

Most events bubble, though there are a few exceptions i.e. focus.

```html
<!-- Clicking on p will trigger all 3 alerts-->
<form onclick="alert('form')">
  FORM
  <div onclick="alert('div')">
    DIV
    <p onclick="alert('p')">P</p>
  </div>
</form>
```

### event.target, this

The most deeply nested element that caused the event is called a **target element**, accessible as event.target. It does not change through the bubbling process.

However, 'this' refers to the current element, the one that has a currently running handler on it.

### Stopping bubbling

A bubbling event goes from the target element straight up until `<html>` or document object. For a handler to stop bubbling, use event.stopPropagation() or event.preventDefault().

However, if an element has multiple event handlers on a single event, even if one of them stops bubbling, the other ones will still execute. To prevent this, use event.stopImmediatePropagation().
