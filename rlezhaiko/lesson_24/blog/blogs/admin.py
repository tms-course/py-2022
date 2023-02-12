from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'theme', 'author', 'creation_date', 'status',)
    search_fields = ('id', 'author__username')