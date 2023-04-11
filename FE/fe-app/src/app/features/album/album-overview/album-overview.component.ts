import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';

import { ApiService } from 'src/app/common/api.service';
import { Album } from '../../artist/artist-overview/models/album.models';
import { MatDialog } from '@angular/material/dialog';
import { ArtistAddEditComponent } from 'src/app/features/artist/artist-add-edit/artist-add-edit.component';

import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import { CoreService } from 'src/app/common/core.service';
import { AlbumAddEditComponent } from '../album-add-edit/album-add-edit.component';

@Component({
  selector: 'app-album-overview',
  templateUrl: './album-overview.component.html',
  styleUrls: ['./album-overview.component.css']
})
export class AlbumOverviewComponent {
  displayedColumns: string[] = ['index', 'title', 'release_date', 'genre', 'length', 'album-actions'];
  dataSource!: MatTableDataSource<any>;
  
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(
    private apiService: ApiService, 
    private router: Router, 
    private _dialog: MatDialog,
    private _coreService: CoreService,
    ) { }

    ngOnInit(): void {
      this.getAlbums();
      this.apiService.refreshRequested$.subscribe(response => {
        this.getAlbums();
      })
    }

  getAlbums() {
    this.apiService.getAlbums().subscribe((albums: Album[]) => {
      // console.log(albums);
      this.dataSource = new MatTableDataSource(albums);
      this.dataSource.sort = this.sort;
      this.dataSource.paginator = this.paginator;
    })
  }

  goToDetails(albumId: string) {
    this.router.navigateByUrl(`/album/${albumId}`);
  }

  onDelete(artistId: string) {
    this.apiService.deleteAlbum(artistId).subscribe({
      next: (response) => {
        this._coreService.openSnackBar('Album deleted successfully', 'done');
      },
      error: console.log
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  openAddComponent() {
    const dialogRef = this._dialog.open(AlbumAddEditComponent);
    dialogRef.afterClosed().subscribe({
      next: (value) => {
        if (value) {
          this.getAlbums();
        }
      }
    })
  }

  openEditComponent(data: any) {
    const dialogRef = this._dialog.open(AlbumAddEditComponent, {
      data: data
    });
    dialogRef.afterClosed().subscribe({
      next: (value) => {
        if (value) {
          this.getAlbums();
        }
      }
    })
  }
}
