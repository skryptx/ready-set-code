import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FeatureCourseCatalogComponent } from './feature-course-catalog.component';

describe('FeatureCourseCatalogComponent', () => {
  let component: FeatureCourseCatalogComponent;
  let fixture: ComponentFixture<FeatureCourseCatalogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FeatureCourseCatalogComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(FeatureCourseCatalogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
