from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HoroscopeViewSet

router = DefaultRouter()
router.register(r'', HoroscopeViewSet, 'horoscope-list')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
