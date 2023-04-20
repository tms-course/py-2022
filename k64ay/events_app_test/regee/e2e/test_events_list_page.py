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
    username = 'user'
    password = '123123123'

    def setUp(self):
        self.browser = webdriver.Chrome('e2e/chromedriver')
        self.user = User(username=self.username)
        self.user.set_password(self.password)
        self.user.save()

    def tearDown(self) -> None:
        self.browser.close()

        return super().tearDown()
    
    def test_create_event_btn_appears(self):
        self.browser.get(f'{self.live_server_url}/events/')
        el = self.browser.find_element(By.XPATH, '//a[contains(@class, "btn-primary")]')
        self.assertEquals(el.text, 'Create event')

    def test_create_event_btn_redirects_to_create_event_page(self):
        create_event_url = self.live_server_url + reverse('create_event')
        self.browser.get(f'{self.live_server_url}/events/')
        self.browser.find_element(By.XPATH, '//a[contains(@class, "btn-primary")]').click()
        self.assertEquals(
            self.browser.current_url,
            create_event_url
        )

    def test_user_sees_event_list(self):
        Event.objects.create(
            organizer=self.user,
            name='Event 1',
            datetime=dt.datetime.now() + relativedelta(months=1),
            location='Minsk',
        )
        
        self.browser.get(self.live_server_url + '/accounts/login/')
        username_el = self.browser.find_element(By.ID, 'username')
        username_el.send_keys(self.username)
        password_el = self.browser.find_element(By.ID, 'password')
        password_el.send_keys(self.password)
        self.browser.find_element(By.XPATH, '//button[@type="submit"]').click()

        self.browser.get(self.live_server_url + '/events/')
        title_elem = self.browser.find_element(By.XPATH, '//div[contains(@class, "card")]//h5')
        self.assertEquals(title_elem.text, 'Event 1')