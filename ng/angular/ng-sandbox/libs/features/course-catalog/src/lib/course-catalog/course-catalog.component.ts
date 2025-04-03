import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { CardComponent } from '@ng-sandbox/shared/ui';

@Component({
  selector: 'cc-course-catalog',
  imports: [CardComponent],
  templateUrl: './course-catalog.component.html',
  styleUrl: './course-catalog.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CourseCatalogComponent implements OnInit {
  public ngOnInit(): void {
    console.log('loaded');
  }
}
