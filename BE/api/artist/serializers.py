# from rest_framework import serializers
# from .models import Artist
# from api.serializers import AlbumSerializer, ArtistSerializer

# class ArtistSerializerById(serializers.ModelSerializer):
#     children = AlbumSerializer(many=True, read_only=True)
#     class Meta:
#         model = Artist
#         fields = ['id', 'name', 'height', 'nationality', 'birth_date', 'children']
        

# class ArtistsOrderedByAvgOfAlbumsNo(serializers.Serializer):
#     artist_id = serializers.StringRelatedField(many=False, read_only=True)
#     artist_id__avg = serializers.FloatField()