from django.db import models
from artist.models import Artist

# Create your models here.

class ArtistInfo(models.Model):
    artist_id = models.OneToOneField(Artist, on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    birth_place = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name