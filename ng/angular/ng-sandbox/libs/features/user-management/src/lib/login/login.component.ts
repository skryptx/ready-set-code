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
import { User } from '@ng-sandbox/domain';
import { Router } from '@angular/router';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { filter } from 'rxjs';
import { UserManagementService } from '@ng-sandbox/shared';

interface UserFormGroup {
  email: FormControl<string | null>;
  password: FormControl<string | null>;
}

@UntilDestroy()
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
    private userManagementService: UserManagementService,
    private router: Router
  ) {
    this.formGroup = this.fb.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  private get loginDetails(): Partial<User> {
    const { email, password } = this.formGroup.value;
    return { email, password } as Partial<User>;
  }

  protected loginUser(): void {
    this.userManagementService
      .isUserValid(this.loginDetails)
      .pipe(filter(Boolean), untilDestroyed(this))
      .subscribe(() => {
        this.router.navigate(['course-catalog']);
      });
  }
}
