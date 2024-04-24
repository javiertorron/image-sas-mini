import { Component, afterRender } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';
import { TokenResponseDTO } from '../../dtos/token-response.dto';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { StorageService } from '../../services/storage.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    MatCardModule,
    CommonModule,
    MatFormFieldModule,
    FormsModule
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username: string
  password: string
  loginError: boolean = false

  constructor(private authService: AuthenticationService, private router: Router, private storageService: StorageService) {
    this.username = "javier.torron"
    this.password = "secretpassword"
  }

  ngOnInit(): void {
    // Verificar si hay un token en el localStorage
    const loginStored = this.authService.isLoggedIn();

    // Si hay un token, navegar a la pantalla de image-list
    if (loginStored) {
      // this.router.navigate(['/image-list']);
    }
  }

  login = () => {
    this.authService.authenticate(this.username, this.password).subscribe({
      next: (response: TokenResponseDTO) => {
        this.authService.storeToken(response.access_token, response.token_type)
        this.router.navigate(['/image-list'])
      },
      error: (error: any) => {
        this.loginError = true
        console.log(error)
      }
    });
  }
}
