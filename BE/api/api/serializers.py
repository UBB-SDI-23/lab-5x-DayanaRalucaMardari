from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from artist.models import Artist
from album.models import Album
from song.models import Song
from playlist.models import Playlist, PlaylistSong
from rest_framework.exceptions import ValidationError

class ArtistSerializer(serializers.ModelSerializer):
    no_albums = serializers.FloatField(read_only=True)

    def validate_height(self, data):
        if data < 0:
            raise ValidationError("Artist height is NOT positive!")
        return data  

    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    def validate_title(self, data):
        if data == "":
            raise serializers.ValidationError("Title cannot be empty!")
        return data 

    def validate_genre(self, data):
        if data == "":
            raise serializers.ValidationError("Genre cannot be empty!")
        return data
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date', 'genre', 'length', 'artist_id']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Playlist.objects.all())])
    description = serializers.CharField(max_length=255)
    avg_length = serializers.FloatField(read_only=True)

    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = '__all__'


class AlbumSerializerById(serializers.ModelSerializer):
    artist_id = ArtistSerializer(read_only=True)

    # validate the existance of the 'artist_id'
    def validate_artist_id(self, data):
        artist = Artist.objects.filter(id=data)
        if not artist.exists():
            raise serializer.ValidationError("Artist does not exist!")
        return data

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date', 'genre', 'length', 'artist_id']
        

class ArtistSerializerById(serializers.ModelSerializer):
    children = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'height', 'nationality', 'birth_date', 'children']
        

class ArtistsOrderedByAvgOfAlbumsNo(serializers.Serializer):
    artist_id = serializers.StringRelatedField(many=False, read_only=True)
    artist_id__avg = serializers.FloatField()


# class Playlist(models.Model):
#     title = models.CharField(max_length=100, unique=True)
#     description = models.CharField(max_length=255)
#     songs = models.ManyToManyField(Song, through='PlaylistSong', related_name="playlists")

#     def __str__(self):
#         return self.title


# class PlaylistSong(models.Model):
#     playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
#     song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
#     no_streams = models.IntegerField(default=0)
#     no_shares = models.IntegerField(default=0)

#     class Meta:
#         unique_together = ("playlist_id", "song_id")