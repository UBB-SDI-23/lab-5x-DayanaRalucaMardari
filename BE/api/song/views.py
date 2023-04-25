from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework import generics
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


class SongList(generics.ListAPIView):
    queryset = Song.objects.all()[:120]
    serializer_class = SongSerializer


class SongDetails(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongCreate(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongUpdate(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDelete(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer