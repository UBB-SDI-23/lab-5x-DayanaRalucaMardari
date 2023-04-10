import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { ApiService } from 'src/app/common/api.service';
import { CoreService } from 'src/app/common/core.service';

@Component({
  selector: 'app-artist-add-edit',
  templateUrl: './artist-add-edit.component.html',
  styleUrls: ['./artist-add-edit.component.css']
})
export class ArtistAddEditComponent implements OnInit {
  artistForm: FormGroup;

  constructor(
    private _fb: FormBuilder, 
    private _apiService: ApiService, 
    private _coreService: CoreService,
    private _dialogRef: MatDialogRef<ArtistAddEditComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any 
    ) { 
    this.artistForm = this._fb.group({
      name: '',
      height: '',
      nationality: ''
    });
  }

  ngOnInit(): void {
      this.artistForm.patchValue(this.data);
  }

  onSubmit() {
    console.log("form called");
    if (this.artistForm.valid) {
      if (this.data) {
        this._apiService
        .updateArtist(this.data.id, this.artistForm.value)
        .subscribe({
          next: (value: any) => {
            this._coreService.openSnackBar('Artist edited successfully');
            this._dialogRef.close(true);
          }, 
          error: (err: any) => {
            console.log(err);
          }
        })
      } else {
        this._apiService
        .addArtist(this.artistForm.value)
        .subscribe({
          next: (value: any) => {
            this._coreService.openSnackBar('Artist added successfully');
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
