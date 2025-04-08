import {
  ChangeDetectionStrategy,
  Component,
  Input,
  OnDestroy,
  OnInit,
  output,
} from '@angular/core';
import { CourseService } from '../services/course.service';
import { Course } from '../interfaces';
import { Observable } from 'rxjs';

@Component({
  selector: 'cc-course-info',
  templateUrl: './course-info.component.html',
  styleUrl: './course-info.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseInfoComponent implements OnInit, OnDestroy {
  private _selectedCourse: Course | null;
  public closeCourseInfo = output<void>();

  constructor(private courseService: CourseService) {}

  public ngOnInit(): void {
    this.courses$.subscribe((courses) => {
      console.log(courses);
    });
  }

  public get selectedCourse(): Course | null {
    return this._selectedCourse;
  }

  @Input()
  public set selectedCourse(val: Course | null) {
    this._selectedCourse = val;
  }

  public ngOnDestroy(): void {
    console.log('Course Info Destroyed!');
  }

  protected get courses$(): Observable<Course[]> {
    return this.courseService.courses$;
  }

  protected onClose(): void {
    this.closeCourseInfo.emit();
  }
}
