from django.db import models

from validators.validators import first_name_length_char_validator, name_start_with_letter_validator, \
    last_name_length_char_validator, password_length_validator


# Create your models here.


class ProfileModel(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[
            first_name_length_char_validator,
            name_start_with_letter_validator,
        ]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=[
            last_name_length_char_validator,
            name_start_with_letter_validator,
        ]
    )
    email = models.EmailField(
        blank=False,
        null=False,
        max_length=40
    )
    password = models.CharField(
        blank=False,
        null=False,
        validators=[
            password_length_validator
        ])

    image = models.URLField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True, default=18)
