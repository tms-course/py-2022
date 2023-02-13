from django.db import models
from blogs.models import Blog


class Post(models.Model):
    STATUS_PUBLISHED = 0
    STATUS_DELETED = 1

    STATUS_CHOICES = [
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_DELETED, 'Deleted'),
    ]

    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING , related_name='posts')
    title = models.CharField(max_length=128, blank=False)
    content = models.TextField(max_length=2048, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PUBLISHED)


    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['blog']),
        ]
