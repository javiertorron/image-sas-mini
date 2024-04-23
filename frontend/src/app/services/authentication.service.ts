import { Injectable, inject  } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, map } from 'rxjs';
import { TokenResponseDTO } from '../dtos/token-response.dto';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private http = inject(HttpClient);

  constructor(private localStorageService: LocalStorageService) {
  }

  authenticate(username: string, password: string): Observable<TokenResponseDTO> {
    return this.http.post<TokenResponseDTO>('http://localhost:8000/token', { username, password });
  }

  logout(): void {
    this.localStorageService.removeItem('token');
    this.localStorageService.removeItem('type');
  }

  storeToken(token: string, type: string): void {
    this.localStorageService.setItem('token', token);
    this.localStorageService.setItem('type', type);
  }

  isLoggedIn(): boolean {
    return this.localStorageService.getItem('token') != null && this.localStorageService.getItem('type') != null
  }

  getTokenHeaderString(): string | null {
    return this.localStorageService.getItem('type') + ' ' + this.localStorageService.getItem('token');
  }
}
