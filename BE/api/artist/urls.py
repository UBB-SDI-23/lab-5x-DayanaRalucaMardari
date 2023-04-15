# created by me
from django.urls import path, include
from . import views
from .views import Top5ArtistsByAlbumsNo, ArtistCreateView, ArtistByMinimumHeight, \
    ArtistDetails, ArtistUpdate, ArtistDelete, ArtistList

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"), # specify the view + name
    # path('', views.getArtistList, name="artist-list"),
    path('', ArtistList.as_view()),
    path('filter/height/minimum/', ArtistByMinimumHeight.as_view()),
    path('id/<str:pk>/', ArtistDetails.as_view()),
    path('create/', ArtistCreateView.as_view()),
    path('update/<str:pk>/', ArtistUpdate.as_view()),
    path('delete/<str:pk>/', ArtistDelete.as_view()),
    # path('delete/<str:pk>/', views.artistDelete, name="artist-delete"),
    path('top/number/albums/', Top5ArtistsByAlbumsNo.as_view()),
]