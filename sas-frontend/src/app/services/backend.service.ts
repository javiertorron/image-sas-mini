import { Injectable, inject } from '@angular/core';
import { AuthenticationService } from './authentication.service';
import { ImageListResponseDTO } from '../dtos/image-list-response.dto';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { UploadImageResponseDTO } from '../dtos/upload-image-response.dto';

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  private http = inject(HttpClient);
  apiUrl: string = "http://localhost:8000"

  constructor(private authenticationService: AuthenticationService) { }

  getThumbnailList(): Observable<ImageListResponseDTO> {
    const httpHeaders: HttpHeaders = new HttpHeaders({
      Authorization: this.authenticationService.getTokenHeaderString()
    });
    return this.http.get<ImageListResponseDTO>(`${this.apiUrl}/image-list`, {headers: httpHeaders});
  }

  getImage(image: string): Observable<Blob> {
    const httpHeaders: HttpHeaders = new HttpHeaders({
      Authorization: this.authenticationService.getTokenHeaderString()
    });
    return this.http.get(`${this.apiUrl}/get-image/${image}`,  { responseType: 'blob', headers: httpHeaders });
  }

  uploadImage(formData: FormData): Observable<UploadImageResponseDTO> {
    const httpHeaders: HttpHeaders = new HttpHeaders({
      Authorization: this.authenticationService.getTokenHeaderString()
    });
    return this.http.post<UploadImageResponseDTO>(`${this.apiUrl}/upload-image`, formData, { responseType: 'json', headers: httpHeaders });
  }
}
