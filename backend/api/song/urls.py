from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', views.getSongList, name="song-list"),
    path('id/<str:pk>/', views.getSongById, name="song-by-id"),
    path('create/', views.songCreate, name="song-create"),
    path('update/<str:pk>/', views.songUpdate, name="song-update"),
    path('delete/<str:pk>/', views.songDelete, name="song-delete"),
]