import { Route } from '@angular/router';

export const umRoutes: Route[] = [
  {
    path: '',
    loadComponent: () =>
      import('@ng-sandbox/features/user-management').then(
        (c) => c.LoginComponent
      ),
  },
  {
    path: 'register',
    loadComponent: () =>
      import('@ng-sandbox/features/user-management').then(
        (c) => c.RegisterComponent
      ),
  },
];
