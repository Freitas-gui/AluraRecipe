from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)
    date_of_created = models.DateField(default=datetime.now(), blank=True)






