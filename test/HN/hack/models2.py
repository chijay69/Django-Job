from django.db import models
from django.contrib.postgres.fields import ArrayField

class Story(models.Model):
    id_ = models.IntegerField(help_text="Item's unique Id")
    deleted = models.BooleanField(default=False)
    type_ = models.CharField(max_length=50)
    by = models.CharField(max_length=50)
    time = models.IntegerField()
    dead = models.BooleanField(default=False)
    kids = ArrayField(models.IntegerField())
    descendants = models.IntegerField()
    score = models.IntegerField()
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    