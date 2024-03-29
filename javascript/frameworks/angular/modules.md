## Feature Modules

Modules are standalone i.e. do not interact with each other. Needed for performance improvement.

```js
// recipe.module.ts
import { NgModule } from '@angular/core';

@NgModule({
  declarations: [
    RecipesComponent,
    RecipeListcomponent
  ],
  exports: [
    RecipesComponent,
    RecipeListcomponent
  ],
  imports: [
  RouterModule.forChild([{path: 'recipes', component: RecipesComponent, canActivate: [AuthGuard}]),
  SharedModule,
  ReactiveFormsModule,
  CoreModule
  ]
})

export class RecipesModule

// app.module.ts
imports: [
  RecipesModule,
  SharedModule
]
```

### Adding Routes

Can either create a routing module for each feature or use forChild() in module component.

### Lazy Loading

Pre-requisite is feature module. Only loads the modules needed for the route. Not worth it for routes that are visited frequently.

```javascript
// app-routing module:

const appRoutes: Routes = [
  { path: 'recipes', loadChildren: './recipes/recipes.module#RecipesModule' }, // entire module is parsed on demand
  // () => import('./recipes/recipes.module').then(m => m.RecipesModule)
];

// recipes-routing,module.ts
const routes: Routes = [
  {
    path: '',
    component: RecipesComponent,
    canActivate: [AuthGuard],
    children: [],
  },
  // importnat to declare path as ''
];

// remember to remove RecipesModule in import from app.module.ts
```

### Preloading

A fast initial load and fast subsequent loads thereafter. When loading services in lazy-loaded modules, will get a separate instance (Angular creates a child instance).

```javascript
// app-routing.module.ts:
imports: [RouterModule.forRoot(appRoutes, {preloadingStrategy: PreloadAllModules}]
```

## Shared Module

Do create a feature module named SharedModule in a shared folder. Declare components, directives and pipes in a shared module when those items will be re-used and reference by the components declared in other feature modules.

Take particular care when providing services in shared modules i.e. avoid specifying app-wide singleton providers. Services are singletons that are provided once for the entire application or in a particular feature module. **Acceptable services are those that are stateless**.

You don't want each module to have its own separate instance of singleton services. Yet there is a real danger of that happening if the SharedModule provides a service.

```javascript
// shared.module.ts
import { NgModule } from '@angular/core';

@NgModule({
  declarations: [
    // shared components
    AlertComponent,
    LoadingSpinnerComponent,
  ],
  imports: [CommonModule, FormsModule],
  exports: [
    AlertComponent,
    LoadingSpinnercomponent,
    CommonModule, // needed for ngIf, ngFor
    FormsModule,
  ],
})
export class SharedModule {}
```

## Core Module

Used to store all services. However, recommended way is to provide services @Injectable at component level.

```javascript
@Injectable({providedIn: 'root'})   // same instance available to all modules

@NgMoule({
  providers: [
    ShoppingListService,
    RecipeService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptorService,
      multi: true
    }
  ]
})
```

### AoT vs JiT

Ahead-of-Time vs Just-in-Time.

```
ng build --prod   // uses AoT compilation
```
