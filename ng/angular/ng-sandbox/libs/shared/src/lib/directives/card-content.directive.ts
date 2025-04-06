import { Directive, inject, TemplateRef } from '@angular/core';

@Directive({
  selector: '[shCardContentTmpl]',
})
export class CardContentDirective {
  public tmpl = inject(TemplateRef);
}
