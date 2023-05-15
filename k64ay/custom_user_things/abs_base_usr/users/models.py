from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    first_name = models.CharField('first name', max_length=64, blank=True)
    last_name = models.CharField('last name', max_length=64, blank=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'