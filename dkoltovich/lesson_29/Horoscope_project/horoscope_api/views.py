from django.shortcuts import render
from rest_framework import viewsets

from .models import Horoscope, Signs
from .serializers import HoroscopeSerializer

class HoroscopeViewSet(viewsets.ModelViewSet):
    queryset = Horoscope.objects.all()
    serializer_class = HoroscopeSerializer
    
