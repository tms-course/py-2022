from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50, unique=False)
    second_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=15, unique=True)
    birth_date = models.DateField(null=False)
    registration_time = models.DateTimeField(auto_now=True)
    