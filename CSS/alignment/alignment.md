## Horizontal Alignment

```css
text-align: center; /* for inline-elements */

margin-left: 5%;
margin-right: 5%;
```

## Vertical Align Property

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

## Block Elements

http://phrogz.net/CSS/vertical-align/index.html

### Method 1

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
