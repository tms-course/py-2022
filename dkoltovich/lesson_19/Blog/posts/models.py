from django.db import models
from blogs.models import Blog


class Post(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS_DELETED = 2
    STATUS_CHOICES = (
        (STATUS_DELETED, 'Deleted'),
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),

    )

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=True)
    content = models.CharField(max_length=1024, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=STATUS_DRAFT, choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-created_time']

        indexes = [
            models.Index(fields=['blog', ]),
            models.Index(fields=['title', ]),
            models.Index(fields=['content', ]),
        ]