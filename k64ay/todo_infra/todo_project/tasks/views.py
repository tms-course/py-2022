from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerPermission


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [
       DjangoFilterBackend, filters.SearchFilter,
       filters.OrderingFilter]
    filterset_fields = ['done', 'desc']
    search_fields = ['desc']
    ordering_fields = ['done', 'created_at']
    pagination_class = StandardResultsSetPagination
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)

    def get_permissions(self):
        # Your logic should be all here
        if self.request.method in ('GET', 'POST'):
            self.permission_classes = [IsAuthenticated, ]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsOwnerPermission, ]

        return super(TaskViewSet, self).get_permissions()