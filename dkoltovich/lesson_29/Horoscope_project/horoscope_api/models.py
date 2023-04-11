from datetime import date

from django.db import models


class Horoscope(models.Model):
    class Sign(models.Choices):
        ARIES = 'Aries'
        TAURUS = 'Taurus'
        GEMINI = 'Gemini'
        CANCER = 'Cancer'
        LEO = 'Leo'
        VIRGO = 'Virgo'
        LIBRA = 'Libra'
        SCORPIO = 'Scorpio'
        SAGITTARIUS = 'Sagittarius'
        CAPRICORN = 'Capricorn'
        AQUARIUS = 'Aquarius'
        PISCES = 'Pisces'
        
    sign = models.CharField(choices=Sign.choices, max_length=11)
    date = models.DateField(blank=False, default=date.today())
    content = models.CharField(max_length=1024)