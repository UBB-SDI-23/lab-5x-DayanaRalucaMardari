from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Avg

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PlaylistSerializer, PlaylistSongSerializer

from .models import Playlist, PlaylistSong
from song.models import Song

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'getPlaylist':'/id/<str:pk>/',
        'Get playlist song': '/get/<str:playlist_pk>/<str:song_pk>/',
        'Create':'/create/',
        'Add song':'add/<str:pk>/',
        'Update playlist':'/update/<str:pk>/',
        'Update playlist song': '/update/song/<str:playlist_pk>/<str:song_pk>/',
        'Delete playlist':'/delete/<str:pk>/',
        'Delete song': '/delete/song/<str:playlist_pk>/<str:song_pk>/',
        'Get playlist by average song length':'/avg/song/length/',
    }

    return Response(api_urls)


class PlaylistList(generics.ListAPIView):
    queryset = Playlist.objects.all()[:130]
    serializer_class = PlaylistSerializer


class PlaylistCreate(generics.CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistDetails(generics.RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistUpdate(generics.UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistDelete(generics.DestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistByAvgSongLength(generics.ListAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        query = Playlist.objects\
                        .annotate(avg_length=Avg('songs__length'))\
                        .order_by('-avg_length')
        print(query.query)
        return query


class PlaylistSongList(generics.ListAPIView):
    queryset = PlaylistSong.objects.all()[:90]
    serializer_class = PlaylistSongSerializer


class GetPlaylistSong(generics.RetrieveAPIView):
    lookup_fields = 'playlist_id'
    lookup_url_kwarg = 'song_id'
    serializer_class = PlaylistSongSerializer    

    def get_object(self):
        playlist_pk = self.kwargs['playlist_id']
        song_pk = self.kwargs['song_id']
        return PlaylistSong.objects.get(playlist_id=playlist_pk, song_id=song_pk)


class AddSongToPlaylist(generics.CreateAPIView):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer


class SongPlaylistUpdate(generics.UpdateAPIView):
    lookup_fields = 'playlist_id'
    lookup_url_kwarg = 'song_id'
    serializer_class = PlaylistSongSerializer

    def get_object(self):
        playlist_pk = self.kwargs['playlist_id']
        song_pk = self.kwargs['song_id']
        return PlaylistSong.objects.get(playlist_id=playlist_pk, song_id=song_pk)


class SongPlaylistDelete(generics.DestroyAPIView):
    lookup_fields = 'playlist_id'
    lookup_url_kwarg = 'song_id'
    serializer_class = PlaylistSongSerializer

    def get_object(self):
        playlist_pk = self.kwargs['playlist_id']
        song_pk = self.kwargs['song_id']
        return PlaylistSong.objects.get(playlist_id=playlist_pk, song_id=song_pk)