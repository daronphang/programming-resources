## Signals

Signals provide a new way for our code to tell our templates (and other code) that our data has changed. This improves Angular's change detection, which also improves performance, and makes our code **more reactive**. Signals enable very **fine-grained** updates to the DOM.

Signals have an easy-to-understand API for reporting data changes to the framework, allowing the framework to optimize change detection and re-rendering in a way that so far was just not possible.

With Signals, **Angular will be able to determine exactly what parts of the page need to be updated and update only those and nothing more**.

Previously with change detection, Angular has to check **all** components on the page, even if the data that they consume didn't change.

Signals are not a direct replacement for RxJs, but they provide an easier-to-use alternative in certain situations when propagating data changes to multiple parts of the application e.g. BehaviorSubject.

Characteristics of signals:

- Variable plus change notification
- Reactive
- Always holds a value
- Synchronous

The main advantage is that we can get notified when the signal value changes, and then do something in response to the new signal value.

https://blog.angular-university.io/angular-signals/

```js
@Component(
    selector: "app",
    template: `
<h1>Current value of the counter {{counter()}}</h1>
<button (click)="increment()">Increment</button>
`)
export class AppComponent {
  counter = signal(0);

  constructor() {
    console.log(`counter value: ${this.counter()}`)
  }

  increment() {
    console.log(`Updating counter...`)
    this.counter.set(this.counter() + 1);
  }
}
```

### Methods

```js
const counter = signal(0);
const counterRead = counter.asReadOnly();

console.log(counter());
counter.set(5);
counter.update((v) => v + 5);
```

### Computed

Signals can be created and derived from other signals. When a signal updates, all its dependent signals will then get updated automatically.

However, we need to be careful with introducing conditional logic inside the computed function. Angular will only consider that one signal has a dependency on another if Angular notices that the signal requires it for calculation on initial construction.

```js
const counter = signal(0);
const derivedCounter = computed(() => {
  return counter() * 10;
});
```

```js
// Considered as two independent signals by Angular.
const counter = signal(0);
const multiplier = 0;
const derivedCounter = computed(() => {
  if (this.multiplier < 10) {
    return 0;
  } else {
    return counter() * this.multiplier;
  }
});
```

### Objects

There is currently no protective mechanism in the Signals API for preventing this misuse, like preventively freezing the array or the object value. Hence, need to ensure mutation of signal values are performed through Signals API e.g. set(), update().

```js
const counter = signal(["hello"]);
counter().push("world"); // works

const counterRead = counter.asReadonly();
counterRead().push("what!"); // works
```

### Effect

We can detect signal changes with effect(). It will run at least once when the effect is declared. Also, effect() can only be used in the constructor.

As effect() can create references to other variables in the application, via a closure, need to watch out for accidental memory leaks. Nonetheless, Angular will automatically clean up the function.

```js
//The effect will be re-run whenever any
// of the signals that it uses changes value.
effect(() => {
  // We just have to use the source signals
  // somewhere inside this effect
  const currentCount = this.counter();
  const derivedCounter = this.derivedCounter();
  console.log(`current values: ${currentCount} 
    ${derivedCounter}`);
});
```
