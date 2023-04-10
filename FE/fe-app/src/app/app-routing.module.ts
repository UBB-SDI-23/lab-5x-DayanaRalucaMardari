import { NgModule, Component } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ArtistOverviewComponent } from './features/artist/artist-overview/artist-overview.component';
import { ArtistDetailsComponent } from './features/artist/artist-details/artist-details.component';
import { AlbumOverviewComponent } from './features/album/album-overview/album-overview.component';
import { AlbumDetailsComponent } from './features/album/album-details/album-details.component';

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'artist', component: ArtistOverviewComponent},
  {path: 'artist/:id', component: ArtistDetailsComponent},
  {path: 'album', component: AlbumOverviewComponent},
  {path: 'album/:id', component: AlbumDetailsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
