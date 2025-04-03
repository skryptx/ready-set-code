import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { CardComponent } from '@ng-sandbox/shared/ui';
import { Course } from './interfaces';

@Component({
  selector: 'cc-course-catalog',
  imports: [CardComponent],
  templateUrl: './course-catalog.component.html',
  styleUrl: './course-catalog.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseCatalogComponent implements OnInit {
  protected courses: Course[] = [];

  public ngOnInit(): void {
    this.initCourses();
  }

  private initCourses(): void {
    this.courses = [
      {
        id: 1,
        title: 'Become a Python Champion',
        image:
          'https://www.google.com/imgres?q=python&imgurl=https%3A%2F%2Fwebandcrafts.com%2F_next%2Fimage%3Furl%3Dhttps%253A%252F%252Fadmin.wac.co%252Fuploads%252FFeatures_Of_Python_1_f4ccd6d9f7.jpg%26w%3D4500%26q%3D90&imgrefurl=https%3A%2F%2Fwebandcrafts.com%2Fblog%2Ffeatures-of-python&docid=ToIIHHdqvx2P6M&tbnid=9AWZNK4TKavriM&vet=12ahUKEwjV_9b8vLyMAxWjp1YBHQWvB0sQM3oECHAQAA..i&w=3536&h=2167&hcb=2&ved=2ahUKEwjV_9b8vLyMAxWjp1YBHQWvB0sQM3oECHAQAA',
      },
      {
        id: 2,
        title: 'Master Angular like a Boss',
        image:
          'https://www.google.com/url?sa=i&url=https%3A%2F%2Fionic.io%2Fblog%2Fcatching-up-with-the-latest-features-in-angular&psig=AOvVaw1gPC0nYqpn6QbY7_8j2Iah&ust=1743790820248000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCj-5W9vIwDFQAAAAAdAAAAABAE',
      },
    ];
  }
}
