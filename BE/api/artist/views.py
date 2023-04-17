from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Q, Sum, Avg 
from rest_framework import status

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# from .serializers import ArtistSerializerById, ArtistsOrderedByAvgOfAlbumsNo
from api.serializers import ArtistSerializer, ArtistSerializerById, ArtistsOrderedByAvgOfAlbumsNo

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


class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistCreateView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistUpdate(generics.UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDelete(generics.DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetails(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializerById


class ArtistByMinimumHeight(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        min_height = self.request.query_params.get('min_height')
        return Artist.objects.filter(height__gt=min_height)


class Top5ArtistsByAlbumsNo(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        query = Artist.objects.annotate(no_albums=Count('album'))\
                              .order_by('-no_albums')[:5]
        return query