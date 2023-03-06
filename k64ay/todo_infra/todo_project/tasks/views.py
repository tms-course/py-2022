import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, decorators
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task
from .permissions import IsOwnerPermission
from .serializers import TaskSerializer
from .tasks import test_task


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
    queryset = Task.objects.all().order_by()
    serializer_class = TaskSerializer
    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter,
        filters.OrderingFilter]
    filterset_fields = ['done', 'desc']
    search_fields = ['desc']
    ordering_fields = ['done', 'created_at']
    ordering = ['-created_at']
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
    page = qp.get("page", 1)
    html_message = render_to_string('emails/test.html', {
        'page': page})

    send_mail(
        'Super-mega subject',
        f'Email body text {page}',
        settings.EMAIL_HOST_USER,
        ['abuudc@fexbox.org'],
        html_message=html_message
    )

    search = qp.get('search', None)
    page = int(qp.get('page', 1))

    if search:
        queryset = queryset.filter(desc__contains=search)

    if page:
        limit = 5
        offset = (page - 1) * limit + 1
        queryset = queryset[offset:offset + limit]

    data = TaskSerializer(queryset, many=True).data

    return Response(data)


@cache_page(60)
@decorators.api_view(['GET'])
def scrape_root_nodes(request):
    test_task.delay()

    return Response({'message': 'Scraping in process'})
