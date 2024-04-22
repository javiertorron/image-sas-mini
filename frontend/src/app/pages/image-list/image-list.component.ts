import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ImageModel } from '../../models/image.model';

@Component({
  selector: 'app-image-list',
  standalone: true,
  imports: [
    CommonModule,
    MatCardModule,
    MatFormFieldModule,
    FormsModule
  ],
  templateUrl: './image-list.component.html',
  styleUrl: './image-list.component.css'
})
export class ImageListComponent {
  images: Array<ImageModel> = []
  showUploadFormFlag: Boolean = false
  newImageUrl: String = ""
  
  showUploadForm = () => {
    this.showUploadFormFlag = !this.showUploadFormFlag 
  }

  uploadImage = () => {
    alert("Upload image")
  }
}
