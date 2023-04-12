import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';

import { ApiService } from 'src/app/common/api.service';
import { Artist } from './models/artist.models';
import { MatDialog } from '@angular/material/dialog';
import { ArtistAddEditComponent } from 'src/app/features/artist/artist-add-edit/artist-add-edit.component';
import { Subject } from 'rxjs';

import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import { CoreService } from 'src/app/common/core.service';

@Component({
  selector: 'app-artist-overview',
  templateUrl: './artist-overview.component.html',
  styleUrls: ['./artist-overview.component.css']
})
export class ArtistOverviewComponent implements OnInit {
  artists$: Artist[] = [];
  displayedColumns: string[] = ['index', 'name', 'height', 'nationality', 'birth_date','artist-actions'];
  dataSource!: MatTableDataSource<any>;
  heightFilter!: number;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(
    private apiService: ApiService, 
    private router: Router, 
    private _dialog: MatDialog,
    private _coreService: CoreService,
    ) { }

  ngOnInit(): void {
    this.getAllArtists();
    this.apiService.refreshRequested$.subscribe(response => {
      this.getAllArtists();
    })
  }

  getArtistByHeight(height: any) {
    this.apiService.getArtistByMinHeight(height).subscribe((artists: Artist[]) => {
      this.dataSource = new MatTableDataSource(artists);
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
    });
  }

  getAllArtists() {
    this.apiService.getArtists().subscribe((artists: Artist[]) => {
      // this.artists$ = artists
      this.dataSource = new MatTableDataSource(artists);
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
    });
  }

  goToDetails(artistId: string) {
    this.router.navigateByUrl(`/artist/${artistId}`);
  }

  // goToAdd() {
  //   this.router.navigateByUrl(`/artist/add`);
  // }

  onDelete(artistId: string) {
    console.log("DELETE CALLED");
    this.apiService.onDeleteArtist(artistId).subscribe({
      next: (response) => {
        this._coreService.openSnackBar('Artist deleted successfully', 'done');
      },
      error: console.log
    });
  }

  openAddComponent() {
    const dialogRef = this._dialog.open(ArtistAddEditComponent);
    dialogRef.afterClosed().subscribe({
      next: (value) => {
        if (value) {
          this.getAllArtists();
        }
      }
    })
  }

  openEditComponent(data: any) {
    const dialogRef = this._dialog.open(ArtistAddEditComponent, {
      data: data
    });
    dialogRef.afterClosed().subscribe({
      next: (value) => {
        if (value) {
          this.getAllArtists();
        }
      }
    })
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
}
