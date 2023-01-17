## Use Cases

- Lazy loading of images.
- Infinite scrolls.
- Trigger scroll-based animations.
- Prefetch of links when they appear on the screen.
- Detect whether an ad was viewed or not.
- Determine whether a user has read an article and to what extent.
- Run costly renderings and animations only when they are visible on the screen.

## Intersection Observer

An asynchronous API that triggers a callback function whenever an element you wish to monitor enters or exits another element (or the viewport), or when the amount by which the two intserect changes by a requested amount. However, it cannot tell you the exact number of pixels that overlap.

```js
// entries output the info related to each element that changes its
// intersection status
const callback = (entries) => {
  entries.forEach((entry) => {
    // loop through all elements that have their intersection status change
    // i.e. element has either entered or left the screen
    const intersecting = entry.isIntersecting;
    entry.target.style.backgroundColor = intersecting ? 'blue' : 'orange';

    // disconnect to avoid memory leaks
    observer.unobserve(entry.target);
  });
};
const target = document.getElementById('test');

var observer = new IntersectionObserver(callback, options);
observer.observe(target);
```

### Properties

```js
let callback = (entries, observer) => {
  entries.forEach((entry) => {
    // Each entry describes an intersection change for one observed
    // target element:
    //   entry.boundingClientRect
    //   entry.intersectionRatio
    //   entry.intersectionRect
    //   entry.isIntersecting
    //   entry.rootBounds
    //   entry.target
    //   entry.time
  });
};
```

### Unobserve/Disconnect

Important to stop observing elements when they no longer need to be observed to avoid memory leaks. Can use either the unobserve method or disconnect method.

```
unobserve       Takes a single element as parameter
disconnect      Takes no parameters and stops observing all elements
```

## Options

```
root            Outer element within which you want to observe for an intersection
target          Element you are watching
threshold       % of element that must be visible before isIntersecting is true
rootMargin      Margin applied to the root before the threshold is calculated
```

### Root

Property that must be an ancestor element of the target element and is used as the viewport for intersection. If root element is specified as null i.e. root: document.querySelector(‘null’), the current viewport of the user will be the root element.

### Threshold

Rather than reporting every infinitesimal change in how much a target element is visible, the API uses thresholds and reports changes to visibility which cross these thresholds.

Can pass an array to threshold which means that the intersection observer will fire each time your target element passes one of the thresholds passed to it.

```js
const options = { threshold: [0, 0.25, 0.5, 0.75, 1] };
const observer = new IntersectionObserver((entries) => {
  entires.forEach((entry) => {
    entry.target.innerText = `${Math.round(entry.intersectionRatio * 100)}%`;
  });
}, options);

observer.observe(document.getElementById('test'));
```

### Root Margin

Property defines exactly the same as margin CSS property. Positive/negative is to grow/shrink the viewport respectively. Positive values are useful to lazy load images or infinite scrolling, to load the data before it becomes visible to the user.

## How Intersections Occur

1. Target element's bounding rectangle (smallest that fully encloses the bounding boxes of every component that makes up the element) is obtained by calling getBoundingClientRect() on the target.
2. Starting at the target's immediate parent block and moving outward, each containing block's clipping is applied to the intersection rectangle.
3. When recursion upward reaches the intersection root, the resulting rectangle is mapped to the intersection root's coordinate space.
4. The resulting rectangle is then updated by intersecting it with the root intersection rectangle and mapped to the coordinate space of the target's document.
