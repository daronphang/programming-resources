## Inbuilt Attribute Directives

A class with @Directive decorator. Helps to change appearance of DOM element/component conditionally. Can assign an object literal inline or by binding to a property.

```
[ngStyle]       Add/remove CSS styles
[ngClass]       Add/remove CSS classes. Can either pass an expression as a string/array/object
[(ngModel)]     Adds two-way binding to HTML form element
```

```
[ngStyle]="{'color': Red,'font-weight': 'Bold','font-size':'35px','borderBottom': borderStyle}"
[ngStyle]="{'font-size.px':24}"
[ngStyle]="{'background-color':person.country === 'UK' ? 'green' : 'red' }
[ngStyle]="appStyleGreen"

[ngStyle]="{'color': changeColor(condition)}"

[ngClass]="['btn', 'btn-primary']"
[ngClass]="{ btn:true, 'btn-primary':true }"
```

```html
<div [ngClass]="isSpecial ? 'specialClass' : ''">This div is special</div>
<input [(ngModel)]="currentItem.name" id="example-ngModel" />
```

```js
changeColor(condition: string) {
  if (condition == 'hello') {
    return 'red';
  } return 'blue';
}
```

### NgModel

Directive binds the value of HTML controls (input, select, text area) to application data i.e. bind input field value to variable. Can include (ngModelChange). Difference between (ngModelChange) and (change):

- (change) is DOM event which fires when user has blurred input
- (ngModelChange) listens to input event and fire before the value bound to NgModel has changed

```js
@Component({
  selector: 'my-app',
  template: `
    <div>
      <input [value]="foo" (change)="changeFn($event)" />
      <p></p>
      <input [ngModel]="bar" (ngModelChange)="modelChangeFn($event)" />
      <p></p>
    </div>
  `,
})
export class AppComponent {
  foo = 'Hello';
  bar = 'World';
  changeFn(e) {
    this.foo = e.target.value;
  }
  modelChangeFn(value) {
    this.bar = value;
  }
}
```

## Building Attribute Directives

Can use either ElementRef, Renderer2 or HostBinding to access and modify DOM elements. Best practice is to use Renderer2 and HostListener. The initial @Input must match with selector name. Make sure the directive is imported and exported in shared module.

```html
<!--component.html-->
<!--defaultColor is static so don't use square brackets-->
<p [appHighlight]="color" defaultColor="violet">Highlight me!</p>
```

```js
// app.component:
export class AppComponent {
  color = 'yellow';
}
```

```js
// highlight.directive.ts
import { Directive, Renderer2, ElementRef, OnInit, HostListener, HostBinding, Input } from '@angular/core';

@directive({
  selector: '[appHighlight]'   // specify directive's CSS attribute selector
})

export class HighlightDirective implements OnInit {
  constructor(private elRef: ElementRef, private renderer: Renderer2) {}

  // passing values into attribute directive
  @Input() appHighlight = '';
  @Input() defaultColor: string = '';    // binding to second property

  @HostBinding('style.backgroundColor') backgroundColor: string;  // shortcut for renderer

  // handling user events
  @HostListener('mouseenter') onMouseEnter(eventData: Event) {
    this.highlight(this.appHighlight || this.defaultColor || 'yellow');
   }

 private highlight(color: string) {
   this.renderer.setStyle(this.elRef.nativeElement, 'background-color', color, false, false);
   // same as this.elementRef.nativeElement.style.backgroundColor = color;  Not good way of acccessing element directly
 }

  ngOnInit() {this.backgroundColor = this.defaultColor}
}

```
