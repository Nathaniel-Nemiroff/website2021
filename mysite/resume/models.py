import datetime
from django.db import models
from django.utils import timezone

class Block(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    content = models.TextField()
    timestart = models.DateField()
    timeend   = models.DateField()
