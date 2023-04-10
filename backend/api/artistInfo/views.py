from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArtistInfoSerializer

from .models import ArtistInfo
from artist.models import Artist
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'GetArtistInfo':'/id/<str:pk>/',
        'Create':'/create/',
        'Update':'/update/<str:pk>/',
        'Delete':'/delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def getArtistInfoList(request):
    artistsInfo = ArtistInfo.objects.all()
    serializers = ArtistInfoSerializer(artistsInfo, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getArtistInfoById(request, pk): 
    # get the artistInfo by the ID of the artist
    # validate the existance of the given PK
    try:
        artistInfo =  ArtistInfo.objects.get(artist_id=pk)
    except ArtistInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistInfoSerializer(artistInfo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def artistInfoCreate(request):
    # validate the existance of the given 'artist_id' FK
    artist_id = request.data['artist_id']
    try:
        Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validare noua
    # sa nu se adauge dubluri. In caz de dubluri sa se faca update?

    serializer = ArtistInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def artistInfoUpdate(request, pk):
    # validate the existance of the given PK
    try:
        artistInfo =  ArtistInfo.objects.get(artist_id=pk)
    except ArtistInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # validate the existance of the given 'artist_id' FK (in case it is updated)
    artist_id = request.data['artist_id']
    try:
        Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistInfoSerializer(instance=artistInfo, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

    
@api_view(['DELETE'])
def artistInfoDelete(request, pk):
    # validate the existance of the given PK
    try:
        artistInfo =  ArtistInfo.objects.get(artist_id=pk)
    except ArtistInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    artistInfo.delete()
    return Response("ArtistInfo deleted successfully!")