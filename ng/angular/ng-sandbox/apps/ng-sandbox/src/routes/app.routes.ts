import { Route } from '@angular/router';
import { ccRoutes } from './cc-routes';
import { umRoutes } from './um-routes';

export const appRoutes: Route[] = [
  {
    path: '',
    children: umRoutes,
  },
  {
    path: 'course-catalog',
    children: ccRoutes,
  },
];
