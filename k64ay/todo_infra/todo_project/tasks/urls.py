from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, \
    filter_view, scrape_root_nodes


router = DefaultRouter()
router.register(r'', TaskViewSet)

urlpatterns = [
    path('filter/', filter_view),
    path('scrape/', scrape_root_nodes),
    path('', include(router.urls)),
]