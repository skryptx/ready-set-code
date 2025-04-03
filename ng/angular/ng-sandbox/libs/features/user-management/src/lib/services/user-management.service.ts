import { Injectable } from '@angular/core';
import { User } from '@ng-sandbox/domain';
import { from, Observable, of } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class UserManagementService {
  private _user: User;

  public get user(): User {
    return this._user;
  }

  public registerUser(user: User): Observable<void> {
    const registerUser$ = new Promise<void>((resolve) => {
      setTimeout(() => {
        this._user = user;
        resolve();
      });
    });

    return from(registerUser$);
  }

  public isUserValid({ email, password }: Partial<User>): Observable<boolean> {
    return of(this.user.email === email && this.user.password === password);
  }
}
