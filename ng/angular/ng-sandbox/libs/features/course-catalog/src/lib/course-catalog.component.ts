import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
  OnInit,
} from '@angular/core';
import { CardComponent } from '@ng-sandbox/shared/ui';
import { Course } from './interfaces';
import { CardContentDirective } from '@ng-sandbox/shared/helpers';
import { AsyncPipe } from '@angular/common';
import { BehaviorSubject, Observable } from 'rxjs';

@Component({
  selector: 'cc-course-catalog',
  imports: [CardComponent, CardContentDirective, AsyncPipe],
  templateUrl: './course-catalog.component.html',
  styleUrl: './course-catalog.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseCatalogComponent implements OnInit {
  protected get courses$(): Observable<Course[]> { 
    return this._courses$.asObservable();
  }
  protected enable = true;
  private _courses$ = new BehaviorSubject<Course[]>([]);
  private courses: Course[] = [];

  constructor(private cdr: ChangeDetectorRef) {}

  public ngOnInit(): void {
    this.initCourses();
  }

  private initCourses(): void {
    this.courses = [
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
    this._courses$.next(this.courses);
    this.cdr.markForCheck();
    setInterval(
      function (this: CourseCatalogComponent) {
        this._courses$.next([...this.courses, ...this.courses]);
      }.bind(this),
      2000
    );
  }

  protected fakeEvent(): void {
    console.log('Fake Event Called!');
  }
}
