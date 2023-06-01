from django.db import models
from django.utils import timezone
import random
# This models import allows us to pull a lot of functionality from the models class that
# was already created for me.

# Create your models here.
# I can inherit a bunch of pre-built functionality by passing models.Model as the argument


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredient = models.ManyToManyField(Ingredient)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
