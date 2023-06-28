## Horizontal Alignment

```css
.class {
  text-align: center; /* for inline-elements */
}
```

````css
.class {
  margin-left: auto;
  margin-right: auto;
}

```css .class {
  display: relative;
  width: 50rem;
  left: calc(50% - 25rem);
}
````

## Vertical Alignment

### Vertical Align Property

Property that sets the vertical alignment of an inline, inline-block or table-cell box. **It cannot be used to vertically align block-level elements**.

```
vertical-align: baseline;
vertical-align: sub;
vertical-align: super;
vertical-align: text-top;
vertical-align: text-bottom;
vertical-align: middle;
vertical-align: top;
vertical-align: bottom;
```

### Block Elements

http://phrogz.net/CSS/vertical-align/index.html

```css
.parent {
  position: relative;
}

.child {
  position: relative; /* absolute */
  top: 50%;
  height: 5em;
  margin-top: -2.5em; /* half the height of child container to offset item up */
}
```

## inset

Shorthand for top, right, bottom, left properties. Has the same multi-value syntax of the margin shorthand.

```
inset: 1em;
```
