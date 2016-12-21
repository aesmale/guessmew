from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Board(models.Model):
    player = models.ForeignKey('Player', on_delete = models.CASCADE)

class Cat(models.Model):
    name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    fur = models.CharField(max_length = 100)
    glasses = models.BooleanField(default = False)
    scarf = models.BooleanField(default = False)
    hat = models.BooleanField(default = False)
    board = models.ManyToManyField(Board)

class Player(models.Model):
    chosencat = models.ForeignKey(Cat)
