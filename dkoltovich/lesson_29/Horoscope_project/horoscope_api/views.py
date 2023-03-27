
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
        print(queryset.count())
        if queryset.count() == 0:
            content = scrape_root_nodes(sign=sign)
            data = {'sign':sign, 'content': content}
            horoscope = HoroscopeSerializer(data=data)
            if horoscope.is_valid():
                horoscope = horoscope.save()
                return Response(horoscope.data)

    data = HoroscopeSerializer(queryset, many=True).data
    
    return Response(data)


def scrape_root_nodes(sign: str):
    from bs4 import BeautifulSoup
    import requests
    
    res = requests.get(f'https://horo.mail.ru/prediction/{sign.lower()}/today/')
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find('div', {'p-prediction__inner'}).find('div', {'class': 'article__item'}).text
    return content
    
    
    
    

    