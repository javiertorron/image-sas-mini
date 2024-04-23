import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { AuthenticationService } from '../../services/authentication.service';
import { TokenResponseDTO } from '../../dtos/token-response.dto';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

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

  constructor(private authService: AuthenticationService, private router: Router) {
    this.username = ""
    this.password = ""
  }

  login = () => {
    this.authService.authenticate(this.username, this.password).subscribe({
      next: (response: TokenResponseDTO) => {
        console.log("Response from backend")
        console.log(JSON.stringify(response))
        this.authService.storeToken(response.token, response.type)
        this.router.navigate(['/image-list'])
      },
      error: (error: any) => {
        this.loginError = true
        console.log(error)
      }
    });
  }
}
