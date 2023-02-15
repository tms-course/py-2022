<<<<<<< HEAD
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


from .models import Task
from .serializers import TaskSerializer
from permissions import IsOwnerPermission


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 4
'''
=======
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerPermission


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'has_next': self.page.has_next(),
            'has_prev': self.page.has_previous(),
            'count': self.page.paginator.count,
            'results': data
        })

>>>>>>> bdde28e3ae4d20ec23f8fa3a00a2ac590ab4db85

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [
<<<<<<< HEAD
        DjangoFilterBackend, filters.SearchFilter,
        filters.OrderingFilter]
=======
       DjangoFilterBackend, filters.SearchFilter,
       filters.OrderingFilter]
>>>>>>> bdde28e3ae4d20ec23f8fa3a00a2ac590ab4db85
    filterset_fields = ['done', 'desc']
    search_fields = ['desc']
    ordering_fields = ['done', 'created_at']
    pagination_class = StandardResultsSetPagination
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
'''

class TaskListView(generics.ListAPIView):
    queryset = Task.object.all()
    serializer_class = TaskSerializer
    permissions_classes = [IsAuthenticated]


class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.object.all()
    serializer_class = TaskSerializer
    permissions_classes = [IsAuthenticated]
=======

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method in ('GET', 'POST'):
            self.permission_classes = [IsAuthenticated, ]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsOwnerPermission, ]

        return super(TaskViewSet, self).get_permissions()
>>>>>>> bdde28e3ae4d20ec23f8fa3a00a2ac590ab4db85
