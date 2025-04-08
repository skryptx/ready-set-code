import { Injectable } from '@angular/core';
import { Course } from '../interfaces';
import { BehaviorSubject, map, Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable()
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

  public getCourses(term: string, mock = true): Observable<Course[]> {
    let courseObs$: Observable<Course[]>;

    if (mock) {
      courseObs$ = of(this.mockData);
    } else {
      courseObs$ = this.http
        .get<{ data: Course[] }>(
          'https://run.mocky.io/v3/6e67152c-fb8f-4089-880e-01f1e4739071'
        )
        .pipe(map(({ data }: { data: Course[] }) => data));
    }

    return courseObs$.pipe(
      map((courses: Course[]) => {
        const filteredCourses = courses.filter((course) =>
          course.title.includes(term)
        );
        this._courses$.next(filteredCourses);

        return filteredCourses;
      })
    );
  }
}
