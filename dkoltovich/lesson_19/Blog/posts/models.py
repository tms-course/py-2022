from django.db import models
from blogs.models import Blog


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    DELETED = 'deleted'

    CHOICES = (
        (DRAFT, DRAFT),
        (PUBLISHED, PUBLISHED),
        (DELETED, DELETED),
    )

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=True)
    content = models.CharField(max_length=1024, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, choices=CHOICES, default=DRAFT)

    class Meta:
        ordering = ['-created_time']

        indexes = [
            models.Index(fields=['blog', ]),
            models.Index(fields=['title', ]),
            models.Index(fields=['content', ]),
        ]