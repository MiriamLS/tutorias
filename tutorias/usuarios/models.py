from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from generales.models import Posgrado

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Hombre'),
        ('F', 'Mujer'),
    )
    gender = models.CharField(_('género'), max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    apellido_materno = models.CharField(_('apellido materno'), max_length=150, blank=True, null=True)
    posgrado = models.ForeignKey(Posgrado, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Posgrado")
