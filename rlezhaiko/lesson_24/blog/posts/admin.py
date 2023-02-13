from django.contrib import admin

from .models import Post


@admin.register(Post)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'blog', 'creation_date', 'edition_date', 'status',)
    search_fields = ('title',)