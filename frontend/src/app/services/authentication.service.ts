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
    this.localStorageService.setItem('token', '');
    this.localStorageService.setItem('type', '');
  }

  storeToken(token: string, type: string): void {
    console.log("Stored")
    this.localStorageService.setItem('token', token);
    this.localStorageService.setItem('type', type);
    console.log(`Type: ${this.localStorageService.getItem('type')}`)
    console.log(`Token: ${this.localStorageService.getItem('token')}`)
  }

  isLoggedIn(): boolean {
    const token = this.localStorageService.getItem('token') || "";
    const type = this.localStorageService.getItem('type') || "";
    return token !== "" && type !== "";
  }

  getTokenHeaderString(): string {
    const token = this.localStorageService.getItem('token');
    const type = this.localStorageService.getItem('type');
    return type + ' ' + token;
  }
}
