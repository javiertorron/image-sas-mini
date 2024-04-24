import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatList, MatListItem, MatListItemAvatar } from '@angular/material/list';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ImageModel } from '../../models/image.model';
import { BackendService } from '../../services/backend.service';
import { ImageListResponseDTO } from '../../dtos/image-list-response.dto';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { AuthenticationService } from '../../services/authentication.service';
import { Router } from '@angular/router';
import { UploadImageResponseDTO } from '../../dtos/upload-image-response.dto';

@Component({
  selector: 'app-image-list',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatFormFieldModule,
    FormsModule,
    MatList,
    MatListItem,
    MatListItemAvatar
  ],
  templateUrl: './image-list.component.html',
  styleUrl: './image-list.component.css'
})
export class ImageListComponent {
  images: Array<ImageModel> = []
  selectedFile: File | null = null;

  constructor(
    private backendService: BackendService, 
    private sanitizer: DomSanitizer, 
    private authService: AuthenticationService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.backendService.getThumbnailList().subscribe({
      next: (response: ImageListResponseDTO) => {
        this.images = response.files.map(filename => new ImageModel(filename));
      },
      error: error => {
        console.error('Error fetching file list:', error);
      }
    });
  }

  uploadImage = () => {
    alert("Upload image")
  }

  loadImage(image: ImageModel): any {
    this.backendService.getImage(image.filename).subscribe(blob => {
      const url = URL.createObjectURL(blob);
      return this.sanitizer.bypassSecurityTrustUrl(url);
    });
  }

  logout = () => {
    this.authService.logout()
    this.router.navigate(['/login'])
  }

  onFileSelected(event: any): void {
    const element = event.currentTarget as HTMLInputElement;
    let fileList: FileList | null = element.files;
    if (fileList && fileList.length > 0) {
      this.selectedFile = fileList[0];
      this.add();
    }
  }

  add(): void {
    if (!this.selectedFile) {
      alert('Please select a file.');
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile, this.selectedFile.name);

    this.backendService.uploadImage(formData).subscribe({
      next: (response:UploadImageResponseDTO) => {
        if (response.filename) {
          this.images.push(new ImageModel(response.filename));
          console.log('File uploaded:', response.filename);
        } else {
          console.error('No filename returned from the server.');
        }
      },
      error: (error) => {
        console.error('Error uploading file:', error);
      }
    });
  }
}
