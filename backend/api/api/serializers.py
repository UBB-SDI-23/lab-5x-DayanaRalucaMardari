from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from artist.models import Artist
from album.models import Album
from song.models import Song
from playlist.models import Playlist, PlaylistSong
from rest_framework.exceptions import ValidationError

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
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    no_albums = serializers.FloatField(read_only=True)

    def validate_height(self, data):
        if data < 0:
            raise ValidationError("Artist height is NOT positive!")
        return data  

    class Meta:
        model = Artist
        fields = '__all__'


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