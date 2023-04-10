import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { ApiService } from 'src/app/common/api.service';
import { CoreService } from 'src/app/common/core.service';
import { Artist, ArtistFK } from '../../artist/artist-overview/models/artist.models';

import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith, tap} from 'rxjs/operators';

@Component({
  selector: 'app-album-add-edit',
  templateUrl: './album-add-edit.component.html',
  styleUrls: ['./album-add-edit.component.css']
})
export class AlbumAddEditComponent implements OnInit{
  albumForm: FormGroup;
  //artist_id = new FormControl();
  filteredArtists!: Observable<ArtistFK[]>;
  options!: ArtistFK[];

  constructor(
    private _fb: FormBuilder, 
    private _apiService: ApiService, 
    private _coreService: CoreService,
    private _dialogRef: MatDialogRef<AlbumAddEditComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any 
    ) {
    this._apiService.getArtistsName().subscribe(item => {
      this.options = item;
    });
    this.albumForm = this._fb.group({
      title: '',
      release_date: '',
      genre: '',
      length: '',
      artist_id: '',
    });
  }

  ngOnInit(): void {
    this.albumForm.patchValue(this.data);
    this.filteredArtists = this._filterArtists();
  }

  selectArtist(name: any) {
    console.log(name);
  }

  private _filterArtists() {
    return this.albumForm.controls['artist_id'].valueChanges.pipe(startWith(''),
    map(item => {
      const name = item;
      return name? this._filter(name as string) : this.options;
    }));
  }

  private _filter(name: string): ArtistFK[] {
    name = name.toString();
    const filterValue = name.toLocaleLowerCase();
    return this.options.filter(option => option.name.toLocaleLowerCase().includes(filterValue));
  }

  onSubmit() {
    console.log("form called");
    if (this.albumForm.valid) {
      if (this.data) {
        this._apiService
        .updateAlbum(this.data.id, this.albumForm.value)
        .subscribe({
          next: (value: any) => {
            this._coreService.openSnackBar('Album edited successfully');
            this._dialogRef.close(true);
          }, 
          error: (err: any) => {
            console.log(err);
          }
        })
      } else {
        this._apiService
        .addAlbum(this.albumForm.value)
        .subscribe({
          next: (value: any) => {
            this._coreService.openSnackBar('Album added successfully');
            this._dialogRef.close(true);
          }, 
          error: (err: any) => {
            console.log(err);
          }
        })
      }
    }
  }
}
