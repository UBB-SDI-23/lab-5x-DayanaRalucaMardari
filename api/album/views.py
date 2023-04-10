from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from artist.serializers import AlbumSerializerById
# from .serializers import AlbumSerializerById
from api.serializers import AlbumSerializer, AlbumSerializerById

from .models import Album
from artist.models import Artist

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'GetAlbum':'/id/<str:pk>/',
        'Create':'/create/',
        'Update':'/update/<str:pk>/',
        'Delete':'/delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def getAlbumList(request):
    albums = Album.objects.all()
    serializers = AlbumSerializer(albums, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getAlbumById(request, pk):
    # validate the existance of the given PK
    try:
        album =  Album.objects.get(id=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

    serializer = AlbumSerializerById(album, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def albumCreate(request):
    print("BACKEND\n")
    print(request.data)
    # validate the existance the given 'artist_id' FK
    # artist_id = request.data['artist_id']
    # try:
    #     Artist.objects.get(id=artist_id)
    # except Artist.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def albumUpdate(request, pk):
    # validate the existance of the given PK
    try:
        album =  Album.objects.get(id=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

     # validate the existance the given 'artist_id' FK
    artist_id = request.data['artist_id']
    try:
        Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(instance=album, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def albumDelete(request, pk):
    # validate the existance of the given PK
    try:
        album =  Album.objects.get(id=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    album.delete()
    return Response("Album deleted successfully!")