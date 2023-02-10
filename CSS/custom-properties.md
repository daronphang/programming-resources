## Custom Properties

Entities defined by CSS authors that contain specific values to be reused throughout a document. Inheritance applies to custom properties.

Can define multiple fallback values when the given variable is not yet defined.

```css
:root {
  --main-bg-color: brown;
}

.one {
  color: var(--my-var, red);
  background-color: var(--main-bg-color);
}
```

### Invalid Properties

When the browser encounters an invalid value for a normal property:

- Checks if the property is inheritable.
- Set the value to its default initial value.

```html
<p>This paragraph is initially black.</p>
```

```css
:root {
  --text-color: 16px;
}

p {
  /* color not applied as it is not a parent element */
  color: blue;
}

p {
  /* 16px is invalid, checks if parent has value */
  color: var(--text-color);
}
```
