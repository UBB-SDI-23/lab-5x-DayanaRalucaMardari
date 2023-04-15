from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework import generics
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


class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetails(generics.RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializerById


class AlbumCreate(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumUpdate(generics.UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDelete(generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


@api_view(['DELETE'])
def albumDelete(request, pk):
    # validate the existance of the given PK
    try:
        album =  Album.objects.get(id=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    album.delete()
    return Response("Album deleted successfully!")