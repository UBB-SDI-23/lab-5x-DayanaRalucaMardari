export interface Artist {
    id: string;
    name: string;
    height: number;
    nationality: string;
    birth_date: string;
}

export interface AddArtistDto {
    name: string;
    height: number;
    nationality: string;
    birth_date: string;
}

export interface ArtistFK {
    id: string;
    name: string;
}