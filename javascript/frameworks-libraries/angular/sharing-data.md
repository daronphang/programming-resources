## Data Binding

```
{{ data }}                     String Interpolation
[html element]="property"      Property Binding
(event)="expression"           Event Binding (HTML to TypeScript, react to user events
[ngValue]="some value"         Binds input value to ngModel of the parent element
```

```html
<!--$event is a reserved variable name used in HTML when performing event binding, outputs the data emitted from the event-->
<div (input)="onUpdateServerName($event)"></div>

<button [disabled]="buttonDisabled"></button> <img [src]="itemImageUrl" />
```

### Parent-to-Child

Data shared from parent to child using @Input(). For detecting changes, use ngOnChanges() or setter function in child component.

```js
// child.component.ts
export class ChildComponent {
  @Input('target.name.alias') item: string = '';
}
```

```html
<!--parent.component.html-->
<!--currentItem is property from parent-->
<app-child [target.name.alias]="currentItem"></app-child>
```

### Child-to-Parent

Data shared from child to parent using @Output().

```js
// child.component.ts
export class ChildComponent {
  @Output() : newItemEvent = new EventEmitter<string>();   // output is string type

  addNewItem(value: string) {
    this.newItemEvent.emit(value);
  }
}
```

```html
<!--child.component.html-->
<label for="item-input">Add an item:</label>
<input type="text" id="item-input" #newItem />
<button (click)="addNewItem(newItem.value)">Add to parent's list</button>
```

```javascript
// parent.component.ts
export class AppComponent {
  items = ['item1', 'item2', 'item3', 'item4'];

  addItem(newItem: string) {
    this.items.push(newItem);
  }
}
```

```html
<!--parent.html-->
<app-child (newItemEvent)="addItem($event)"></app-child>
```

## Services

Service is a broad category encompassing any value, function or feature that an application needs. Angular distinguishes components from services to increase modularity and reusability. By separating a component's view-related features from other kinds of processing, you can make your component lean and efficient.

Main objective is to organize and share business logic, models, data and functions between different components that may/may not be related. Shouldn't instantiate services on your own but instead use Dependency Injector i.e. inject an instance of class service into component in constructor method.

### Lifecycle

Gets instantiated once during lifetime of app and should be treated as a Singleton i.e. a class containing methods that maintain data throughout the application's lifecycle. Data does not get refreshed and is available all the time. Useful for cross-component communication.

### Creating an injectable service

When specifying variables in the constructor, you can choose between private, public or protected. Use private if you don't need to use them outside of the current class/component. Protected members are accessible from inside the class and **extending classes** as well.

```js
// accounts.service.ts
statusUpdated = new EventEmitter<string>();

// account.component.ts to emit
someFunction() {
  this.accountService.statusUpdated.emit(status);
}

// anotherComponent.ts to listen
someFunction() {
  this.accountService.statusUpdated.subscribe(place some function);
}

constructor(private loggingService: LoggingService) {   // private or public. Need perform this for both service and component.ts
}
```

### Updating a variable from a service

There are times whereby you need to get a value from a service level as soon as your application starts up. This would mean that your service would have to initialize, followed by calling the method that populates your service variable, all before your application finishes with the start-up process. However, your variable would be undefined as the component will read the value from the service before it has the chance to initialize itself and update the variable.

The solution is to **cast the variable as a Behavior Subject**. Instead, the component subscribes to the service level variable (an Observable).

### Services injected into other services

If service A depends on service B, inject service B into service A's constructor method.

```js
// service A.service.ts
constructor(private serviceB: ServiceB) {}

someFunction() {
  this.serviceB.log('');
}
```
