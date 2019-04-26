from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class AbstractPhone(models.Model):
    """Abstract phone number model

    Phone number in accordance with E.164 recommendation.
    """
    phone_regex = RegexValidator(
        regex=r'^\+\d{8,15}$',
        message="Phone number must be entered in the format: '+99999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], verbose_name='phone number', max_length=16, blank=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractPhone):
    """User model

    Contain abstract model of Django user and abstract model of phone number.
    """
    def __str__(self):
        return self.username
