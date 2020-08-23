from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)
    preparation_mode = models.CharField(max_length=300)
    time_mode = models.IntegerField(validators=[MinValueValidator(1)])
    Yield = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    date_of_created = models.DateField(default=datetime.now())
