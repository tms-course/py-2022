from django.db import models
from blogs.models import Blog


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128, blank=False)
    content = models.TextField(max_length=2048, blank=False)
    creation_date = models.DateTimeField(auto_now=True)
    edition_date = models.DateTimeField(auto_now=True)


    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['blog']),
        ]
