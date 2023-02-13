from django.contrib import admin

from .models import Post


@admin.action(description="Publish posts")
def update_status(modeladmin, request, queryset):
    queryset.update(status=Post.STATUS_PUBLISHED)


@admin.register(Post)
class AdminBlog(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'blog', 'creation_date', 'edition_date', 'status',)
    search_fields = ('title',)
    actions = [update_status]
