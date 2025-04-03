import { ChangeDetectionStrategy, Component } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';

interface UserRegisterFormGroup {
  email: FormControl<string | null>;
  password: FormControl<string | null>;
}

@Component({
  selector: 'um-register',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
  ],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
})
export class RegisterComponent {
  protected formGroup: FormGroup<UserRegisterFormGroup>;

  constructor(private fb: FormBuilder) {
    this.formGroup = this.fb.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  protected registerUser(): void {
    alert(JSON.stringify(JSON.stringify(this.formGroup.value)));
  }
}
