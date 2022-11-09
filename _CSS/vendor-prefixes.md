## Vendor Prefixes

Browser vendors used to add prefixed to experimental or nonstandard CSS properties and JS APIs, so developers could experiment with new ideas to help prevent them from being relied upon in production.

To determine if a particular CSS property is supported in browser, refer to www.caniuse.com. Yellow ribbons indicate browser has support with prefix added.

```
-webkit-    Chrome, Safari, newer versions of Opera and Edge, iOS browsers
-moz-       Firefox
-o-         Old pre-webkit versions of Opera
-ms-        IE and Edge before Chromium
```

```css
nav {
  background-color: red;
  background-image: url(gradient-slice.png);
  background-image: -webkit-linear-gradient(top right, #a60000, #ffffff);
  background-image: -moz-linear-gradient(top right, #a60000, #ffffff);
  background-image: -ms-linear-gradient(top right, #a60000, #ffffff);
  background-image: -o-linear-gradient(top right, #a60000, #ffffff);
  background-image: linear-gradient(top right, #a60000, #ffffff);
}
```

### Should you use vendor prefixes?

It boils down to a matter of opinion, but official W3C policy states that you shouldn't use experimental properties in production code.

### CSS Preprocessors

CSS preprocessors like SASS or LESS can handle vendor prefixes by creating a mixin function that will add the prefixes you have defined automatically.

## Fallback

If a feature is not supported in a particular browser, it will result in your content breaking where it is not usable. To remedy this, can provide a fallback property later in the cascade.

```css
nav {
  width: 180px;
  width: 18rem; /* rem not supported in older browsers, will rely on px */
}
```
