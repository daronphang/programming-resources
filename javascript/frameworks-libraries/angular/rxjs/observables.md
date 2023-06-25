## Observables

A function that creates an observer and attaches it to the source where values are expected i.e. clicks, mouse events. Observables are lazy Push collections of multiple values; need to subscribe in order to see data.

An Observable allows you to handle different asynchronous events, from single finite operation (HTTP request) to multiple repeatable actions (keystrokes, cursor movements). Can use of() method as mock API which returns an Observable and emits values in a sequence upon subscription. For infinite subscriptions, need call OnDestroy() to manually unsubscribe. Examples include forms, router, and intervals. For finite subscriptions like HTTP calls or take(1), no need to unsubscribe.

```js
const observable = new Observable((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);
  setTimeout(() => {
    subscriber.next(4);
    subscriber.complete();
  }, 1000);
});
```

### Advantages Over Promises

- An Observable pushes a stream of values whereas Promise pushes one resolved value.
- Observables are declarative whereby computation does not start until subscription whereas promises are executed immediately on creation.
- Error handlers can be done inside Observables rather than a construct like Promises.
- Data can be transformed using operators through pipe().

## Observer

A consumer of values delivered by an Observable. They are simply objects with three callbacks, one for each type of notification delivered by the Observable: next, error, and complete.

To use an Observer, need to provide it to the subscribe of an Observable. Can also provide the callback as an argument without attaching an Observer object.

```js
const observer = {
  next: (x) => console.log('Observer got a next value: ' + x),
  error: (err) => console.error('Observer got an error: ' + err),
  complete: () => console.log('Observer got a complete notification'),
};

observable.subscribe(observer);

// without attaching an Observer object
// providing 'next' callback
observable.subscribe((x) => console.log('hello world'));
```

## Subscription

An object that represents a disposable resource, usually the execution of an Observable. Has one important method, unsubscribe, that takes no argument and disposes the resource held by the subscription.

```js
const observable = interval(1000);
const subscription = observable.subscribe((x) => console.log(x));
subscription.unsubscribe();
```

### Subscribe

Subscribe() can take 3 arguments as follows:

1. onNext: Function to invoke for each element in observable sequence.
2. onError: Function to invoke upon exceptional termination.
3. onCompleted: Function to invoke upon graceful termination.

### Unsubscribe

When navigating somewhere else, Angular will destroy the component; need to unsubscribe to prevent memory leak. Use pipe operators to auto-unsubscribe such as first() and take(). For unsubscribing best practices:

- Store all subscriptions in an array and using .forEach() in ngOnDestroy().
- Using .takeUntil()

### Emitting Empty Observables

```js
import { NEVER, EMPTY, of } from 'rxjs';

someObs$.pipe(
  tap(() => {
    NEVER; // emits no events and never ends
    EMPTY; // emits only complete;
    of(); // emits both next and complete
  })
);
```

### Subscribing to Multiple Observables

```
combineLatest()      Emits initial value only when all Observables emit at least one value
forkJoin()           Emits the last emitted value from each observable when **all completes**
```
