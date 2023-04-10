from django.urls import path, include
from . import views
from .views import PlaylistByAvgSongLength

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', views.getPlaylistList, name="playlist-list"),
    path('id/<str:pk>/', views.getPlaylistById, name="playlist-by-id"),
    path('get/<str:playlist_pk>/<str:song_pk>/', views.getPlaylistSong, name="get-playlist-song"),
    path('create/', views.playlistCreate, name="playlist-create"),
    path('add/<str:pk>/', views.addSongToPlaylist, name="playlist-add-song"),
    path('update/<str:pk>/', views.updatePlaylist, name="playlist-update"),
    path('update/song/<str:playlist_pk>/<str:song_pk>/', views.updateSongPlaylist, name="playlist-song-update"),
    path('delete/<str:pk>/', views.deletePlaylist, name="playlist-delete"),
    path('delete/song/<str:playlist_pk>/<str:song_pk>/', views.deletePlaylistSong, name="playlist-song-delete"),
    path('filter/song/avg/length/', PlaylistByAvgSongLength.as_view()),
]