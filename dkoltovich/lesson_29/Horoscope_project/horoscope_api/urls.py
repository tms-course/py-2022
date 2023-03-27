from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HoroscopeViewSet, filter_view

router = DefaultRouter()
router.register(r'', HoroscopeViewSet)


urlpatterns = [
    path('filter/', filter_view),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
