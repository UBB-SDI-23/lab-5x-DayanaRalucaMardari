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


@api_view(['GET'])
def getPlaylistList(request):
    playlists = Playlist.objects.all()
    serializers = PlaylistSerializer(playlists, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getPlaylistById(request, pk):
    # validate the existance of the given PK
    try:
        playlist =  Playlist.objects.get(id=pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSerializer(playlist, many=False)
    return Response(serializer.data)


class PlaylistByAvgSongLength(generics.ListAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        query = Playlist.objects\
                        .annotate(avg_length=Avg('songs__length'))\
                        .order_by('-avg_length')
        print(query.query)
        return query


@api_view(['GET'])
def getPlaylistSong(request, playlist_pk, song_pk):
    # validate the existance of the given playlist 'playlist_pk'
    try:
        Playlist.objects.get(id=playlist_pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validate the existance of the given playlist 'song_pk'
    try:
        Song.objects.get(id=song_pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    playlist_song = PlaylistSong.objects.get(playlist_id=playlist_pk, song_id=song_pk)

    serializer = PlaylistSongSerializer(playlist_song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def playlistCreate(request):
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['POST'])
def addSongToPlaylist(request, pk):
    # validate the existance of the given playlist 'pk'
    try:
        Playlist.objects.get(id=pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validate the existance of the given 'song_id'
    song_id = request.data['song_id']
    try:
        Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['PUT'])
def updatePlaylist(request, pk):
    # validate the existance of the given playlist 'pk'
    try:
        playlist = Playlist.objects.get(id=pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlaylistSerializer(instance=playlist, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateSongPlaylist(request, playlist_pk, song_pk):
    # validate the existance of the given playlist 'playlist_pk'
    try:
        Playlist.objects.get(id=playlist_pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validate the existance of the given playlist 'song_pk'
    try:
        Song.objects.get(id=song_pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    playlist_song = PlaylistSong.objects.get(playlist_id=playlist_pk, song_id=song_pk)

    serializer = PlaylistSongSerializer(instance=playlist_song, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deletePlaylist(request, pk):
    # validate the existance of the given PK
    try:
        playlist =  Playlist.objects.get(id=pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    playlist.delete()
    return Response("Playlist deleted successfully!")


@api_view(['DELETE'])
def deletePlaylistSong(request, playlist_pk, song_pk):
    # validate the existance of the given playlist 'playlist_pk'
    try:
        Playlist.objects.get(id=playlist_pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validate the existance of the given playlist 'song_pk'
    try:
        Song.objects.get(id=song_pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    playlist_song = PlaylistSong.objects.get(playlist_id=playlist_pk, song_id=song_pk)
    playlist_song.delete()
    return Response("Playlist song deleted successfully!")
