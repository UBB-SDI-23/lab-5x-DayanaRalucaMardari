from django.db import models
from song.models import Song
# from .playlistsong import PlaylistSong

class Playlist(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, through='PlaylistSong', related_name="playlists")

    def __str__(self):
        return self.title


class PlaylistSong(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    no_streams = models.IntegerField(default=0)
    no_shares = models.IntegerField(default=0)

    class Meta:
        unique_together = ("playlist_id", "song_id")