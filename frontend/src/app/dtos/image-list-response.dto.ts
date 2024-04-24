export class ImageListResponseDTO {
  files: string[];

  constructor(files: string[]) {
    this.files = files;
  }
}