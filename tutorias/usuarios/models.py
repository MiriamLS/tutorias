from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Hombre'),
        ('F', 'Mujer'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
