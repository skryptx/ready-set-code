import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { CourseListComponent } from './course-list/course-list.component';
import { CourseInfoComponent } from './course-info/course-info.component';
import { CourseService } from './services/course.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { Course } from './interfaces';
import { AsyncPipe } from '@angular/common';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';

@UntilDestroy()
@Component({
  selector: 'cc-course-catalog',
  imports: [AsyncPipe, CourseListComponent, CourseInfoComponent],
  templateUrl: './course-catalog.component.html',
  styleUrl: './course-catalog.component.scss',
  providers: [CourseService],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseCatalogComponent implements OnInit {
  private _selectedCourse$ = new BehaviorSubject<Course | null>(null);

  constructor(private courseService: CourseService) {}

  protected get selectedCourse$(): Observable<Course | null> {
    return this._selectedCourse$.asObservable();
  }

  public ngOnInit(): void {
    this.initCourses();
  }

  protected onSelectCourse(course: Course): void {
    this._selectedCourse$.next(course);
  }

  protected closeCourseInfo(): void {
    this._selectedCourse$.next(null);
  }

  private initCourses(): void {
    this.courseService.getCourses('').pipe(untilDestroyed(this)).subscribe();
  }
}
