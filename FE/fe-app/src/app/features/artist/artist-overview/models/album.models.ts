export interface Album {
    id: string;
    title: string;
    release_date: string;
    genre: string;
    length: string;
    artist_id: any;
}

export interface AddAlbumDto {
    title: string;
    release_date: string;
    genre: string;
    length: string;
    artist_id: any;
}