import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'cc-course-catalog',
  imports: [CommonModule],
  templateUrl: './feature-course-catalog.component.html',
  styleUrl: './feature-course-catalog.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FeatureCourseCatalogComponent {}
