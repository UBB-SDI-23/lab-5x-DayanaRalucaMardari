from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q, Sum, Avg 
from rest_framework import status

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .serializers import ArtistSerializerById, ArtistsOrderedByAvgOfAlbumsNo
from api.serializers import ArtistSerializer

from .models import Artist
from album.models import Album
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'GetArtistByMinHeight': '/list?min_height=<int:min_height>/',
        'GetArtist':'/id/<str:pk>/',
        'Create':'/create/',
        'Update':'/update/<str:pk>/',
        'Delete':'/delete/<str:pk>/',
        'Artists by avg of albums NO': '/avg/albums/',
        'Add albums to artist':'/<str:pk>/songs',
    }

    return Response(api_urls)


# @api_view(['PUT'])
# def artistUpdate(request, pk):
#     try:
#         artist =  Artist.objects.get(id=pk)
#     except Artist.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ArtistSerializer(instance=artist, data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

@api_view(['POST'])
def addAlbumsToArtist(request, pk):
    try:
        artist =  Artist.objects.get(id=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
          

    


@api_view(['GET'])
def getArtistList(request):
    artists = Artist.objects.all()
    serializers = ArtistSerializer(artists, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getArtistById(request, pk):
    try:
        artist =  Artist.objects.get(id=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializerById(artist, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getArtistByMinimumHeight(request):
    minimum_height = request.GET.get('min_height')
    artists = Artist.objects.all()

    if minimum_height is not None:
        artists = artists.filter(height__gt=minimum_height)

    serializers = ArtistSerializer(artists, many=True)
    return Response(serializers.data)
########################


class Top5ArtistsByAlbumsNo(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        query = Artist.objects.annotate(no_albums=Count('album'))\
                              .order_by('-no_albums')[:5]
        print(query.query)
        return query


@api_view(['POST'])
def artistCreate(request):
    serializer = ArtistSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def artistUpdate(request, pk):
    try:
        artist =  Artist.objects.get(id=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def artistDelete(request, pk):
    try:
        artist =  Artist.objects.get(id=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    artist.delete()
    return Response("Artist deleted successfully!")
