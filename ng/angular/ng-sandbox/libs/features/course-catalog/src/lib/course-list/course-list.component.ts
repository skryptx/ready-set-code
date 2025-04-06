import {
  ChangeDetectionStrategy,
  Component,
  OnInit,
  output,
  SkipSelf,
} from '@angular/core';
import { Course } from '../interfaces';
import { CardComponent } from '@ng-sandbox/ui';
import { CardContentDirective, HighlightedDirective } from '@ng-sandbox/shared';
import { CourseService } from '../services/course.service';
import { Observable } from 'rxjs';
import { AsyncPipe } from '@angular/common';

@Component({
  selector: 'cc-course-list',
  imports: [
    AsyncPipe,
    CardComponent,
    CardContentDirective,
    HighlightedDirective,
  ],
  templateUrl: './course-list.component.html',
  styleUrl: './course-list.component.scss',
  providers: [CourseService],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseListComponent implements OnInit {
  selectCourse = output<Course>();

  constructor(@SkipSelf() private courseService: CourseService) {}

  public ngOnInit(): void {
    this.courses$.subscribe((courses) => {
      console.log(courses);
    });
  }

  protected get courses$(): Observable<Course[]> {
    return this.courseService.courses$;
  }

  public onSelectCourse(course: Course): void {
    this.selectCourse.emit(course);
  }
}
