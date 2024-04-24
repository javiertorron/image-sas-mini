import { Injectable, Inject, PLATFORM_ID } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { isPlatformBrowser } from '@angular/common';
import { Observable } from 'rxjs';
import { TokenResponseDTO } from '../dtos/token-response.dto';
import { LocalStorageService } from './local-storage.service';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private token: string = "";
  private type: string = "";
  private isBrowser: boolean;

  constructor(
    private http: HttpClient,
    private localStorageService: LocalStorageService,
    @Inject(PLATFORM_ID) platformId: Object
  ) {
    this.isBrowser = isPlatformBrowser(platformId);
  }

  authenticate(username: string, password: string): Observable<TokenResponseDTO> {
    return this.http.post<TokenResponseDTO>('http://localhost:8000/token', { username, password });
  }

  logout(): void {
    this.token = "";
    this.type = "";
    if (this.isBrowser) {
      this.localStorageService.clear();
    }
  }

  storeToken(token: string, type: string): void {
    this.token = token;
    this.type = type;
    if (this.isBrowser) {
      this.localStorageService.setItem('authToken', token);
      this.localStorageService.setItem('tokenType', type);
    }
  }

  isLoggedIn(): boolean {
    if (this.isBrowser) {
      this.token = this.localStorageService.getItem('authToken') || "";
      this.type = this.localStorageService.getItem('tokenType') || "";
    }
    return this.token !== "" && this.type !== "";
  }

  getTokenHeaderString(): string {
    if (this.isBrowser) {
      const token = this.localStorageService.getItem('authToken');
      const type = this.localStorageService.getItem('tokenType');
      if (token && type) {
        return type + ' ' + token;
      }
    }
    return "";
  }
}
