## Testing

Unittests are written in Jasmine framework with Karma as test runner.

```
describe(string, function)    Function takes a title and function containing one or more specs
it(string, function)          Function takes title and function containing one or more expectations
expect(actual)                Takes a value and returns a boolean
Matcher functions             toBeTruthy(), toEqual(), toMatch(), toBe(), toContain(); chained alongside with an expect()

TestBed                       Used to configure and initialize the environment unit tests
beforeEach                    Global function in Jasmine that runs some setup code before each spec
TestBed.createComponent()     Creates an instance of component; uses expect() and matcher()
detectChanges()               Binds the data to component instance
ComponentFixture              Provides methods and proeprties that help test component's functionality

jasmine.createSpy('service')                        Used when there is no function to spy on
jasmine.createSpyObj('service', ['method'])         Used to create a mock that will spy on one ore more methods
```

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

## Example

```js
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { TitleComponent } from './title.component';
import { UserService } from './users.service';

describe('TitleComponent', () => {
  let component: TitleComponent;
  let fixture: ComponentFixture<TitleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [TitleComponent]    // mocks: []UserService] converts to Jasmine spy automatically
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TitleComponent);
    component = fixture.componentInstance;    // creates an instance of class TitleComponent
    fixture.detectChanges();          // simulate running on browser environment
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

// testing @Input
it('should correctly render the passed @input value', () => {
  component.message = 'New title';
  fixture.detectchanges();
  const compiled = fixture.debugElement.nativeElement;      // creates access to child element
  expect(compiled.querySelector('p').textContent).toBe('New title')';
});

// testing @Output
it('test @output', () => {
  spyOn(component.changeTitleEvent, 'emit');
  const button = fixture.nativeElement.querySelector('button');
  fixture.nativeElement.querySelector('input').value = 'Another new title';
  const inputText = fixture.nativeElement.querySelector('input').value;

  button.click();
  fixture.detectChanges();

  expect(component.changeTitleEvent.emit().toHaveBeenCalledWith(inputText);
});
```

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
