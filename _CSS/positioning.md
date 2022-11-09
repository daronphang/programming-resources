## Overview

Both absolute and fixed will not flow around the elements on page and do not take up space. For relative, takes up space but offsets do not occupy space.

```
static
absolute    Position anywhere on page, relative to next parent element with relative/absolute positioning
fixed       Positioned relative to viewport/browser window i.e. for navbar
relative    Relative to itself and able to use z-index
sticky      Positioned based on user's scroll position
```

## Static

Position an element based on its current position in the flow. Top, right, bottom, left and z-index properties do not apply. This is the default for every single page element.

## Relative

Position an element based on its current position without changing layout around it. Takes up the original space and hence, leaves a gap where it would have been without additional positioning. Has ability to use z-index; even if it is not used, the element will appear on top of any other statically positioned element.

## Fixed

Element is positioned relative to the viewport or the browser window itself. Viewport doesn't change when the window is scrolled and hence, it will stay right where it is. No space is created as the element is removed from the normal document flow. If there is no width set or no content is available, the element would not be visible.

## Absolute

Position an element based on its closest positioned ancestor/parent position. **Does not take up space as elements are removed from the flow of elements on the page**. If there is no parent, it will position based on <html> element i.e. relative to the page itself. **For children elements to have positioning of "absolute", parent is required to have position as either "relative" or "absolute"**. Take note that when an element has position relative/absolute, it will be placed on top of any element with "static" positioning.

All elements that have position 'absolute' are **automatically treated as display 'block'**.

## Sticky

Positions based on the user's scroll position; toggles between 'relative' and 'fixed'. It is positioned relative until a given offset position is met in the viewport. When it crosses the threshold, the element sticks in place (becomes fixed), until it reaches the boundary of its parent element.

### Requirements

1. Specify an edge (top/left/bottom/right) for the element to stick to.
2. Do not use overflow (auto/scroll/hidden) on parent element.
3. Sticky only works when sticky container (parent element) has more than one child element. Sticky element can only float over sibling elements.

## Example

```html
<div class="”parent”">
  <div class="”box”" id="”one”">One</div>
  <div class="”box”" id="”two”">Two</div>
  <div class="”box”" id="”three”">Three</div>
  <div class="”box”" id="”four”">Four</div>
</div>
```

```css
.parent {
  border: 2px black dotted;
  display: inline-block;
}

.box {
  display: inline-block;
  background: red;
  width: 100px;
  height: 100px;
}

#relative {
  top: 20px;
  left: 20px;
  background: green;
  position: relative;
}
```
