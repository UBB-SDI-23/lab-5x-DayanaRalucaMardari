from unittest import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from artist.models import Artist
from album.models import Album
from song.models import Song
from .models import Playlist

import json

# Create your tests here.

class PlaylistListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create artist
        artist = Artist.objects.create(name='test-artist', height=170, nationality='test-nat', birth_date='1990-03-04T00:00:00Z')
        # create album
        album = Album.objects.create(title="test-album", release_date="2020-10-03T00:00:00Z", genre="Pop", length="34:54", artist_id=artist)
        # create songs
        songs = [
            Song(title='title1', label='records', length='2:00', album_id=album),
            Song(title='title2', label='records', length='1:00', album_id=album),
            Song(title='title3', label='records', length='3:00', album_id=album),
            Song(title='title4', label='records', length='1:00', album_id=album),
            Song(title='title5', label='records', length='4:00', album_id=album)
        ]
        Song.objects.bulk_create(songs)
        # create playlists
        playlists = [
            Playlist(title='playlist1'),
            Playlist(title='playlist2')
        ]
        Playlist.objects.bulk_create(playlists)
        # add songs to playlists
        playlists[0].songs.set([songs[0], songs[2]]) # 5 / 2 = 2.5
        playlists[1].songs.set([songs[1], songs[3], songs[4]]) # 6 / 3 = 2.0


    def test_playlist_list_url_exists(self):
        response = self.client.get('/playlist/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


    def test_playlist_by_avg_song_length(self):
        response = self.client.get('/playlist/avg/song/length/')
        self.assertEqual(response.status_code, 200)

        response.render()
        expected_json = [
            {'id': 1, 'avg_length': 2.5, 'title': 'playlist1', 'description': '', 'songs': [1, 3]},
            {'id': 2, 'avg_length': 2.0, 'title': 'playlist2', 'description': '', 'songs': [2, 4, 5]}
        ]
        self.assertEqual(json.loads(response.content), expected_json)
