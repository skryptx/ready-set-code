import { Directive, inject, TemplateRef } from '@angular/core';

@Directive({
  selector: '[hpCardContentTmpl]',
})
export class CardContentDirective {
  public tmpl = inject(TemplateRef);
}
