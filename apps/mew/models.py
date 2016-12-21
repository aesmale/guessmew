from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.Charfield(max_length = 100)
    color = models.CharField(max_length = 100)
    fur = models.Charfield(max_length = 100)
    glasses = models.BooleanField(default = False)
    scarf = models.BooleanField(default = False)
    hat = models.BooleanField(default = False)

class Player(models.Model):
    chosencat = models.ForeignKey(Cat)

class Board(models.Model):
    player = models.ForeignKey(Player)
    cats = models.ManyToManyField(Cat)
