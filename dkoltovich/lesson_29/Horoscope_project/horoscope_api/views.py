
from django.shortcuts import render
from rest_framework import viewsets, filters, decorators
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from bs4 import BeautifulSoup


from .models import Horoscope
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
    queryset = Horoscope.objects.all()
    qp = request.query_params
    
    sign = qp.get('sign', None)
    
    if sign:
        queryset = queryset.filter(sign=sign)
    data = HoroscopeSerializer(queryset, many=True).data
    
    return Response(data)


    
    
    

    