from celery import Celery
from celery.schedules import crontab

app = Celery('horoscope')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    # Executes every midnight.
    'add-every-midnight': {
        'task': 'tasks.scrape_horoscope',
        'schedule': crontab()

        #'schedule': crontab(hour=1, minute=0),
    },  
}


@app.task(bind=True)
def scrape_horoscope():
    from bs4 import BeautifulSoup
    import requests
    from serializers import HoroscopeSerializer
    signs = ['Taurus', 'Gemini', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    for sign in signs:
        res = requests.get(f'https://horo.mail.ru/prediction/{sign.lower()}/today/')
        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.find('div', {'p-prediction__inner'}).find('div', {'class': 'article__item'}).text
        data = {'sign':sign, 'content': content}
        sign_horoscope = HoroscopeSerializer(data=data)
        if sign_horoscope.is_valid():
            sign_horoscope = sign_horoscope.save()

    return content
    

beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

app.conf.timezone = 'UTC'

