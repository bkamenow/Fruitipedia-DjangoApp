from django.db import models

from validators.validators import fruit_name_validator, fruit_name_contain_only_letters_validator


# Create your models here.

class FruitModel(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        validators=[
            fruit_name_validator,
            fruit_name_contain_only_letters_validator,
        ])
    image = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    nutrition = models.TextField(blank=True, null=True)
