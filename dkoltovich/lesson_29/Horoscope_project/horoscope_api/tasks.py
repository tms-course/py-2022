from bs4 import BeautifulSoup
import requests

from .serializers import HoroscopeSerializer
from Horoscope_project import celery_app

all_signs: set = {'Cancer', 'Aries', 'Taurus', 'Gemini', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'}


@celery_app.task(bind=True)
def every_day_horoscope_scraping(request):

    for sign in all_signs:
        res = requests.get(f'https://horo.mail.ru/prediction/{sign.lower()}/today/')
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.find('div', {'p-prediction__inner'}).find('div', {'class': 'article__item'}).text
        data = {'sign':sign, 'content': content}
        sign_horoscope = HoroscopeSerializer(data=data)
        if sign_horoscope.is_valid():
            sign_horoscope = sign_horoscope.save()

    return content


@celery_app.task
def scrape_signs_on_date(**kwargs):
    import datetime as dt
    date = kwargs.get('date', None)
    known_signs = set(kwargs['signs'])
    date_dict = {
        'yesterday': dt.date.today() - dt.timedelta(days=1),
        'tomorrow': dt.date.today() + dt.timedelta(days=1),
        'today' : dt.date.today()
        }
    
    signs_to_scrape = all_signs.difference(known_signs)
    
    for sign in signs_to_scrape:
        res = requests.get(f'https://horo.mail.ru/prediction/{sign.lower()}/{date}/')
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.find('div', {'p-prediction__inner'}).find('div', {'class': 'article__item'}).text
        
        data = {'date': date_dict[date], 'sign':sign, 'content': content}
        sign_horoscope = HoroscopeSerializer(data=data)

        if sign_horoscope.is_valid():
            sign_horoscope = sign_horoscope.save()

    return content
    

