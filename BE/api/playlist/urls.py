from django.urls import path, include
from . import views
from .views import PlaylistByAvgSongLength, PlaylistList, PlaylistSongList, \
    PlaylistDetails, GetPlaylistSong, PlaylistCreate, PlaylistUpdate, PlaylistDelete, \
    AddSongToPlaylist, SongPlaylistUpdate, SongPlaylistDelete

urlpatterns = [
    # path('', views.apiOverview, name="api-overview"),
    path('', PlaylistList.as_view()),
    path('all/', PlaylistSongList.as_view()),
    path('id/<str:pk>/', PlaylistDetails.as_view()),
    path('get/<int:playlist_id>/<int:song_id>/', GetPlaylistSong.as_view()),
    path('create/', PlaylistCreate.as_view()),
    path('update/<str:pk>/', PlaylistUpdate.as_view()),
    path('delete/song/<int:playlist_id>/<int:song_id>/', SongPlaylistDelete.as_view()),
    path('delete/<str:pk>/', PlaylistDelete.as_view()),
    path('filter/song/avg/length/', PlaylistByAvgSongLength.as_view()),
    path('add/', AddSongToPlaylist.as_view()),
    path('update/song/<str:playlist_id>/<str:song_id>/', SongPlaylistUpdate.as_view()),   
]