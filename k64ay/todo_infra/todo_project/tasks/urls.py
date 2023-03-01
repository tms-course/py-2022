from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, filter_view, scrape_page

router = DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('filter/', filter_view),
    path('scrape/', scrape_page),
    path('', include(router.urls)),
]
