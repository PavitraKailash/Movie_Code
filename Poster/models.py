from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    ratings = models.IntegerField()


class Poster(models.Model):
    movieId = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="movieId")
    poster = models.ImageField(upload_to='Poster_Pics/', null=True)
