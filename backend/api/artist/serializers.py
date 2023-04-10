from rest_framework import serializers
from .models import Artist
from api.serializers import AlbumSerializer, ArtistSerializer

class ArtistSerializerById(serializers.ModelSerializer):
    children = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'height', 'nationality', 'birth_date', 'children']
        

class ArtistsOrderedByAvgOfAlbumsNo(serializers.Serializer):
    artist_id = serializers.StringRelatedField(many=False, read_only=True)
    artist_id__avg = serializers.FloatField()

    # def validate_artist_id_is_positive(self, data):
    #     if data['id'] < 0:
    #         raise serializer.ValidationError("Artist id is NOT positive!")
    #     return data

    # def validate_artist_height_is_positive(self, data):
    #     if data['height'] < 0:
    #         raise serializer.ValidationError("Artist height is NOT positive!")
    #     return data    

    # def validate_artist_id_existance(self, data):
    #     artist = Artist.objects.filter(id=data['id'])
    #     if not artist.exists():
    #         raise serializer.ValidationError("Artist does not exist!")
    #     return data

    # def validate_avg_not_negative(self, data):
    #     if data['artist_id__avg'] < 0:
    #         raise serializer.ValidationError("The average cannot be negative!")
    #     return data