from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, filter_view


router = DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('filter/', filter_view),
    path('', include(router.urls)),
]