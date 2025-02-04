from django.db import models

class Video(models.Model):
    sno = models.AutoField(primary_key=True)
    visi = models.BooleanField() # visibility
    pf = models.CharField(max_length=1)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tviews = models.PositiveIntegerField()
    tlikes = models.PositiveIntegerField()
    slug = models.CharField(max_length=25, unique=True)
    source = models.CharField(max_length=250)
    def __str__(self):
        return self.slug


class Playlist(models.Model):
    sno = models.AutoField(primary_key=True)
    visi = models.BooleanField() # visibility
    pf = models.CharField(max_length=1)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.CharField(max_length=250)
    slug = models.CharField(max_length=25, unique=True)
    def __str__(self):
        return self.slug
