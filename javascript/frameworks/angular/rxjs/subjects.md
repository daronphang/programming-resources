## Subjects

An RxJS Subject is a special type of Observable (implements Observer interface and inherits operators and methods) that allows values to be multicasted to many Observers. An important distinction between Subject and Observable is that an Observable is unicast while **Subject is multicast** i.e. Subject can cast values to multiple subscribers, while each subscribed Observer owns an independent execution of the Observable. Also have ReplaySubject for replaying last emitted event, and BehaviorSubject for setting initial value.

Every Subject is an Observable. Given a Subject, you can subscribe to it, providing an Observer, which will start recieving values normally.

Every Subject is also an Observer. It is an object with the methods next(), error() and complete(). To feed a new value to the Subject, just call next(theValue), and it will be multicasted to the Observers registered to listen to the Subject.

**Subjects will only emit to current subscribers and won't hold the value.** To consider using ReplaySubject or BehaviorSubject instead.

```
Subject
BehaviorSubject     Stores the latest/current value emitted to its consumers
ReplaySubject       Similar to BehaviorSubject, can send old values to new subscribers
AsyncSubject        Only the last value of Observable execution is sent to Observers
```

```js
const subject = new Subject();
subject.next('This is an observable');
subject.subscribe(value => console.log(value));   // 'This is an observable'
subject.next('This is another observable');

const behSubject = new BehaviorSubject('set initial value');
behSubject.subcribe(value => console.log('value');
```

Recommended way rather than using emit(). Used for active events rather than passive like HTTPrequests.

```js
// services:
import { Subject } from 'rxjs';

someEmitter = new Subject<boolean>();

// component.ts to listen:
this.services.someEmitter.subscribe()   // or next()
```

## Comparing Subjects

BehaviourSubject will return the initial value or the current value on Subscription; when it is subscribed it emits the value immediately. A Subject doesn't hold a value, and each subscriber will only receive the upcoming values.

```js
const subject = new Rx.Subject();
subject.next(1);
subject.subscribe((x) => console.log(x));
subject.next(2);
subject.next(3);
// empty console
// 2
// 3
```

```js
const subject = new Rx.BehaviorSubject(0);
subject.next(1);
subject.subscribe((x) => console.log(x));
// console outputs 1
```

## Subjects vs Variables

When sharing data between components using Services, preferred is to use Observables:

- Variable requires polling and has slower performance
- Angular change detection directly supports Observables

## Subjects vs Observables

- Observable and its Subscriber have one-to-one relationship (unicast)
- Subject allows values to be multicasted to many Observers (one-to-many relationship)
