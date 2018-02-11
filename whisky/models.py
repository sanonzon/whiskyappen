from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
   
# Destillery   
class Destillery(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

# Whisky model
class Whisky(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    strength = models.FloatField(default=0)
    malt = models.CharField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now) 
    destillery = models.ForeignKey(Destillery, blank=True, null=True, on_delete=models.PROTECT)
    chill_filtered = models.BooleanField(default=False)
    coloured = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s years' % (self.name,self.age)

# A bunch of ratings per whisky to calculate an average
class Rating(models.Model):
    whisky = models.ForeignKey(Whisky, on_delete=models.CASCADE)
    rating = models.FloatField(default=None, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s: %s' % (self.whisky.name, str(self.rating))

