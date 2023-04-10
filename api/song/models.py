from django.db import models
from album.models import Album

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=255, unique=True)
    record_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    label = models.CharField(max_length=100)
    length = models.CharField(max_length=20)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
            return self.title