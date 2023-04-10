from django.db import models
from artist.models import Artist

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255, unique=True)
    release_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    genre = models.CharField(max_length=100)
    length = models.CharField(max_length=20)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='album', blank=True, null=True)
    
    def __str__(self):
        return self.title