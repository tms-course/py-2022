from django.db import models
from ckeditor.fields import RichTextField

from blogs.models import Blog


class Post(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS_DELETED = 2

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_DELETED, 'Deleted'),
    ]

    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING , related_name='posts')
    title = models.CharField(max_length=128, blank=False)
    content = RichTextField(max_length=2048, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PUBLISHED)


    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['blog']),
        ]
