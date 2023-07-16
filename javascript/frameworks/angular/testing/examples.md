## Testing Throw Error

Wrap the method in another function.

```js
expect(() => {
  someFunction();
}).toThrowError('hello world');
```

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
