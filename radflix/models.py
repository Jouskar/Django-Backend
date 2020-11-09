from django.db import models

# Create your models here.


class Movie(models.Model):
    show_id = models.IntegerField(default=0)
    type = models.CharField(max_length=7, default='')
    title = models.CharField(max_length=100, default='')
    director = models.CharField(max_length=200, default='')
    cast = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')
    date_added = models.DateField()
    release_year = models.SmallIntegerField()
    rating = models.CharField(max_length=200, default='')
    duration = models.SmallIntegerField()
    listed_in = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
