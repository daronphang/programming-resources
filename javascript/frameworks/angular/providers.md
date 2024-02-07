## Angular Providers

Angular providers allow us to register classes, functions, or values as dependencies using the DI system. The providers are registered using a **token**, which are used to locate the provider i.e. each provider is uniquely identified by a token in the ProvidersArray.

Angular creates an injector for each component/directive it creates. It also creates a root-level injector (app-level scope) and module level injector for lazy loaded modules. Each injector gets its own copy of the Providers.

The injector maintains an internal collection of token-provider in the ProvidersArray. The token acts as a key to that collection and the injector uses that token to locate the provider.

### Configuration

There are two ways to register providers.

```js
// using providers
const providers = [ProductService]; // shorthand
const providers = [{ provide: ProductService, useClass: ProductService }];

// using providedIn
@Injectable({
  providedIn: "root",
})
class ProductService {}
```

### Multiple providers with the same token

You can add as many dependencies to the ProvidersArray. However, the last provider to register wins. To prevent this, set multi property to true.

```js
const providers = [
  { provide: ProductService, useClass: ProductService },
  { provide: ProductService, useClass: FakeProductService }, // always injected
];

const providers = [
  { provide: ProductService, useClass: ProductService, multi: true },
  { provide: ProductService, useClass: FakeProductService, multi: true },
];
```

## Tokens

### Type Token

The type being injected is used as the token.

```js
const providers = [{ provide: ProductService, useClass: ProductService }];

class ProductComponent {
  constructor(private productService : ProductService) {}
}
```

### String Token

You can use a string literal to register the dependency.

```js
const providers = [{ provide: 'ENV', useValue: 'DEVELOPMENT' }];

class ProductComponent {
  constructor(@Inject('ENV') private env: string) {}
}
```

### Injection Token

The issue with using string tokens is that multiple developers can use the same string token, and you also do not have control over third-party modules using the same token. If the token is reused, the last to register overwrites all previously registered tokens.

Angular provides InjectionToken class to ensure unique tokens are created.

```js
const TOKEN = new InjectionToken() < string > "";
const providers = [{ provide: 'TOKEN', useValue: "hello world" }];

class ProductComponent {
  constructor(@Inject('TOKEN') private token: string) {}
}
```

## Providers

### useClass

You do not have to specify in providers for services using providedIn.

```js
const providers: [{ provide: ProductService, useClass: ProductService }];

// same as above
@Injectable({
  providedIn: 'root',
})
class ProductService {}
```

### useValue

Lets you inject a value, object or function. When injecting objects, use Object.freeze to prevent the values from being changed.

```js
const APP_CONFIG = Object.freeze({
  serviceURL: "www.serviceUrl.comapi",
});

const providers = [{ provide: "APP_CONFIG", useValue: APP_CONFIG }];
```

### useExisting

Creates two ways to access the same service object with two different tokens.

```js
class CarService {
  getWeight(): number {...}
  getColor(): string {...}
  getName(): string {...}
  getWidth(): number {...}
  getHeight(): number { … }
  getModel(): string {...}
  getYear(): number {...}
  ...
}

export abstract class CarSizeService {
  abstract getHeight: number;
  abstract getWidth: number;
}

const providers = [{ provide: CarSizeService, useExisting: CarService}];
```

### useFactory

Specifies the function that is called and injects its return value. Useful for performing init functions.

If using APP_INITIALIZER, the useFactory function needs to return a function that returns a promise or an observable.

```js
export function initApp(env: string, appService: AppService) {
  if (env === "PRODUCTION") appService.env = "hello";
  else appService.env = "world";
  return () => of(true);
}

const providers = [
  {provide: 'ENV', useValue: 'DEVELOPMENT'}.
  {
    provide: APP_INITIALIZER,
    useFactory: initApp,
    deps: ["ENV", AppService],
    // provider token provides an array of elements
    // no overrides are performed
    // however, all providers of the same token must set multi=true
    multi: true,
  },
];
```
