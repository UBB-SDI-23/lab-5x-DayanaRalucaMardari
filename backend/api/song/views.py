from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import SongSerializer

from .models import Song
from album.models import Album

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'GetSong':'/id/<str:pk>/',
        'Create':'/create/',
        'Update':'/update/<str:pk>/',
        'Delete':'/delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def getSongList(request):
    songs = Song.objects.all()
    serializers = SongSerializer(songs, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getSongById(request, pk):
    # validate the existance of the given PK
    try:
        song =  Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def songCreate(request):
    # validate the existance the given 'album_id' FK
    album_id = request.data['album_id']
    try:
        Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)


@api_view(['PUT'])
def songUpdate(request, pk):
    # validate the existance of the given PK
    try:
        song =  Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validate the existance of the given 'album_id' FK
    album_id = request.data['album_id']
    try:
        Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SongSerializer(instance=song, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def songDelete(request, pk):
    # validate the existance of the given PK
    try:
        song =  Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    song.delete()
    return Response("Song deleted successfully!")