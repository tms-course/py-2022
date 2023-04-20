import datetime as dt
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from events.models import Event


class TestEventListPage(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user = User.objects.get(username='admin')
        self.brower = webdriver.Chrome('e2e/chromedriver')

    def tearDown(self) -> None:
        self.brower.close()

        return super().tearDown()
    
    def test_create_event_btn_appears(self):
        self.brower.get(self.live_server_url + reverse('event_list'))
        el = self.brower.find_element(By.XPATH, 
                                      '//a[contains(@class, "btn-primary")]')
        self.assertEquals(el.text, 'Create event')

    def test_user_sees_event_list(self):
        Event.objects.create(
            organizer=self.user,
            name='Event 1',
            datetime=dt.datetime.now() + relativedelta(months=1),
            location='Minsk',
        )

        self.brower.get(self.live_server_url + '/accounts/login/')
        username_el = self.brower.find_element(By.ID, 'username')
        username_el.send_keys('admin')
        password_el = self.brower.find_element(By.ID, 'password')
        password_el.send_keys('admin')
        self.brower.find_element(By.XPATH, '//button[@type="submit"]').click()

        self.brower.get(self.live_server_url + reverse('event_list'))
        title_el = self.brower.find_element(By.XPATH, '//div[contains(@class, "card")]//h5')
        self.assertEquals(title_el.text, 'Event 1')
