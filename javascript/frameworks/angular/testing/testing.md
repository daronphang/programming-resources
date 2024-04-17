## Testing

Unittests are written in Jasmine framework with Karma as test runner.

### Configuration

If you want to customize Karma, you can create a karma.conf.js file.

### Other test frameworks

You can also unit test an Angular application with other testing libraries and test runners. Each library and runner has its own distinctive installation procedures, configuration, and syntax.

### Running specific files

Changing karma.conf.js does not do anything, nor does changing tsconfig.spec.json which just tells the compiler what files to compile. Tests are loaded via src/test.js file.

You can change the regex to exclude some tests, but it may be hard on complicated setups. Alternatively, you can import the tests you want:

```js
// const context = require.context('./', true, /\.spec\.ts/);
import "./app/some/folder";
```

### Guidelines

- Used for testing behaviors such as if/for loops, executing functions etc.
- Should be tested in isolation without any dependencies
- When subscribing to Observables, to provide both success and failure callbacks
- When testing components with services dependencies, always use mock services
- When accessing DOM, always use debugElement and not nativeElement
- Always use fixture.detectChanges() when making a change
- Don't overuse NO_ERRORS_SCHEMA

## Methods

### TestBed

Used to configure and initialize the environment unit tests.

### detectChanges()

Binds the data to the component's instance.

### jasmine.spyOn()

A spy can stub any function and track calls to it and all arguments. With spyOn(), you should have a method on the object. The advantage of using this is that you can call the original method.

### jasmine.createSpy()

Used when there is no function to spy on. It will track calls and arguments like spyOn() but there is no implementation. Unlike spyOn(), the method to be spied upon need not exist at all.

### jasmine.createSpyObj()

Used to create a mock that will spy on one or more methods. It returns an object that has a property for each string that is a spy.

### NativeElement

If your tests run in a browser, it is safe to use NativeElement, as its value will always be an HTMLElement or one of its derived classes. Moreover, the properties of NativeElement depend upon the runtime environment e.g. browser, non-browser platform.

Knowing that it is an HTMLElement of some sort, use the standard HTML querySelector to dive deeper into the element tree.

### DebugElement

DebugElement is an Angular class that contains all kinds of references and methods relevant to investigate an element or component.

Angular relies on the DebugElement abstraction to **work safely across all supported platforms**. Instead of creating an HTML element tree, Angular creates a DebugElement tree that wraps the native elements for the runtime platform. The nativeElement property unwraps the DebugElement and returns the platform-specific element object.

NativeElement returns DOM tree (browser specific API) whereas DebugElement returns a JS object. If the application is running on non-browser platform, should use DebugElement.

### By

The DebugElement offers query methods that work for all supported platforms. These query methods take a predicate function that returns true when a node in the DebugElement tree matches the selection criteria.

```js
import { By } from "@angular/platform-browser";

it("should find the <p> with fixture.debugElement.query(By.css)", () => {
  const bannerDe: DebugElement = fixture.debugElement;
  const paragraphDe = bannerDe.query(By.css("p"));
  const p: HTMLElement = paragraphDe.nativeElement;
  expect(p.textContent).toEqual("banner works!");
});
```

## Change Detection

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

## Spying on functions from modules

Below is a workaround if you encounter 'not declared writable or has no setter' while using spyOn.

```js
// tsconfig.spec.json
{
  "compilerOptions": {
    "module": "commonjs",
  }
}
```

```js
import * as something from "./someModule";

it("should spy on function", () => {
  spyOn(something, "someFunction");
});
```
