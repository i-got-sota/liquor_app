from django.db import models
from django.contrib.auth.models import AbstractUser

from .validate import validate_age

class CustomUser(AbstractUser):
    """ ユーザーモデル"""
    """age = models.PositiveIntegerField(verbose_name='年齢',
                                      validators = [validate_age])"""

    class Meta:
        verbose_name_plural = 'CustomUser'

