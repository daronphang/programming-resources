## Animations

Consists of two components, a style describing the CSS animation and a set of keyframes that indicate the start and end states. When specifying CSS styles inside @keyframes, animation will gradually change from current style to new style at certain times.

However, **there are certain properties that cannot be animated** i.e. display.

### Animation Properties

```
animation-name                 Name of keyframes
animation-duration             Duration for animation to complete one cycle
animation-timing-function      Establishes preset acceleration curves such as ease-in-out, linear, cubic-bezier
animation-delay                Delay between element loaded and start of animation sequence
animation-iteration-count      Number of times animation should repeat, can specify infinite
animation-direction            Sets the direction after cycle; default resets on each cycle; normal, alternate
animation-fill-mode            Sets styles to its target before/after its execution; none, forwards, backwards, both
animation-play-state           Pause/play animation; paused, running
```

### Animation Sequence (Keyframes)

Keyframes define the appearance of the animation. Each keyframe describes how the animated element should render at a given time during the animation sequence. Have special aliases: 'from' and 'to'.

```css
p {
  animation-duration: 3s;
  animation-name: slidein;
}

@keyframes slidein {
  from {
    margin-left: 100%;
    width: 300%;
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}
```

```css
p {
  animation-duration: 3s;
  animation-name: slidein;
}

@keyframes slidein {
  from {
    margin-left: 100%;
    width: 300%;
  }

  75% {
    font-size: 300%;
    margin-left: 25%;
    width: 150%;
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}
```

## Animation Timing

### Steps

Displays an animation iteration along n stops along the transition, with each stop having an equal length of time. Allows us to break an animation or transition into segments, rather than one continuous transition from one state to another i.e. second hand of clock.

Direction of start denotes a left-continuous function and the animation's first step will be completed as soon the animation begins i.e. jumps immediately to the end of the first step and stays until the end of the step duration.

Direction of end denotes a right-continuous function and stays put until the duration of the first step is completed.

```css
/* steps(n, <jumpterm or direction>) */
/* defaults to end */
animation-timing-function: steps(4, jump-start);
animation-timing-function: steps(10, jump-end);
animation-timing-function: steps(20, jump-none);
animation-timing-function: steps(5, jump-both);
animation-timing-function: steps(6, start);
animation-timing-function: steps(8, end);
```

```css
.second {
  animation: tick-tock 60s steps(60, end) infinite;
}

@keyframes tick-tock {
  to {
    transform: rotate(360deg);
  }
}
```

## Examples

### Hover with underline animation

```css
/*need to use pseudo element to avoid applying animation to text*/
.activeRouterClass::after {
  border-bottom: 2px solid white;
  display: block;
  content: '';
  animation-name: activeRouter;
  animation-duration: 0.5s;
}

@keyframes activeRouter {
  0% {
    transform: scaleX(0);
    border-bottom: 0px;
  }
  100% {
    transform: scaleX(1);
    border-bottom: 2px solid white;
  }
}
```

### Retrigger Animation

Need to clear and re-enter animation name via DOM manipulation.

```js
useEffect(() => {
  const handleAnimation = () => {
    const element = document.getElementById(id);
    element.style.animationName = '';
  };
  document.addEventListener('animationend', handleAnimation);

  return () => {
    document.removeEventListener('animationend', handleAnimation);
  };
}, []);

const onClick = (e) => {
  const element = document.getElementById('contactMeButton');
  if (element) {
    element.style.animationName = 'buttonOnError';
  }
};
```
