import { NgTemplateOutlet } from '@angular/common';
import {
  AfterContentInit,
  Component,
  contentChild,
  input,
  TemplateRef,
} from '@angular/core';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'ui-card',
  imports: [MatCardModule, NgTemplateOutlet],
  templateUrl: './card.component.html',
  styleUrl: './card.component.scss',
})
export class CardComponent implements AfterContentInit {
  protected cardContentTmpl = contentChild('cardContentTmpl', {
    read: TemplateRef,
  });

  data = input<any>();

  public ngAfterContentInit(): void {
    console.log(this.cardContentTmpl);
    console.log(this.data);
  }
}
