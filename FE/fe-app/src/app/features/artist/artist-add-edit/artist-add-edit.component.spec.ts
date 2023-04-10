import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtistAddEditComponent } from './artist-add-edit.component';

describe('ArtistAddEditComponent', () => {
  let component: ArtistAddEditComponent;
  let fixture: ComponentFixture<ArtistAddEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArtistAddEditComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArtistAddEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
