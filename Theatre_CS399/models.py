from django.db import models

class MovieInfo(models.Model):
    movie_name = models.CharField(max_length = 254)
    movie_description = models.CharField(max_length = 254)