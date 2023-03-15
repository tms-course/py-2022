from django.db import models


class Signs(models.Model):
    
    name = models.CharField(max_length=64, blank=False, default=None)

class Horoscope(models.Model):
    sign = models.ForeignKey(Signs, unique=False, on_delete=models.CASCADE)
    date = models.DateField(blank=False, default=None)
    content = models.CharField(max_length=1024)
    