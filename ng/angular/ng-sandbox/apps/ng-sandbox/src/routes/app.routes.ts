import { Route } from '@angular/router';

export const appRoutes: Route[] = [
  {
    path: '',
    loadChildren: () => import('./um-routes').then((c) => c.umRoutes),
  },
];
