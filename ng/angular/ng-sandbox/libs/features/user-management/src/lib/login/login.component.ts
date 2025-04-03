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
import { UserManagementService } from '../services';
import { User } from '@ng-sandbox/domain';

interface UserFormGroup {
  email: FormControl<string | null>;
  password: FormControl<string | null>;
}

@Component({
  selector: 'um-login',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
})
export class LoginComponent {
  protected formGroup: FormGroup<UserFormGroup>;

  constructor(
    private fb: FormBuilder,
    private userManagementService: UserManagementService
  ) {
    this.formGroup = this.fb.group({
      email: ['', Validators.required, Validators.email],
      password: ['', Validators.required],
    });
  }

  private get loginDetails(): Partial<User> {
    const { email, password } = this.formGroup.value;
    return { email, password } as Partial<User>;
  }

  protected loginUser(): void {
    this.userManagementService.isUserValid(this.loginDetails).subscribe();
  }
}
