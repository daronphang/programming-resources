## Sizing

When building accessible websites, need to consider inclusion. Hence, should use em or rem over px as they scale with the user's setting.

### Absolute Length

```
cm
mm
in
px
```

### Relative Length

```
em      Element, responsive unit interpreted into equivalent px unit by the browser
rem     Relative to font-size of browser base font size and does not inherit from parent element
vw      Relative to 1% of width of viewport; scales with sizing
vh      Relative to 1% of height of viewport
vmax    Takes the max between vw and vh
vmin    Takes the min between vw and vh
%       Relative to parent element
```

## rem vs px

Key argument for using rem is accessibility to respect end users changing font sizes on their browsers. By default, 1rem is equivalent to 16px.

Though users are able to change font-size using zoom and px would automatically be scaled, rem allows users to change zoom-level of whole document at once i.e. borders, padding, margins will scale fluidly. Moreover, using px will overwrite user's preferences.

When adjusting the root font-size, never use px but % to define as you would completely remove user's ability to change font-size on their end.

```css
:root {
  font-size: 100px; /* dont do this */
}

:root {
  font-size: 62.5%; /* 10/16 = 62.5%, equals to 10px */
  /* any conversion of px to rem is by bumping a decimal place */
}

body {
  font-size: 1.6rem; /* to make default font-size */
}
```

### Media Queries

Using rem with media queries will run into issues. Use em instead.

## em vs rem

With em unit, the computed pixel is derived from the font size of the styled element while putting the inherited (parent and grandparent) values into consideration i.e. cascades down. This is irrespective of the font size assigned to the html element (computes to 42px instead of 54px).

When using rem, the px equivalence depends on the font size of the html element.

```css
html {
  font-size: 18px;
}

section {
  font-size: 14px;
  padding: 3em;
}
```

### Inheritance

```html
<section class="page-wrapper">
  Grandparent
  <div class="container">
    Parent
    <div class="container">Child</div>
  </div>
</section>
```

```css
html {
  font-size: 16px;
}

/* inherits from parent (html) element */
.page-wrapper {
  font-size: 1.5em; /* 1.5*16 = 24px */
}

.container {
  padding: 2em; /* 2*24 = 48px */
}
```
