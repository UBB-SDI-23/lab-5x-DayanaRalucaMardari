from rest_framework import serializers
from .models import ArtistInfo

class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistInfo
        fields = '__all__'