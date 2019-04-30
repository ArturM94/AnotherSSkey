from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


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


class CustomUserManager(UserManager):
    """Custom user manager

    User manager for custom user model
    """

    def create_user(self, username, email=None, password=None, **extra_fields):
        super().create_user(username, email, password, **extra_fields)
        extra_fields.setdefault('phone_number', None)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        super().create_superuser(username, email, password, **extra_fields)
        extra_fields.setdefault('phone_number', None)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, AbstractPhone):
    """User model

    Custom user model that contain abstract model of Django user and abstract model of phone number.
    """
    email = models.EmailField(_('email address'), unique=True, blank=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
