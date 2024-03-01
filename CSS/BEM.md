## BEM

The BEM approach ensures that everyone who participates in the development of a website works with a single codebase and speaks the same language. Using proper naming will prepare you for the changes in design of the website.

### Block

Blocks are the main building blocks of BEM. They represent a standalone entity that carries all the relevant HTML and CSS within it.

```
container
nav-bar
btn
modal
accordion
header
```

### Element

Elements are the children of blocks and are used to create more specific styling. A double underscore is used to separate the block from the element.

```
navigation__menu
navigation__link
navigation__dropdown
```

### Modifier

Modifiers are a powerful feature of BEM that allows you to create variations of blocks and elements without having to create new class names. Modifiers are used to change the appearance of an element or block based on certain conditions, such as state, theme, or size.

```
orange
activated
small
```

### Examples

```css
.opinions-box {
  margin: 0 0 8px 0;
  text-align: center;

  &__view-more {
    text-decoration: underline;
  }

  &__text-input {
    border: 1px solid #ccc;
  }

  &--is-inactive {
    color: gray;
  }
}
```

```html
<div class="product-card__like-button--liked"></div>
```
