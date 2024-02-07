## Selectors

### +

The '+' selector is used to select elements that are placed immediately after the specified element but not inside the particular element i.e. not parent/child but a sibling.

```css
.current + sibling {
}
```

### space

Space refers to a descendant selector. Targets all tags within the particular element.

```css
.container p {
}
```

### >

Targets elements which are direct children of the particular element.

```html
<div id="container">
  <p>First</p>
  <div>
    <p>Child Paragraph</p>
    <!-- not targeted! -->
  </div>
  <p>Second</p>
  <p>Third</p>
</div>
```

```css
div#container p {
  font-weight: bold;
}
```

### ~

A general sibling combinator and similar to adjacent sibling combinator. Selects all elements that is preceded by a former selector.

```css
div ~ p {
  background-color: blue;
}
```
