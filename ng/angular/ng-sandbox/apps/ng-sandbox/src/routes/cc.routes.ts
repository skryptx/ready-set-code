import { Route } from '@angular/router';

export const ccRoutes: Route[] = [
  {
    path: '',
    loadComponent: () =>
      import('@ng-sandbox/features/course-catalog').then(
        (c) => c.CourseCatalogComponent
      ),
  },
];
