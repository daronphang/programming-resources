## Pure components as classes

For components with no dependencies, you can simply create the component and poke at its API.

```js
@Component({
  standalone: true,
  selector: "lightswitch-comp",
  template: ` <button type="button" (click)="clicked()">Click me!</button>
    <span>{{ message }}</span>`,
})
export class LightswitchComponent {
  isOn = false;
  clicked() {
    this.isOn = !this.isOn;
  }
  get message() {
    return `The light is ${this.isOn ? "On" : "Off"}`;
  }
}
```

```js
describe("LightswitchComp", () => {
  it("#clicked() should toggle #isOn", () => {
    const comp = new LightswitchComponent();
    expect(comp.isOn).withContext("off at first").toBe(false);
    comp.clicked();
    expect(comp.isOn).withContext("on after click").toBe(true);
    comp.clicked();
    expect(comp.isOn).withContext("off after second click").toBe(false);
  });

  it('#clicked() should set #message to "is on"', () => {
    const comp = new LightswitchComponent();
    expect(comp.message)
      .withContext("off at first")
      .toMatch(/is off/i);
    comp.clicked();
    expect(comp.message).withContext("on after clicked").toMatch(/is on/i);
  });
});
```

## Components with dependencies

When a component has dependencies, you should use TestBed to both create the component and its dependencies.
