## Reactive Programming

Reactive programming is a declarative programming paradigm that is structured around asynchronous event processing and data streams. The reactive manifesto states that reactive systems are:

- Responsive
- Resilient
- Elastic
- Message driven

### Programming with asynchronous data streams

Event buses or typical click events are an asynchronous event stream, on which you can observe and do some side effects. Reactive is that idea on steroids.

Streams are cheap and ubiquitous. You are able to create data streams of anything, including variables, user inputs, properties, caches, and not just from click or hover events i.e. Twitter feed. Events, messages, calls, and failures are conveyed by a data stream. You can listen to that stream and react accordingly.

You are also given a toolbox of functions to combine, create and filter any of those streams. A stream can be used as an input to another.

### Observables can be cold or hot

Cold observables are lazy. They don't do anything until someone starts observing them, and only start running when they are consumed. The data produced by cold stream is not shared among subscribers, and when you subscribe, you get all the items.

Hot streams are active before the subscription. The data is independent of an individual subscriber. When an observer subscribes to a hot observable, it will get all the values in the stream that are emitted **after it subscribes**.

### Contrast with Event Driven

In constrast with event-driven, reactive programming deals with **data**. You declare a reaction to a change. Hence, it might be considered as a pull or watch strategy.

## Streams

A stream is a sequence of ongoing events ordered in time. It can emit three different events: a value, an error, or completed signal.

The emitted events are captured asynchronously, by defining a function that will execute in any of those events.

The listeners of a stream are called subscribers. The functions we are defining are called observers. The stream is the subject/observable being observed.
