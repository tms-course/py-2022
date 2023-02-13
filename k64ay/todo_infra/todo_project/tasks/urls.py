from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import  TaskListView


router = DefaultRouter()
router.register(r'', TaskListView)
router.register(r'', TaskListView)

urlpatterns = [
    path('', include(router.urls)),
    path('', TaskListView.as_view(), name='user-list')
]