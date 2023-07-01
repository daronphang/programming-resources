## Inbuilt Structural Directives

Responsible for HTML layout. Used for manipulating, modifying and removing elements inside a component template. \* character translate the attribute into a <ng-template> element.

```
*ngIf="property"                    Conditionally add/remove elements from DOM (it is not hidden)
*ngFor="let x of array"             Makes each item available to HTML for each iteration
[ngSwitch] & *ngSwitchCase/Default  Used when displaying an element tree containing many children
```

```html
<app-item-detail *ngFor="let item of items" [item]="item"></app-item-detail>
<div *ngFor="let item of items; let i=index">{{i + 1}} - {{item.name}}</div>

<ul *ngFor="let person of people" [ngSwitch]="person.country">
 <li *ngSwitchCase="'UK'"
     class="text-success">{{ person.name }} ({{ person.country }})
 </li>
 <li *ngSwitchCase="'USA'"
     class="text-primary">{{ person.name }} ({{ person.country }})
 </li>
 <li *ngSwitchDefault      // displayed when no match is found
     class="text-warning">{{ person.name }} ({{ person.country }})
 </li>
</ul>
```

```html
<!--ng-template doesn't render anything by default-->
<p *ngIf="serverCreated">Server was created</p>

<ng-template #noServer>
  <!--# is used to create a marker-->
  <p>No server was created</p>
</ng-template>

<!-- *ngIf is just syntactic sugar i.e. nicer syntax for something existing -->
<!-- both are the same -->
<p *ngIf="isVisible">This is visible</p>
<ng-template [ngIf]="isVisible"><p>This is visible</p></ng-template>
```

### ngFor Objects

```js
// defined in component
ObjectKeys = Object.keys;
```

```html
<div *ngFor="let key of ObjectKeys(submittedRequestsService.requestDetails$ | async)"></div>
```

## Building Custom Structural Directives

1. Use Directive decorator to define Custom Directive.
2. Provide a selector which represents this Directive.
3. Constructor receives TemplateRef and ViewContainerRef.

TemplateRef refers to the content enclosed within the container. ViewContainerRef refers to the container to which directive is applied. They are injected to get access to them.

```js
// unless.directive.ts:
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appUnless]'
})

export class UnlessDirective {
  constructor(private template: TemplateRef<any>, private container: ViewContainerRef) {}

  @Input() set appUnless(value: boolean) {    // bind value to property appUnless using setter method
  if (!condition) {
    this.container.createEmbeddedView(this.template);
  } else {
    this.container.clear();
  }
  }
}
```

```html
<!--parent.component.html-->
<div *appUnless="isVisible">
  <!--<div> referred by ViewContainerRef-->
  <h1>This is the template area</h1>
  <!--Content inside container (<h1>) referred by TemplateRef-->
</div>
```
