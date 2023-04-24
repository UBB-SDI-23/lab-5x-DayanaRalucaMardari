import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { Artist, AddArtistDto, ArtistFK } from '../features/artist/artist-overview/models/artist.models';

import { tap, map } from 'rxjs';
import { AddAlbumDto, Album } from '../features/artist/artist-overview/models/album.models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  //baseUrl = 'http://localhost:8000/api'; // have to change it to the AWS
  // baseUrl = 'http://13.49.125.36:80/api';
  baseUrl = 'https://dayanamdr.ignorelist.com/api';
  _refreshRequested$ = new Subject<void>();

  constructor(private http: HttpClient) { }

  get refreshRequested$() {
    return this._refreshRequested$;
  }

  // artist
  getArtists(): Observable<Artist[]> {
    return this.http.get(`${this.baseUrl}/artist/`) as Observable<Artist[]>;
  }

  getArtist(artistId: string): Observable<Artist> {
    return this.http.get(`${this.baseUrl}/artist/id/${artistId}/`) as Observable<Artist>;
  }

  addArtist(artist: AddArtistDto): Observable<Artist> {
    return this.http.post(`${this.baseUrl}/artist/create/`, artist) as Observable<Artist>;
  }

  updateArtist(artistId: string, artist: AddArtistDto): Observable<Artist> {
    return this.http.put(`${this.baseUrl}/artist/update/${artistId}/`, artist) as Observable<Artist>;
  }

  onDeleteArtist(artistId: string) {
    return this.http.delete(`${this.baseUrl}/artist/delete/${artistId}/`)
             .pipe(tap(() => {this._refreshRequested$.next();}));
  }

  getArtistByMinHeight(minHeight: any): Observable<Artist[]> {
    return this.http.get(`${this.baseUrl}/artist/filter/height/minimum?min_height=${minHeight}`) as Observable<Artist[]>;
  }

  getArtistsName(): Observable<ArtistFK[]> {
    return this.http.get<ArtistFK[]>(`${this.baseUrl}/artist/`);
  }

  // album
  getAlbums(): Observable<Album[]> {
    return this.http.get(`${this.baseUrl}/album/`) as Observable<Album[]>;
  }

  getAlbum(albumId: string): Observable<Album> {
    return this.http.get(`${this.baseUrl}/album/id/${albumId}/`) as Observable<Album>;
  }

  addAlbum(album: AddAlbumDto): Observable<Album> {
    console.log("api called");
    console.log(album);
    return this.http.post(`${this.baseUrl}/album/create/`, album) as Observable<Album>;
  }

  updateAlbum(albumId: string, album: AddAlbumDto): Observable<Album> {
    return this.http.put(`${this.baseUrl}/album/update/${albumId}/`, album) as Observable<Album>;
  }

  deleteAlbum(albumId: string) {
    return this.http.delete(`${this.baseUrl}/album/delete/${albumId}/`)
             .pipe(tap(() => {this._refreshRequested$.next();}));
  }
}
