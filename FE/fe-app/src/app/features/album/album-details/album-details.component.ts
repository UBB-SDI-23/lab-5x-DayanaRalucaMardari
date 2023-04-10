import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Album } from '../../artist/artist-overview/models/album.models';
import { ApiService } from 'src/app/common/api.service';


@Component({
  selector: 'app-album-details',
  templateUrl: './album-details.component.html',
  styleUrls: ['./album-details.component.css']
})
export class AlbumDetailsComponent {
  albumId?: string;
  album?: Album;

  constructor(
    private apiService: ApiService, 
    private activatedRoute: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.activatedRoute.params.subscribe(params => {
      this.albumId = params['id']
      this.apiService.getAlbum(this.albumId!).subscribe((album: Album) => {
        this.album = album;
      })
    })
  }
}
