# created by me
from django.urls import path, include
from . import views
from .views import Top5ArtistsByAlbumsNo

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"), # specify the view + name
    path('', views.getArtistList, name="artist-list"),
    path('filter/height/minimum/', views.getArtistByMinimumHeight, name="artist-by-minimum-height"),
    path('id/<str:pk>/', views.getArtistById, name="artist-by-id"),
    path('create/', views.artistCreate, name="artist-create"),
    path('update/<str:pk>/', views.artistUpdate, name="artist-update"),
    path('delete/<str:pk>/', views.artistDelete, name="artist-delete"),
    path('top/number/albums/', Top5ArtistsByAlbumsNo.as_view()),
]