# from rest_framework import serializers
# from album.models import Album
# from .models import Artist
# from api.serializers import ArtistSerializer


# class AlbumSerializerById(serializers.ModelSerializer):
#     artist_id = ArtistSerializer(read_only=True)

#     # validate the existance of the 'artist_id'
#     def validate_artist_id(self, data):
#         artist = Artist.objects.filter(id=data)
#         if not artist.exists():
#             raise serializer.ValidationError("Artist does not exist!")
#         return data

#     class Meta:
#         model = Album
#         fields = ['id', 'title', 'release_date', 'genre', 'length', 'artist_id']
        