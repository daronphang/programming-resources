## Components with Dependencies

Components often have service dependencies. A component-under-test does not have to be injected with real services. It is usually better if they are test doubles such as stubs, fakes, spies or mocks. The purpose of the spec is to test the component, not the service, and real services can be trouble.

### Fakes

```js
class FakeService {
  someMethod() {
    return 'some stub';
  }
}

beforeEach(() => {
  TestBed.configureTestingModule({
    // provide the component-under-test and dependent service
    providers: [SomeComponent, { provide: RealService, useClass: FakeService }],
  });
  // inject both the component and the dependent service.
  comp = TestBed.inject(SomeComponent);
  service = TestBed.inject(RealService);
});

it('some test', () => {
  const spy = spyOn(service, 'someMethod');
  fixture.detectChanges();
});
```

If you want to use the real class but mock a method, can use Partial.

```js
class FakeService implements Partial<RealService> {
  someMethod() {
    return 'some stub';
  }
}
```

### Spies

jasmine.createSpy can be used when there is no function to spy on. It will track calls and arguments like a spyOn but there is no implementation.

jasmine.createSpyObj is used to create a mock that will spy on one or more methods. It returns an object that has a property for each string that is a spy.

```js
beforeEach(() => {
  testQuote = 'Test Quote';

  // Create a fake TwainService object with a `getQuote()` spy
  const twainService = jasmine.createSpyObj('TwainService', ['getQuote']);
  // Make the spy return a synchronous Observable with the test data
  getQuoteSpy = twainService.getQuote.and.returnValue(of(testQuote));

  TestBed.configureTestingModule({
    declarations: [TwainComponent],
    providers: [{ provide: TwainService, useValue: twainService }],
  });

  fixture = TestBed.createComponent(TwainComponent);
  component = fixture.componentInstance;
  quoteEl = fixture.nativeElement.querySelector('.twain');
});

it('should show quote after component initialized', () => {
  fixture.detectChanges(); // onInit()

  // sync spy result shows testQuote immediately after init
  expect(quoteEl.textContent).toBe(testQuote);
  expect(getQuoteSpy.calls.any()).withContext('getQuote called').toBe(true);
});
```

## Nested Components

Use technique Shallow Component Testing. Can either use one approach or combine them.

```js
@Component({ selector: 'app-banner', template: '' })
class BannerStubComponent {}

TestBed.configureTestingModule({
  declarations: [AppComponent, BannerStubComponent, RouterLinkDirectiveStub],
  schemas: [NO_ERRORS_SCHEMA],
});
```
