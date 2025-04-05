import {
  Directive,
  ElementRef,
  HostBinding,
  HostListener,
  Input,
} from '@angular/core';

@Directive({
  selector: '[hpHighlighted]',
})
export class HighlightedDirective {
  @Input() public color = 'yellow';
  @Input() public backgroundColor = 'black';

  constructor(private el: ElementRef) {}

  @HostListener('mouseenter')
  public onMouseEnter(): void {
    this.el.nativeElement.style.backgroundColor = this.backgroundColor;
    this.el.nativeElement.style.color = this.color;
  }

  @HostListener('mouseleave')
  public onMouseLeave(): void {
    this.el.nativeElement.style.backgroundColor = 'black';
    this.el.nativeElement.style.color = 'yellow';
  }
}
