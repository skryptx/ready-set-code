import {
  AfterViewInit,
  ChangeDetectionStrategy,
  Component,
  ElementRef,
  OnInit,
  output,
  SkipSelf,
  viewChild,
} from '@angular/core';
import { Course } from '../interfaces';
import { CardComponent } from '@ng-sandbox/ui';
import { CardContentDirective, HighlightedDirective } from '@ng-sandbox/shared';
import { CourseService } from '../services/course.service';
import { debounceTime, Observable, switchMap } from 'rxjs';
import { AsyncPipe } from '@angular/common';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';

@UntilDestroy()
@Component({
  selector: 'cc-course-list',
  imports: [
    AsyncPipe,
    CardComponent,
    CardContentDirective,
    HighlightedDirective,
    ReactiveFormsModule,
  ],
  templateUrl: './course-list.component.html',
  styleUrl: './course-list.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseListComponent implements OnInit, AfterViewInit {
  public selectCourse = output<Course>();

  protected search = new FormControl<string>('');

  protected searchTerm = viewChild<HTMLInputElement, ElementRef>('searchTerm', {
    read: ElementRef,
  });

  constructor(@SkipSelf() private courseService: CourseService) {}

  public ngOnInit(): void {
    this.search.valueChanges
      .pipe(
        debounceTime(300),
        switchMap((term) => this.courseService.getCourses(term ?? '')),
        untilDestroyed(this)
      )
      .subscribe();
  }

  public ngAfterViewInit(): void {
    this.searchTerm()?.nativeElement.addEventListener('keyup', () => {
      console.log(this.search.value);
    });
  }

  protected get courses$(): Observable<Course[]> {
    return this.courseService.courses$;
  }

  public onSelectCourse(course: Course): void {
    this.selectCourse.emit(course);
  }
}
