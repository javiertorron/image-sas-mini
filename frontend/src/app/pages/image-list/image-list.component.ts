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
  showUploadFormFlag: Boolean = false
  newImageUrl: String = ""

  constructor(private backendService: BackendService, private sanitizer: DomSanitizer) {}

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
  
  showUploadForm = () => {
    this.showUploadFormFlag = !this.showUploadFormFlag 
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
}
