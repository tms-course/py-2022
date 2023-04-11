
from django.shortcuts import render
from rest_framework import viewsets, filters, decorators
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import datetime as dt

from .models import Horoscope
from .tasks import scrape_signs_on_date

from .serializers import HoroscopeSerializer

class HoroscopeViewSet(viewsets.ModelViewSet):
    queryset = Horoscope.objects.all()
    serializer_class = HoroscopeSerializer
    NUM_OF_SIGNS = 12
    
    filter_backends = [
       DjangoFilterBackend, filters.SearchFilter,
       filters.OrderingFilter]
    filterset_fields = ['sign', 'date']
    search_fields = ['date', 'sign']
    ordering_fields = ['date', 'sign']
    ordering = ['-date']

    def list(self, request):
        date = request.GET.get('date', None)
        qs = self.filter_queryset(self.queryset)
        if date and qs.count() < self.NUM_OF_SIGNS:
            tomorrow = str(dt.date.today() + dt.timedelta(days=1))
            yesterday = str(dt.date.today() - dt.timedelta(days=1))
            today = str(dt.date.today())
            
            if date in (today, tomorrow, yesterday):
                signs = list(str(obj.sign) for obj in qs)
                if date == today:
                    date = 'today'
                elif date == tomorrow:
                    date = 'tomorrow'
                else:
                    date = 'yesterday'
                scrape_signs_on_date.delay(signs=signs, date=date)
                return Response('Scraping in process', 200)
            else:
                return Response('Enable to get horoscope on this date', 403)
        
        return Response(self.serializer_class(qs, many=True).data, status=200)
 