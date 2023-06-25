## Directives

Directives are classes that add additional behavior or styling to elements. Three types are Components, Structural and Attribute. They are markers on DOM element that tell Angular to attach a specified behavior to that element.

## Local References of HTML Elements

Can only be used in HTML and not in TypeScript. Can add into any HTML tag.

```html
<input #serverNameInput />
```

To use local reference in TypeScript, use ViewChild decorator.

```javascript
export class ExampleComponent implements OnInit {
  @ViewChild('serverNameInput', { static: true }) serverNameInput: ElementRef; // property

  // to access value:
  onAddServer() {
    serverName: this.serverNameInput.nativeElement.value;
  }
}
```
