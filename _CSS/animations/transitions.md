## Transitions

Work best for simple from-to movements, while CSS animations are for more complex series of movements. Properties are defined in CSS classes.

```
transition    <property> <duration> <timing-function> <delay>

// to control the individual components of the transition
transition-delay
transition-duration
transition-property
transition-timing-function    ease, linear, ease-in, ease-out, ease-in-out, cubic-bezier(n,n,n,n)
```

```css
div {
  width: 100px;
  height: 100px;
  background: red;
  transition: width 2s, height 4s;
}

div:hover {
  width: 300px;
  height: 500px;
}
```

### With Transform

Transform property allows you to rotate, skew, scale or translate an element.

```
matrix
translate
scale
rotate
skew
scale
```

```css
transform-origin: 0% 50%; /*Default is set at center*/
transform-origin: -100% 50%; /*X-offset, Y-offset*/

transform: matrix(1, 2, 3, 4, 5, 6);
transform: matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);
transform: perspective(17px);
transform: rotate(0.5turn);
transform: rotate3d(1, 2, 3, 10deg);
transform: rotateX(10deg);
transform: rotateY(10deg);
transform: rotateZ(10deg);
transform: translate(12px, 50%);
transform: translate3d(12px, 50%, 3em);
transform: translateX(2em);
transform: translateY(3in);
transform: translateZ(2px);
transform: scale(2, 0.5);
transform: scale3d(2.5, 1.2, 0.3);
transform: scaleX(2);
transform: scaleY(0.5);
transform: scaleZ(0.3);
transform: skew(30deg, 20deg);
transform: skewX(30deg);
transform: skewY(1.07rad);

/* Multiple function values */
transform: translateX(10px) rotate(10deg) translateY(5px);
transform: perspective(500px) translate(10px, 0, 20px) rotateY(3deg);
```

```html
<p>Click anywhere to move the ball</p>
<div id="foo" class="ball"></div>
```

```js
const f = document.getElementById('foo');
document.addEventListener(
  'click',
  (ev) => {
    f.style.transform = `translateY(${ev.clientY - 25}px)`;
    f.style.transform += `translateX(${ev.clientX - 25}px)`;
  },
  false
);
```

```css
.ball {
  border-radius: 25px;
  width: 50px;
  height: 50px;
  background: #c00;
  position: absolute;
  top: 0;
  left: 0;
  transition: transform 1s;
}
```
