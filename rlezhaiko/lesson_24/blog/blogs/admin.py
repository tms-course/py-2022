from django.contrib import admin

from .models import Blog


@admin.action(description="Publish blogs")
def update_blogs_status(modeladmin, request, queryset):
    queryset.update(status=Blog.STATUS_PUBLISHED)


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'theme', 'author', 'creation_date', 'status',)
    search_fields = ('author__username',)
    list_filter = ('author', 'status',)
    ordering = ('-creation_date',)
    actions = [update_blogs_status]