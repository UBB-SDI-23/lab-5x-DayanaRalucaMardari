import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Artist } from '../artist-overview/models/artist.models';
import { ApiService } from 'src/app/common/api.service';


@Component({
  selector: 'app-artist-details',
  templateUrl: './artist-details.component.html',
  styleUrls: ['./artist-details.component.css']
})
export class ArtistDetailsComponent implements OnInit {
  artistId?: string;
  artist?: Artist;

  constructor(
    private apiService: ApiService, 
    private activatedRoute: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.activatedRoute.params.subscribe(params => {
      this.artistId = params['id']
      this.apiService.getArtist(this.artistId!).subscribe((artist: Artist) => {
        this.artist = artist;
      })
    })
  }
}
