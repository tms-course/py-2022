from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    SEX_FEMALE = 0
    SEX_MALE = 1

    GENDERS = ((SEX_FEMALE, 'Female'),
               (SEX_MALE, 'Male'))
    
    sex = models.SmallIntegerField(choices=GENDERS, default=SEX_MALE)
    birth_date = models.DateField('Birthdate', blank=True, null=True)