from __future__ import unicode_literals

from django.db import models

# Whisky model
class Whisky(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    strength = models.FloatField()

    def __str__(self):
        return self.name

# A bunch of ratings per whisky to calculate an average
class Rating(models.Model):
    whisky = models.ForeignKey(Whisky, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return "%s: %s"%(self.whisky.name, str(self.rating))
   