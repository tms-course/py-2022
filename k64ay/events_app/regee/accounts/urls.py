from django.urls import path, include

from . import views

urlpatterns = [
    path('logout', views.logout_user, name='logout_user'),
    path('', include('django.contrib.auth.urls')),
]
