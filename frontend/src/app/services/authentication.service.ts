import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, map } from 'rxjs';
import { TokenResponseDTO } from '../dtos/token-response.dto';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private tokenSubject: BehaviorSubject<string | null>;
  public token$: Observable<string | null>;
  private typeSubject: BehaviorSubject<string | null>;
  public type$: Observable<string | null>;

  constructor(private http: HttpClient) {
    this.tokenSubject = new BehaviorSubject<string | null>(localStorage.getItem('token'));
    this.typeSubject = new BehaviorSubject<string | null>(localStorage.getItem('type'));
    this.token$ = this.tokenSubject.asObservable();
    this.type$ = this.typeSubject.asObservable();
  }

  public get tokenValue(): string | null {
    return this.tokenSubject.value;
  }

  authenticate(username: string, password: string): Observable<TokenResponseDTO> {
    return this.http.post<TokenResponseDTO>('http://backend:8000/token', { username, password });
  }

  logout(): void {
    localStorage.removeItem('token');
    this.tokenSubject.next(null);
  }

  storeToken(token: string, type: string): void {
    localStorage.setItem('token', token);
    localStorage.setItem('type', type);
    this.tokenSubject.next(token);
    this.typeSubject.next(type);
  }

  isLoggedIn(): Observable<boolean> {
    return this.tokenSubject.asObservable().pipe(
      map(token => !!token)
    );
  }

  getTokenHeaderString(): string | null {
    return localStorage.getItem('type') + ' ' + localStorage.getItem('token');
  }
}
