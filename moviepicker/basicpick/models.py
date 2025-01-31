from django.db import models
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('genre_name',)

    def __str__(self):
        return f"{self.genre_name}"

class Movie(models.Model):
    movie_name = models.CharField(max_length=250)
    movie_genre = models.ManyToManyField(Genre, through='MovieGenre') 
    release_year = models.PositiveIntegerField(default=1900)
    location = models.CharField(max_length=100, blank=True)
    watched = models.BooleanField(default=False)
    rewatch = models.BooleanField(default=False)
    date_watched = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.movie_name}"

class MovieGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.movie} ({self.genre})"