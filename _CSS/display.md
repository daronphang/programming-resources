## Display

CSS property sets whether an element is treated as a block or inline element and the layout used for its children.

```
display: block;
display: inline;
display: inline-block;
display: flex;
display: inline-flex;
display: grid;
display: inline-grid;
display: flow-root;
display: table;
```

### Block

The element generates a block element box, with line breaks both before and after the element when in the normal flow. **Required if need to style an element with width and height**. Examples include div, section and p.

### Inline

Do not generate line breaks before or after themselves i.e. do not take up an entire space but the space an element would only take. Examples include span, anchor, and img.

### Inline-Block

Has the advantage of applying width and height while the element is inline by presentation.
