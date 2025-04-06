import { Injectable } from '@angular/core';
import { Course } from '../interfaces';
import { BehaviorSubject, map, Observable, of } from 'rxjs';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { HttpClient } from '@angular/common/http';

@Injectable()
@UntilDestroy()
export class CourseService {
  private _courses$ = new BehaviorSubject<Course[]>([]);

  private readonly mockData: Course[] = [
    {
      id: 1,
      title: 'Become a Python Champion',
      imageUrl: 'https://picsum.photos/id/237/200/300',
    },
    {
      id: 2,
      title: 'Master Angular like a Boss',
      imageUrl: 'https://picsum.photos/seed/picsum/200/300',
    },
  ];

  constructor(private http: HttpClient) {}

  public get courses(): Course[] {
    return this._courses$.value;
  }

  public get courses$(): Observable<Course[]> {
    return this._courses$.asObservable();
  }

  public initCourses(): void {
    this.getCourses(false)
      .pipe(untilDestroyed(this))
      .subscribe((courses) => this._courses$.next(courses));
  }

  public getCourses(mock = true): Observable<Course[]> {
    if (mock) {
      return of(this.mockData);
    }

    return this.http
      .get<{ data: Course[] }>(
        'https://run.mocky.io/v3/6e67152c-fb8f-4089-880e-01f1e4739071'
      )
      .pipe(map(({ data }: { data: Course[] }) => data));
  }
}
