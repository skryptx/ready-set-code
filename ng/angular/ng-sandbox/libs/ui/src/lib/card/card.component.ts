import { NgTemplateOutlet } from '@angular/common';
import {
  Component,
  contentChild,
  ContentChild,
  input,
  TemplateRef,
} from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { CardContentDirective } from '@ng-sandbox/shared';

@Component({
  selector: 'ui-card',
  imports: [MatCardModule, NgTemplateOutlet],
  templateUrl: './card.component.html',
  styleUrl: './card.component.scss',
})
export class CardComponent {
  protected cardContentTmpl = contentChild(CardContentDirective);

  data = input<unknown>();
}
