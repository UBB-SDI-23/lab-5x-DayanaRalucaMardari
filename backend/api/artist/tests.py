from unittest import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from artist.models import Artist
from album.models import Album

import json

# Create your tests here.

class ArtistListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create the artists
        number_of_artists = 5
        for artist_id in range(number_of_artists):
            Artist.objects.create(
                name=f"artist_{artist_id + 1}",
                height=170,
                nationality="American",
                birth_date="1990-03-04T00:00:00Z"
            )
        # create the albums
        artist_1=Artist.objects.get(id=1)
        artist_2=Artist.objects.get(id=2)
        artist_3=Artist.objects.get(id=3)

        Album.objects.create(title="title1", release_date="2020-10-03T00:00:00Z", genre="Pop", length="34:54", artist_id=artist_1)
        Album.objects.create(title="title2", release_date="2022-02-12T00:00:00Z", genre="R&B", length="40:02", artist_id=artist_1)
        Album.objects.create(title="title3", release_date="2019-05-22T00:00:00Z", genre="Pop", length="45:00", artist_id=artist_2)
        Album.objects.create(title="title4", release_date="2015-01-27T00:00:00Z", genre="Rock", length="51:32", artist_id=artist_2)
        Album.objects.create(title="title5", release_date="2018-05-22T00:00:00Z", genre="Pop", length="55:20", artist_id=artist_1)
        Album.objects.create(title="title6", release_date="2016-10-15T00:00:00Z", genre="Electro", length="49:20", artist_id=artist_3)

    
    def test_artist_list_url_exists(self):
        response = self.client.get("/artist/list/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    
    def test_top_5_artists_by_no_albums(self):
        response = self.client.get("/artist/top/no-albums/", format='json')
        self.assertEqual(response.status_code, 200)

        response.render()
        expected_json = [
            {'id': 1, 'no_albums': 3.0, 'name':'artist_1', 'height': 170, 'nationality': 'American', 'birth_date': '1990-03-04T00:00:00Z'},
            {'id': 2, 'no_albums': 2.0, 'name':'artist_2', 'height': 170, 'nationality': 'American', 'birth_date': '1990-03-04T00:00:00Z'},
            {'id': 3, 'no_albums': 1.0, 'name':'artist_3', 'height': 170, 'nationality': 'American', 'birth_date': '1990-03-04T00:00:00Z'},
            {'id': 4, 'no_albums': 0.0, 'name':'artist_4', 'height': 170, 'nationality': 'American', 'birth_date': '1990-03-04T00:00:00Z'},
            {'id': 5, 'no_albums': 0.0, 'name':'artist_5', 'height': 170, 'nationality': 'American', 'birth_date': '1990-03-04T00:00:00Z'} 
        ]
        self.assertEqual(json.loads(response.content), expected_json)




