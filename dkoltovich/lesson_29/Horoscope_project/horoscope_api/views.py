
from django.shortcuts import render
from rest_framework import viewsets, filters, decorators
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import datetime as dt

from .models import Horoscope
from .tasks import scrape_signs_on_date, all_signs

from .serializers import HoroscopeSerializer

class HoroscopeViewSet(viewsets.ModelViewSet):
    queryset = Horoscope.objects.all()
    serializer_class = HoroscopeSerializer
    
    filter_backends = [
       DjangoFilterBackend, filters.SearchFilter,
       filters.OrderingFilter]
    filterset_fields = ['sign', 'date']
    search_fields = ['date', 'sign']
    ordering_fields = ['date', 'sign']
    ordering = ['-date']
    

@decorators.api_view(['GET'])
def filter_view(request):
    NUM_OF_SIGNS = 12
    queryset = Horoscope.objects.all()
    qp = request.query_params
    
    sign = qp.get('sign', None)
    date = qp.get('date', None)

    
    if sign:
        queryset = queryset.filter(sign=sign)
    if date:
        queryset = queryset.filter(date=date)
    
    if date and queryset.count() < NUM_OF_SIGNS:
        tomorrow = str(dt.date.today() + dt.timedelta(days=1))
        yesterday = str(dt.date.today() - dt.timedelta(days=1))

        if date in (str(dt.date.today()), str(tomorrow), str(yesterday)):
            
            signs = list(str(obj.sign) for obj in queryset)
            if date == str(dt.date.today()):
                date = 'today'
            elif date == tomorrow:
                date = 'tomorrow'
            else:
                date = 'yesterday'
            scrape_signs_on_date.delay(signs=signs, date=date)
            return Response('Scraping in process', 200)
        else:
            return Response('Enable to get horoscope on this date', 403)
        
    data = HoroscopeSerializer(queryset, many=True).data

    return Response(data)

    
    

    