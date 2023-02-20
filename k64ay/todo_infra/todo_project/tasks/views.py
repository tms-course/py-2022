from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, filters, decorators
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

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)

    def get_permissions(self):
        print(self.request.custom)
        if self.request.method in ('GET', 'POST'):
            self.permission_classes = [IsAuthenticated, ]
        elif self.request.method == 'PUT':
            self.permission_classes = [IsOwnerPermission, ]

        return super(TaskViewSet, self).get_permissions()
    

@decorators.api_view(['GET'])
def filter_view(request):
    queryset = Task.objects.all()
    qp = request.query_params

    search = qp.get('search', None)
    page = int(qp.get('page', 1))

    if search:
        queryset = queryset.filter(desc__contains=search)

    if page:
        limit = 5
        offset = (page - 1) * limit + 1
        queryset = queryset[offset:offset+limit]

    data = TaskSerializer(queryset, many=True).data

    return Response(data)