from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)
    date_of_created = models.DateField(default=datetime.now(), blank=True)
    time_preparation = models.DurationField()
    mode_preparation = models.CharField(max_length=300)
    WITHOUT = 'WI'
    PASTA = 'PA'
    VEGAN = 'VE'
    CANDY = 'CA'
    STATUS_CATEGORY = (
        (PASTA, 'Pasta'),
        (WITHOUT, 'Without'),
        (VEGAN, 'Vegan'),
        (CANDY, 'Candy'),
    )
    category = models.CharField(
        max_length=2,
        choices=STATUS_CATEGORY,
        default=WITHOUT
    )

    def __str__(self):
        return '%s' % (self.name)




