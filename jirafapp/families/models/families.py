"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.validators import UniqueValidator

# Utils
from jirafapp.utils.models import JirafaModel

GENDER_CHOICES = [
        ('M', 'M'),
        ('F', 'F'),
    ]


class Kid(JirafaModel):
    """Kid model.
    
    A kid is a member of family."""

    parent = models.ForeignKey('users.user', on_delete=models.CASCADE)

    gender = models.CharField(
        'Genero',
        max_length=2,
        choices=GENDER_CHOICES,
    )

    username = models.SlugField(
        max_length=40,
        unique=True
    )
    
    name = models.CharField(
        'Kid Name',
        max_length=500,
    )

    birthdate = models.DateField(
        'Birthdate'
    )

    premature_date = models.DateField(
        'Premature date estimated',
        null=True,
        blank=True
    )

    class Meta:
        """Meta class."""

        verbose_name = 'Niño'
        verbose_name_plural = 'Niños'

    def __str__(self):
        """Return name."""
        return self.name


class KidHeight(JirafaModel):
    """Kid's heights data model."""

    kid = models.ForeignKey('families.kid', on_delete=models.CASCADE)

    height = models.CharField(
        'Height',
        max_length=10,
    )

    age_height = models.CharField(
        'Age height',
        max_length=10,
    )

    percentile = models.CharField(
        'Percentile',
        max_length=10,
    )

    date_height = models.DateField(
        'Date Heigth'
        
    )

    class Meta:
        """Meta class."""

        verbose_name = 'Altura Niño'
        verbose_name_plural = 'Alturas de los Niño'

    def __str__(self):
        """Return name."""
        return '{}|{}'.format(self.kid, self.height)


