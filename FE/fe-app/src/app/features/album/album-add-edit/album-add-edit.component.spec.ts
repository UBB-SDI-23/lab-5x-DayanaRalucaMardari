import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlbumAddEditComponent } from './album-add-edit.component';

describe('AlbumAddEditComponent', () => {
  let component: AlbumAddEditComponent;
  let fixture: ComponentFixture<AlbumAddEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AlbumAddEditComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AlbumAddEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
