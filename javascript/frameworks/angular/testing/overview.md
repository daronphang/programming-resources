## Testing

Unittests are written in Jasmine framework with Karma as test runner.

### Methods

#### TestBed

Used to configure and initialize the environment unit tests.

#### detectChanges()

Binds the data to the component's instance.

#### jasmine.spyOn()

A spy can stub any function and track calls to it and all arguments. With spyOn(), you should have a method on the object. The advantage of using this is that you can call the original method.

#### jasmine.createSpy()

Used when there is no function to spy on. It will track calls and arguments like spyOn() but there is no implementation. Unlike spyOn(), the method to be spied upon need not exist at all.

#### jasmine.createSpyObj()

Used to create a mock that will spy on one or more methods. It returns an object that has a property for each string that is a spy.

#### NativeElement, DebugElement

NativeElement returns a reference to the DOM element, while DebugElement is an Angular class that contains all kinds of references and methods relevant to investigate an element or component.

NativeElement returns DOM tree (browser specific API) whereas DebugElement returns a JS object. If the application is running on non-browser platform, should use DebugElement.

### Change Detection

When modifying variables of test component, calling fixture.detectChanges() might not work due to ChangeDetectionStrategy.onPush() setting. Two ways to bypass this:

1. Place fixture.detectChanges() inside each it() instead of inside beforeEach().
2. Override settings when compiling.

```js
  .overrideComponent( ChipsLevelsComponent, {
    set: { changeDetection: ChangeDetectionStrategy.Default }
  })
  .compileComponents();
```

For modifying properties of services, can create mock class and using array methods like push.

### Configuration

If you want to customize Karma, you can create a karma.conf.js file.

### Other test frameworks

You can also unit test an Angular application with other testing libraries and test runners. Each library and runner has its own distinctive installation procedures, configuration, and syntax.

### Running specific files

Changing karma.conf.js does not do anything, nor does changing tsconfig.spec.json which just tells the compiler what files to compile. Tests are loaded via src/test.js file.

You can change the regex to exclude some tests, but it may be hard on complicated setups. Alternatively, you can import the tests you want:

```js
// const context = require.context('./', true, /\.spec\.ts/);
import './app/some/folder';
```

## Best Practices

- Used for testing behaviors such as if/for loops, executing functions etc.
- Should be tested in isolation without any dependencies
- When subscribing to Observables, to provide both success and failure callbacks
- When testing components with services dependencies, always use mock services
- When accessing DOM, always use debugElement and not nativeElement
- Always use fixture.detectChanges() when making a change
- Don't overuse NO_ERRORS_SCHEMA
