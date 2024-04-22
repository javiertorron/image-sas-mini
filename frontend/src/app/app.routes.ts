import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { ImageListComponent } from './pages/image-list/image-list.component';

export const routes: Routes = [
    { path: '', redirectTo: '/login', pathMatch: 'full' },
    { path: 'login', component: LoginComponent },
    { path: 'image-list', component: ImageListComponent },
];
