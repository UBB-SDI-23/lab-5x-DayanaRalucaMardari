from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('list/', views.getArtistInfoList, name="artist-info-list"),
    path('id/<str:pk>/', views.getArtistInfoById, name="artist-info-by-id"),
    path('create/', views.artistInfoCreate, name="artist-info-create"),
    path('update/<str:pk>/', views.artistInfoUpdate, name="artist-info-update"),
    path('delete/<str:pk>/', views.artistInfoDelete, name="artist-info-delete"),
]